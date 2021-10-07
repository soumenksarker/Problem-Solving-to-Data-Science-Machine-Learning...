import re
pattern = r"(try your own program)"
sentence = "if you wanna feel the freedom than try your own program"
match = re.search(pattern,sentence)
print(match.group(1))

match= re.search(r"(freedom.*)",sentence)
print(match.group(0))
