import os
#
from generate_page import generate_page
#
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    #
    current_source_listing = os.listdir(dir_path_content)
    #
    for item_to_bring_over in current_source_listing:
        #
        current_item_to_pull_path = f"{dir_path_content}/{item_to_bring_over}"
        current_path_to_pull_destination = f"{dest_dir_path}/{item_to_bring_over}" 
        #
        if os.path.isfile(current_item_to_pull_path):
          # This is a file. Pull it over
          page_name = current_path_to_pull_destination[:-2]
          generate_page(current_item_to_pull_path, template_path, f"{page_name}html")
        else:
            # This is a directory.
            # Make it in the destination folder.
            os.mkdir(current_path_to_pull_destination)
            # Use the next source and next destination and recurse.
            generate_pages_recursive(current_item_to_pull_path, template_path, current_path_to_pull_destination)   
    return

#