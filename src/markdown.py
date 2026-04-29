from textnode import TextNode, TextType
import re

def markdown_to_blocks(markdown):
    blocks = []
    temp_blocks = markdown.split("\n\n")

    for text in temp_blocks:
        if text == "":
            continue
        blocks.append(text.strip())

    return blocks

def text_to_textnode(text):
    start_node = TextNode(text,TextType.TEXT)
    new_nodes = [start_node]
    new_nodes = split_nodes_delimiter(new_nodes,"**",TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes,"_",TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes,"`",TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_text = node.text.split(delimiter)

        if len(split_text) % 2 == 0:
            raise Exception("Markdown delimiters not balanced.")
        
        for index in range(len(split_text)):
            if split_text[index] == "":
                continue
            new_nodes.append(TextNode(split_text[index],text_type if index % 2 ==1 else TextType.TEXT))

    return new_nodes
        
def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return links

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        node_text = node.text
        images = extract_markdown_images(node_text)

        if not images:
            new_nodes.append(node)
            continue
        
        current_text = node_text
        for image in images:
            delimiter = f"![{image[0]}]({image[1]})"
            split_text = current_text.split(delimiter,1)

            if len(split_text) != 2:
                raise Exception("Invalid markdown, image sections not closed")

            current_text = split_text[1]
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0],TextType.TEXT))
            new_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))

        if split_text[1] != "":
            new_nodes.append(TextNode(split_text[1],TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        node_text = node.text
        links = extract_markdown_links(node_text)

        if not links:
            new_nodes.append(node)
            continue
        
        current_text = node_text
        for link in links:
            delimiter = f"[{link[0]}]({link[1]})"
            split_text = current_text.split(delimiter,1)

            if len(split_text) != 2:
                raise Exception("Invalid markdown, link sections not closed")

            current_text = split_text[1]
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0],TextType.TEXT))
            new_nodes.append(TextNode(link[0],TextType.LINK,link[1]))
    
    if split_text[1] != "":
            new_nodes.append(TextNode(split_text[1],TextType.TEXT))

    return new_nodes