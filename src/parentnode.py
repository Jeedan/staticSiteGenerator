from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    """An HTML node that can contain other HTML nodes as children.

    Examples:
        ParentNode(
            "div",
            [LeafNode("span", "child text")],
            {"class": "container"},
        )
        -> <div class="container"><span>child text</span></div>
    """
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    """Render this node and all of its children as an HTML string.

    Returns:
        A string containing the opening tag, the rendered children,
        and the closing tag.

    Raises:
        ValueError: If `tag` is missing or empty, or if `children`
            is None.
    """
    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("All Parent nodes must have a tag")
        
        if self.children is None:
            raise ValueError("The list of children is missing or invalid! All children must have a value")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html() 
        
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"