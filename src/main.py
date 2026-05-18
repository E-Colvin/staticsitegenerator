from textnode import TextNode, TextType
from markdown import *
import os
import shutil

def main():
    copy_folder = "static/"
    paste_folder = "public/"
    copy_to(copy_folder,paste_folder)
    generate_page("content/index.md","template.html","public/index.html")
    print("done")

def copy_to(copy_folder,paste_folder):
    clear_target_folder(paste_folder)
    copy_contents = os.listdir(copy_folder)

    for item in copy_contents:
        if os.path.isdir(copy_folder+item):
            os.mkdir(paste_folder+item)
            copy_to(copy_folder+item+"/",paste_folder+item+"/")
        else:
            shutil.copy(copy_folder+item,paste_folder+item)

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
