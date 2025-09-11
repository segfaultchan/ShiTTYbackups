import shutil
import tempfile
import os
import json

from datetime import date
from pathlib import Path

from time import sleep

with open("config.json", "r", encoding="utf-8") as config:
    dirs = json.load(config)

def main():
    # replace path with realpath
    for dir in dirs:
        dir[0] = str(Path(dir[0]).expanduser().resolve())

    # move every dir & files in it to tempdir
    with tempfile.TemporaryDirectory() as tmpdir:        
        for dir in dirs:
            dest = os.path.join(tmpdir, dir[1], os.path.basename(dir[0]))
            
            if not os.path.exists(dest):
                os.makedirs(dest, exist_ok=True)

            # if path is file
            if os.path.isfile(dir[0]):
                shutil.copy(dir[0], dest)
            # if path is directory
            if os.path.isdir(dir[0]):
                shutil.copytree(dir[0], dest, dirs_exist_ok=True)

        shutil.make_archive(f"backup-{date.today().isoformat()}", "zip", tmpdir)

if __name__ == "__main__":
    main()