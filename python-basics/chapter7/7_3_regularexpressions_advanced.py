import re

# |
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

# ^
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))

# $
print(re.search('short$', 'Life is too short'))

#group
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))

p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))

