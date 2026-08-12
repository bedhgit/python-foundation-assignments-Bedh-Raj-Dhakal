# Define the total rows successfully loaded
rows_loaded = 9800

# Define the total rows that failed to load
rows_failed = 200

# Define the pipeline runtime in minutes
runtime_minutes = 18

# Calculate total rows processed (loaded + failed)
total_rows = rows_loaded + rows_failed

# Calculate the failure rate as a percentage
failure_rate = (rows_failed / total_rows) * 100

# Determine pipeline status based on failure rate AND runtime
if failure_rate <= 2 and runtime_minutes <= 20:
    # Only Healthy if BOTH failure rate is low AND runtime is fast
    status = "Healthy"
elif failure_rate <= 5:
    # Failure rate is acceptable (<=5%), but either runtime was too slow
    # (if <=2%) or failure rate itself is in the warning range (2-5%)
    status = "Warning"
else:
    # Failure rate above 5% is always Critical, regardless of runtime
    status = "Critical"

# Print the failure rate formatted to 2 decimal places
print(f"Failure rate: {failure_rate:.2f}%")

# Print the final pipeline status
print(f"Pipeline status: {status}")

# --- Test Case 2 ---
# rows_loaded = 9500
# rows_failed = 500
# runtime_minutes = 15
# Expected: Failure rate: 5.00%  |  Pipeline status: Warning

# --- Test Case 3 ---
# rows_loaded = 9900
# rows_failed = 100
# runtime_minutes = 30
# Expected: Failure rate: 1.00%  |  Pipeline status: Warning
# (Low failure rate but slow runtime -> cannot be Healthy, but not Critical either)
