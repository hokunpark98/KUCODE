from unittest.mock import patch

from rest_framework.test import APIRequestFactory, APITestCase

from account.models import Student
from repo.api.views import get_repositories_for_crawling
from repo.models import Repository


class CrawlingRepositoryOrderTestCase(APITestCase):
    def test_repositories_follow_recent_course_student_priority(self):
        students = [
            Student.objects.create(id="B", name="B", github_id="b"),
            Student.objects.create(id="A", name="A", github_id="a"),
            Student.objects.create(id="C", name="C", github_id="c"),
            Student.objects.create(id="D", name="D", github_id="d"),
        ]
        Repository.objects.create(id="repo-c", name="C", owner_github_id="c")
        Repository.objects.create(id="repo-d", name="D", owner_github_id="d")
        Repository.objects.create(id="repo-b", name="B", owner_github_id="b")
        Repository.objects.create(id="repo-a", name="A", owner_github_id="a")
        request = APIRequestFactory().get(
            "/",
            {"student_order": "recent_courses"},
        )

        with patch(
            "repo.api.views.get_students_for_crawling",
            return_value=students,
        ):
            repositories = get_repositories_for_crawling(request)

        self.assertEqual(
            [repository.owner_github_id for repository in repositories],
            ["b", "a", "c", "d"],
        )
