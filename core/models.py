from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.models import Page
from wagtail.search import index
from wagtailmetadata.models import MetadataPageMixin


class ExtPage(MetadataPageMixin, Page):
    keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Meta keywords"))

    search_fields = Page.search_fields + [
        index.SearchField("keywords", partial_match=True, boost=2),
    ]

    settings_panels = Page.settings_panels

    class Meta:
        abstract = True
