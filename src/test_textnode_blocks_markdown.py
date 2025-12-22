import unittest

from block_markdown import markdown_to_blocks

class TestTextNode(unittest.TestCase):    
    def test_markdown_to_blocks_cases(self):
        # a list of tuples for cases
        # name of test, markdown, expected result
        cases = [
            (
                # name
                "markdown_to_blocks",
                # md or input
                """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
""",
                # expected result
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            ),
            (
                "empty_blocks",
                """
""",
                [
                ]
            ),
            (
                "one_line",
                """
This is **bolded** paragraph
""",
                [
                    "This is **bolded** paragraph",
                ]
            ),
            (
                "empty_blocks",
                """
""",
                [
                ]
            ),
            (
                "no_trailing_newline",
                """
First paragraph\n\nSecond paragraph
""",
                [
                    "First paragraph", "Second paragraph",
                ]
            ),
            (
                "multiple_blank_lines_between_blocks",
                """
First\n\n\n\nSecond
""",
                [
                  "First", "Second"
                ]
            ),
            (
                "leading_and_trailing_blank_lines",
                """
\n\nFirst\n\nSecond\n\n
""",
                [
                  "First", "Second"
                ]
            ),
            (
                "whitespace_only_blocks",
                """
First\n\n   \n\t\nSecond
""",
                [
                  "First", "Second"
                ]
            ),
            (
                "three_paragraphs",
                """
A\n\nB\n\nC
""",
                [
                  "A", "B", "C"
                ]
            ),
        ]

        for name, md, expected in cases:
            with self.subTest(name=name):
                self.assertEqual(markdown_to_blocks(md), expected)

if __name__ == "__main__":
    unittest.main()