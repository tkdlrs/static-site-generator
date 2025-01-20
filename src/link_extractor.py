import re 
from textnode import TextType, TextNode
#
def extract_markdown_links(text):
    all_links = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return all_links
#
def split_nodes_link(old_nodes):
    #
    new_nodes = []
    #
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        # 
        link_counter = 0
        list_links_as_tuples = extract_markdown_links(old_node.text)
        sections = re.split(r"(\[.*?\]\(.*?\))", old_node.text)
        #
        if len(sections) % 2 == 0:
            raise Exception("Invalid markdown provided.")
        # 
        for i in range(len(sections)):               
            item = sections[i]
            #
            if item == "":
                continue
            # 
            if i % 2 == 0:
                new_nodes.append(TextNode(item, TextType.TEXT))
            else:
                new_nodes.append(TextNode(
                    list_links_as_tuples[link_counter][0], 
                    TextType.LINK, 
                    list_links_as_tuples[link_counter][1]
                    ))
                link_counter += 1
    #    
    return new_nodes

#