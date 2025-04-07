import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()
