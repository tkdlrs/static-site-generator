from textnode import TextNode, TextType
from splitter import split_nodes_delimiter
from image_extractor import split_nodes_image
from link_extractor import split_nodes_link

"""
"""
def text_to_textnodes(text):
    nodes = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_delimiter([nodes], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    #   
    return new_nodes

#
