def find_range(numbers):
    if not numbers:
        return "List is empty. Cannot calculate range."
    
    # Find the maximum and minimum values in the list
    max_val = max(numbers)
    min_val = min(numbers)
    
    # Calculate the range
    range_val = max_val - min_val
    return range_val

# Example usage:
my_list = [10, 5, 8, 3, 12, 15]
result = find_range(my_list)
print(f"The range of the list is: {result}")
# Expected output: "The range of the list is: 12" (since max - min = 15 - 3 = 12)