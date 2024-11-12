import os

# List of folder names from your input
folder_names = [
    "Businesspeople (Entrepreneurs, Investors, Self-employed)",
    "Family reunification",
    "Foreign students",
    "French courses",
    "Permanent immigration pilot program for workers in targeted sectors",
    "Permanent Workers - Application for Selection Certificate",
    "Permanent workers – Programme de l'expérience québécoise",
    "Refugees and other clienteles",
    "Temporary workers",
    "Z - All Forms"
]

# Directory to create the folders in (current directory in this example)
base_directory = "./folders"

# Function to create folders
def create_folders(folder_names, base_directory):
    for folder_name in folder_names:
        # Create the path for the folder
        folder_path = os.path.join(base_directory, folder_name)
        
        try:
            # Create the directory
            os.makedirs(folder_path, exist_ok=True)
            print(f"Created folder: {folder_path}")
        except Exception as e:
            print(f"Error creating folder {folder_path}: {e}")

# Run the function
create_folders(folder_names, base_directory)