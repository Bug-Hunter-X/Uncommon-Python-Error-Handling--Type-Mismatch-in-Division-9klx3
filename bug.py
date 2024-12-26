def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        if isinstance(x,(int,float)) and isinstance(y,(int,float)):
            return "Uncommon Error: Type mismatch"
        else:
            return "Error: Invalid input types"

# Example usage:
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Cannot divide by zero
print(function_with_uncommon_error(10, "a")) # Output: Error: Invalid input types
print(function_with_uncommon_error("a",10)) # Output: Uncommon Error: Type mismatch
print(function_with_uncommon_error("a","b")) # Output: Error: Invalid input types