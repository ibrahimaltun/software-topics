#### metaclass

- Bir sınıf tanımlanırken o sınıfın instantiate sürecine müdahele etmeye izin verir. Bu süreçte metaclass şunları yapabilir: attribute'leri değiştir, doğrula, otomatik metot ekle, kayıt tut, <b>alt sınıflamayı engelle</b>, örnekleme davranışını(instance creation) özelleştir vb.

##### Metaclass hooks

- new(mcls, name, bases, namespace): Metaclass'ın yeni sınıf nesnesini oluşturmadan önce çağrılır.
- init():
- call():
- prepare():

## ---------------------
