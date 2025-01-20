import unittest
from link_extractor import extract_markdown_links

"""
print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
"""
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