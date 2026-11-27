from django.core.management.base import BaseCommand
from onlinecourse.models import Choice, Course, Lesson, Question


class Command(BaseCommand):
    help = "Create a sample course, lessons, and mock exam questions."

    def handle(self, *args, **options):
        course, _ = Course.objects.get_or_create(
            name="Introduction to Artificial Intelligence",
            defaults={"description": "Learn the foundations of AI, machine learning, and responsible AI."},
        )
        lesson1, _ = Lesson.objects.get_or_create(
            course=course, title="What is Artificial Intelligence?",
            defaults={"content": "Artificial Intelligence is the field of building systems that perform tasks requiring human-like intelligence.", "order": 1},
        )
        lesson2, _ = Lesson.objects.get_or_create(
            course=course, title="Introduction to Machine Learning",
            defaults={"content": "Machine learning allows systems to learn patterns from data and improve at a task.", "order": 2},
        )
        examples = [
            (lesson1, "Which statement best describes Artificial Intelligence?", [
                ("A computer system performing tasks that normally require human intelligence", True),
                ("A type of computer hardware only", False),
                ("A programming language", False),
            ]),
            (lesson1, "Which of these is an example of an AI application?", [
                ("A voice assistant that understands spoken requests", True),
                ("A basic light switch", False),
                ("A standard ruler", False),
            ]),
            (lesson2, "What does a machine learning model learn from?", [
                ("Data", True),
                ("Random guesses only", False),
                ("The monitor resolution", False),
            ]),
        ]
        for lesson, question_text, choices in examples:
            question, _ = Question.objects.get_or_create(lesson=lesson, question_text=question_text)
            for choice_text, is_correct in choices:
                Choice.objects.get_or_create(
                    question=question, choice_text=choice_text,
                    defaults={"is_correct": is_correct},
                )
        self.stdout.write(self.style.SUCCESS("Demo course and mock exam are ready."))
