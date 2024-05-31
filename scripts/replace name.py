import os

def replace_in_filename(folder_path, old_substring, new_substring):
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return
    
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if the current item is a file
        if os.path.isfile(file_path):
            # Replace the old substring with the new substring in the filename
            new_filename = filename.replace(old_substring, new_substring)
            
            # Rename the file
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")

# Get user input for folder path, old substring, and new substring
folder_path = input("Enter the folder path: ")
old_substring = input("Enter the old substring to replace: ")
new_substring = input("Enter the new substring: ")

# Call the function to replace substrings in file names
replace_in_filename(folder_path, old_substring, new_substring)
