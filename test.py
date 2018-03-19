import socket
from urllib.request import urlopen, URLError, HTTPError

socket.setdefaulttimeout( 23 )  # timeout in seconds

url = 'https://google.com/'
try :
    response = urlopen( url )
except HTTPError(e):
    print(str(e.code))
except URLError(e):
    print(str(e.reason))
else :
    html = response.read()
    print('got response!')