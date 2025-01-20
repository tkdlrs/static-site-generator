from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output = []
    #
    hash_text_type = {
        "" : TextType.TEXT,
        "**" : TextType.BOLD,
        "*" : TextType.ITALIC,
        "`" : TextType.CODE
    }
    #
    for node in old_nodes:
        # do something
        split_node_on_delimiter = node.text.split(delimiter)
        for i in range(len(split_node_on_delimiter)):
            #
            if len(split_node_on_delimiter) % 2 != 1:
                raise Exception('Invalid markdown provided.')
            #
            item = split_node_on_delimiter[i]
            #
            # 
            if i % 2 == 0:
                new_node = TextNode(item, TextType.TEXT)
            else:
                new_node = TextNode(item, hash_text_type[delimiter])
            #
            output.append(new_node)
    #
    return output

# TODO:// READ AND LEARN FROM THIS BELOW. IT IS THE VERSION THAT THEY CAME UP WITH. THEN USE IT TO FIX MY VERSION ABOVE. DON'T COPY THEM BUT STEAL WHAT IS USEFULL
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


