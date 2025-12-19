import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter
class TestTextNode(unittest.TestCase):
    #split delimiter test
    def test_split_node_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        # print(f"\nDEBUG:\n{node}")
        # print(f"\nDEBUG:\n{new_nodes}")
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ])
    # no matching delimiter
    def test_split_node_delimiter_no_matching_delimiter(self):
        node = TextNode("This is text with a `code block` `word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)
    
    # multiple delimiters
    def test_split_node_delimiter_multiple_delimiter(self):
        node = TextNode("This is `code` and `more`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("more", TextType.CODE), 
            TextNode("", TextType.TEXT)
            ])
        
    # no delimiter
    def test_split_node_delimiter_no_delimiter(self):
        node = TextNode("This is all just text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [
            TextNode("This is all just text", TextType.TEXT),
            ])
   
    # already split nodes
    def test_split_node_delimiter_non_text_node(self):
        nodes = [
            TextNode("This is all just text", TextType.TEXT),
            TextNode("but this is bold", TextType.BOLD),
            ]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("This is all just text", TextType.TEXT),
            TextNode("but this is bold", TextType.BOLD),
            ])
    # text node with delimiter, and one without
    def test_split_node_delimiter_mixed_text_node(self):
        nodes = [
            TextNode("This is *all* just text", TextType.TEXT),
            TextNode("but this is bold", TextType.BOLD),
            ]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("all", TextType.BOLD),
            TextNode(" just text", TextType.TEXT),
            TextNode("but this is bold", TextType.BOLD),
            ])
        
  
        
if __name__ == "__main__":
    unittest.main()