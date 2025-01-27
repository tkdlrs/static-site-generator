import os
import shutil
#
from textnode import TextNode, TextType
from generate_page import generate_page

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
    current_directory = os.curdir
    # START SECTION ~THAT IS MAKING/REMAKING THE 'public' DIRECTORY
    public_directory_exists = os.path.exists("public")
    if public_directory_exists:
         # It does exist, so delete it. Then re-make it.
        print('Previous version existed. Deleting and re-creating.')
        # UNCOMMENT THIS LATER. IT STILL SCARES ME. I DON'T WANT TO DOING SOMETHING STUPID ON ACCIDENT.
        # delete it..
        shutil.rmtree("public")
        # remake it.
        os.mkdir("public")
    else:
        os.mkdir("public")
    # END SECTION
    # START SECTION ~THAT IS HANDING THE COPYING OF FILES.    
    src_path = f"{current_directory}/static";
    dst_path = f"{current_directory}/public";
    #
    copy_directory_over(src_path, dst_path)
    # END SECTION
    # START SECTION ~That generates the pages
    generate_page("./content/index.md", './template.html', "./public/index.html")
    # END SECTION
    print("-----+ LET IT END +-----")
#
main()
