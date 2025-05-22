from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title', 'description')  # 🔍 admin panelda qidirish
# tests/admin.py


from .models import Test, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4  # har bir savolga 4ta javob joyi chiqadi

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    show_change_link = True

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'test')
    inlines = [AnswerInline]

class TestAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [QuestionInline]

admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
