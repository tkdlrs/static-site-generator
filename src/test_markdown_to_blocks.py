import unittest

from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(2, 2)
    #
    def test_basic_case(self):
        input_text = "# This is a heading \n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n\n"
        list_text_blocks = ["# This is a heading",
                            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                            ]
        
        self.assertEqual(markdown_to_blocks(input_text), list_text_blocks)
    
    # additional cases from the guided project 
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

#
if __name__ == "__main__":
    unittest.main()

#
