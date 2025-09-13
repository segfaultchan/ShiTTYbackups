import shutil #, sys
from pathlib import Path
from colorama import Fore
import json

# archive
arch_name="its_backup"
arch_format="zip"
arch_dir="./backup/"

# backup dirs/fils
dirs = [
    ["~/.config","config"],
    ["/etc/shadowsocks-rust/","shadowsocks"],
    ["~/.ssh","dotfiles/ssh"]
]
files = [
    ["~/.zshrc","dotfiles/zshrc"]
]
# exclude paths
exclude = ["config/discord",]

#def args_check():
#    args = sys.argv[1:]

def dir_backup():
    for x in dirs:
        new = Path(x[0]).expanduser()
        if not new.exists():
            print(Fore.RED,x[0],": no such directory")
            continue
        x[0] = str(new.resolve())
        try:
            shutil.copytree(src=x[0],dst=arch_dir+x[1],ignore_dangling_symlinks=True,dirs_exist_ok=True)
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
            shutil.copyfile(src=x[0],dst=arch_dir+x[1])
        except FileNotFoundError as error:
            raise(error)
        except IsADirectoryError:
            print(Fore.RED,"u must write a path/to/file to files",Fore.WHITE)

def excepts_delete():
    for x in exclude:
        try:
            shutil.rmtree(arch_dir+x)
        except FileNotFoundError as error:
            print(Fore.RED,error,Fore.WHITE)
            continue

def archive():
    shutil.make_archive(base_name=arch_name,format=arch_format,root_dir="./")
    
def final():
    shutil.rmtree(arch_dir)

def main():
# function stack
#    args_check()
    dir_backup()
    file_backup()
    excepts_delete()
    archive()
    final()

if __name__ == "__main__":
    main()
