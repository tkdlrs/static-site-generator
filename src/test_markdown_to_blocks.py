import unittest

from markdown_to_blocks import markdown_to_blocks, block_to_block_type

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
    def test_block_to_block_type(self):
        header_markdown = "# This is a heading"
        header_type = block_to_block_type(header_markdown)
        self.assertEqual(header_type, "heading")
        #
        pargraph_markdown = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        paragraph_type = block_to_block_type(pargraph_markdown)
        self.assertEqual(paragraph_type, "paragraph")
        #
        unorder_list_markdown = "* This is a list\n* with items"
        unorder_list_type = block_to_block_type(unorder_list_markdown)
        self.assertEqual(unorder_list_type, "unordered_list")
        #
        unorder_minus_list_markdown = "- This is a list\n- with items"
        unorder_minus_list_type = block_to_block_type(unorder_minus_list_markdown)
        self.assertEqual(unorder_minus_list_type, "unordered_list")
        #
        order_list_markdown = "1. This is a list\n2. with items\n3. and things.\n4. even stuff"
        order_list_type = block_to_block_type(order_list_markdown)
        self.assertEqual(order_list_type, "ordered_list")
        #
        quote_markdown = ">this is a quote"
        quote_type = block_to_block_type(quote_markdown)
        self.assertEqual(quote_type, "quote")
        #
        code_markdown = "```\n<h1>html is totally code</h1>```"
        code_type = block_to_block_type(code_markdown)
        self.assertEqual(code_type, "code")
    
    # Tests from the guided project....
    def test_block_to_block_types(self):
        # they needed these...
        # okay I need to be honest the way Boot.dev came up with is gross to me. It's a lot of if/elif/else and '.startswith()' checks... 
        block_type_paragraph = "paragraph"
        block_type_heading = "heading"
        block_type_code = "code"
        block_type_quote = "quote"
        block_type_olist = "ordered_list"
        block_type_ulist = "unordered_list"
        #
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

#
if __name__ == "__main__":
    unittest.main()

#
