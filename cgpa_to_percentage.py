def cgpa_to_percentage(cgpa, scale=10.0):
    """
    Convert CGPA to percentage using the given scale.
    
    Args:
        cgpa (float): The CGPA score (typically between 0 and 10)
        scale (float): The maximum CGPA scale (default is 10.0)
        
    Returns:
        float: The equivalent percentage
    """
    if cgpa < 0 or cgpa > scale:
        raise ValueError(f"CGPA must be between 0 and {scale}")
    return (cgpa / scale) * 100

def get_valid_float_input(prompt, min_val=0.0, max_val=10.0):
    """
    Get a valid float input from the user within specified range.
    """
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("CGPA to Percentage Converter")
    print("===========================")
    
    # Get user input
    cgpa = get_valid_float_input("Enter your CGPA (0-10): ", 0.0, 10.0)
    
    # Ask if user wants to use a custom scale
    use_custom_scale = input("Use custom scale? (default is 10.0) [y/N]: ").strip().lower()
    
    if use_custom_scale == 'y':
        scale = get_valid_float_input("Enter the maximum CGPA scale: ", 1.0, 100.0)
        percentage = cgpa_to_percentage(cgpa, scale)
        print(f"\nCGPA {cgpa:.2f} on a {scale} scale is equivalent to {percentage:.2f}%")
    else:
        percentage = cgpa_to_percentage(cgpa)
        print(f"\nCGPA {cgpa:.2f} is equivalent to {percentage:.2f}%")

if __name__ == "__main__":
    main()
