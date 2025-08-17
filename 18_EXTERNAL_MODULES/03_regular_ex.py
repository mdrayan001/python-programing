import re
text = "The quick brown fox jumps over the lazy dog."

# https://regexr.com/   

# Search for a pattern 
match = re.search("brown", text)
print(match)
if match:
    print("Match found!")
    print("Start index:",match.start())
    print("End index:",match.end())       # Output: Match found! Start index: 10 End index: 15
    
    
# find all occurrences of a pattern
matches = re.findall("the", text, re.IGNORECASE)    # case - insensitive search
print("Matches:",matches)   # Output: Matches: ['The', 'the']

# Replace a pattern
new_text = re.sub("fox","cat", text)
print("New text:",new_text)    # Output: New text: The quick brown cat jumps over the lazy dog.