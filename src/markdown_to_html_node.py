import re
#
from htmlnode import ParentNode, LeafNode

from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from text_to_text_node import text_to_textnodes
from textnode import text_node_to_html_node

"""
this function should take a markdown file and convert it into a single 'div' html node with children of all the elements in it

"""
#
def markdown_to_html_node(markdown):
    html_node = ParentNode("div", [], None)
    #
    hash_mapping = {
        "ordered_list" : handle_ordered_list,
        "unordered_list": handle_unordered_list,
        "quote" : handle_quote,
        "heading": handle_heading,
        "code": handle_code,
        "paragraph": handle_paragraph
        }
    #
    children_nodes = []
    # Split the markdown into blocks
    markdown_blocks = markdown_to_blocks(markdown)
    # Loop over each block:
    for block in markdown_blocks:
        # Determine the type of block, if no block throw an error.
        current_block_type = block_to_block_type(block)
        if current_block_type not in hash_mapping:
            raise ValueError("Invalid block type")
        # Based on the type of block, create a new HTMLNode with the proper data
        the_thing = hash_mapping[current_block_type]
        kids = the_thing(block)
        #
        children_nodes.append(kids)
    #
    html_node.children = children_nodes
    # Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.
    return html_node 

#
def handle_ordered_list(current_block):
    # print("trying to handle an ordered list")
    order_list_parent = ParentNode("ol", [])
    # Need to remove the "*" character at the begining of each line.
    lines = current_block.split("\n")
    html_nodes = []
    for line in lines:
        current_line_text = line[3:]
        kids = []
        thing_as_text_node = text_to_textnodes(current_line_text)
        #
        for t_node in thing_as_text_node:
            current_node_as_html = text_node_to_html_node(t_node)
            kids.append(current_node_as_html)
            list_item = ParentNode("li", kids)

        html_nodes.append(list_item)
        #
    #
    order_list_parent.children = html_nodes
    return order_list_parent
#
def handle_unordered_list(current_block):
    # print("trying to handle an unordered list")
    unorder_list_parent = ParentNode("ul", [])
    # Need to remove the "*" character at the begining of each line.
    lines = current_block.split("\n")
    html_nodes = []
    for line in lines:
        current_line_text = line[2:]
        kids = []
        thing_as_text_node = text_to_textnodes(current_line_text)
        #
        for t_node in thing_as_text_node:
            current_node_as_html = text_node_to_html_node(t_node)
            kids.append(current_node_as_html)
            list_item = ParentNode("li", kids)

        html_nodes.append(list_item)
    #
    unorder_list_parent.children = html_nodes
    return unorder_list_parent
#
def handle_quote(current_block):
    # print("trying to handle a blockquote")
    sections = current_block[1:]
    sections = re.sub(r"\n> ", " ", sections).lstrip()
    blockquote = LeafNode("blockquote", sections)
    #
    html_nodes = []
    current_block_text_nodes = text_to_textnodes(current_block)
    for node in current_block_text_nodes:
        current_node_as_html = text_node_to_html_node(node)
        html_nodes.append(current_node_as_html)
    #
    blockquote.children = html_nodes
    #
    return blockquote
#
def handle_heading(current_block):
    # print("trying to handle a heading")
    sections = current_block.split()
    content = " ".join(sections[1:])
    # get number count of hashtag to determiner header level.
    header_level = str(len(sections[0]))
    #
    header = LeafNode(f"h{header_level}", content)    
    return header
#
def handle_code(current_block):
    # print("trying to handle code")
    # print(current_block, "current_block")
    code_element = ParentNode("code", [])
    code_kids = []
    last_back_tick = current_block.rfind("`")
    sections = current_block[3:(last_back_tick - 3)]
    #
    current_blocks_text_nodes = text_to_textnodes(sections)
    for node in current_blocks_text_nodes:
        current_node_as_html = text_node_to_html_node(node)
        code_kids.append(current_node_as_html)
    #
    code_element.children = code_kids
    pre = ParentNode("pre", [code_element])
    return pre
#
def handle_paragraph(current_block):
    # print("trying to handle paragraph")
    pargraph_parent = ParentNode("p", [])
    html_nodes = []
    current_block_text_nodes = text_to_textnodes(current_block)
    for node in current_block_text_nodes:
        current_node_as_html = text_node_to_html_node(node)
        html_nodes.append(current_node_as_html)
    #
    pargraph_parent.children = html_nodes
    #
    return pargraph_parent 

#