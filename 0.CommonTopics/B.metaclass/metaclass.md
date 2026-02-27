## metaclass

- Bir sınıf tanımlanırken o sınıfın instantiate sürecine müdahele etmeye izin verir. Bu süreçte metaclass şunları yapabilir: attribute'leri değiştir, doğrula, otomatik metot ekle, kayıt tut, <b>alt sınıflamayı engelle</b>, örnekleme davranışını(instance creation) özelleştir vb.

### Metaclass hooks [new, init, call, prepare]

#### Sınıf bildirim sırası:

1. metaclass.prepare(name, bases) — class bloğu için namespace (mapping) hazırlanır.
2. class bloğu çalışır; attributeler namespace’e eklenir.
3. metaclass.new(mcls, name, bases, namespace) — sınıf nesnesi oluşturulmadan önce çağrılır.
4. metaclass.init(cls, name, bases, namespace) — sınıf nesnesi yaratıldıktan sonra başlatma yapılır.

5. Sınıf örneklenirken (örnek oluşturma): metaclass.call(cls, \*args, \*\*kwargs) — MyClass(...) yapıldığında çağrılır.

---

#### hook detayları

1. prepare()

- Ne zaman çağrılır: class tanımı başlarken, class bloğunun yürütüleceği namespace(mapping) oluşturulmadan hemen önce çağrılır.
- Amaç: class bloğunda kullanılacak namespace türünü belirlemek ve başlangıçta bazı başlayıcı öğeler inject etmek.
- Parametreler: def prepare(mcls, name, bases, \*\*kw) -> mapping. Burada mcls metaclass(class of class), name sınıf adı, bases base sınıfların tuple'ı.
- Return: class bloğu için bir mapping(dict benzeri) olmalı. Bu mapping içine class gövdesi çalışırken tanımlanan isimler yazılır.
- bkz. meta_class_prepare.py

2. new()

- Ne zaman çağrılır: class bloğu yürütüldükten sonra, ama sınıf nesnesi gerçekten oluşturulmadan hemen önce. Burada yeni sınıf nesnesi (type instantiation) oluşturulur.
- Amaç: sınıf nesnesinin oluşturulma sürecine müdahale; namespace’i değiştirmek, attribute eklemek/silmek, farklı bir sınıf objesi döndürmek.
- Parametreler:
  - mcls: metaclass (ör. class MyMeta(type): ...)
  - name: oluşturulan sınıfın adı (string)
  - bases: base sınıfların tuple'ı
  - namespace: class bloğunda oluşan mapping (ör. dict veya prepare tarafından döndürülen mapping)

3. init()

- Ne zaman çağrılır: metaclass.new() tarafından bir class objesi döndürüldükten sonra, oluşturulan sınıf nesnesinin (cls) başlatılması için çağrılır. Yani class objesi artık var ve bu kanca sınıf seviyesinde ek başlatma/validasyon yapmak için kullanılır.
- Amaç: oluşturulmuş sınıf üzerinde doğrulama, kayıt, ek attribute’ları compute etme veya meta-initialization yapmak.
- Parametreler:
  - cls: yeni oluşturulan sınıf objesi (ör. class My: ... -> My)
  - name, bases, namespace: aynı bilgiler (namespace genelde orijinal mapping)
- Dönen değer: None. Burada sınıf objesini döndürmüyorsun; sadece başlatma yapıyorsun.

4. call()

- Ne zaman çağrılır: Sınıf örneği oluşturulurken; yani MyClass(\*a, \*\*k) ifadesinde metaclass’ın call'ı ilk çağrılan kancadır.
- Amaç: örnekleme sürecini (instance creation) kontrol etmek. Buradan instance önbellekleme (singleton/flyweight), factory davranışı, argument validation, örnek oluşturma öncesi/sonrası davranış eklemek mümkün.
- Parametreler:
  - cls: sınıf (ör. MyClass)
  - \*args, \*\*kwargs: örnekleme argümanları

#### hangi hook’ta ne yapmalı?

- prepare: class bloğunun namespace’ini hazırlamak / sıralama veya başlangıç verisi inject etmek.
- new: sınıf nesnesi yaratılmadan önce namespace’i değiştirmek veya farklı bir sınıf objesi döndürmek (low-level).
- init: oluşturulmuş sınıf üzerinde validation, registry, ek başlatma işleri yapmak (high-level initialization).
- call: sınıf örneği oluşturulurken kontrol; singleton, factory, caching, argument validation.
