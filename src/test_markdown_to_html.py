import unittest

from markdown_to_html import markdown_to_html_node

class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_unordered_list(self):
        md = """
- list item 1
- list item 2
- list item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>list item 1</li><li>list item 2</li><li>list item 3</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. list item 1
2. list item 2
3. list item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>list item 1</li><li>list item 2</li><li>list item 3</li></ol></div>",
        )


    # test code blocks
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_markdown_to_html_edge_cases(self):
        # a list of tuples for cases
        # name of test, markdown, expected result
        cases = [
            (
                # name
                "simple_paragraph",
                # md or input
                "This is just a simple paragraph.",
                # expected result
                "<div><p>This is just a simple paragraph.</p></div>",
            ),        
            (
                # name
                "multiple_paragraphs",
                # md or input
                "First.\n\nSecond.",
                # expected result
                "<div><p>First.</p><p>Second.</p></div>",
            ),        
            (
                # name
                "inline_formatting_paragraph",
                # md or input
                """**Bold** and _italic_ and `code`.""",

                # expected result
                "<div><p><b>Bold</b> and <i>italic</i> and <code>code</code>.</p></div>",
            ),        
            (
                # name
                "single_heading",
                # md or input
                """# Heading one""",

                # expected result
                "<div><h1>Heading one</h1></div>",
            ),              
            (
                # name
                "different_heading_level",
                # md or input
                """###### Heading six""",

                # expected result
                "<div><h6>Heading six</h6></div>",
            ),        
            (
                # name
                "multi_line_different_heading_levels",
                # md or input
                "# Heading one\n\n## Heading two\n\n### Heading three\n\n#### Heading four\n\n##### Heading five\n\n###### Heading six\n\n",

                # expected result
                "<div><h1>Heading one</h1><h2>Heading two</h2><h3>Heading three</h3><h4>Heading four</h4><h5>Heading five</h5><h6>Heading six</h6></div>",
            ),       
            (
                # name
                "heading_with_inline_formatting",
                # md or input
                """### This is _italic_ and **bold**""",

                # expected result
                "<div><h3>This is <i>italic</i> and <b>bold</b></h3></div>",
            ),       
            (
                # name
                "multi_line_quote_block",
                # md or input
                """>>This is a quote
>This is still part of the quote.
>End of the quote.""",

                # expected result
                "<div><blockquote>This is a quote This is still part of the quote. End of the quote.</blockquote></div>",
            ),       
            (
                # name
                "inline_formatting_in_quote_block",
                # md or input
                """>>This is a `code` quote
>This is **still** part of the quote.
>_End_ of the quote.""",

                # expected result
                "<div><blockquote>This is a <code>code</code> quote This is <b>still</b> part of the quote. <i>End</i> of the quote.</blockquote></div>",
            ),       
            (
                # name
                "inline_unordered_list",
                # md or input
                """- List item **one**
- List item _two_
- List item `three`""",

                # expected result
                "<div><ul><li>List item <b>one</b></li><li>List item <i>two</i></li><li>List item <code>three</code></li></ul></div>",
            ),       
            (
                # name
                "non_1_ordered_list",
                # md or input
                """5. fifth
6. sixth
7. seventh""",
                # expected result
                "<div><ol><li>fifth</li><li>sixth</li><li>seventh</li></ol></div>",
            ),       
            (
                # name
                "inline_formatting_ordered_list",
                # md or input
                """1. **First**
2. _Second_
3. `Third`""",
                # expected result
                "<div><ol><li><b>First</b></li><li><i>Second</i></li><li><code>Third</code></li></ol></div>",
            ),       
            (
                # name
                "mixed_document_formatting",
                # md or input
                """
# Heading

This is a paragraph.

>This is a quote block.
>Another one

- First item
- Second item

1. **First**
2. _Second_
3. `Third`

```
This is code block
```
""",
                # expected result
                "<div><h1>Heading</h1><p>This is a paragraph.</p><blockquote>This is a quote block. Another one</blockquote><ul><li>First item</li><li>Second item</li></ul><ol><li><b>First</b></li><li><i>Second</i></li><li><code>Third</code></li></ol><pre><code>This is code block\n</code></pre></div>",
            ),
        ]

        for name, md, expected in cases:
            with self.subTest(name=name):
                node = markdown_to_html_node(md)
                html = node.to_html()
                #print(f"\ndebug: current_test: {name}\nhtml: {html}\nexpected: {expected}\n")
                self.assertEqual(html, expected)

if __name__ == "__main__":
    unittest.main()