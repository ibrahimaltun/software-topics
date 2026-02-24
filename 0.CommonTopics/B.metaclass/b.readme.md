## metaclass

- Bir sınıf tanımlanırken o sınıfın instantiate sürecine müdahele etmeye izin verir. Bu süreçte metaclass şunları yapabilir: attribute'leri değiştir, doğrula, otomatik metot ekle, kayıt tut, <b>alt sınıflamayı engelle</b>, örnekleme davranışını(instance creation) özelleştir vb.

### Metaclass hooks [new, init, call, prepare]

#### Sınıf bildirim sırası:

1. metaclass.prepare(name, bases) — class bloğu için namespace (mapping) hazırlanır.
2. class bloğu çalışır; attributeler namespace’e eklenir.
3. metaclass.new(mcls, name, bases, namespace) — sınıf nesnesi yaratılmadan önce çağrılır.
4. metaclass.init(cls, name, bases, namespace) — sınıf nesnesi yaratıldıktan sonra başlatma yapılır.

5. Sınıf örneklenirken (örnek oluşturma): metaclass.call(cls, \*args, \*\*kwargs) — MyClass(...) yapıldığında çağrılır.

---

#### hook detayları

1. prepare

- Ne zaman çağrılır: class tanımı başlarken, class bloğunun yürütüleceği namespace(mapping) oluşturulmadan hemen önce çağrılır.
- Amaç: class bloğunda kullanılacak namespace türünü belirlemek ve başlangıçta bazı başlayıcı öğeler inject etmek.
- Parametreler: def prepare(mcls, name, bases, \*\*kw) -> mapping. Burada mcls metaclass(class of class), name sınıf adı, bases base sınıfların tuple'ı.
- Return: class bloğu için bir mapping(dict benzeri) olmalı. Bu mapping içine class gövdesi çalışırken tanımlanan isimler yazılır.
- bkz. meta_class_prepare.py

2.
