def sanitize_name(first_name: str, last_name: str) -> str:
    """
    Cleans, trims, and formats first and last names into title case.
    Handles accidental double spaces, trailing spaces, and typos like 'mCdonald'.
    """
    
    clean_first = " ".join(first_name.strip().split())
    clean_last = " ".join(last_name.strip().split())
    
    
    full_name = f"{clean_first} {clean_last}"
    
    
    return full_name.title()


if __name__ == "__main__":
    
    input_first = "   joHN   "
    input_last = "  dOE  "
    
    cleaned_name = sanitize_name(input_first, input_last)
    
    
    print(f"Original: '{input_first}' '{input_last}'")
    print(f"Sanitized Full Name: '{cleaned_name}'")