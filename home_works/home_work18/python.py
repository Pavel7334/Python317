import re

s = "+ 7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
pattern = r'\+?7\d{10}'

print(re.findall(pattern, s))
