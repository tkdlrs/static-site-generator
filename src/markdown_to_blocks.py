
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

