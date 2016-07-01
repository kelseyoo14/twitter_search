from unittest import TestCase
from server import app


class FlaskTest(TestCase):
    def setUp(self):
        """Do before each test"""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'SecretKey!'
        self.client = app.test_client()

    def tearDown(self):
        """Do after each test"""

    def test_homepage(self):
        """Test displaying twitter search homepage"""

        result = self.client.get("/")

        self.assertIn('Twitter Search!', result.data)

    def test_results(self):
        """Test displaying twitter search results"""

        result = self.client.get('/results?search-terms=kittens&language=en&filter=&number-of-tweets=20')

        self.assertIn('search =', result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()
