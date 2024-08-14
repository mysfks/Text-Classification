import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
workspace_path = 'C:/Users/myusu/OneDrive/Masaüstü/trt'

"""
saglik
bilim-teknoloji
egitim
kultur-sanat
ekonomi
spor
"""

for page_number in range(2, 500):  
    url = f"https://www.trthaber.com/haber/spor/{page_number}.sayfa.html"
    response = requests.get(url)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi, "html.parser")
    
    haberler = soup.find_all("div", {"class": "standard-left-thumb-card"})  

    for haber in haberler:
        kategori = haber.find("div", {"class": "category-tag"}).text.strip("\n").strip()
        baslik_element = haber.find("div", {"class": "title"})
        baslik = baslik_element.text.strip("\n").strip() if baslik_element else ""  
        icerik_element = haber.find("div", {"class": "description"})
        icerik = icerik_element.text.strip("\n").strip() if icerik_element else ""  
        data.append({"Kategori": kategori, "Başlık": baslik, "İçerik": icerik})


df = pd.DataFrame(data)
print(df)
df.to_csv('C:/Users/myusu/OneDrive/Masaüstü/trt/spor.csv', index=False)