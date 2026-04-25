from textnode import TextNode, TextType
import re

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