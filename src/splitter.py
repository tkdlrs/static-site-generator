from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    #
    hash_text_type = {
        "" : TextType.TEXT,
        "**" : TextType.BOLD,
        "*" : TextType.ITALIC,
        "`" : TextType.CODE
    }
    #
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        #
        sections = old_node.text.split(delimiter)
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
                new_nodes.append(TextNode(item, hash_text_type[delimiter]))           
    #
    return new_nodes
