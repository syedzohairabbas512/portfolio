from django.shortcuts import render, redirect
from django.contrib import messages
from syed.models import Contact
from django.core.mail import send_mail
from django.conf import settings
from .help import thanks_message
from .forms import ProjectForm, ContactForm
from .models import Project
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def index(request):
    projects = Project.objects.all().order_by("-id")[:3]
    contact_form = ContactForm()
    print(projects)
    context = {
        'projects': projects,
        'contact_form': contact_form,
    }

    return render(request, "index.html", context)


def view_all(request):
    projects = Project.objects.all().order_by("-id")
    context = {
        'projects': projects,
    }
    return render(request, "view_all.html", context)


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New project added successfully!')
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database first
            saved_form = form.save()

            # Send email to the user
            user_subject = "Syed's Portfolio | Thanks for visiting my portfolio"
            user_message = thanks_message
            send_mail(user_subject, user_message, settings.DEFAULT_FROM_EMAIL, [saved_form.email])

            # Send email to your team

            admin_subject = 'New Message from Portfolio Contact Form'
            admin_message = f'You have received a new message from:\n\nName: {saved_form.name}\nEmail: {saved_form.email}\nMessage: {saved_form.message}'
            send_mail(admin_subject, admin_message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])

            # Display success message to the user
            messages.success(request, 'Your message has been sent successfully!')
            
            return redirect('index')
        else:
            error_message = 'There was an error with your submission. Please correct the following:'
            for field, errors in form.errors.items():
                error_message += f"\n- {field.capitalize()}: {', '.join(errors)}"
            messages.error(request, error_message)
    else:
        contact_form = ContactForm()

    return render(request, 'index.html', {'contact_form': contact_form})