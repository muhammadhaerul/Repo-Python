import re

string = input('')
pattern = r"[a-zA-Z24680]{40}[13579\s]{5}"

x = re.fullmatch(pattern, string)

if x:
  print(True)
else:
  print(False)