import os
import shutil
#
from textnode import TextNode, TextType

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
    # node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # print(node)
    current_directory = os.curdir
    current_directory_listing = os.listdir(current_directory)
    print(current_directory_listing, "current_directory_listing before")

    # SECTION THAT IS MAKING/REMAKING THE 'public' DIRECTORY
    public_directory_exists = os.path.exists("public")
    if public_directory_exists:
         # It does exist, so delete it. Then re-make it.
        print('delete it them make it.')
        # UNCOMMENT THIS LATER. IT STILL SCARES ME. I DON'T WANT TO DOING SOMETHING STUPID ON ACCIDENT.
        # delete it..
        shutil.rmtree("public")
        # remake it.
        os.mkdir("public")
    else:
        os.mkdir("public")
    
    current_directory_listing = os.listdir(current_directory)
    print(current_directory_listing, "current_directory_listing after")
    # END SECTION

    # # SECTION THAT IS HANDING THE COPYING OF FILES.
    static_directory_listing = ()
    print(static_directory_listing, "static_directory_listing after")
    
    src_path = f"{current_directory}/static";
    dst_path = f"{current_directory}/public";

    copy_directory_over(src_path, dst_path)

    # END SECTION
    print("-----+ LET IT END +-----")

#
main()
