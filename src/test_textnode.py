import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url,None)

    def test_repr_url(self):
        node = TextNode("This is a text node", TextType.BOLD,"boot.dev")
        exp_repr = "TextNode(This is a text node, bold, boot.dev)"
        self.assertEqual(node.__repr__(),exp_repr)
    
    def test_repr_nourl(self):
        node = TextNode("This is a text node", TextType.BOLD,)
        exp_repr = "TextNode(This is a text node, bold, None)"
        self.assertEqual(node.__repr__(),exp_repr)

    def test_textype(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_dif_text(self):
        node = TextNode("This is a text node!", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_textype(self):
        node = TextNode("This is a text node", TextType.ITALIC, "boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()