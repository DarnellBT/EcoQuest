""""Defines views for about."""
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):

    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            print(name, email, message)
            
          

            html_content = render_to_string(
                "email/contact_email.html", {
                'name': name,
                'email': email,
                'message': message,
                }
            )

            email = EmailMessage(
                subject="Contact Form Submission",
                body=html_content,
                from_email="ecoquest.noreply@gmail.com",
                to=["ecoquest.customer.service@outlook.com"],
            )

            email.content_subtype = "html"
            email.send()

            return redirect("./")

    context = {
        'form':form,
    }

    return render(request, 'contact.html', context)
