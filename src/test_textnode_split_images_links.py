import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_image, split_nodes_link
class TestTextNode(unittest.TestCase):
    # multiple images
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_image_at_start_and_end(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) at the start and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" at the start and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
     
    def test_only_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )

    def test_no_images(self):
        node = TextNode(
            "This is text with a text node",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [node],
            new_nodes,
        )
    
    def test_no_images_empty_text_node(self):
        node = TextNode(
            "",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [],
            new_nodes,
        )

    # multiple links
    def test_split_links(self):
        node = TextNode(
            "Only a link here: [Boot.dev](https://www.boot.dev) and another here [youtube](https://www.youtube.com/@bootdotdev/)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Only a link here: ", TextType.TEXT),
                TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another here ", TextType.TEXT),
                TextNode(
                    "youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev/"
                ),
            ],
            new_nodes,
        )
    
    def test_link_at_start_and_end(self):
        node = TextNode(
            "[Boot.dev](https://www.boot.dev) and another here [youtube](https://www.youtube.com/@bootdotdev/)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another here ", TextType.TEXT),
                TextNode(
                    "youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev/"
                ),
            ],
            new_nodes,
        )
    def test_only_link(self):
        node = TextNode(
            "[Boot.dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
            ],
            new_nodes,
        )

    def test_no_links(self):
        node = TextNode(
            "This is text with a text node",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [node],
            new_nodes,
        )
    
    def test_no_links_empty_text_node(self):
        node = TextNode(
            "",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()