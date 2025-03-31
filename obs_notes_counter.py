from pathlib import Path

def find_dirs(path):
    if not Path(path).is_dir():
        return 0
    count = 0
    for item in Path(path).iterdir():
        if item.is_dir():
            count += 1 + find_dirs(item) 
    return count

def find_md_files(path):
    count = 0
    for item in Path(path).iterdir():
        if item.is_dir():
            count += find_md_files(item)  
        else:
            if item.suffix.lower() in (".md", ".markdown"):
                count += 1
    return count

if __name__ == "__main__":
    
    dir_path = Path(input("Enter directory path (to count directories): "))
    subdir_count = find_dirs(dir_path)
    print(subdir_count)

    md_files_path = Path(input("Enter directory path (to count markdown files): "))
    num_of_notes = find_md_files(md_files_path)
    print(num_of_notes)


