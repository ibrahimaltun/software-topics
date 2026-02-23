### cre1_singleton_config.py

- An application reads configuration from a file once and all parts of the app must read the same settings.
- Note: The metaclass holds instances per subclass, is thread-safe, and ignores subsequent constructor args (common Singleton caveat).

### cre1_singleton_logging.py

- A centralized logging facility that configures formatting/handlers once and modules fetch the same logger instance.

#### metaclass

- Bir sınıf tanımlanırken o sınıfın instantiate sürecine müdahele etmeye izin verir. Bu süreçte metaclass şunları yapabilir: attribute'leri değiştir, doğrula, otomatik metot ekle, kayıt tut, <b>alt sınıflamayı engelle</b>, örnekleme davranışını(instance creation) özelleştir vb.

##### Metaclass hooks

- new():
- init():
- call():
- prepare():

## ---------------------
