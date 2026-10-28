from django.test import TestCase


class CurriculumViewsTests(TestCase):
    def test_home_links_to_matias_cv(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Matías Olivares")
        self.assertContains(response, 'href="/cv/matias/"')

    def test_matias_cv_shows_provided_profile_and_experience(self):
        response = self.client.get("/cv/matias/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ingeniería Civil en Computación e Informática")
        self.assertContains(response, "Desarrollo web")
        self.assertContains(response, "tres sitios web y software")
        self.assertContains(response, "Guardia de seguridad en un pub")
        self.assertContains(response, "Cajero en Doggis")
