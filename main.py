from pathlib import Path
import shutil
import time

def find_msg_package_directories(root_dir: Path) -> list[Path]:
    result_dirs = []
    for xmlpath in root_dir.rglob('package.xml'):
        if xmlpath.is_file() and (any(xmlpath.parent.rglob('*.msg')) or any(xmlpath.parent.rglob('*.idl'))):
            result_dirs.append(xmlpath.parent)
    return result_dirs


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Find and copy directories containing package.xml and .msg files.")
    parser.add_argument("source_directory", type=str, help="The root directory to search in.")
    args = parser.parse_args()

    source_directory = Path(args.source_directory)
    destination_directory = Path(__file__).resolve().parent / f'ws_{int(time.time())}' / 'src'
    destination_directory.mkdir(parents=True)

    directories = find_msg_package_directories(source_directory)
    for directory in directories:
        print('Found:', directory)
        shutil.copytree(directory, destination_directory / directory.name)
