import re

print(True if re.match(
    r'(a|b){0,}aa(a|b){0,}$',
    'bababaa'
) is not None else False)