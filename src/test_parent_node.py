import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("p", "Hello")
        child2 = LeafNode("p", "World")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(parent.to_html(), "<div><p>Hello</p><p>World</p></div>")

    def test_to_html_missing_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "Oops")])

    def test_to_html_missing_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_to_html_invalid_children_type_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", "not a list")

    def test_to_html_deeply_nested(self):
        leaf = LeafNode("em", "deep")
        inner = ParentNode("span", [leaf])
        mid = ParentNode("section", [inner])
        outer = ParentNode("div", [mid])
        self.assertEqual(outer.to_html(), "<div><section><span><em>deep</em></span></section></div>")
