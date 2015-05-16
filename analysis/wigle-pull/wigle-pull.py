__author__ = 'Charlie'

import urllib2
import csv

# Make authentication POST for access to API and retrieve auth cookie
url = 'https://WiGLE.net/gps/gps/GPSDB/login?credential_0=sonyc_wifi&credential_1=sonyc@CUSP&noexpire=on'
response = urllib2.urlopen(url)
cookie = response .info()['Set-Cookie']
content = response.read()

# Make data request to API using New York City lat/lng bounds sending cookie
url = 'https://wigle.net/gpsopen/gps/GPSDB/confirmquery?longrange1=-74.1673798561&longrange2=-73.7215881348&latrange1=40.5693281185&latrange2=40.894646156&simple=true'
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', cookie))
response = opener.open(url)
content = response.read()

# Write '~' delimited data to file
f = open('temp.csv', 'w')
f.write(content)
f.close()

# Print data
with open('temp.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='~', quotechar='|')
    for row in reader:
        print ', '.join(row)




