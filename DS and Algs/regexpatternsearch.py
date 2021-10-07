#search method for finding any pattern from anywhere
import re
pattern = r"(your base)"
sentence = "All your base are belong to us"
match = re.search(pattern, sentence)
print(match.group(1))

