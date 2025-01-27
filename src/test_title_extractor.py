import unittest
from title_extractor import extract_title
#
class TestTitleExtractor(unittest.TestCase):
    def test_sanity_check(self):
        self.assertEqual(2, 2)
    #
    def test_missing_header(self):
        markdown = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        with self.assertRaises(Exception):
            extract_title(markdown)
    #
    def test_grabs_header(self):        
        markdown = "# This represents a header"
        self.assertEqual(extract_title(markdown), "This represents a header")



#
if __name__ == "__main__":
    unittest.main()

 