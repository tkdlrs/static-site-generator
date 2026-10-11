import sys
import os
import shutil
#
from textnode import TextNode, TextType
from generate_page import generate_page
from generate_multiple_pages import generate_pages_recursive

# recursively pull over all the static assets
def copy_directory_over(source_path, destination_path):
    #
    current_source_listing = os.listdir(source_path)
    #
    for item_to_copy in current_source_listing:
        #
        current_item_to_copy_path = f"{source_path}/{item_to_copy}"
        current_path_to_copy_destination = f"{destination_path}/{item_to_copy}" 
        #
        if os.path.isfile(current_item_to_copy_path):
          # This is a file. Copy it over
          shutil.copy(current_item_to_copy_path, current_path_to_copy_destination)
        else:
            # This is a directory.
            # Make it in the destination folder.
            os.mkdir(current_path_to_copy_destination)
            # Use the next source and next destination and recurse.
            copy_directory_over(current_item_to_copy_path, current_path_to_copy_destination )   
    return
#
def main():
    print("-----+ LET US BEGIN +-----")
    basepath = "/"
    if len(sys.argv) >= 2:
        basepath = sys.argv[1]
    # 
    print("basepath", basepath)
    output_directory = "docs"
    # 
    current_directory = os.curdir
    # START SECTION ~THAT IS MAKING/REMAKING THE 'public' DIRECTORY
    public_directory_exists = os.path.exists(output_directory)
    if public_directory_exists:
         # It does exist, so delete it. Then re-make it.
        print('Previous version existed. Deleting and re-creating.')
        # delete it..
        shutil.rmtree(output_directory)
        # remake it.
        os.mkdir(output_directory)
    else:
        os.mkdir(output_directory)
    # END SECTION
    # START SECTION ~THAT IS HANDING THE COPYING OF FILES.    
    src_path = f"{current_directory}/static"
    dst_path = f"{current_directory}/{output_directory}"
    #
    copy_directory_over(src_path, dst_path)
    # END SECTION
    # START SECTION ~That generates the pages
    content_source = f"{current_directory}/content"
    content_destination = f"{current_directory}/{output_directory}"
    #
    generate_pages_recursive(content_source, "./template.html", content_destination, basepath)
    # END SECTION
    print("-----+ LET IT END +-----")
#
main()
