def format_feedback(customer_name, feedback):
    
    customer_name = customer_name.strip().title()

    
    feedback = feedback.strip()

    
    if feedback:
        feedback = feedback[0].upper() + feedback[1:]

    
    feedback = feedback.replace("can't", "cannot")
    feedback = feedback.replace("won't", "will not")

    
    formatted_message = (
        f"Customer Name: {customer_name}\n"
        f"Feedback: {feedback}\n"
        f"Thank you, {customer_name}, for sharing your valuable feedback."
    )

    return formatted_message



name = input("Enter customer name: ")
feedback = input("Enter customer feedback: ")


result = format_feedback(name, feedback)


print("\n--- Formatted Customer Feedback ---")
print(result)