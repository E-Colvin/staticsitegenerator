import unittest

from textnode import TextNode, TextType
from markdown import *

class TestMarkdownBlocks(unittest.TestCase):
    def test_extract_title_middle(self):
        md = """
random leading text
# Toast!
Some extra stuff
"""

        self.assertEqual(extract_title(md),"Toast!")\
            
    def test_extract_title(self):
        md = """
# Toast!
Some extra stuff
"""

        self.assertEqual(extract_title(md),"Toast!")\

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
        def test_paragraphs(self):
            md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            )

        def test_codeblock(self):
            md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
            )

        def test_block_to_block_types(self):
            block = "# heading"
            self.assertEqual(block_to_blocktype(block), BlockType.HEADING)
            block = "```\ncode\n```"
            self.assertEqual(block_to_blocktype(block), BlockType.CODE)
            block = "> quote\n> more quote"
            self.assertEqual(block_to_blocktype(block), BlockType.QUOTE)
            block = "- list\n- items"
            self.assertEqual(block_to_blocktype(block), BlockType.UNORDERED_LIST)
            block = "1. list\n2. items"
            self.assertEqual(block_to_blocktype(block), BlockType.ORDERED_LIST)
            block = "paragraph"
            self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

        def test_md_to_blocks_and_block_to_block_type(self):
            md = """
# A heading

###### another heading

####### an invalid heading

```
 some code ```

> a quote

- item a
- item b
- item c

1. item 1
2. item 2
3. item 3

1. item 1
4. item 2
3. item 3

"""
            blocks = markdown_to_blocks(md)
            block_types = []
            for block in blocks:
                block_types.append(block_to_blocktype(block))
            expected_types = [BlockType.HEADING,BlockType.HEADING,BlockType.PARAGRAPH,BlockType.CODE,BlockType.QUOTE,BlockType.UNORDERED_LIST,BlockType.ORDERED_LIST,BlockType.PARAGRAPH]
            self.assertListEqual(block_types,expected_types)


        def test_block_to_blocktype_paragraph(self):
            md = """item A item B"""
            self.assertEqual(block_to_blocktype(md),BlockType.PARAGRAPH)

        def test_block_to_blocktype_ordered_list(self):
            md = """1. item A
2. item B"""
            self.assertEqual(block_to_blocktype(md),BlockType.ORDERED_LIST)

        def test_block_to_blocktype_unordered_list(self):
            md = """- item A
- item B"""
            self.assertEqual(block_to_blocktype(md),BlockType.UNORDERED_LIST)

        def test_block_to_blocktype_quote(self):
            md = "> This should be a quote"
            self.assertEqual(block_to_blocktype(md),BlockType.QUOTE)

        def test_block_to_blocktype_code(self):
            md = """```
Some code```"""
            self.assertEqual(block_to_blocktype(md),BlockType.CODE)

        def test_block_to_blocktype_headers(self):
            md = ("""
# A heading

###### another heading

####### an invalid heading


""")
            blocks = markdown_to_blocks(md)
            block_types = []
            for block in blocks:
                block_types.append(block_to_blocktype(block))
            self.assertListEqual(block_types,[BlockType.HEADING,BlockType.HEADING,BlockType.PARAGRAPH])


        def test_markdown_to_blocks(self):
            md = ("""
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
""")
            blocks = markdown_to_blocks(md)
            
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_markdown_to_blocks_large_split(self):
            md = ("""
This is a paragraph



With a big split""")

            blocks = markdown_to_blocks(md)
            self.assertListEqual(blocks,
            ["This is a paragraph","With a big split"])

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnode(text)

        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ]

        self.assertListEqual(new_nodes,expected_nodes)

class TestMarkdownImagesAndLinks(unittest.TestCase):
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

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
            "This is text with a [link](https://boot.dev) and [another link](https://wikipedia.org) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://wikipedia.org"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_multiple_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ]
        self.assertListEqual(new_nodes,expected_nodes)

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

    def test_split_images_and_links(self):
        node = TextNode("This is a text with an ![image](boot.dev/image) and a [link](boot.dev/link)",TextType.TEXT)
        new_nodes = split_nodes_link([node])
        new_nodes = split_nodes_image(new_nodes)
        expected_nodes = [
            TextNode("This is a text with an ",TextType.TEXT),
            TextNode("image",TextType.IMAGE, "boot.dev/image"),
            TextNode(" and a ",TextType.TEXT),
            TextNode("link",TextType.LINK,"boot.dev/link"),
        ]

        self.assertListEqual(new_nodes,expected_nodes)
    
    def test_split_images_and_links_again_opposite_call_order(self):
        node = TextNode("This is a text with an ![image](boot.dev/image) and a [link](boot.dev/link)",TextType.TEXT)
        new_nodes = split_nodes_image([node])
        #print(new_nodes)
        new_nodes = split_nodes_link(new_nodes)
        #print(new_nodes)
        expected_nodes = [
            TextNode("This is a text with an ",TextType.TEXT),
            TextNode("image",TextType.IMAGE, "boot.dev/image"),
            TextNode(" and a ",TextType.TEXT),
            TextNode("link",TextType.LINK,"boot.dev/link"),
        ]

        self.assertListEqual(new_nodes,expected_nodes)

class TestMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image 2](https://i.imgur.com/img2.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"),("image 2","https://i.imgur.com/img2.png")], matches)

    def test_no_alt_text(self):
        matches = extract_markdown_images("None image part ![](https://i.imgur.com/zfafdsa.jpg)")

        self.assertListEqual([("","https://i.imgur.com/zfafdsa.jpg")],matches)

class TestMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Some text with a [link](boot.dev)"
        )

        self.assertListEqual([("link","boot.dev")],matches)

    def test_multiple_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],matches)

class TestMarkdownDelimiter(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertListEqual(new_nodes,expected_nodes)

    def test_bold_delimiter(self):
        node = TextNode("This is text with a **code block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertListEqual(new_nodes,expected_nodes)
    
    def test_multiple_bold_delimiter(self):
        node = TextNode("**This** is `text` with a **code block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected_nodes = [
            TextNode("This",TextType.BOLD),
            TextNode(" is `text` with a ", TextType.TEXT),
            TextNode("code block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertListEqual(new_nodes,expected_nodes)

    def test_italics_delimiter(self):
        node = TextNode("_This is text with a code block word_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        expected_nodes = [
            TextNode("This is text with a code block word", TextType.ITALIC)
        ]

        self.assertListEqual(new_nodes,expected_nodes)

    def test_multiple_nodes(self):
        node1 = TextNode("This is text with a **code block** word", TextType.TEXT)
        node2 = TextNode("**This** is `text` with a **code block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1,node2], "**", TextType.BOLD)

        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This",TextType.BOLD),
            TextNode(" is `text` with a ", TextType.TEXT),
            TextNode("code block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertListEqual(new_nodes,expected_nodes)

    def test_nested_calls(self):
        node = TextNode("**This** is `text` with a **code block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes,"`",TextType.CODE)
        
        expected_nodes = [
            TextNode("This",TextType.BOLD),
            TextNode(" is ",TextType.TEXT),
            TextNode("text",TextType.CODE),
            TextNode(" with a ", TextType.TEXT),
            TextNode("code block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes,expected_nodes)
    
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )