import unittest

from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type

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

    def test_block_to_blocks_type_cases(self):
         cases = [
            (
                # name
                "blocks_to_paragraph",
                # md or input
                """This is a Paragraph.""",
                # expected result
                BlockType.PARAGRAPH,
            ), 
            (
                # name
                "blocks_to_empty",
                # md or input
                """""",
                # expected result
                BlockType.PARAGRAPH,
            ),
            (
                # name
                "blocks_to_heading",
                # md or input
                """# This is a Heading.""",
                # expected result
                BlockType.HEADING,
            ),(
                # name
                "multiple_headings",
                # md or input
                """###### This is a 6 Heading.""",
                # expected result
                BlockType.HEADING,
            ),
            (
                "heading_no_space",
                "######No space",
                BlockType.PARAGRAPH
            ),
            (
                "blocks_to_code",
                """```
This is a Code Block
```""",
                BlockType.CODE,
            ),
            (
                # name
                "blocks_to_quote",
                # md or input
                """>This is a quote""",
                # expected result
                BlockType.QUOTE,
            ), 
            (
                # name
                "multi_line_quote",
                # md or input
                """>This is a quote
>This is a quote
>This is a quote
>This is a quote
>This is a quote
>This is a quote""",
                # expected result
                BlockType.QUOTE,
            ),
            (
                # name
                "multi_line_with_empty_quote",
                # md or input
                """>This is a quote
>This is a quote
>
>This is a quote
>This is a quote
>This is a quote""",
                # expected result
                BlockType.QUOTE,
            ), 
            (
                # name
                "broken_multi_line_quote",
                # md or input
                """>This is a quote
>This is a quote

>This is a quote
>This is a quote
>This is a quote""",
                # expected result
                BlockType.PARAGRAPH,
            ),
            (
                # name
                "blocks_to_unordered_list",
                # md or input
                """- This is an unordered list item""",
                # expected result
                BlockType.UNORDERED_LIST,
            ),
            (
                # name
                "multi_line_unordered_list",
                # md or input
                """- This is an unordered list item
- This is an unordered list item
- This is an unordered list item
- This is an unordered list item
- This is an unordered list item""",
                # expected result
                BlockType.UNORDERED_LIST,
            ),
            (
                # name
                "blocks_to_ordered_list",
                # md or input
                """
1. This is an ordered list item
""",
                # expected result
                BlockType.ORDERED_LIST,
            ),
            (
                # name
                "multi_line_ordered_list",
                # md or input
                """1. This is an ordered list item
2. This is an ordered list item
3. This is an ordered list item
4. This is an ordered list item""",
                # expected result
                BlockType.ORDERED_LIST,
            ),
            (
                # name
                "wrong_start_ordered_list",
                # md or input
                """79. This is an ordered list item""",
                # expected result
                BlockType.PARAGRAPH,
            ),
            (
                # name
                "wrong_increment_ordered_list",
                # md or input
                """1. This is an ordered list item
3. This is an ordered list item
5. This is an ordered list item""",
                # expected result
                BlockType.PARAGRAPH,
            ),
         ]
         for name, md, expected in cases:
            with self.subTest(name=name):
                self.assertEqual(block_to_block_type(md.strip()), expected)

if __name__ == "__main__":
    unittest.main()