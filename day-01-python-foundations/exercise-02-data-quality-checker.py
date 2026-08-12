# Define the total number of rows in the dataset
total_rows = 2000

# Define the number of rows with missing data
missing_rows = 120

# Define the number of duplicate rows
duplicate_rows = 30

# Calculate total problematic rows (missing + duplicates, assumed non-overlapping)
problematic_rows = missing_rows + duplicate_rows

# Calculate the percentage of problematic rows out of total rows
problem_percentage = (problematic_rows / total_rows) * 100

# Classify the dataset based on the problem percentage
if problem_percentage <= 2:
    # 2% or less is considered Excellent
    classification = "Excellent"
elif problem_percentage <= 5:
    # More than 2% but at most 5% is considered Acceptable
    classification = "Acceptable"
else:
    # More than 5% needs cleaning
    classification = "Needs Cleaning"

# Print the total number of rows
print(f"Total rows: {total_rows}")

# Print the total number of problematic rows
print(f"Problematic rows: {problematic_rows}")

# Print the problem percentage formatted to 2 decimal places
print(f"Problem percentage: {problem_percentage:.2f}%")

# Print the final classification
print(f"Final classification: {classification}")
