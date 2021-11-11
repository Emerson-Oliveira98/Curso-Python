from datetime import datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup

df = ExtracaoPortal().extrair("https://globoesporte.globo.com/")
df.head()