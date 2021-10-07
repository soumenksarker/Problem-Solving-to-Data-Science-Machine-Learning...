import re
precompiled_pattern = re.compile(r"(.*\d+)")
matches = precompiled_pattern.match("The answer is 42!")
print(matches.group(1))
matches = precompiled_pattern.match("Or it can be 43!")
print(matches.group(1))
