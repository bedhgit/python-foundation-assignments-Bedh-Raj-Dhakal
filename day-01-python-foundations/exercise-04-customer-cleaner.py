# Define the raw, unclean name with extra spaces and inconsistent casing
raw_name = "  sAgar THAPA "

# Define the raw, unclean city with extra spaces and inconsistent casing
raw_city = "kATHMANDU "

# Define the raw age as a string
raw_age = "27"

# Define the raw email with extra spaces and inconsistent casing
raw_email = " SAGAR@MAIL.COM "

# Clean the name: strip whitespace, then title-case each word
clean_name = raw_name.strip().title()

# Clean the city: strip whitespace, then title-case it
clean_city = raw_city.strip().title()

# Clean the age: strip whitespace, then convert the string to an integer
clean_age = int(raw_age.strip())

# Clean the email: strip whitespace, then convert to lowercase (emails are conventionally lowercase)
clean_email = raw_email.strip().lower()

# Use a ternary expression to determine adult status based on age
status = "Adult" if clean_age >= 18 else "Minor"

# Print the cleaned name
print(f"Name: {clean_name}")

# Print the cleaned city
print(f"City: {clean_city}")

# Print the cleaned age
print(f"Age: {clean_age}")

# Print the cleaned email
print(f"Email: {clean_email}")

# Print the adult/minor status
print(f"Status: {status}")
