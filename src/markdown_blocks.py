from enum import Enum

# paragraph
    # If none of the below conditions are met, the block is a normal paragraph
# heading
    # Headings start with 1-6 # characters, followed by a space and then the heading text.
# code
    # Code blocks must start with 3 backticks and end with 3 backticks
# quote
    # Every line in a quote block must start with a > character
# unordered_list
    # Every line in an unordered list block
    #  must start with a - character, followed by a space.
# ordered_list
    # Every line in an ordered list block
    #  must start with a number followed by a . character and a space.
    #  The number must start at 1 and increment by 1 for each line.
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if not block:
        return BlockType.PARAGRAPH
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ","##### ", "###### ")):
        return BlockType.HEADING
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(f">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith(f"- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    # find first occurence of ". " and 
    # then check if all characters before it are digits
    dot_index = block.find(". ")
    if dot_index != -1 and block[:dot_index].isdigit():
        i = int(block[:dot_index])
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

# It takes a raw Markdown string as input
# splits the given string with double space into a list of lines
# each line will be a block element that we will turn into Html nodes 
def markdown_to_blocks(md):
    if not md:
        return []
    
    blocks = []
    split_md = md.split("\n\n")
    for block in split_md:
        stripped_block = block.strip()
        if not stripped_block:
            continue
        blocks.append(stripped_block)
    # the above can be done in 1 line 
    # loop over md and split it on double newline 
    # append and strip b into a list if b.strip() is not empty
    # return [b.strip() for b in md.split("\n\n") if b.strip()]
    return blocks

# just for debugging
def _print_list_lines(blocks):
    print("\n")
    for block in blocks:
        print(f"{block}")