import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import requests

main = "https://www.msw.ph/"
mswmega = "https://megasportsworld.com"
mswlive = "https://mswlive.com/"
mswsites = "https://www.mswsites.com/"
facebook = "https://www.facebook.com/"

msw = requests.post(main)
mega = requests.post(mswmega)
live = requests.post(mswlive)
sites = requests.post(mswsites)
fb = requests.post(facebook)

mswmain = msw.elapsed.total_seconds()
mswmega = mega.elapsed.total_seconds()
mswlive = live.elapsed.total_seconds()
mswsites = sites.elapsed.total_seconds()
face = fb.elapsed.total_seconds()

print("Live", random.uniform(mswlive,mswlive))
print("MSW PH", random.uniform(mswmain,mswmain))
print("Megasportworld", random.uniform(mswmega,mswmega))
print("sites", random.uniform(mswsites,mswsites))
print("Facebook", random.uniform(face,face))