import unittest
from extracttitle import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_with_title_tag(self):
        html_content = "# Test Title\n\nSome content here."
        title = extract_title(html_content)
        self.assertEqual(title, "Test Title")

    def test_extract_title_without_title_tag(self):
        html_content = "Test Title\n\nSome content here."
        with self.assertRaises(Exception):
            extract_title(html_content)

if __name__ == '__main__':
    unittest.main()