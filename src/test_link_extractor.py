import unittest
from link_extractor import extract_markdown_links, split_nodes_link
from textnode import TextNode, TextType

#
class TestLinkExtractor(unittest.TestCase):
    def test_basic(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        an_example = extract_markdown_links(text)
        #
        self.assertEqual(an_example, 
                            [
                             ("to boot dev", "https://www.boot.dev"),
                             ("to youtube", "https://www.youtube.com/@bootdotdev")
                            ]
                         )
        #
        self.assertEqual(type(an_example[0]), tuple)
        self.assertTupleEqual(an_example[0], ("to boot dev", "https://www.boot.dev"))
        #
        self.assertEqual(type(an_example[1]), tuple)
        self.assertTupleEqual(an_example[1], ("to youtube", "https://www.youtube.com/@bootdotdev")) 
    #
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )
    #
    def test_split_nodes_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes, [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
            ])
    #
    def test_split_out_single_link(self):
        node = TextNode("[Google](https://google.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes, [
            TextNode("Google", TextType.LINK, "https://google.com")])
    #
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


#