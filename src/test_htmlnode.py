import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()