from django.db.models import Count, Prefetch
from django.shortcuts import render
from django_app.models import Teacher, Course


def index(request):
    # Курсы с предзагруженными студентами
    course_with_students = Prefetch(
        'courses',
        queryset=Course.objects.prefetch_related('students')
    )

    teachers = (
        Teacher.objects
        .prefetch_related(course_with_students)
        .annotate(total_students=Count('courses__students', distinct=True))
    )

    return render(
        request,
        "index.html",
        {
            "teachers": teachers,
        },
    )
