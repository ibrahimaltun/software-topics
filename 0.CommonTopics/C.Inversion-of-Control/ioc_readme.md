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
