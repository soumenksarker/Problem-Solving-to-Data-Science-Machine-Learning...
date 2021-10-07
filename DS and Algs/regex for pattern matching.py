#this has done from only starting only
import re
pattern = "abc"
string = "abc123"
match = re.match(pattern, string)
print(match.group())
