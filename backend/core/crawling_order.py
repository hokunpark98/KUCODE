from django.db.models import F

from account.models import Student
from course.models import Course_registration
from repo.models import Repository


RECENT_COURSES_ORDER = "recent_courses"


def uses_recent_courses_order(request):
    return request.GET.get("student_order") == RECENT_COURSES_ORDER


def get_students_for_crawling(request, reverse_default=False):
    students = list(Student.objects.all())
    if not uses_recent_courses_order(request):
        return students[::-1] if reverse_default else students

    students_by_id = {student.id: student for student in students}
    registration_student_ids = Course_registration.objects.filter(
        student__isnull=False
    ).order_by(
        F("course_year").desc(nulls_last=True),
        F("course_semester").desc(nulls_last=True),
        "-course_id",
        "-id",
    ).values_list("student_id", flat=True)

    ordered_students = []
    seen_student_ids = set()

    for student_id in registration_student_ids:
        if student_id in seen_student_ids:
            continue

        student = students_by_id.get(student_id)
        if student is not None:
            ordered_students.append(student)
            seen_student_ids.add(student_id)

    ordered_students.extend(
        student for student in students if student.id not in seen_student_ids
    )
    return ordered_students


def get_repositories_for_crawling(request):
    repositories = list(Repository.objects.all())
    if not uses_recent_courses_order(request):
        return repositories

    students = get_students_for_crawling(request)
    github_id_priority = {}
    for index, student in enumerate(students):
        if student.github_id:
            github_id_priority.setdefault(student.github_id, index)
    default_priority = len(github_id_priority)

    return sorted(
        repositories,
        key=lambda repository: github_id_priority.get(
            repository.owner_github_id,
            default_priority,
        ),
    )
