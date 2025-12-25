import os
import shutil
from copystaticfiles import copy_files_recursively
from textnode import TextNode, TextType
from generateContent import generate_pages_recursively
# move these into constants.py file later
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
STATIC_DIR = os.path.join(PROJECT_ROOT, "static")
PUBLIC_DIR = os.path.join(PROJECT_ROOT, "public")
MARKDOWN_DIR = os.path.join(PROJECT_ROOT,"content")
TEMPLATE_PATH = os.path.join(PROJECT_ROOT,"template.html")

def delete_public_directory():
   if os.path.exists(PUBLIC_DIR):
      if os.path.abspath(PUBLIC_DIR) == os.path.abspath("/"):
                raise RuntimeError("Refusing to delete root directory")
    
      if os.path.basename(PUBLIC_DIR) != "public":
         raise RuntimeError("Refusing to delete directory not named 'public'")
            
      shutil.rmtree(PUBLIC_DIR)
   os.makedirs(PUBLIC_DIR)


def main():
   # test image url: https://i.imgur.com/XGG62uL.png
   test_node = TextNode("test", TextType.LINK, "https://i.imgur.com/XGG62uL.png")
   print(test_node.__repr__()) 

   # delete public/ directory if it exists
   delete_public_directory()
   # generate index.html page from contents/index.md
   generate_pages_recursively(
   MARKDOWN_DIR,
   TEMPLATE_PATH,
   PUBLIC_DIR
)

   # copies files from static/ to public/
   copy_files_recursively(STATIC_DIR, PUBLIC_DIR)

if __name__ == "__main__":
    main()
