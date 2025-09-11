import shutil
import tempfile
import os
from datetime import date
from pathlib import Path

# directory_to_archive, its_parent_directory, save_as(optional)
dirs = [
    ["test_directory", "dotfiles", ""]
]

def main():
    # replace path with realpath
    for dir in dirs:
        dir[0] = str(Path(dir[0]).expanduser().resolve())

    # move every dir & files in it to tempdir
    with tempfile.TemporaryDirectory() as tmpdir:        
        for dir in dirs:
            dest = os.path.join(tmpdir, os.path.basename(dir[0]))
            
            # if path is file
            if os.path.isfile(dir[0]):
                shutil.copy(dir[0], dest)
            # if path is directory
            if os.path.isdir(dir[0]):
                shutil.copytree(dir[0], dest)

        shutil.make_archive(f"backup-{date.today().isoformat()}", "zip", tmpdir)

if __name__ == "__main__":
    main()