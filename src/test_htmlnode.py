import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_single_prop(self):
        node = HTMLNode(tag="a", props={"href": "www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="www.google.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(tag="img", props={"src": "image.png", "alt": "A test image"})
        self.assertEqual(node.props_to_html(), ' src="image.png" alt="A test image"')

    def test_props_to_html_empty_props(self):
        node = HTMLNode(tag="div", props={})
        self.assertEqual(node.props_to_html(), '')

if __name__ == "__main__":
    unittest.main()