import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
         # test image url: https://i.imgur.com/XGG62uL.png
        node3 = TextNode("This is a Link Node", TextType.LINK, "https://i.imgur.com/XGG62uL.png")
        node4 = TextNode("This is an Image Node", TextType.IMAGE, "https://i.imgur.com/XGG62uL.png")
        node5 = TextNode("This is a Link with a missing url", TextType.LINK)
        
        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertIsNotNone(node3.url,f"url is: {node3.url}" )
        self.assertIsNone(node5.url,f"url is: {node5.url}" )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        # print(f"\nDEBUG: {html_node}")
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    # Bold test
    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        # print(f"\nDEBUG: {html_node}")
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    # Italic test
    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        # print(f"\nDEBUG: {html_node}")
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")

    # Code test
    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        # print(f"\nDEBUG: {html_node}")
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    # Link test
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        # print(f"\nDEBUG: {html_node}")
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")

    # Image test
    def test_image(self):
        node = TextNode("This is a image node", TextType.IMAGE, "https://google.com")
        html_node = text_node_to_html_node(node)
        # print(f"\nDEBUG: {html_node}")
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")

    # text to textNode
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(text)
        self.assertEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ], text_nodes
        )
    
    # empty string
    def test_text_to_textnodes_empty(self):
        text = ""
        self.assertEqual(
            [],
            text_to_textnodes(text),
        )
    
    # plain text,
    def test_text_to_textnodes_plain_text(self):
        text = "Just some plain text"
        self.assertEqual(
            [TextNode("Just some plain text", TextType.TEXT)],
            text_to_textnodes(text),
        )
    
    # single 
    def test_text_to_textnodes_single_bold(self):
        text = "**bold**"
        self.assertEqual(
            [TextNode("bold", TextType.BOLD)],
            text_to_textnodes(text),
        )
    
    # multiple same type
    def test_text_to_textnodes_multiple_bold(self):
        text = "**one** and **two**"
        self.assertEqual(
            [
                TextNode("one", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("two", TextType.BOLD),
            ],
            text_to_textnodes(text),
        )

    # single image
    def test_text_to_textnodes_image_only(self):
        text = "![alt](https://example.com/img.png)"
        self.assertEqual(
            [TextNode("alt", TextType.IMAGE, "https://example.com/img.png")],
            text_to_textnodes(text),
        )

    # single image
    def test_text_to_textnodes_link_only(self):
        text = "[click](https://example.com)"
        self.assertEqual(
            [TextNode("click", TextType.LINK, "https://example.com")],
            text_to_textnodes(text),
        )
    
    # TODO: this does not produce markdown for nested 
    def test_fake_nested(self):
        text = "Start **bold _and italic_ bold** end"

        self.assertEqual(
             [
                TextNode("Start ", TextType.TEXT),
                TextNode("bold _and italic_ bold", TextType.BOLD),
                TextNode(" end", TextType.TEXT),
            ],
            text_to_textnodes(text),
        )

if __name__ == "__main__":
    unittest.main()