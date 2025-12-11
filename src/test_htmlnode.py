import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("p", "Hello", children=[], props={"class" : "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class" : "text"})
    
    def test_props_to_html_none(self):
        node = HTMLNode("p", "Hello", props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(props={"href" : "https://google.com"} )
        self.assertEqual(node.props_to_html(), " href=\"https://google.com\" ")

    def test_props_to_html_multiple(self):
        node = HTMLNode("a", "link", children=None, props={"href" : "https://google.com", "target" : "_blank"} )
        self.assertEqual(node.props_to_html()," href=\"https://google.com\" target=\"_blank\" ")
    
    def test_repr(self):
        node = HTMLNode("p", "Hello", children=None, props={"class": "highlight"})
        self.assertEqual(
            repr(node),
            "HTMLNode(p, Hello, None, {'class': 'highlight'})"
        )
    def test_to_html_not_implemented(self):
        node = HTMLNode("p", "Hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()
            
if __name__ == "__main__":
    unittest.main()