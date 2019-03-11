
# stringIO

# byteIo

from io import StringIO
f = StringIO("Hello!\nHi!\nGoodBye")
while True:
    s = f.readline();
    if s == '':
        break
    print(s.strip())

