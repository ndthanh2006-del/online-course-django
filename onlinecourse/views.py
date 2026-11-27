from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Course, Submission


def home(request):
    courses = Course.objects.all()
    return render(request, "onlinecourse/home.html", {"course_list": courses})


def course_details(request, course_id):
    course = get_object_or_404(Course.objects.prefetch_related("lessons__questions__choices"), pk=course_id)
    return render(request, "onlinecourse/course_details_bootstrap.html", {"course": course})


def submit(request, course_id):
    course = get_object_or_404(Course.objects.prefetch_related("lessons__questions__choices"), pk=course_id)
    if request.method != "POST":
        return redirect("onlinecourse:course_details", course_id=course.id)

    questions = [q for lesson in course.lessons.all() for q in lesson.questions.all()]
    correct = 0
    answer_summary = {}

    for question in questions:
        selected_id = request.POST.get(f"question_{question.id}")
        selected_choice = question.choices.filter(pk=selected_id).first() if selected_id else None
        is_correct = bool(selected_choice and selected_choice.is_correct)
        if is_correct:
            correct += 1
        answer_summary[str(question.id)] = {
            "question": question.question_text,
            "selected": selected_choice.choice_text if selected_choice else "Not answered",
            "correct": is_correct,
            "correct_answer": next(
                (choice.choice_text for choice in question.choices.all() if choice.is_correct),
                "No correct answer configured"
            ),
        }

    submission = Submission.objects.create(
        student=request.user if request.user.is_authenticated else None,
        student_name=request.user.username if request.user.is_authenticated else request.POST.get("student_name", "Guest"),
        course=course,
        score=correct,
        total_questions=len(questions),
        answers=answer_summary,
    )
    return redirect("onlinecourse:show_exam_result", submission_id=submission.id)


def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    return render(request, "onlinecourse/exam_result.html", {"submission": submission})
