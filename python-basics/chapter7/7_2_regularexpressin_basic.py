# meta characters
    #. ^ * + ? {} [] \ | ()

# character class []
    # [abc] :  a or b or c
    # [a-z] : any character in a - z
    # [a-zA-Z0-9] : all of these
    # ^ means not [^0-9] : not numbers
    # \d - [0-9]와 동일한 표현식이다.
    # \D - [^0-9]와 동일한 표현식이다.
    # \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
    # \S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
    # \w - [a-zA-Z0-9_]와 동일한 표현식이다.
    # \W - [^a-zA-Z0-9_]와 동일한 표현식이다.

# Dot .
    # : everything but \n
    # a.b : azb afb ...
    # a.b != a[.]b

# repeat * , + , {}
    # ca*t : ct, caaaat ....
    # ca+t : ca*t - ct
    # ca{3}t : caaat
    #ca{0,2}t : ct, cat, caat

# ?
    # ab?c = ab{0,1}c

# re module
import re
p = re.compile('[a-z]+') # returns an object

# match
m = p.match("3 python")
print(m)
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')

# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())

# search
m = p.search('here')
print(m)

# find all
print(p.findall("life is beautiful 32sd"))

# finditer
result = p.finditer("life is too short") # returns object
# print(result)

# compile options

p = re.compile('a.b')
m = p.match('a\nb')
print("compile options",m)

    # re.DOTALL
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print("compile options",m)
    # re.IGNORECASE

    #re.MULTILINE
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

    # re.VERBOSE
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)

# backslach
p = re.compile(r'\\section')
