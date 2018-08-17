from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class StaticPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [FieldPanel("body")]
