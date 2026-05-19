from textnode import TextNode, TextType
from pathlib import PurePath, Path
from markdown import *
import os
import shutil

def main():
    copy_folder = "static/"
    paste_folder = "public/"
    copy_to(copy_folder,paste_folder)
    generate_pages_recursive("content","template.html","public")
    print("done")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_contents = os.listdir(dir_path_content)

    for item in dir_contents:
        if os.path.isfile(os.path.join(dir_path_content,item)):
            if PurePath(os.path.join(dir_path_content,item)).suffix==".md":
                generate_page(os.path.join(dir_path_content,item),template_path,Path(os.path.join(dest_dir_path,item)).with_suffix(".html"))
        elif os.path.isdir(os.path.join(dir_path_content,item)):
            generate_pages_recursive(os.path.join(dir_path_content,item),template_path,os.path.join(dest_dir_path,item))


def copy_to(copy_folder,paste_folder):
    clear_target_folder(paste_folder)
    copy_contents = os.listdir(copy_folder)

    for item in copy_contents:
        if os.path.isdir(copy_folder+item):
            os.mkdir(paste_folder+item)
            copy_to(os.path.join(copy_folder,item),os.path.join(paste_folder,item))
        else:
            shutil.copy(os.path.join(copy_folder,item),os.path.join(paste_folder,item))

def clear_target_folder(target):
    if os.path.exists(target):
        shutil.rmtree(target)
        os.mkdir(target)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, encoding="utf-8") as from_file:
        from_md = from_file.read()

    with open(template_path, encoding="utf-8") as template_file:
        template_md = template_file.read()

    html_string = markdown_to_html_node(from_md).to_html()
    title = extract_title(from_md)

    template_md = template_md.replace("{{ Title }}",title).replace("{{ Content }}", html_string)
    
    os.makedirs(os.path.dirname(dest_path),exist_ok=True)
    with open(dest_path, encoding="utf-8",mode = 'w') as dest_file:
        dest_file.write(template_md)

if __name__ == "__main__":
    main()
