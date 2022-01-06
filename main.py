import re
import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd


url = 'https://www.hokkaido-np.co.jp/news/n_economy'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
elems = soup.select('[class="categoryArchiveItemTitle"]')
# print(elems[1])

article = soup.find_all(href=re.compile("article/"))
# print(article)

list = []
for el in article:
    try:
        list.append(el.contents[3].text)
        # print("-"*10)
    except:
        break
    
st.write('''
        # 北海道新聞
        ''')

df = pd.DataFrame({'最新情報':list})
df = df.style.hide_index()
st.dataframe(df)