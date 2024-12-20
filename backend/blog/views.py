from django.views.generic import ListView, DetailView, View, CreateView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import TGForm
import requests

import os
# Import load_dotenv module
from dotenv import load_dotenv
from config import key
from .models import *


def send_to_telegram(message):
    # Load the dotenv function
    load_dotenv()

    # bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    # chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot_token = key.BOT_TOKEN
    chat_id = key.CHAT_ID
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message,
    }
    requests.post(url, data=payload)


def form_view(request):
    if request.method == 'POST':
        form = TGForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            message = form.cleaned_data['message']
            number = form.cleaned_data['number']
            date_of_birth = form.cleaned_data['date_of_birth']
            time_slots = form.cleaned_data['time_slots']
            service = form.cleaned_data['service']

            full_message = f"first_name: {first_name}\nlast_name: {last_name}\nMessage: {message}" \
                           f"\nPhone number: {number}\ndate_of_birth: {date_of_birth}\ntime_slots: {time_slots}" \
                           f"\nservice: {service}"

            send_to_telegram(full_message)
            messages.add_message(request, messages.INFO,
                                 'Your request has been received. Please wait for visit confirmation. ')
            form.save()
            return redirect('form_view')
    else:
        form = TGForm()

    return render(request, 'base.html', {'form': form, 'posts': ContactDetails.objects.all(), 'title': 'ACE OF STATE'})



class ContactDetailsView(ListView):
    model = ContactDetails
    template_name = 'base.html'
    context_object_name = 'contact_details'

    def get_queryset(self):
        return ContactDetails.objects.all()
