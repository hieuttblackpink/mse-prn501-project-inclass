import urllib.request

data = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in data:
    print(line.decode().strip())