from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from syed.models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .help import message, subject


# Create your views here.


def index(request):
    if request.method == "POST":
        from_email = settings.EMAIL_HOST_USER
        recipient_list = []
        name = request.POST.get("name").strip()
        email = request.POST.get("email").strip()
        phone = request.POST.get("phone").strip()
        message_content = request.POST.get("message").strip()
        if not name or not email or not phone or not message_content:
            return messages.error(request, "Must provide all fields!")

        try:
            validate_email(email)
            recipient_list.append(email)
        except ValidationError:
            return messages.error(request, "Invalid email adress!")
        # Send the email to the user
        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            # Send the email notification to me that someone send me the message
            subject_for_me = "New Message from Portfolio Contact Form"
            message_for_me = f"You have received a new message from {name} ({email}).\n\nMessage: {message_content}\n\nPhone: {phone}"
            send_mail(
                subject_for_me,
                message_for_me,
                from_email,
                [from_email],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
            # Save the form data to the database
            contact = Contact(
                name=name,
                email=email,
                phone=phone,
                message=message_content,
                date=datetime.today(),
            )
            contact.save()
            return redirect("/")
        except Exception as e:
            return messages.error(
                request,
                "An error occured while sending the message. Please try again later!",
            )

    return render(request, "index.html")


def view_all(request):
    return render(request, "view_all.html")

