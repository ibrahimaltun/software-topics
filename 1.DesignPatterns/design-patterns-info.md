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

- Alternatif olarak Dpendency Injection(DI) önerilir.

### cre1_singleton_config.py

- An application reads configuration from a file once and all parts of the app must read the same settings.
- Note: The metaclass holds instances per subclass, is thread-safe, and ignores subsequent constructor args (common Singleton caveat).

### cre1_singleton_logging.py

- A centralized logging facility that configures formatting/handlers once and modules fetch the same logger instance.

## ---------------------
