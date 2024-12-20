from wagtail.blocks import CharBlock, RichTextBlock, StreamBlock, StructBlock


class SectionBlock(StructBlock):
    sectie_titel =          CharBlock()
    kolom_links = RichTextBlock()
    kolom_rechts = RichTextBlock()


class ContactSectionBlock(StructBlock):
    sectie_titel = CharBlock()
    contact_info = RichTextBlock()


class BodyBlock(StreamBlock):
    sectie = SectionBlock()
    contact_sectie = ContactSectionBlock()
