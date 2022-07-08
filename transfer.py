import re

txtlist = ''
with open(file='test.txt', mode='r', encoding='utf-8') as fp:
    txtlist = fp.readlines()

for txt in txtlist:
    FIRST_SEMICOLON = re.compile(".*:\s")
    SEMICOLON_location = FIRST_SEMICOLON.match(txt).end() - 2
    Str = "'" + txt[:SEMICOLON_location] + "'" + ': ' + "'" + txt[SEMICOLON_location + 2:-1] + "',"

    print(Str)
