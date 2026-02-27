## Inversion of Control(IoC)

- Geleneksel kodlamada "kodun kendisi bağımlılıkları ve akışı çağırır" mantığı yerine, yüksek seviyeli bileşenler düşük seviyeli bileşenlerin nasıl ve ne zaman çağrılacağını belirlemez; bunun yerine "kontrolü framework, container vb. gibi dışardaki bir yapıya verir" mantığını benimser.

- IoC'de amaç, bağımlılıkların ve kontrol akışının merkezileştirilmesi, test edilebilirlik sağlanması ve esnekliktir.

### IoC Yaygın Mekanizmaları

1. Dependency Injection(DI): En yaygın uygulamadır. Bağımlılıklar dışarıdan(constructor, setter veya metod parametresi olarak) verilir.
2. Service Locator: Bileşen runtime'da bir locator/container'dan bağımlılık ister.(Kolay ama bağımlılığı gizlediği için genelde <b>anti-pattern</b> sayılır)
3. Event-driven/Callback/Observer: Bileşenler olayları yayar/abone olur, çağırma kontrolü olay döngüsü/framework üzerindedir.
4. Template Method/Framework Callbacks(Hollywood): Framework belirli hook'ları çağırır, kullanıcı kodu sadececallback sağlar.
5. Factory/Abstract Factory: Nesne oluşturma kontrolünü fabrikaya vererek, kontrolü tersine çevirir.

   Not: IoC bir prensiptir, DI ise bu prensibin uygulamalarından birisidir.

### IoC'nin Faydaları

- Loose coupling: Bileşenler somut implementasyonlara sıkıca bağlı olmaz.
- Test edilebilirlik: Mock/stub enjekte ederek birimi izole edersin.
- Değiştirilebilirlik: Yeni implementasyonları konfigürasyonla değiştirebilirsin.
- Composition root: Uygulamanın başlangıcında tüm wiring’i tek yerde toplayabilirsin.

### IoC ile ilişkiki Yazılım İlkeleri

1. SOLID (özellikle D: Dependecny Inversion)
   - S: Single Responsibility Principle (Tek sorumluluk)
   - O: Open/Closed Principle (Açık/Kapalı)
   - L: Liskov Substitution Principle
   - I: Interface Segregation Principle
   - D: Dependency Inversion Principle — Yüksek seviye modüller düşük seviye modüllere bağlı olmamalıdır; her ikisi de soyutlamalara bağlı olmalıdır. DI/IoC doğrudan D prensibini uygular.

2. Separation of Concerns (sorumluluk ayrımı)
3. DRY (Don't Repeat Yourself)
4. KISS (Keep It Simple, Stupid)
5. YAGNI (You Aren't Gonna Need It) — gereksiz karmaşıklıktan kaçın
6. Principle of Least Astonishment (beklentiyi bozmama)
7. Law of Demeter (aydınlatıcı: "sadece yakın arkadaşlarla konuş")
8. Composition over Inheritance (tercih edilen kompozisyon)
9. Tell, Don't Ask; Command-Query Separation

### Dependency Injection

- Bir sınıfın veya fonksiyonun ihtiyaç duyduğu bağımlılıkların(diğer nesneler, servisler gibi) kendisinin oluşturması yerine dışardan("enjekte" edilerek) verilmesi tekniğidir.
- DI'de amaç, bağımlılıkları gevşetmek(loose coupling), test edilebilirliği kolaylaştırmak ve bileşenleri yeniden kullanılabilir hale getirmektir.

#### Neden kullanılır?

- Test edilebilirlik: Nesnenin gerçek bağımlılık yerine sahte (mock/stub) versiyonunu enjekte ederek izole test yazabilirsin.
- Değiştirilebilirlik: Farklı implementasyonları konfigürasyon/ortam değiştirerek değiştirebilirsin (örn. gerçek ve in-memory repo).
- Single Responsibility: Sınıfların tek sorumluluğu olur — iş mantığı, bağımlılık yaratma değil.
- Konfigürasyon merkezi: Nesne grafiği bir yerde (wiring) toplanır; değişim yönetimi kolaylaşır.
