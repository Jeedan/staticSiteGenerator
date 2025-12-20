import re
from textnode import TextType, TextNode


def text_to_textnodes(text):
    #This is **text** with an _italic_ word and a `code block` 
    # and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) 
    # and a [link](https://boot.dev)
    node = TextNode(text, TextType.TEXT)
    new_nodes = [node]
    bold = split_nodes_delimiter(new_nodes, "**", TextType.BOLD )
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC )
    code = split_nodes_delimiter(italic, "`", TextType.CODE )
    image = split_nodes_image(code)
    link = split_nodes_link(image)

    return link

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            #print(f"old_node:{old_node.text_type}")
            new_nodes.append(old_node)
        else:

            if delimiter not in old_node.text:
                new_nodes.append(old_node)
            else:
                # if number of delimiters is odd, we have no matching delimiter
                deli_length = len(old_node.text.split(delimiter)) 
                num_of_delimiters = deli_length - 1 
                if num_of_delimiters % 2 != 0:
                    raise Exception("Invalid Markdown")
            
                # loop over nodeds for multiple delimiters
                split_nodes = old_node.text.split(delimiter)
                # enumerate turns split nodes into a tuple so we need part
                for i, part in enumerate(split_nodes):
                    if i % 2 == 0:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(part, text_type))
    #print(f"new_nodes: {new_nodes}")
    return new_nodes

# split images and links from a raw text into Textnodes 
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        images = extract_markdown_images(original_text)

        # no images we just append the node if its not empty as well
        if len(images) == 0:
            if node.text.strip():
                new_nodes.append(node)
        else:
            for image_alt, image_link in images:
                sections = original_text.split(f"![{image_alt}]({image_link})", 1)
                before = sections[0]
                after = sections [1]
                # if before is non-empty, append TEXT node
                if before:
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

                # move forward to shrink the text we need to split
                original_text = after  
            # if there is remainder text
            if original_text.strip():
                new_nodes.append(TextNode(original_text, TextType.TEXT))
                
    # print(f"\nnew_nodes: {new_nodes}")
    return new_nodes

# same for Links
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        # just add the node if it is not of type text
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text
        links = extract_markdown_links(original_text)

        # no links
        if len(links) == 0:
            if node.text.strip():
                new_nodes.append(node)
        else:
            for link_text, link_url in links:
                section = original_text.split(f"[{link_text}]({link_url})", 1)
                before = section[0]
                after = section[1]

                # if before is non-empty, append TEXT node
                if before:
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                # move forward to shrink the text we need to split
                original_text = after
            if original_text.strip():
                new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

# images
# r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
def extract_markdown_images(text):
    # # images
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return _extract_markdown(text, pattern)

# regular links
#r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return _extract_markdown(text, pattern)

# helper function to extract text based on a regex pattern
def _extract_markdown(text, pattern):
    if text is None:
        raise Exception("Input text cannot be None or Empty")
    return re.findall(pattern, text)
