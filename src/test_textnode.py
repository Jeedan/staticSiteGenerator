import unittest

from textnode import TextNode, TextType, text_node_to_html_node

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
    

if __name__ == "__main__":
    unittest.main()