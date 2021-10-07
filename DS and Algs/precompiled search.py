import re
precompiled_pattern = re.compile(r"(\d+)")
matches = precompiled_pattern.search("The andwer is 41")
print(matches.group(1))
