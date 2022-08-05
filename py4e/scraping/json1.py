import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    sum = 0
    address = input('Enter location: ')
    if len(address) < 1: break
    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    js = json.loads(data)
    for item in js["comments"]:
        counts = int(item["count"])
        sum = sum + counts
    print(sum)
    #info = js["comments"]

    #for item in info:
        #print(info[1])

    #for item in counts:
        #x = int(item.text)
        #sum = sum + x
    #print(sum)
