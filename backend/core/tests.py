from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from account.models import Student
from core.crawling_order import (
    get_repositories_for_crawling,
    get_students_for_crawling,
)
from course.models import Course, Course_registration
from repo.models import Repository

class HealthCheckAPITestCase(APITestCase):
    def test_health_check(self):
        url = reverse('healthcheck')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": "OK"})


class CrawlingOrderTestCase(APITestCase):
    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.student_a = Student.objects.create(id="A", name="A", github_id="a")
        self.student_b = Student.objects.create(id="B", name="B", github_id="b")
        self.student_c = Student.objects.create(id="C", name="C", github_id="c")
        self.student_without_course = Student.objects.create(
            id="D",
            name="D",
            github_id="d",
        )

        old_course = Course.objects.create(
            course_id="OLD",
            year=2025,
            semester=2,
            name="Old",
            prof="Professor",
        )
        recent_course = Course.objects.create(
            course_id="RECENT",
            year=2026,
            semester=1,
            name="Recent",
            prof="Professor",
        )
        other_recent_course = Course.objects.create(
            course_id="RECENT2",
            year=2026,
            semester=1,
            name="Other recent",
            prof="Professor",
        )

        Course_registration.objects.create(
            course=old_course,
            course_year=2025,
            course_semester=2,
            student=self.student_a,
        )
        Course_registration.objects.create(
            course=recent_course,
            course_year=2026,
            course_semester=1,
            student=self.student_c,
        )
        Course_registration.objects.create(
            course=other_recent_course,
            course_year=2026,
            course_semester=1,
            student=self.student_a,
        )
        Course_registration.objects.create(
            course=other_recent_course,
            course_year=2026,
            course_semester=1,
            student=self.student_b,
        )

    def test_recent_courses_order_prioritizes_recent_courses_and_deduplicates_students(self):
        request = self.request_factory.get(
            "/",
            {"student_order": "recent_courses"},
        )

        students = get_students_for_crawling(request)

        self.assertEqual(
            [student.id for student in students],
            ["B", "A", "C", "D"],
        )

    def test_default_order_keeps_existing_reverse_behavior_when_requested(self):
        request = self.request_factory.get("/")
        existing_order = list(Student.objects.values_list("id", flat=True))

        students = get_students_for_crawling(request, reverse_default=True)

        self.assertEqual(
            [student.id for student in students],
            existing_order[::-1],
        )

    def test_repositories_follow_recent_course_student_priority(self):
        Repository.objects.create(id="repo-c", name="C", owner_github_id="c")
        Repository.objects.create(id="repo-d", name="D", owner_github_id="d")
        Repository.objects.create(id="repo-b", name="B", owner_github_id="b")
        Repository.objects.create(id="repo-a", name="A", owner_github_id="a")

        request = self.request_factory.get(
            "/",
            {"student_order": "recent_courses"},
        )

        repositories = get_repositories_for_crawling(request)

        self.assertEqual(
            [repository.owner_github_id for repository in repositories],
            ["b", "a", "c", "d"],
        )
