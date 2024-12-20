from wagtail import blocks
from wagtail.blocks import CharBlock

__all__ = ["SocialMediaIconBlock", "FooterBlock"]


class SocialMediaIconBlock(blocks.StructBlock):
    PLATFORM_CHOICES = [
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("twitter", "Twitter"),
        ("whatsapp", "WhatsApp"),
        ("youtube", "YouTube"),
    ]

    platform = blocks.ChoiceBlock(choices=PLATFORM_CHOICES)
    url = blocks.URLBlock("URL")

    class Meta:
        template = "blocks/social_media_icon_block.html"
        icon = "external-link-alt"
        label = "Social media icon"

    def get_context(self, value, parent_context=None):
        ctx = super().get_context(value, parent_context)

        # add label for display name of social media platform kjhaskdjhkjsdh
        ctx["label"] = dict(self.PLATFORM_CHOICES).get(
            value["platform"], value["platform"]
        )
        return ctx


class FooterItemsBlock(blocks.StructBlock):
    social_media_icons = blocks.ListBlock(child_block=SocialMediaIconBlock())
    kvk = CharBlock()
    iban = CharBlock()


class FooterBlock(blocks.StreamBlock):
    footer = FooterItemsBlock()
