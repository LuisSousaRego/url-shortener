import unittest
from main import create_short_url, read_shortcode, read_stats

class TestMain(unittest.TestCase):

    def test_create_short_url(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_read_shortcode(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

    def test_read_stats(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

read_stats
if __name__ == '__main__':
    unittest.main()
