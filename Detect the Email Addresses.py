import re

n = int(input())
text = ""
for _ in range(n):
    text += input() + "\n"

email_pattern = r'\b[\w\.-]+@[\w\.-]+\b'
emails_found = re.findall(email_pattern, text)

unique_emails = sorted(set(emails_found))

print(';'.join(unique_emails))
