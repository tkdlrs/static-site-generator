# from enum import Enum
import re
"""
"""

def markdown_to_blocks(markdown):
    list_block_strings = []
    markdown_as_lines = markdown.split("\n\n")
    for line in markdown_as_lines:
        line = line.strip()
        if line == "":
            continue

        list_block_strings.append(line)
    #
    return list_block_strings
    

def block_to_block_type(line_of_markdown):
    hash_mapping = {
        r"^\d+\. " : "ordered_list",
        r"^\* |\- ": "unordered_list",
        r"^>" : "quote",
        r"^#+ ": "heading",
        r"^```\n": "code",
    }
    for pattern in hash_mapping:
        if re.match(pattern, line_of_markdown):
            return hash_mapping[pattern]
    else:
        return "paragraph"

