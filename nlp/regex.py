import re

def show_all_matches(regexes, subject, re_length=6):
    print('Sentence:')
    print()
    print('    {}'.format(subject))
    print()
    print(' regexp{} | matches'.format(' ' * (re_length - 6)))
    print(' ------{} | -------'.format(' ' * (re_length - 6)))
    for regexp in regexes:
        fmt = ' {:<%d} | {!r}' % re_length
        matches = re.findall(regexp, subject)
        if len(matches) > 8:
            matches = matches[:8] + ['...']
        print(fmt.format(regexp, matches))

sentence = '''
You can find us on the web at https://codeup.com. Our ip address is 123.123.123.123 (maybe).
'''.strip()

url_re = r'(https?)://(\w+)\.(\w+)'

protocol, domain, tld = re.search(url_re, sentence).groups()

print(f'''
protocol: {protocol}
domain:   {domain}
tld:      {tld}
''')

re.search(url_re, sentence).groups()



url_re = r'(?P<protocol>https?)://(?:\w+)\.(?P<tld>\w+)'

match = re.search(url_re, sentence)

print(f'''
groups: {match.groups()}
referencing a group by name: {match.group('tld')}
group dictionary: {match.groupdict()}
''')


re.sub(r'\D', '', 'abc 123')

def is_vowel(string):
    reg = r'[aeiuo]'
    match = re.findall(reg,string)
    if len(match) == 1:
        print("is vowel")
    else:
        print("is not vowel")


def is_valid_username(string):
    reg = r'\b[a-z0-9_]{1,31}\b'
    match = re.findall(reg, string)
    if len(match) == 1:
        return True
    else:
        return False

def capture_phones(string):
    reg = r'([\d+])?([()\d]{3,5})?[\s\.-]?(\d{3})[\.\-\s]?([\d]{4})'
    match = re.findall(reg, string)
    print(match)


def format_dates(string):
    reg = r'(\d{2})\/(\d{2})\/(\d{2})'
    match = re.search(reg, string).groups()
    print(f"{match[2]}/{match[0]}/{match[1]}")



