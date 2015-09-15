#!c:/Program Files/Python 3.5/python

print("Content-type: text/html")
print()
print('<h2>hello</h2>')
from os import environ
print(environ['REMOTE_ADDR'])
print('</br>')
for n in environ:
    print('"' + n + '":\t"' + environ[n] + '"<br>')
print(len(environ))
