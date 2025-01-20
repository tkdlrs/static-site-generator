import unittest
from image_extractor import extract_markdown_images, split_nodes_image
from textnode import TextNode, TextType
#
class TestImageExtractor(unittest.TestCase):
    def test_basic(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        an_example = extract_markdown_images(text)
        #
        self.assertEqual(an_example, 
                            [
                             ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                             ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
                            ]
                         )
        #
        self.assertEqual(type(an_example[0]), tuple)
        self.assertTupleEqual(an_example[0], ("rick roll", "https://i.imgur.com/aKaOqIh.gif"))
        #
        self.assertEqual(type(an_example[1]), tuple)
        self.assertTupleEqual(an_example[1], ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"))

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    #
    def test_split_nodes_images(self):
        node = TextNode("This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            ])
    #
    def test_split_out_single_image(self):
        node = TextNode("![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")])

    #
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
    #
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
    #
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

#