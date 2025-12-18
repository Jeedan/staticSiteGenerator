
from textnode import TextType, TextNode

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
                         