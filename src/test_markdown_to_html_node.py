import unittest 
from markdown_to_html_node import markdown_to_html_node
from textnode import TextNode

'''
'''
class TestMarkDownToHTMLNode(unittest.TestCase):
    def test_sanity_check(self):
        self.assertEqual(2, 2)
    #
    def test_basics(self):
        markdown_document = """
# header 1 

Tongue pork belly rump capicola biltong kielbasa. Tri-tip **meatball** beef ribs frankfurter prosciutto brisket pig. 
Turkey rump pastrami, **landjaeger** kevin sausage jerky ribeye biltong pancetta flank.  
*Bresaola* picanha pastrami, porchetta shank tenderloin ham filet mignon turducken ground round andouille tongue brisket. 
Meatball prosciutto ham hock, drumstick hamburger cupim pork loin filet mignon.

## header 2 

Shoulder landjaeger ribeye, biltong andouille pastrami pig shankle kevin boudin meatloaf jowl. 
Salami landjaeger strip steak short ribs pork chuck. 
**Cow pork belly** ham hock sirloin beef ribs pork chop turkey *prosciutto* capicola fatback brisket pig kevin drumstick pastrami. 
Porchetta chicken chuck venison, tenderloin ribeye tri-tip prosciutto meatball chislic ham pancetta landjaeger short ribs turducken. 
Pancetta alcatra chuck pastrami pork belly. Buffalo ground round short ribs frankfurter. 
Hamburger capicola jerky shankle meatloaf salami tongue filet mignon bresaola turducken rump beef ribs ham hock ball tip buffalo.

### header 3 

* bullet one thing
* bullet list two  
* 3 bullet list

## header 2

>"This is a quote." -someone 

## header 2

Shoulder landjaeger ribeye, biltong andouille pastrami pig shankle kevin boudin meatloaf jowl. 
Salami landjaeger strip steak short ribs pork chuck. 
**Cow pork belly** ham hock sirloin beef ribs pork chop turkey *prosciutto* capicola fatback brisket pig kevin drumstick pastrami.
Porchetta chicken chuck venison, tenderloin ribeye tri-tip prosciutto meatball chislic ham pancetta landjaeger short ribs turducken.
Pancetta alcatra chuck pastrami pork belly.
Buffalo ground round short ribs frankfurter. 
Hamburger capicola jerky shankle meatloaf salami tongue filet mignon bresaola turducken rump beef ribs ham hock ball tip buffalo.

1. one
2. two
3. three
4. four

## level 2 header

```
**html is totally code**
*I'm serious*
```

""" 
        # markdown_document_node = TextNode(markdown_document)
        conversion = markdown_to_html_node(markdown_document)

        # print("-----+-----")
        # print(conversion, "conversion")
        # print("-----+-----")
        # I'm not sure of what I would compare this too.
        self.assertEqual(conversion, conversion)

    #
    def test_header(self):
        md = """
# this should be an h1
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>this should be an h1</h1></div>")

    #
    def test_simple_ordered_list(self):
        md = """
1. This is a list
2. with items
3. and *more* items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ol></div>",
        )
    #
    def test_simple_bullet_list(self):
        md = """
- This is a list
- with items
- and *more* items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul></div>",
        )

    ##### TESTs stolen from the guided project.
    def test_paragraph(self):
            md = """
    This is **bolded** paragraph text in a p tag here
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

    This is another paragraph with *italic* text and `code` here

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
- and *more* items

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


#
if __name__ == "__main__":
    unittest.main()





