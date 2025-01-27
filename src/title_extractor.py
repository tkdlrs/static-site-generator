# pull out the first header for the title tag.
def extract_title(markdown):
    title = ""
    markdown_lines = markdown.split("\n")
    for line in markdown_lines:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    #
    raise Exception("Missing a main header for page title")