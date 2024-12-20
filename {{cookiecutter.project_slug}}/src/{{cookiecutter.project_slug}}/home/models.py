from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Orderable, Page

from py10 import blocks


class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey("home.HomePage", related_name="carousel_afbeeldingen")
    carousel_afbeelding = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [FieldPanel("carousel_afbeelding")]


class HomePage(Page):
    bedrijfsnaam = models.CharField(
        verbose_name="bedrijfsnaam",
        max_length=100,
    )
    straat = models.CharField(
        verbose_name="straat",
        max_length=100,
    )
    postcode = models.CharField(
        verbose_name="postcode",
        max_length=10,
    )
    stad = models.CharField(
        verbose_name="stad",
        max_length=10,
    )
    land = models.CharField(
        verbose_name="land",
        max_length=10,
    )
    email = models.EmailField(blank=True)
    telefoon = models.CharField(
        verbose_name="telefoon",
        max_length=25,
    )
    bedrijfs_afbeelding = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    hero = StreamField(
        blocks.HeroStreamBlock(max_num=1),
        blank=True,
        null=True,
        verbose_name="Hero",
        use_json_field=True,
    )
    inhoud = StreamField(blocks.BodyBlock(), blank=True, use_json_field=True)
    footer = StreamField(blocks.FooterBlock(max_num=1), blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel(
                    "carousel_afbeeldingen",
                    max_num=5,
                    min_num=1,
                    label="Carousel afbeeldingen",
                ),
                FieldPanel("hero"),
            ],
            heading="Hero",
        ),
        FieldPanel("inhoud"),
        FieldPanel("footer"),
    ]

    promote_panels = Page.promote_panels + [
        MultiFieldPanel(
            [
                FieldPanel("bedrijfsnaam"),
                FieldPanel("straat"),
                FieldPanel("postcode"),
                FieldPanel("stad"),
                FieldPanel("land"),
                FieldPanel("telefoon"),
                FieldPanel("bedrijfs_afbeelding"),
            ],
            "Voor gestructureerde data",
        ),
    ]
