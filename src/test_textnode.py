import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()