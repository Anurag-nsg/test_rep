from pathlib import Path

def extract_file_paths():
    directory_path = "/Users/anuragnarsingoju/Downloads/2-1 project/exe_files"
    extensions = {".exe",".dll",".sys",".acm",".ax",".cpl",".drv",".efi",".mui",".ocx",".scr",".tsp",".mun"} 
    directory = Path(directory_path)
    # Make sure the directory exists
    if not directory.exists() or not directory.is_dir():
        return []
    file_paths = []
    for file_path in directory.glob(f'*/'):
        if file_path.is_file() and file_path.suffix.lower() in extensions:
            file_paths.append(file_path)
    return file_paths