import sys
from pathlib import Path
from colorama import init, Fore, Style

init()

def display_directory_structure(path, indent=0):
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(" " * indent + Fore.BLUE + f"[DIR] {item.name}" + Style.RESET_ALL)
                display_directory_structure(item, indent + 4)
            else:
                print(" " * indent + Fore.GREEN + f"[FILE] {item.name}" + Style.RESET_ALL)
    except PermissionError:
        print(" " * indent + Fore.RED + f"[ERROR] Немає доступу до {path.name}" + Style.RESET_ALL)

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Використовуйте команду: python search.py <шлях_до_директорії>" + Style.RESET_ALL)
        return

    directory_path = sys.argv[1]
    path = Path(directory_path)

    if not path.exists():
        print(Fore.RED + "Вказаний шлях не існує." + Style.RESET_ALL)
        return
    if not path.is_dir():
        print(Fore.RED + "Вказаний шлях не веде до директорії." + Style.RESET_ALL)
        return

    print(Fore.CYAN + f"Структура директорії: {path}" + Style.RESET_ALL)
    display_directory_structure(path)

if __name__ == "__main__":
    main()
