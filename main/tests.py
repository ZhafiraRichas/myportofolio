from django.test import TestCase
from django.urls import reverse

from main.models import Education, Experience


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")

    def test_experience_page_renders_template(self):
        # Halaman HTML hanya merender struktur dan modal AJAX
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, "Experience")
        # Memastikan script memanggil API List Experience
        self.assertContains(response, reverse("api:experience-list"))


class EducationTest(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            title="S1 Teknik Informatika",
            description="Pendidikan sarjana di bidang teknologi informasi.",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.education.title)
        self.assertContains(response, f'href="{reverse("main:show_education")}"')

    def test_education_model(self):
        self.assertEqual(str(self.education), "S1 Teknik Informatika")

    def test_education_page_renders_template(self):
        # Halaman HTML hanya merender struktur dan modal AJAX
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, "Education")
        # Memastikan script memanggil API List Education
        self.assertContains(response, reverse("api:education-list"))