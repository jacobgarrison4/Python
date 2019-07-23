import urllib.request

page = urllib.request.urlopen('http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=1916-02-01&latitude=44.0519&longitude=-123.0867&maxradiuskm=250&minmagnitude=5')

line = page.readline().decode()
print(line)
