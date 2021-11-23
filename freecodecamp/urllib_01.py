import urllib.request

fhand = urllib.request.urlopen('http://dr-chuck.com/page1.htm')

counts = dict()

for line in fhand:
  print(line.decode().strip())
  
print(counts)
  