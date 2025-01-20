import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    #
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )
    
    #
    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    # Test that I came up with.
    def test_basics_text_to_html(self):
        plain_text_node = TextNode("PLAIN TEXT, should not yell.", TextType.TEXT)
        plain_html_node = text_node_to_html_node(plain_text_node)
        self.assertEqual(plain_html_node.to_html(), "PLAIN TEXT, should not yell.")
        #
        link_text_node = TextNode("Click here!", TextType.LINK, "https://www.boot.dev")
        plain_link_html_node = text_node_to_html_node(link_text_node)
        self.assertEqual(plain_link_html_node.to_html(), "<a href=\"https://www.boot.dev\">Click here!</a>")
        # Either they do not know how images work or something.
        # Anyways, this test fixes a bug in this guided project... 
        # That or maybe they were saving it for later as a learning opportunity.
        # Either way I've fixed it. it would have drove me crazy otherwise. 
        # I may be new to testing. But I am used to being burned, and this is a common easly avoided issue.
        image_as_text_node = TextNode("Boot Dev logo", TextType.IMAGE, "https://www.boot.dev/img/bootdev-logo-full-small.webp")
        image_as_markup = text_node_to_html_node(image_as_text_node)
        self.assertEqual(image_as_markup.to_html(), "<img src=\"https://www.boot.dev/img/bootdev-logo-full-small.webp\" alt=\"Boot Dev logo\" />")


if __name__ == "__main__":
    unittest.main()
