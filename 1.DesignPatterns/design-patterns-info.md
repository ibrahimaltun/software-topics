## 1. Singleton Pattern

- Amaç: Bir sınıfın yalnızca tek bir örneğinin var olmasını garanti etmek ve bu örneğe global bir erişim noktası sağlamak.
- Dezavantajlar:
  - Global state oluşturur -> testleri zorlaştırır, bağımlılıkları gizler.
  - Tight coupling ve zorlukla mock edilebilirlik.
  - Multiprocessing veya süreç tabanlı ortamlarda ekstra önlemler gereklidir.
  - Çoklu thread'lerde eşzamanlı örnekleme denemeleri: race condition durumunda birden fazla örnek oluşturma durumu olabilir.
  - init tekrar çağrılması durumu olabilir: bazı naive implementasyonlarda aynı istance yeniden init edilir.
  - Multiprocess durumlarda process'ler arası singleton paylaşılmaz, her process kendi instance'ını oluşturur.
  - Seirleştirme(pickle): unpickling yeni bir örnek oluşturabilir, dikkatli olmak gerekir.

- Alternatif olarak Dependency Injection(DI) önerilir.

### cre1_singleton_config.py

- An application reads configuration from a file once and all parts of the app must read the same settings.
- Note: The metaclass holds instances per subclass, is thread-safe, and ignores subsequent constructor args (common Singleton caveat).

### cre1_singleton_logging.py

- A centralized logging facility that configures formatting/handlers once and modules fetch the same logger instance.

---

## 2. Factory Pattern

- Amaç: Herhangi bir nesnenin oluşturulmasını istemciden(client code) soyutlayarak, hangi somut sınıfın kullanılacağına karar verme sorumluluğunu merkezi hale getirmektir.
- Nesne oluşturma kodunu dağıtmak yerine tek yerde toplar; istemci kodu somut sınıflara bağlı kalmaz, değişiklikler(yeni somut sınıf ekleme, konfigürasyon) daha az etkiyle yapılır.

### Varyasyonlar

1. Simple Factory(Factory Fonksiyonu): Tek bir fonksiyon ya da sınıf, parametreye göre uygun nesneyi döndürür. (Resmi GoF deseni -> Gang of Four: başlangıçta 23 tasarım desenini ortaya çıkartan 4 kişilik bir ekip, ayrıca bu desenler GoF patternleri olarak da anılır)
2. Factory Method: Bir üst sınıf/fonksiyon "factory method" tanımlar; alt sınıflar bu metodu ezerek farklı nesneler yaratır. (OOP tabanlı esneklik)
3. Abstract Factory: Birbiriyle ilişkili veya bağımlı nesne ailelerini üreten arayüz. Örneğin farklı UI temaları için widget-factory’leri (buton, pencere, menü).

### Avantajlar

- Bağımlılık azaltma (low coupling).
- Yeni türler eklemek genelde istemciyi bozmaz (open/closed).
- Test edilebilirlik artar (mock/replace kolay).

### Dezavantajlar

- Fazladan sınıf/soyutlama katmanı (boilerplate).
- Çok küçük projelerde aşırı mimari olabilir.

### Ne zaman kullanmalı:

- Nesne yaratımı kararının birden çok yerde tekrarlandığı, varyasyonun konfigürasyona veya runtime koşullarına bağlı olduğu durumlarda.
- Birden çok somut sınıfın ortak arayüzle değiştirilebilir olması istendiğinde.

### Dikkat edilmesi gerekenler

- Factory’ler genelde Dependency Injection ile birlikte iyi çalışır; DI container kullanıyorsan factory kullanımını container üzerinden çözebilirsin.
- Çok karmaşık factory zincirleri yerine basit ve anlaşılır bir factory seç; gerektiğinde Abstract Factory’yi tercih et.
- Thread-safety: Factory içinde state (örn. cache, singleton lifecyle) tutuyorsan eşzamanlama gerekir; ama stateless factory’ler genelde thread-safe’dir.

---

## 4. Builder Pattern

- Amaç (Intent): Karmaşık bir nesnenin (veya nesne ailesinin) oluşturma sürecini adım adım soyutlamak; aynı oluşturma sürecinden farklı temsil veya farklı ürünler üretebilmek.
- Ne çözer: Çok sayıda opsiyon/parametreyle karmaşık nesne inşa ederken oluşturma kodunun istemciye dağılmasını önler; özellikle oluşturma algoritmasının adımları sabit ama ürün temsili farklıysa uygundur.

### Bileşenler

- Builder (arayüz): Ürünün parçalarını oluşturmak için metotlar (ör: set_title, add_section).
- ConcreteBuilder: Builder arayüzünü uygular; Product içeriğini tutar ve get_result() döndürür.
- Director (opsiyonel): Oluşturma algoritmasını (adımları) koordine eder.
- Product: Oluşturulan nesne (rapor stringi, SQL sorgusu, vb.)

### Avantaj / Dezavantaj

- Adımların ayrılması, okunabilir kod, farklı temsiller (formatlar), test kolaylığı.
- Fazladan sınıf katmanı (boilerplate), bazı durumlarda fluent API veya fabrika fonksiyonuyla da yeterli olabilir.
  - Not: Builder genelde mutable bir nesne olarak adım adım doldurulur; tipik olarak tek bir thread / create-per-client için kullanılır — thread-safety gerekiyorsa harici senkronizasyon veya her thread için ayrı builder kullan.
    İmplementasyon varyasyonları
