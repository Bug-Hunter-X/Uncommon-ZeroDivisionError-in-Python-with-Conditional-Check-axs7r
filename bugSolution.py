def function_with_uncommon_error(a, b):
    if a == 0:
        return float('inf') # Handle division by zero gracefully
    return a + b