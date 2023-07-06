# Web Scraping ile Kitap Verilerini MongoDB'ye Kaydetme

Bu proje, web scraping kullanarak iki farklı web sitesinden kitap verilerini çekip MongoDB veritabanına kaydetmek için oluşturulmuştur. İki örnek spider (`KitapsepetiSpider` ve `ExampleSpider`) kullanılmıştır.

## Kurulum

1. Bu projenin çalışması için Python 3.7 veya üzeri bir sürümün yüklü olması gerekmektedir.

2. Proje dosyalarını bilgisayarınıza indirin veya kopyalayın.

3. Terminali açın ve projenin ana dizinine gidin.

4. Sanal bir Python ortamı oluşturun ve aktifleştirin:

- python -m venv env    
- env\Scripts\activate 



5. Gerekli Python paketlerini yüklemek için aşağıdaki komutu çalıştırın:

- pip install -r requirements.txt



6. MongoDB veritabanını yükleyin ve çalıştırın.

## Spider Ayarları

Spider'lar aşağıdaki ayarlara sahiptir:

- `KitapsepetiSpider`:
 - Başlangıç URL'si: `'https://www.kitapsepeti.com/roman'`
 - Çekilen veriler `kitapsepeti` koleksiyonuna kaydedilir.
 - JSON formatında `books.json` dosyasına veriler kaydedilir.
 - İstekler arasında 5 saniye bekleme süresi vardır.

- `ExampleSpider`:
 - Başlangıç URL'si: `'https://www.kitapyurdu.com/index.php?route=product/category/&filter_category_all=true&category_id=64&sort=purchased_365&order=DESC&filter_in_stock=1'`
 - Çekilen veriler `kitapyurdu` koleksiyonuna kaydedilir.
 - JSON formatında `books.json` dosyasına veriler kaydedilir.

## Veritabanı Bağlantısı

Veriler, MongoDB veritabanına kaydedilir. Bağlantı ayarları aşağıdaki gibidir:

- Host: `localhost`
- Port: `27017`
- Database adı: `smartmaple`

## Projeyi Çalıştırma

1. Terminalde projenin ana dizinine gidin.

2. Aşağıdaki komutu kullanarak `KitapsepetiSpider`'ı çalıştırın:


- scrapy crawl kitapsepeti


3. Aşağıdaki komutu kullanarak `ExampleSpider`'ı çalıştırın:


- scrapy crawl example