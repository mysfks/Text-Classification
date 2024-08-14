# Text-Classification
# Haber Kategorilendirme Projesi

Bu proje, bir haber sitesinden verileri çekip, bu verileri kategori bazında sınıflandırmayı amaçlamaktadır. Proje kapsamında PySpark ve makine öğrenmesi teknolojileri kullanılmıştır.

## İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Gereksinimler](#gereksinimler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Dosyalar](#dosyalar)
- [Özellikler](#özellikler)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## Proje Hakkında

Bu projede iki temel dosya bulunmaktadır:

1. **Haber Toplayıcı Dosya:** Her bir kategoriden haberleri alıp bir CSV dosyasına dönüştürür.
2. **Veri Birleştirici Dosya:** Elde edilen haber kategorilerini birleştirip tek bir veri seti haline getirir. Bu veri seti üzerinde PySpark ve makine öğrenmesi teknikleri kullanılarak sınıflandırma işlemleri gerçekleştirilir.

Projede, sınıflandırma işlemlerinin doğruluğunu ölçmek amacıyla bir başarı oranı hesaplanmaktadır.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılım ve kütüphanelerin kurulmuş olması gerekmektedir:

- [Python 3.x](https://www.python.org/)
- [PySpark](https://spark.apache.org/docs/latest/api/python/)
- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)

## Kurulum

Projenin yerel ortamınıza kurulumu için aşağıdaki adımları takip edebilirsiniz:

```bash
# Projeyi klonlayın
git clone https://github.com/kullanıcı-adı/haber-kategorilendirme-projesi.git

# Proje dizinine gidin
cd haber-kategorilendirme-projesi

# Gerekli bağımlılıkları yükleyin
pip install -r requirements.txt

## Dosyalar

- **`haber_toplayici.py`**: Belirlenen haber kategorilerini çekip, her bir kategori için ayrı CSV dosyaları oluşturan dosya.
- **`veri_birlestirici.py`**: Kategori bazında oluşturulan CSV dosyalarını birleştirip tek bir veri seti oluşturan ve bu veri seti üzerinde PySpark ve makine öğrenmesi işlemleri yapan dosya.

## Özellikler

- **Otomatik Kategorilendirme**: Haber verilerini belirlenen kategorilere göre otomatik olarak sınıflandırır.
- **PySpark ve Makine Öğrenmesi Entegrasyonu**: PySpark ve makine öğrenmesi tekniklerini kullanarak sınıflandırma işlemleri gerçekleştirir.
- **Veri Birleştirme**: Farklı kategorilere ait haber verilerini tek bir veri setinde birleştirir ve bu veri seti üzerinde analizler yapar.

## Katkıda Bulunma

Projeye katkıda bulunmak isterseniz aşağıdaki adımları takip edebilirsiniz:

1. Bu projeyi forklayın.
2. Kendi dalınızda (branch) değişiklik yapın: `git checkout -b yeni-özellik`
3. Değişikliklerinizi commitleyin: `git commit -m 'Yeni bir özellik eklendi'`
4. Dalınıza push edin: `git push origin yeni-özellik`
5. Bir Pull Request açın.

Her türlü katkı değerlidir ve memnuniyetle karşılanır.

## Lisans

Bu proje [Lisans Adı](link) ile lisanslanmıştır.

Projenin kullanımı, kopyalanması, değiştirilmesi ve dağıtılması bu lisans altında gerçekleştirilir.

