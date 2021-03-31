from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['message-name']
        email = request.POST['message-email']
        message = request.POST['message']

        # Send an email:
        send_mail(
            f'A new email from {name}',
            message,
            email,
            ['sahilahmad2550@gmail.com', 'sahil@sahilahmad.com'],
        )

        return render(request, 'contact.html', {"name": name})
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def pricing(request):
    return render(request, 'pricing.html')


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        phone_number = request.POST['your-phone']
        you_email = request.POST['your-email']
        address = request.POST['your-address']
        your_message = request.POST['your-message']
        return render(request, 'appointment.html', {'your_name': your_name})
    else:
        return render(request, 'appointment.html')
