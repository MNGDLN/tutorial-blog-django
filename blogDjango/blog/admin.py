from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from tinymce.widgets import TinyMCE
from django.db import models


class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["tutorial_title",'tutorial_published',"tutorial_description"]}),
        ("URL", {"fields": ["tutorial_slug"]}),
        ("Series", {"fields": ["tutorial_series", ]}),
        ("Content", {"fields": ["tutorial_content"]}),
        ("Status", {"fields": ["status"]}),
        
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
    list_display = ('tutorial_title','tutorial_series',)
    prepopulated_fields = {'tutorial_slug': ('tutorial_title',)}


class TutorialSeriesAdmin(admin.ModelAdmin):
    list_display = ('tutorial_series',)
    prepopulated_fields = {'series_slug': ('tutorial_series',)}


class TutorialCategoryAdmin(admin.ModelAdmin):
    list_display = ('tutorial_category',)
    prepopulated_fields = {'category_slug': ('tutorial_category',)}


admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(TutorialSeries, TutorialSeriesAdmin)
admin.site.register(TutorialCategory, TutorialCategoryAdmin)
