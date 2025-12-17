import unittest

from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
       node = LeafNode("p", "Hello", props={"class" : "text"})
       self.assertEqual(node.tag, "p")
       self.assertEqual(node.value, "Hello")
       self.assertEqual(node.props, {"class" : "text"})
       self.assertEqual(node.to_html(), "<p class=\"text\">Hello</p>")


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()