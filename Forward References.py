import re

Regex_Pattern = r'^tac(tac(tic)?)+'

Test_String = input()

if re.match(Regex_Pattern, Test_String):
    print("true")
else:
    print("false")
