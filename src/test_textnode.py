import unittest

from textnode import *
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node not equal", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_link_image_not_eq(self):
        node = TextNode("This is an link node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is an image node", TextType.IMAGE, "/path/to/image.jpg")
        self.assertNotEqual(node, node2)

    def test_link_eq(self):
        node = TextNode("This is an link node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is an link node", TextType.LINK, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_link_not_eq(self):
        node = TextNode("This is an link node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is not equal", TextType.LINK, "https://www.facebook.com")
        self.assertNotEqual(node, node2)

    ###TEXT NODE TO HTML NODE TESTS###

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic text node")

    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_image(self):
        node = TextNode("This is a image node", TextType.IMAGE, "/path/to/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {
            "src": "/path/to/image.jpg",
            "alt": "This is a image node"
        })

if __name__ == "__main__":
    unittest.main()
