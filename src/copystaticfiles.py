import os
import shutil

def copy_files_recursively(static_dir, output_dir):
    """
    Copy static files from the static directory to the output directory.
    """
    try:
        static_dir = os.path.abspath(static_dir)
        output_dir = os.path.abspath(output_dir)
        print(f"Preparing to copy static files from '{static_dir}' to '{output_dir}'")
        #full path
        if not os.path.exists(static_dir):
            print(f"Static directory '{static_dir}' does not exist. Skipping copy.")
            return
        
        # copy contents of static into public
        for name in os.listdir(static_dir):
            print(f"Found item in static: {name}")
            from_path = os.path.join(static_dir, name)
            dest_path = os.path.join(output_dir, name)
            if os.path.isfile(from_path):
                shutil.copy(from_path, dest_path)
            else:
                os.makedirs(dest_path, exist_ok=True)
                copy_files_recursively(from_path, dest_path)
                

        print(f"Successfully copied files '{static_dir}' copied to '{output_dir}'")
    except Exception as e:
        print(f"An error occured: {e}")
        return
    
## EXAMPLES
# for root, dirs, files in os.walk(static_dir):
#     # get our current relative path
#     rel_path = os.path.relpath(root, static_dir)
#     # determine destination directory
#     # if we are at the root of static_dir, rel_path will be "."
#     dest_dir = (output_dir if rel_path == "." else os.path.join(output_dir, rel_path))

#     #create directories
#     os.makedirs(dest_dir, exist_ok=True)
#     # copy the files
#     for file in files:
#         src_file = os.path.join(root, file)
#         dest_file = os.path.join(dest_dir, file)
#         shutil.copy2(src_file, dest_file)
    # alternatively, we could use shutil.copytree
    # for item in os.listdir(static_dir):
    #     src_path = os.path.join(static_dir, item)
    #     dst_path = os.path.join(output_dir, item)
    #     if os.path.isdir(src_path):
    #         shutil.copytree(src_path, dst_path)
    #     else:
    #         shutil.copy2(src_path, dst_path)