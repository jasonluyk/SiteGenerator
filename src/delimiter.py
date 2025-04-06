from htmlnode import *
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
        else:
            text = old_node.text

        if delimiter in text:
            start_pos = text.find(delimiter)
            end_pos = text.find(delimiter, start_pos + len(delimiter))
            if end_pos == -1:
                raise Exception(f"No closing delimiter found for {delimiter}")
            
            before_text = text[:start_pos]
            delimiter_text = text[start_pos + len(delimiter):end_pos]
            after_text = text[end_pos + len(delimiter):]

            if before_text:
                 result.append(TextNode(before_text, TextType.TEXT))

            result.append(TextNode(delimiter_text, text_type))

            if after_text:
                result.append(TextNode(after_text, TextType.TEXT))



        else:
            result.append(old_node)

    return result
