from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Orderable, Page

from hoepla import blocks


class HomePage(Page):
    welcome = models.CharField(
        verbose_name="welcome",
        max_length=100,
    )

    content_panels = Page.content_panels + [
        FieldPanel("welcome"),
    ]
