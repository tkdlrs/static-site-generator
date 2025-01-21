# from enum import Enum
import re
"""
"""

def markdown_to_blocks(markdown):
    list_block_strings = []
    markdown_as_lines = markdown.split("\n\n")
    for line in markdown_as_lines:
        if line.strip() == "":
            continue

        list_block_strings.append(line.strip())
    #
    return list_block_strings

# class BlockType(Enum):
#    PARAGRAPH = "paragraph"
#    HEADING = "heading"
#    CODE = "code"
#    QUOTE = "quote"
#    UNORDERED_LIST = "unordered_list"
#    ORDERED_LIST = "ordered_list"
    

def block_to_block_type(line_of_markdown):
    hash_mapping = {
        r"^\d+\. " : "ordered_list",
        r"^\*|\- ": "unordered_list",
        r"^>" : "quote",
        r"^#+ ": "heading",
        r"^```": "code",
    }
    for pattern in hash_mapping:
        if re.match(pattern, line_of_markdown):
            return hash_mapping[pattern]
    else:
        return "paragraph"

