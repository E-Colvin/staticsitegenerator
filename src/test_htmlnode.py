import unittest

from htmlnode import HTMLNode,LeafNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a","This is a value paragraph",props={"href": "https://www.google.com","blah":"irjaoipoiu"})
        self.assertEqual(node.props_to_html()," href=\"https://www.google.com\" blah=\"irjaoipoiu\"")
    
    def test_values(self):
        node = HTMLNode("a","This is a value paragraph",props={"href": "https://www.google.com","blah":"irjaoipoiu"})

        self.assertEqual(node.tag,"a")
        self.assertEqual(node.value,"This is a value paragraph")
        self.assertEqual(node.children,None)
        self.assertEqual(node.props,{"href": "https://www.google.com","blah":"irjaoipoiu"})

    def test_repr(self):
        node = HTMLNode("a","This is a value paragraph")
        self.assertEqual(node.__repr__(),f"Tag: a\nValue: This is a value paragraph\nChildren: None\nProps: None")

    def test_repr2(self):
        node = HTMLNode("a","This is a value paragraph",props={"href": "https://www.google.com","blah":"irjaoipoiu"})
        self.assertEqual(node.__repr__(),f"Tag: a\nValue: This is a value paragraph\nChildren: None\nProps: {{\'href\': \'https://www.google.com\', \'blah\': \'irjaoipoiu\'}}")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_values(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(node.tag,"a")
        self.assertEqual(node.value,"Click me!")
        self.assertEqual(node.props,{"href": "https://www.google.com"})
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
if __name__ == "__main__":
    unittest.main()