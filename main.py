from ast import For
import shutil
from pathlib import Path
from colorama import Fore

dirs = [
    ["~/.config","config"],
    ["/etc/shadowsocks-rust/","shadowsocks"],
    ["~/.ssh","dotfiles/ssh"]
]
files = [
    ["~/.zshrc","dotfiles/zshrc"]
]

def dir_backup():
    for x in dirs:
        new = Path(x[0]).expanduser()
        if not new.exists():
            print(Fore.RED,x[0],": no such directory")
            continue
        x[0] = str(new.resolve())
        try:
            shutil.copytree(src=x[0],dst=x[1],ignore_dangling_symlinks=True,dirs_exist_ok=True)
        except shutil.Error as error:
            print(Fore.YELLOW,"socket files or something are not copied")
        except FileNotFoundError as error:
            raise(error)
            

def file_backup():
    for x in files:
        new = Path(x[0]).expanduser()
        if not new.exists():
            print(Fore.RED,x[0],": no such file")
            continue
        x[0] = str(new.resolve())
        try:
            shutil.copyfile(src=x[0],dst=x[1])
        except FileNotFoundError as error:
            raise(error)
        except IsADirectoryError:
            print(Fore.RED,"u must write a path/to/file to files",Fore.WHITE)


def main():
    dir_backup()
    file_backup()

if __name__ == "__main__":
    main()
