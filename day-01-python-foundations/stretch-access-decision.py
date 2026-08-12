# Define the user's role
user_role = "analyst"

# Define whether the user's account is active
is_active = True

# Define the dataset the user is requesting to access
requested_dataset = "sales_data"

# Define the list of roles that are allowed to request access
allowed_roles = ["analyst", "data scientist", "engineer"]

# Define the list of datasets that are restricted regardless of role
restricted_datasets = ["salary_data", "personal_data"]

# Check the conditions in priority order and give a specific reason for denial
if not is_active:
    # Deny first if the account itself is inactive
    print("Access denied because the user is inactive.")
elif user_role not in allowed_roles:
    # Deny if the role is not in the allowed list
    print("Access denied because the role is not allowed.")
elif requested_dataset in restricted_datasets:
    # Deny if the requested dataset is on the restricted list
    print("Access denied because the dataset is restricted.")
else:
    # All three conditions passed, so access is granted
    print("Access granted.")

# --- Scenario 2: Inactive user ---
# user_role = "analyst"
# is_active = False
# requested_dataset = "sales_data"
# Expected: Access denied because the user is inactive.

# --- Scenario 3: Role not allowed ---
# user_role = "intern"
# is_active = True
# requested_dataset = "sales_data"
# Expected: Access denied because the role is not allowed.

# --- Scenario 4: Restricted dataset ---
# user_role = "engineer"
# is_active = True
# requested_dataset = "salary_data"
# Expected: Access denied because the dataset is restricted.
