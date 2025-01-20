import unittest
from image_extractor import extract_markdown_images
"""
text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
"""

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