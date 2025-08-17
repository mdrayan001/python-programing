def convert_string(text):
    # Step 1: Replace "you" (lowercase) with "this"
    text = text.replace("you", "this")
    
    # Step 2: Replace "You" (uppercase first letter) with "this"
    # This ensures we handle sentences starting with "You"
    text = text.replace("You", "this")
    
    # Step 3: Replace "are" (lowercase) with "is"
    text = text.replace("are", "is")
    
    # Step 4: Replace "Are" (uppercase first letter) with "is"
    text = text.replace("Are", "is")
    
    # Step 5: Replace all spaces with a dash "-"
    # This creates the final hyphen-separated string
    text = text.replace(" ", "-")
    
    # Step 6: Return the modified text
    return text


# -------------------
# Example Test Cases
# -------------------

# A list of sentences to test the function
examples = [
    "hey you are good",
    "you are amazing",
    "Are you ready",
    "I think you are the best",
    "You are strong",
    "No matter who you are"
]

# Loop through each example and print the result
for sentence in examples:
    print(f"{sentence}  -->  {convert_string(sentence)}")
