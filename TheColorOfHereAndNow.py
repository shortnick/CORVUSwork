

from __future__ import print_function
import os, sys, PIL, random, time

from PIL import Image

t0 = time.clock()
#take coordinates
askfor = "Please enter your lat/long coordinates in decimal format, preferably to 5 or 6 digits of precision. \nFirst, latitude (the y axis), then longitude (x axis). For Western or Southern hemispheres, use negative values. \nFor example, Santiago in Chile is 33 degrees south of the equator and 70 degrees west of the prime meridian. \nIt would be input as '-33.4569400 -70.6482700'\n Your location---> "

ans = input(askfor)
print ("you entered", ans)

lat = float(ans.split(' ')[0])
longi= float(ans.split(' ')[1])


def decdeg2dms(dd):
    negative = dd < 0
    dd = abs(dd)
    minutes,seconds = divmod(dd*3600,60)
    degrees,minutes = divmod(minutes,60)
    if negative:
        if degrees > 0:
            degrees = -degrees
        elif minutes > 0:
            minutes = -minutes
        else:
            seconds = -seconds
    return (degrees,minutes,seconds)

lat = str(decdeg2dms(lat))
longi = str(decdeg2dms(longi))

lat = lat.strip(' ').strip('(').strip(')').split(',')
longi = longi.strip(' ').strip('(').strip(')').split(',')

numbers = []
for num in lat:
	num = float(num)
	num = round(num)
	numbers.append(num)

for num in longi:
	num = float(num)
	num = round(num)
	numbers.append(num)


now = (round(time.clock()-t0))



r = (now*random.choice(numbers)) % 255
g = (now*random.choice(numbers)) % 255
b = (now*random.choice(numbers)) % 255

print(r,g,b)	

im = Image.new("RGB",(600,600),"rgb("+str(r)+","+str(g)+","+str(b)+")")

im.show()

