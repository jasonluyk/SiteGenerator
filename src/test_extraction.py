import unittest
from extract import *
from textnode import *

def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


def test_extract_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev)")
    self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )


def test_split_links(self):
    node = TextNode(
        "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
            TextNode(" with text that follows", TextType.TEXT),
        ],
        new_nodes,
    )


def test_text_to_textnodes(self):
    nodes = text_to_textnodes(
        "This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
    )
    self.assertListEqual(
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ],
        nodes,
    )
