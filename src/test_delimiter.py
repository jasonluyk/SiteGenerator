import unittest
from textnode import TextNode, TextType
from delimiter import *  # Replace with your actual module name

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold_delimiter(self):
        # Test splitting with ** delimiter
        node = TextNode("This is text with a **bolded phrase** in it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "bolded phrase")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " in it")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
    
    def test_code_delimiter(self):
        # Test splitting with ` delimiter
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        
