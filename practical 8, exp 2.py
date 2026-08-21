import re

def moderate_feedback(feedback_text: str, target_words: list[str], mask: str = "****") -> str:
    """
    Identifies target words in a text block and replaces them with a mask.
    Matches whole words only and ignores capitalization variations.
    """
    if not target_words:
        return feedback_text

    
    pattern = r'\b(' + '|'.join(re.escape(word) for word in target_words) + r')\b'
    
    
    regex = re.compile(pattern, flags=re.IGNORECASE)
    
    
    return regex.sub(mask, feedback_text)


if __name__ == "__main__":
    
    banned_list = ["terrible", "garbage", "hate", "scam"]
    user_feedback = "This service is GARBAGE! I absolutely hate the new update. It feels like a scam."
    
    
    clean_text = moderate_feedback(user_feedback, banned_list)
    
    
    print("Original Feedback:")
    print(user_feedback)
    print("\nModerated Feedback:")
    print(clean_text)