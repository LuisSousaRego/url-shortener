import unittest
import utils

class TestUtils(unittest.TestCase):

    def test_sanitize_url(self):
        result = utils.sanitize_url("http://example.com/page?query=test&query2=test2#test")
        self.assertEqual(result, "http://example.com/page")

    def test_validate_shortcode(self):
        long = utils.validate_shortcode("abc1234")
        short = utils.validate_shortcode("abc12")
        invalid_character = utils.validate_shortcode("abc1!_")
        valid = utils.validate_shortcode("ab_123")

        self.assertFalse(long)
        self.assertFalse(short)
        self.assertFalse(invalid_character)
        self.assertTrue(valid)

    def test_generate_shortcode(self):
        shortcode = utils.generate_shortcode()
        is_valid = utils.validate_shortcode(shortcode)
        self.assertTrue(is_valid)

if __name__ == '__main__':
    unittest.main()
