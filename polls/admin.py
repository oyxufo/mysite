from django.contrib import admin
from .models import Question
from .models import Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None,           {'fields': ['question_text']}),
        # ('choice',         {'fields': ['choice_text']}),
        ('Date information', {'fields': ['pub_date']}),

    ]
    inlines = [ChoiceInline]


admin.site.register(Question,QuestionAdmin)
# assert isinstance(admin.site.register, object)
# admin.site.register(Choice)

