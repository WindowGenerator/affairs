import re

from pathlib import Path
from typing import Iterator


COMPILED_IMPORT_FINDER = re.compile(r"import\s+.+_?pb2")


def api_pkgs(dir_pth: Path) -> Iterator[Path]:
    for path in dir_pth.iterdir():
        if not path.is_dir():
            continue

        api_path = path / f"{path.name}_api"
            
        if not api_path.exists():
            continue
        
        yield api_path


def format(_dir: str) -> None:
    dir_pth = Path(_dir)

    for api_pkg_path in api_pkgs(dir_pth):
        for file_path in api_pkg_path.iterdir():
            if not file_path.is_file() and file_path:
                continue
            
            contenent_to_write = ""
            with open(file_path, "rt") as file_fd:
                for line in file_fd.readlines():

                    if not COMPILED_IMPORT_FINDER.match(line):
                        contenent_to_write += line
                        continue
                
                    new_line = f"from . {line}"
                    contenent_to_write += new_line
                
            with open(file_path, "wt") as file_fd:
                file_fd.write(contenent_to_write)

        
        


def main() -> None:
    format("pkgs")


if __name__ == "__main__":
    main()
