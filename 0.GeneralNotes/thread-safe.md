## Thread-Safe

- Thread-safe: Function, class veya data structure gibi bir bileşenin aynı anda birden fazla thread(iş parçacığı) tarafından kullanıldığında doğru ve beklenen davranışı sürdürmesi demektir.

- Temelde sorun, aynı veriye eşzamanlı erişim sonucu "race condition" (yarış durumu) oluşabilir; sonuç belirsiz veya hatalı olur.

- Çözüm yolları: Eşzamanlama(locks, mutex, semafor), atomik işlemler, immutable(değiştirilemez) veri, thread-local storage, yüksek seviye thread-safe veri yapıları(queue vb.) veya süreç tabanlı paralellik(multiprocessing)

### Problem tam olarak nerede başlıyor?

- Birden fazla thread aynı anda aynı paylaşılan veriyi okur ya da yazar.
- Örneğin sayacı(counter) artırma işlemi tek bir yüksek seviyeli ifade gibi görünse de, altta birden çok CPU komutu/bytecode çalışır: oku -> artır -> yaz. Bu adımlar başka bir thread tarafından ara adımda kesintiye uğrayabilir ve iki thread aynı eski değeri okuyup üzerine yazarsa artış adımı kaybolur.

---

### Temel kavramlar nelerdir?

1. Race Condition: 2 veya daha fazla thread'in yürütme sırasına bağlı olarak farklı sonuçların ortaya çıkması.

2. Atomicity(Atomiklik): Bir işlemin bölünemez olması - ya tamamen gerçekleşir ya hiç gerçekleşmez. Atomik işlemler race durumuna uğramaz.

3. Visibility(Görünürlük): Bir thread'in yaptığı değişikliklerin diğer thread'ler tarafından ne zaman görüülür. Bazı bellek modellerindne yazılan veri hemen görünmeyebilir.

4. Ordering(Sıralama): İşelemler farklı thread'lerde farklı sıralarda gözlemlenebilir, bellek bariyerleri ve senkronizasyon sıralamayı etkiler.

5. Deadlock(Kilitlenme): 2 veya daha fazla thread karşılıklı olarak birbirlerinin kilitlerini beklerse sistem kitlenir.

6. Livelock: Thread'lerin sürekli aktif fakat ilerleme göstermediği durum.

---

### Eşzamanlama araçları

- threading.Lock (mutex): Kritik bölgeyi (critical section) korur.
- threading.RLock (re-entrant lock): Aynı thread'in aynı kilidi tekrar almasına izin verir.
- threading.Condition: Bekleme/yeni durum bildirimi için kullanılır.
- threading.Event: Bir olayın gerçekleşmesini beklemek/bildirmek için kullanılabilir.
- threading.Semaphore: Sınırlı sayıda eşzamanlı erişim gerekiyorsa.
- queue.Queue: Producer-consumer tipinde thread-safe kuyruk (hazır ve güvenli).
- concurrent.futures.ThreadPoolExecutor: Thread havuzu, görev yönetimi.
- threading.local: Her thread için ayrı veri saklamak (paylaşımı engeller).
- multiprocessing: CPU-bound işler için süreç (process) tabanlı paralellik (GIL engellemesine karşı).

Not: CPython'un GIL (Global Interpreter Lock) adlı mekanizması vardır; bu, aynı anda sadece bir thread'in Python bytecode çalıştırmasına izin verir. Ancak:

- GIL, tüm thread-safety problemlerini ortadan kaldırmaz. Örneğin birkaç bytecode içeren bir işlemin atomik olduğunu garanti etmez; yine race condition oluşabilir.
- GIL I/O sırasında serbest bırakılır; dolayısıyla I/O-bound uygulamalarda thread'ler birbirini etkileyebilir.
- Yine de kodda kesin doğruluk gerekiyorsa explicit (açık) kilit kullanmak en güvenli yaklaşımdır.

### Örnekler

1. Thread-safe olmayan sayaç (race condition): Gerçek değer, beklenen değerden küçük olacaktır. Çünkü artışlar kaybolur: race condition
2. Lock kullanarak thread-safe sayaç: with self.\_lock ile her artış atomik hale gelir; sonuç beklenen değer olur.
3. Producer-Consumer yapısı ve queue.Queue ile thread-safe: queue'lar zaten thread safe'tir ek kiltlemeye gerek yoktur.
4. Burada thread1 lock_a sonra lock_b alırken, thread2 ters sırada alırsa karşılıklı bekleme (deadlock) oluşabilir. Kaçınma yolları:
   - Kilitleri tutarlı (aynı) sırada al (ör. önce lock_a sonra lock_b her yerde).
   - try-acquire ile timeout kullan, başarısızsa geri çekil ve yeniden dene.
   - Daha yüksek seviyeli eşzamanlama yapıları kullan.
