from wagtail.blocks import CharBlock, StreamBlock


class HeroStreamBlock(StreamBlock):
    onder_titel = CharBlock()

    class Meta:
        # template = "cms/blocks/hero.html"
        icon = "square"
        label = "Hero"
