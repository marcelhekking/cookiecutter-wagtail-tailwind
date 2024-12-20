import django.views as views
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from .forms import OwnerForm

BEVESTIGING = """
Bij deze bevestigen wij dat we je contactformulier hebben ontvangen.

Wij zullen zo spoedig mogelijk contact met je opnemen.
"""


class ContactFormView(views.generic.edit.FormView):
    form_class = OwnerForm
    template_name = "contact/contact.html"
    success_url = reverse_lazy("submitted")

    def form_valid(self, form):
        # instance = form = MyForm(request.POST)

        # send emails...
        msg_plain = render_to_string(
            "contact/email.txt",
            {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "message": form.cleaned_data["message"],
            },
        )
        send_mail(
            subject="Test",
            message=msg_plain,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=settings.EMAIL_RECIPIENT_LIST,
            fail_silently=False,
        )

        # send email customer
        send_mail(
            subject="Bevestiging",
            message=BEVESTIGING,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[form.cleaned_data["email"]],
            fail_silently=False,
        )

        return super().form_valid(form)


class SubmittedView(views.generic.TemplateView):
    template_name = "contact/submitted.html"
