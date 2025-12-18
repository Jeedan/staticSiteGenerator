import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        bold_node = LeafNode("b", "Bold")
        italic_node = LeafNode("i", "italic")
        text_node = LeafNode(None, "text")
        parent_node = ParentNode("p", [bold_node, italic_node, text_node])

        self.assertEqual(parent_node.to_html(), "<p><b>Bold</b><i>italic</i>text</p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grand_grandchildren(self):
        grand_grand_child_node = LeafNode("em", "grand grandchild")
        grandchild_node = ParentNode("b", [grand_grand_child_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b><em>grand grandchild</em></b></span></div>",)
    
    def test_to_html_with_props(self):
        parent_node = ParentNode("div", [LeafNode(None, "hi")], {"class": "container"})
        self.assertEqual(parent_node.to_html(), "<div class=\"container\">hi</div>")
        
    def test_to_html_with_emptychildren(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(),"<div></div>")
    
    def test_tag_is_none(self):
        parent_node = ParentNode(None, [LeafNode(None, "hi")])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_children_is_none(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()


        