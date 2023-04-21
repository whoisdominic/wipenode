import os
import shutil

def remove_node_modules(path):
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if name == 'node_modules':
                node_modules_path = os.path.join(root, name)
                print(f'Removing {node_modules_path}')
                shutil.rmtree(node_modules_path)

if __name__ == '__main__':
    dir_to_search = input('Enter the directory to search for "node_modules" folders: ')
    remove_node_modules(dir_to_search)
    
