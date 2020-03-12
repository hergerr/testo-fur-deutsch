from django.contrib import admin
from .models import Word, VerbRektion, LearningSet


class WordInline(admin.TabularInline):
    model = Word


class VerbRektionInline(admin.TabularInline):
    model = VerbRektion


class LearningSetInlineAdmin(admin.ModelAdmin):
    inlines = [WordInline, VerbRektionInline]

admin.site.register(LearningSet, LearningSetInlineAdmin)
