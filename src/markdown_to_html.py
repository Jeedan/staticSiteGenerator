from parentnode import ParentNode
from textnode import TextNode,TextType, text_node_to_html_node
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type
from inline_markdown import text_to_textnodes

def markdown_to_html_node(md):
    # split the markdown into blocks
    blocks = markdown_to_blocks(md)
    #print(f"\n")
    #print(f"DEBUG: {blocks}")
    html_nodes = []
    # loop over each block to determine the block's type
    for block in blocks:
        block_type = block_to_block_type(block)

        normalize_blocks = block.replace("\n", " ")
        if block_type == BlockType.PARAGRAPH:
            html_nodes.append(text_to_children(normalize_blocks)) 
        
        if block_type == BlockType.HEADING:
            html_nodes.append(heading_to_children(normalize_blocks)) 

        if block_type == BlockType.QUOTE:
            html_nodes.append(quoteblock_to_children(normalize_blocks))
        
        if block_type == BlockType.UNORDERED_LIST:
            html_nodes.append(unordered_list_to_children(block))
        
        if block_type == BlockType.ORDERED_LIST:
            html_nodes.append(ordered_list_to_children(block))

        if block_type == BlockType.CODE:
            #print(f"code:\n{block},\nblock_type:{block_type}")
            html_nodes.append(codeblock_to_children(block))

    #print("BLOCKS:", repr(blocks))
    #print(f"html_nodes: {html_nodes}")
    root_div = ParentNode("div", html_nodes)
    #print(f"root_div: {root_div}")
    return root_div


def html_nodes_from_children(text_nodes):
    return [text_node_to_html_node(node) for node in text_nodes]

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    #print(f"text_node: {text_node}")
    html_nodes = html_nodes_from_children(text_nodes)
    return ParentNode("p",html_nodes)

# headings
def heading_to_children(text):
    #print(f"heading_to_children: {text}")

    heading_level = 0
    heading_text = ""
    for i in text:
        if i == "#":
            heading_level += 1
        else:
            break
    
    heading_text = text[heading_level:].strip()
    #print(f"heading_text: {heading_text}")
    text_nodes = text_to_textnodes(heading_text)
    ##print(f"heading_node: {text_nodes}")
    html_nodes = html_nodes_from_children(text_nodes)

    return ParentNode(f"h{heading_level}", html_nodes)


# quoteblocks
def quoteblock_to_children(text):
    #print(f"quoteblock_to_children: {text}")

    quoteblock = text.split("\n")
    cleaned_lines= []
    for quote in quoteblock:
        cleaned = quote.replace(">", "")
        cleaned_lines.append(cleaned)
    quote_text = " ".join(cleaned_lines)
    #print(f"quote_text: {quote_text}")
    text_nodes = text_to_textnodes(quote_text)
    html_nodes = html_nodes_from_children(text_nodes)
    
    ##print(f"quote_nodes: {html_nodes}")
    return ParentNode(f"blockquote", html_nodes)


# unordered list
def unordered_list_to_children(text):
    lines = text.split("\n")
   # print(f"lines: {lines}")
    li_nodes = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        #print(f"line: {line}")
        
        if line.startswith("- "):
            li_text = line[2:]
        else:
            li_text = line
        text_nodes = text_to_textnodes(li_text)
        html_children = html_nodes_from_children(text_nodes)
        #print(f"unordered_list_nodes: {html_children}")
        li_nodes.append(ParentNode("li", html_children))

    return ParentNode(f"ul", li_nodes)

# ordered list
def ordered_list_to_children(text):
    lines = text.split("\n")
    #print(f"lines: {lines}")
    li_nodes = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        #print(f"line: {line}")

        # first occurence of "."
        dot_index = line.find(". ")    
        # if index is not the end and the slice from beginning to dot_index is a number
        if dot_index != -1 and line[:dot_index].isdigit():
            li_text = line[dot_index + 2 :]
        else:
            li_text = line
        text_nodes = text_to_textnodes(li_text)
        html_children = html_nodes_from_children(text_nodes)
        #print(f"unordered_list_nodes: {html_children}")
        li_nodes.append(ParentNode("li", html_children))

    return ParentNode(f"ol", li_nodes)

    # code block
def codeblock_to_children(text):
    lines = text.split("\n")
    code_block = lines[1:-1]
    #print(f"code_block: {code_block}")
    code_text = "\n".join(code_block)
    code_text += "\n"
    code_node = TextNode(code_text, TextType.CODE)
    html_node = text_node_to_html_node(code_node)
    return ParentNode(f"pre", [html_node])