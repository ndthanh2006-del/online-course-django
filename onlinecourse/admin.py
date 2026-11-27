from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


class ChoiceInline(TabularInline):
    model = Choice
    extra = 2


class QuestionInline(TabularInline):
    model = Question
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "lesson")
    search_fields = ("question_text",)
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order")
    list_filter = ("course",)
    search_fields = ("title",)
    inlines = [QuestionInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("student_name", "course", "score", "total_questions", "submitted_at")
    list_filter = ("course", "submitted_at")
    readonly_fields = ("score", "total_questions", "answers", "submitted_at")


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
