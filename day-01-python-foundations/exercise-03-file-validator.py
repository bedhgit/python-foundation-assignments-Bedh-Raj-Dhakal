# Ask the user to enter a file name
file_name = input("Enter the file name: ")

# Remove extra whitespace and convert to lowercase for case-insensitive comparison
file_name = file_name.strip().lower()

# Define the set of accepted file extensions
valid_extensions = (".csv", ".json", ".parquet")

# Check if the file name ends with one of the valid extensions
if file_name.endswith(valid_extensions):
    # Print success message if the extension is valid
    print(f"'{file_name}' is a valid file type.")
else:
    # Print error message if the extension is not accepted
    print(f"'{file_name}' is not a valid file type. Accepted types: .csv, .json, .parquet")
