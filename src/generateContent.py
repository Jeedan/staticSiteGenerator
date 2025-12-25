import os
from extracttitle import extract_title
from markdown_to_html import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, base_path="/"):
    abs_from_path = os.path.abspath(from_path)
    abs_template_path = os.path.abspath(template_path)
    abs_dest_path = os.path.abspath(dest_path)

    try:
        print(f"Generating page from {abs_from_path} using {abs_template_path}")
        with open(abs_from_path, "r") as f:
            markdown_file = f.read()
        
        with open(abs_template_path, "r") as f:
            template_file = f.read()

        html_string = markdown_to_html_node(markdown_file).to_html()
        #print(f"html_string: {html_string}")
        title = extract_title(markdown_file)
        html_page = template_file.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
        html_page = html_page.replace("href=\"/", f"href=\"{base_path}").replace("src=\"/", f"src=\"{base_path}")
        #print(f"title: {title}")

        dir_name = os.path.dirname(abs_dest_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        with open(abs_dest_path, "w") as f:
            f.write(html_page)
    except Exception as e:
        print(f"Error generating page: {e}")
        raise e
    print(f"Successfully generated Page at {abs_dest_path}")

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path, base_path):
    abs_dir_path_content = os.path.abspath(dir_path_content)
    abs_dest_dir_path =  os.path.abspath(dest_dir_path)
    print(f"Generating pages recursively from {abs_dir_path_content} to {abs_dest_dir_path}")
    try:
        for dirpath, dirnames, filenames in os.walk(abs_dir_path_content):
            for file in filenames:
                print(f"DEBUG file: {file} in dirpath: {dirpath}")
                if file.endswith(".md"):
                    # relative path from content/ directory and all its sub directories
                    rel_dir = os.path.relpath(dirpath, abs_dir_path_content)
                    # full path to markdown file
                    from_path = os.path.join(dirpath, file)
                    # destination path with folder structure added to it
                    dest_subdir = os.path.join(abs_dest_dir_path, rel_dir)
                    # destination file path with .html extension for files
                    dest_path = os.path.join(dest_subdir, file[:-3] + ".html")
                    print(f"DEBUG rel_dir: {rel_dir}")
                    print(f"DEBUG from_path: {from_path}")
                    print(f"DEBUG dest_subdir: {dest_subdir}")
                    print(f"DEBUG dest_path: {dest_path}")
                    # recursively generate pages
                    generate_page(from_path, template_path, dest_path, base_path)
    except Exception as e:
        print(f"Error generating pages recursively: {e}")
        raise e
    
    print(f"Successfully generated Pages at {abs_dest_dir_path}")