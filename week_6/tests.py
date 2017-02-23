import unittest
from server import app

class FlaskTestsNoLogin(unittest.TestCase):

  def setUp(self):
      """Stuff to do before every test."""

      self.client = app.test_client()
      app.config['TESTING'] = True

  def tearDown(self):
      """Stuff to do after each test."""

  def test_homepage(self):
      """test that the login form shows on the home page"""

      result = self.client.get("/")
      self.assertEqual(result.status_code, 200)
      self.assertIn('<form action="/process_login" method="POST">', result.data)

  def test_secretpage(self):
    """test that user can't see secret data without login"""

    result = self.client.get("/super_secret")
    self.assertEqual(result.status_code, 200)
    self.assertIn("You must be logged in", result.data)
    self.assertNotIn("Super secret", result.data)

if __name__ == "__main__":
  unittest.main()