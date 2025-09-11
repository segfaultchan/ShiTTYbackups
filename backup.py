import shutil
from pathlib import Path
from colorama import Fore

data = [
    ["~/.config","config"],
    ["/etc/shadowsocks-rust/","shadowsocks"],
    ["~/.zshrc","dotfiles"],
    ["~/.ssh/","dotfiles"],
]



def main():
    for paths in data:
        converted = Path(paths[0]).expanduser()
        paths[0] = str(converted.resolve())
#    print(f"{Fore.GREEN}convert success{Fore.WHITE}")


if __name__ == "__main__":
    main()
