from datetime import datetime

import requests
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .credentials import *
from .forms import DonateForm
from .models import Donate

def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def donations(request):
    return render(request, 'donation/donation.html')

@login_required(login_url='login')
def donate(request):
    if request.method == 'POST':
        request.session['amount'] = request.POST.get('amount')
        request.session['phone_number'] = request.POST.get('phone_number')

        form = DonateForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            phone_number = form.cleaned_data['phone_number']
            donate = Donate.objects.create(user=request.user, amount=amount, phone_number=phone_number)
            donate.save()
            return redirect('initiate_stk_push')
    else:
        form = DonateForm()
    return render(request, 'donation/donate.html', {'form': form})

@login_required(login_url='login')
def initiate_stk_push(request):
    amount = request.session.get('amount')
    phone_number = request.session.get('phone_number')
    print(amount)
    print(phone_number)
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    access_token = MpesaAccessToken.validated_mpesa_access_token
    online_password = LipanaMpesaPassword.decode_password

    headers = {
        'Authorization': 'Bearer %s' % access_token,
        'Content-Type': 'application/json'
    }

    stk_request = {
        "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
        "Password": online_password,
        "Timestamp": LipanaMpesaPassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": '600978',
        "PartyB": LipanaMpesaPassword.Business_short_code,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Donation program",
        "TransactionDesc": "Testing stk push"
    }

    response = requests.post(api_url, json=stk_request, headers=headers)

    print(response.text)

    return redirect('donations')
