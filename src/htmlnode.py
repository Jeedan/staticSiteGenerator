
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
    
        

        