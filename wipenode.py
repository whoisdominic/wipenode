import os
import shutil


class Fore:
    GREEN = "\033[32m"
    RED = "\033[31m"
    RESET = "\033[0m"


def get_dir_size(path):
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size


def format_size(size):
    if size >= 1024**3:  # Gigabytes
        return f"{size / (1024**3):.2f} GB"
    else:  # Megabytes
        return f"{size / (1024**2):.2f} MB"


def remove_node_modules(path):
    total_memory_freed = 0
    for root, dirs, _ in os.walk(path):
        for name in dirs:
            if name == 'node_modules':
                node_modules_path = os.path.join(root, name)
                memory_freed = get_dir_size(node_modules_path)
                total_memory_freed += memory_freed
                print(
                    f"{Fore.GREEN}Removing {node_modules_path} ({format_size(memory_freed)}){Fore.RESET}")
                try:
                    shutil.rmtree(node_modules_path)
                except Exception as e:
                    print(
                        f"{Fore.RED}An error occurred while trying to remove {node_modules_path}: {e}{Fore.RESET}")
    return total_memory_freed


if __name__ == '__main__':
    try:
        dir_to_search = input(
            'Enter the directory to search for "node_modules" folders: ')
        total_memory_freed = remove_node_modules(dir_to_search)
        print(
            f"{Fore.GREEN}Total memory freed: {format_size(total_memory_freed)}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Fore.RESET}")
