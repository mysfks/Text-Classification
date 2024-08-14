import pandas as pd
import random

"""
saglik
bilim-teknoloji
egitim
kultur-sanat
ekonomi
spor
"""

# Dosyaların listesini ve birleştirilecek sütunları belirleyin
dosya_listesi = ['trt/spor.csv', 'trt/saglik.csv', 'trt/egitim.csv','trt/ekonomi.csv','trt/kultur-sanat.csv','trt/bilim-teknoloji.csv']
birlestirilecek_sutunlar = ['Kategori', 'Başlık', 'İçerik']

# Tüm dosyaları okuyun, her bir satırı karışık bir şekilde birleştirin
tum_veri = []
for dosya in dosya_listesi:
    df = pd.read_csv(dosya)
    tum_veri.extend(df[birlestirilecek_sutunlar].values.tolist())

# Verileri karıştırın
random.shuffle(tum_veri)

# Yeni bir DataFrame oluşturun ve CSV dosyasına yazın
yeni_df = pd.DataFrame(tum_veri, columns=birlestirilecek_sutunlar)
yeni_df.to_csv('trt/karisik_veri.csv', index=False)