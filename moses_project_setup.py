''' This module provides functions to create various project folders. '''

# Import standard library modules
import pathlib
import time

# Create a base path object
base_path = pathlib.Path.cwd()

def create_folders_for_range(start: int, end: int) -> None:
    ''' Creates folders for each year in a given range. '''
    for year in range(start, end + 1):
        folder = base_path.joinpath(str(year))
        folder.mkdir(exist_ok=True)
    print(f"Created folders for years from {start} to {end}")

def create_folders_from_list(names: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    ''' Creates folders based on a list of names with optional transformations. '''
    for name in names:
        if to_lowercase:
            name = name.lower()
        if remove_spaces:
            name = name.replace(" ", "")
        
        folder = base_path.joinpath(name)
        try:
            folder.mkdir(exist_ok=True)
        except Exception as e:
            print(f"Failed to create folder '{name}': {e}")
    
    print(f"Created folders from list: {names}")

def create_prefixed_folders(names: list, prefix: str) -> None:
    ''' Creates folders with a specified prefix. '''
    for name in names:
        folder = base_path.joinpath(f"{prefix}{name}")
        folder.mkdir(exist_ok=True)
    print(f"Created folders with prefix '{prefix}'")

def create_folders_periodically(seconds: int) -> None:
    ''' Creates a folder every few seconds for a specified duration. '''
    start_time = time.time()
    index = 0
    while time.time() - start_time < seconds:
        folder = base_path.joinpath(f"folder_{index}")
        folder.mkdir(exist_ok=True)
        index += 1
        time.sleep(5)
    print(f"Created folders periodically for {seconds} seconds")

def main() -> None:
    ''' Main function to demonstrate folder creation functions. '''
    print("Starting folder creation...")

    create_folders_for_range(2021, 2023)
    print("Created folders for range.")

    create_folders_from_list(['data-csv', 'data-json'])
    print("Created folders from list.")

    create_prefixed_folders(['csv', 'json'], 'data-')
    print("Created prefixed folders.")

    create_folders_periodically(20)
    print("Created folders periodically.")

    # Test options for creating folders from a list
    regions = [
        "North America", 
        "South America", 
        "Europe", 
        "Asia", 
        "Africa", 
        "Oceania", 
        "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)
    print("Created folders with options (lowercase and no spaces).")

    print("Completed folder creation.")

if __name__ == '__main__':
    main()
