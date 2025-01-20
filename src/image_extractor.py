import re
from textnode import TextType, TextNode
#
def extract_markdown_images(text):
    all_images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return all_images
#
def split_nodes_image(old_nodes):
    #
    new_nodes = []
    #
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        # 
        link_counter = 0
        list_image_tuples = extract_markdown_images(old_node.text)
        sections = re.split(r"(!\[.*?\]\(.*?\))", old_node.text)
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
                    list_image_tuples[link_counter][0], 
                    TextType.IMAGE, 
                    list_image_tuples[link_counter][1]
                    ))
                link_counter += 1
    #    
    return new_nodes

#