from markdown_to_html_node import markdown_to_html_node
from title_extractor import extract_title
# 
def generate_page(from_path, template_path, dest_path):
   #
   print(f"Generating page from {from_path} to {dest_path} using {template_path}")
   
   # Get the content to make the markup.
   with open(from_path, "r", encoding="utf-8") as path_file:
    path_file_content = path_file.read()
    path_file.close()
    

   # Get the markup template.
   with open(template_path, "r", encoding="utf-8") as template_file:
    template_file_content = template_file.read()
    template_file.close()
   
   # Take the markdown content and make it HTML
   html_nodes = markdown_to_html_node(path_file_content)
   html_markup = html_nodes.to_html()
   title_is = extract_title(path_file_content)

   # Update the HTML content from template to have the Markdown file 
   template_file_content = template_file_content.replace("{{ Title }}", title_is)
   template_file_content = template_file_content.replace("{{ Content }}", html_markup)

   # Write the new and updated HTML to a new file.
   with open(dest_path, 'w', encoding="utf-8") as dest_file:
    dest_file.write(template_file_content)
    dest_file.close()

   #
   return
#