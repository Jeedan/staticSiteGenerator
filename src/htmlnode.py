
class HTMLNode:
    # tag - a string representing the HTML tag name ("p", "a", "h1")
    # value - a string representing the value of the HTML tag (like text in <p></p>)
    # children - a list of HTMLNode objects representing the children of THIS node
    # props - a dictionary of key-value pairs representing the attributes of the HTML tag (eg: <a> tag might have "href": "https://google.com")
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        attributes = ""
        for key, value in self.props.items():
            attributes += f" {key}=\"{value}\""
        return attributes
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

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