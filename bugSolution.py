def function_with_uncommon_error(x, y):
    try:
        if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
            raise TypeError("Invalid input types: Both inputs must be numbers.")
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError as e:
        return f"Error: {e}"

# Example usage:
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Cannot divide by zero
print(function_with_uncommon_error(10, "a")) # Output: Error: Invalid input types: Both inputs must be numbers.
print(function_with_uncommon_error("a",10)) # Output: Error: Invalid input types: Both inputs must be numbers.
print(function_with_uncommon_error("a","b")) # Output: Error: Invalid input types: Both inputs must be numbers.