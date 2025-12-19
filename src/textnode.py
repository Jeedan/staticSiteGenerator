from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        # if text_type == link or image set url, else url = NONE
        if self.text_type == TextType.LINK or self.text_type == TextType.IMAGE:
            self.url = url
        else:
            self.url = None

    # returns True if all of the properties of two TextNode objects are equal.
    # Our future unit tests will rely on this method to compare objects.
    def __eq__(self, otherNode):

        equal_text = self.text == otherNode.text
        equal_text_type = self.text_type == otherNode.text_type
        equal_url = self.url == otherNode.url 

        if equal_text and equal_text_type and equal_url:
            return True
        return False
    
    # returns a string representation of the TextNode object
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("text_node is not a valid TextType")
