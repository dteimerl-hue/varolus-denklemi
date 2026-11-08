# Varoluş Denklemi — 12 yeni bilim deneyimi fikri

Ölçüt: oyuncu *eliyle* bir şey yapar, ölçer ya da keşfeder; pasif metin yok. Mevcut içerikle (Büyük Patlama/CMB, dolanıklık/tünelleme/dekoherans, Mars/Europa/Enceladus, nöron eşiği, yer hücreleri, bellek pekiştirme, Navier-Stokes/Reynolds, Apophis, Jack Hills zirkonu, Theia, mevcut mini oyunlar Eşik/Yörünge Yakalama/Yankı Dizisi/ER=EPR kalibrasyonu) çakışmayan konular seçildi. Sıralama: en etkileşimli ve bilimsel olarak en sağlam olanlar önce.

Ortak teknik ilkeler (hepsi tek HTML, sunucusuz):
- Canlı veri `fetch` ile, 6-8 sn zaman aşımı; başarısız olursa gömülü "anlık görüntü" (snapshot) verisine düşülür ve Motor bunu dürüstçe söyler: "Canlı bağlantı yok; elimdeki son kayıt şu tarihli." Uydurma değer üretilmez (oyunun "sis gösterir" ilkesi).
- Oyuncunun ölçtüğü değerler Günlük → Veriler sekmesine "kendi ölçümüm" etiketiyle yazılır; gerçek değerle yan yana gösterilir, ama "doğru/yanlış" yerine "sapma: %x" denir.
- CORS durumu her API için ayrıca belirtildi; "doğrulanmalı" yazanlar için artifact ortamından bir kez test edilmeli.

Maliyet ölçeği: **küçük** = 1-2 gün, ≤300 satır, yalnız canvas/DOM; **orta** = 3-5 gün, yeni 3D nesne + arayüz + veri katmanı; **büyük** = 1 hafta+, yeni oda/mekanik.

---

## 1. Galileo'nun Eğik Düzlemi — "Zamanı Müzikle Ölç"

**Oyuncunun yaptığı:** Yuva boyutundaki atölyede ahşap bir eğik düzlem var. Oyuncu eğimi kaydırıcıyla ayarlar, bilyeyi bırakır ve bilye düzlem üzerindeki küçük "perde tellerine" (Galileo'nun lavta telleri gibi) çarptıkça tık sesi duyulur. Oyuncu telleri sürükleyerek öyle yerleştirir ki tık sesleri *eşit aralıklı* duyulsun (metronomla karşılaştırmalı). Sonra tellerin konumlarını cetvelle okur: 1, 4, 9, 16... birimlik mesafeler çıkar; ardışık aralıklar 1:3:5:7. Oyun, oyuncunun kendi tel konumlarından üssü (d ∝ t^n) hesaplar ve n≈2'yi gösterir.

**Öğretilen kavram:** Düzgün ivmeli hareket, d ∝ t², "tek sayılar kuralı"; zamanı doğrudan ölçemediğinde onu eşit aralıklara *dönüştürerek* ölçmek (deney tasarımı dehası). Yuvarlanan katı küre için a = (5/7)·g·sinθ (sürtünmesiz kayma değil).

**Kaynak:** Galileo, *Discorsi* (İki Yeni Bilim), 1638, Üçüncü Gün; Stillman Drake, "The Role of Music in Galileo's Experiments", *Scientific American*, Haziran 1975 (Galileo'nun tık-eşitleme yöntemi rekonstrüksiyonu). Wikipedia kartı: "Galileo'nun eğik düzlem deneyi".

**Boyut:** Yuva (genç Dünya atölyesi) ya da Tesis atölyesi.

**Maliyet:** Küçük (2D canvas + Web Audio tık sesleri; fizik tek satır: s = ½·a·t²).

**Tuzak:** (1) Pisa Kulesi efsanesini doğru gibi anlatmamak — belgelenmiş deney eğik düzlemdir. (2) Ekranda "g = 9,81 ölçtün" dememek: yuvarlanma ataleti nedeniyle eğik düzlemden g'yi çıkarmak 5/7 çarpanı ister; bu çarpan anlatılmadan g gösterilirse yanlış öğretilir. (3) Galileo su saati de kullandı; "kronometresi yoktu, o yüzden kulak kullandı" demek doğru, "kronometre icat etti" demek yanlış.

---

## 2. Eratosthenes'in Gölgesi — İki Gnomon, Bir Gezegen (Sunrise-Sunset API)

**Oyuncunun yaptığı:** Oyuncu Tesis'in üstündeki Kapadokya yüzeyine (38,6°K, 34,8°D) bir gnomon (dikey çubuk) diker; haritadan ikinci bir şehir seçer (önerilen: aynı boylama yakın, örn. İskenderiye 31,2°K ya da Kahire). Oyun her iki nokta için o günün *gerçek* güneş öğle vaktini (solar_noon) API'den çeker; oyuncu 3D sahnede gölgeyi iletki aracıyla ölçer (güneş yüksekliği fiziksel gökyüzünden alınır). İki açının farkını ve iki şehir arasındaki kuzey-güney mesafeyi (haritadan cetvelle) girer; oyun oyuncunun sayılarıyla Dünya çevresini hesaplar.

**Öğretilen kavram:** Dünya'nın küreselliği ve çevresinin ölçülmesi; açı ↔ yay uzunluğu ilişkisi (Δφ/360° = d/Çevre); güneş deklinasyonu (öğle gölge açısı = |enlem − deklinasyon|). Kaynak belirsizliği: Eratosthenes'in "stadion" biriminin uzunluğu (157-185 m) bilinmediği için ünlü "%1-2 hata" iddiası şüphelidir — oyun bunu açıkça söyler.

**Kaynak:** Kleomedes, *Göksel Cisimlerin Dairesel Hareketleri Üzerine* (Eratosthenes'in 5000 stadia / 1/50 daire hesabının aktarımı, ~MÖ 240); gerçek meridyen çevresi 40.008 km. API: `https://api.sunrise-sunset.org/json?lat=38.6&lng=34.8&formatted=0` (anahtarsız, HTTPS, CORS açık; `solar_noon`, `sunrise`, `sunset`, `day_length` alanları). Deklinasyon oyun içinde hesaplanır: δ ≈ 23,44°·sin(360°·(N−81)/365).

**Boyut:** Yuva (genç Dünya'dan 2050'ye köprü: "insan bu gezegeni önce ölçtü").

**Maliyet:** Küçük-orta (gnomon 3D nesnesi mevcut gölge sistemiyle; iletki arayüzü canvas; API tek çağrı).

**Tuzak:** (1) İki şehir aynı boylamda değilse öğle vakitleri farklıdır; oyun oyuncuyu "aynı anda" değil "her birinin kendi öğlesinde" ölçmeye yönlendirmeli. (2) "Eratosthenes Dünya'nın yuvarlak olduğunu kanıtladı" demek yanlış — küresellik o dönemde zaten kabul görüyordu; o *çevresini ölçtü*. (3) Oyun içi güneş yüksekliği gerçek tarih/saatle tutarlı olmalı; yoksa API'den gelen gerçek öğle vakti ile sahne çelişir.

---

## 3. Sismograf Terminali — Kapadokya'nın Altında Dünya'yı Dinle (USGS canlı)

**Oyuncunun yaptığı:** Tesis'e bir sismograf konsolu eklenir. Canlı USGS akışından son 24 saatin depremleri döner küre üzerinde noktalar olarak belirir. Oyuncu büyüklük eşiğini kaydırıcıyla ayarlar (M2,5 → M4,5 → M6) ve her eşikte kaç deprem kaldığını görür. Bir depremi seçince konsol, Tesis'e olan uzaklığı ve P ile S dalgalarının *ne zaman* geleceğini hesaplar; oyuncu "S−P süresi × 8 ≈ km" kuralıyla üç istasyondan üçgenleme yaparak depremin yerini kendisi bulur (oyun, gerçek konumu ancak oyuncu tahmin ettikten sonra açar).

**Öğretilen kavram:** Logaritmik büyüklük ölçeği (her 1 birim ≈ 31,6 kat enerji; log₁₀E = 1,5M + 4,8 J); P (~6 km/s) ve S (~3,5 km/s) dalga hızları; üçgenleme; küçük depremlerin büyüklerden çok daha sık olması (Gutenberg-Richter). Türkiye'nin aktif fay sisteminde yaşadığı gerçeği oyunun kendi coğrafyasıyla bağlanır.

**Kaynak:** USGS Earthquake Hazards Program GeoJSON özet akışları: `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson` (ayrıca `2.5_day`, `4.5_week`; anahtarsız, CORS açık, dakikada bir güncellenir; her kayıtta `mag`, `magType`, `place`, `time`, `coordinates[lon,lat,depth_km]`). Büyüklük-enerji: Gutenberg & Richter 1956, *Bull. Seismol. Soc. Am.* 46. Türkiye için karşılaştırma kartı: AFAD / Kandilli (API yok, yalnız bağlantı).

**Boyut:** Tesis (yeraltı — "Motor Çekirdeği'nin yanında Dünya'nın nabzı"); Yuva ile de bağlanır.

**Maliyet:** Küçük-orta (küre zaten var; noktalar + konsol arayüzü; fallback için 50 depremlik gömülü snapshot).

**Tuzak:** (1) "Richter ölçeği" demek yanlış olabilir — akıştaki `magType` çoğunlukla Mw/mww/ml; "moment büyüklüğü" diyerek doğrusunu öğretmek gerekir. (2) Deprem *tahmini* yapılabilirmiş izlenimi asla verilmemeli; olasılıksal uzun vadeli "öngörü" ile kısa vadeli "kehanet" farkı Motor'un ağzından açıkça söylenmeli. (3) İlk büyüklükler sonradan revize edilir; akış gecikmeli olabilir — "canlı" demek yerine "en son bildirilen" demeli. (4) S−P×8 kuralı yerel kabuk için kaba bir yaklaşımdır; uzak depremler için geçersiz.

---

## 4. Yarı Ömür Zarları — Aşıklı Höyük'ün Yaşı (radyokarbon)

**Oyuncunun yaptığı:** Masada 1000 "atom" (parlayan küpler) var. Oyuncu her "vuruş"ta zar atar; her atom belirli bir olasılıkla söner. Oyuncu sönen sayısını kendi sayar, grafiğe işler, yarıya düşme süresini *okur* (her denemede biraz farklı çıkar — bu kasıtlı). Sonra oyun gerçek bir örnek verir: Kapadokya'daki Aşıklı Höyük'ten kömür — "kalan C-14 oranı %36" gibi — ve oyuncu kendi ölçtüğü yarı ömürle yaşı hesaplar; ardından IntCal kalibrasyon eğrisinde "radyokarbon yılı → takvim yılı" dönüşümünü kaydırıcıyla yapar.

**Öğretilen kavram:** Üstel bozunma, rastgelelik ve büyük sayılar yasası (tek atom için kehanet yok, 1000 atom için var); yarı ömür (5730 ± 40 yıl); kalibrasyon gerekliliği (atmosferik C-14 sabit değil); C-14'ün yalnız ~50 bin yıla kadar işe yaraması. Zirkonun U-Pb ile tarihlenmesi (oyunda mevcut) ile aynı mantık, farklı saat — iki yöntem birbirine bağlanır.

**Kaynak:** Libby, Anderson & Arnold 1949, *Science* 109:227; Reimer ve ark. 2020, "The IntCal20 Northern Hemisphere radiocarbon age calibration curve", *Radiocarbon* 62(4):725-757. Aşıklı Höyük: ~MÖ 8350-7300 kal. (Özbaşaran ve ark., *The Early Settlement at Aşıklı Höyük*, 2018). Göbekli Tepe: III. tabaka ~MÖ 9500 (Dietrich ve ark. 2013, *Antiquity* 87). Wikipedia kartı: "Radyokarbon tarihleme", "Aşıklı Höyük".

**Boyut:** Yuva (genç Dünya + insanın ilk yerleşimleri, Kapadokya'nın kendi tarihi).

**Maliyet:** Küçük (canvas, Math.random; IntCal20 eğrisinin 0-12.000 yıl bölümü ~200 noktalık gömülü tablo).

**Tuzak:** (1) "Radyokarbon yılı" ile "takvim yılı"nı eşitlemek; 1950 öncesi "BP" konvansiyonunu anlatmadan yaş vermek. (2) Libby yarı ömrü (5568) ile Cambridge yarı ömrü (5730) karışıklığı — laboratuvarlar raporlarda hâlâ 5568 kullanır; oyun tek birini seçip bunu söylemeli. (3) C-14 ile dinozor/kaya yaşı hesaplanabilirmiş izlenimi. (4) Zar simülasyonunda "her yarı ömürde tam yarısı söner" demek — rastgele sapmayı göstermek deneyin asıl amacı.

---

## 5. ISS'yi Yakala — "10 Dakika Sonra Nerede?" (wheretheiss.at canlı)

**Oyuncunun yaptığı:** Gezegen boyutundaki gözlem güvertesinde döner Dünya üzerinde ISS'nin *gerçek* anlık konumu, yüksekliği ve hızı görünür. Oyuncu bir işaretçiyi sürükleyerek "10 dakika sonra burada olacak" tahmini yapar; oyun gerçek zamanlı bekler (ya da oyuncu "ileri sar" derse yörünge mekaniğiyle hesaplar) ve gerçek konumu gösterir, sapmayı km olarak ölçer. İkinci tur: oyuncu hız ve yükseklikten yörünge periyodunu kendisi hesaplar (T = 2π(R+h)/v) ve "bir tur sonra yer izi neden ~23° batıya kayıyor?" sorusunu Dünya'nın dönüşüyle çözer.

**Öğretilen kavram:** Yörünge hızı (~7,66 km/s), ~93 dakikalık periyot, yer izi ve Dünya dönüşü, "ağırlıksızlık = yerçekimsizlik değil, serbest düşüş" (ISS yüksekliğinde g yüzeyin ~%90'ı).

**Kaynak:** `https://api.wheretheiss.at/v1/satellites/25544` (anahtarsız, HTTPS, CORS açık, ~1 istek/sn sınır; `latitude, longitude, altitude [km], velocity [km/h], timestamp`). Yedek: NASA Spot the Station (yalnız bağlantı). Yörünge: Vallado, *Fundamentals of Astrodynamics* (daire yörünge formülleri).

**Boyut:** Gezegen (ya da Yuva 2050 — "insanlık 25 yıldır sürekli yörüngede").

**Maliyet:** Küçük (küre mevcut; işaretçi sürükleme + tek API çağrısı; fallback için TLE'den basit propagasyon yerine "son bilinen konum + sabit hız" yaklaşımı yeterli).

**Tuzak:** (1) `api.open-notify.org` yalnız HTTP'dir; HTTPS artifact içinden karışık içerik engeline takılır — kullanılmamalı. (2) "10 dakika ileri sar" hesabı basit daire yörüngeyle yapılırsa birkaç km sapar; bu sapma gizlenmemeli ("modelim basit, gerçek yörünge hafif eliptik ve sürtünmeyle alçalıyor"). (3) ISS'nin "uzayda" olduğunu söylerken atmosferin tamamen bittiğini ima etmemek — termosferde, sürekli yükseltme gerekir.

---

## 6. Transit Avı — Işık Eğrisine Gezegen Sığdır (NASA Exoplanet Archive TAP)

**Oyuncunun yaptığı:** Gezegen boyutunda bir teleskop konsolu. Canlı TAP sorgusuyla transit yöntemiyle keşfedilmiş gerçek gezegenlerden biri seçilir (ör. "bu hafta keşfedilen en yeni gezegen" ya da TRAPPIST-1 e). Oyun, yıldız yarıçapı ve gezegen yarıçapından *sentetik* ışık eğrisi üretir (gürültülü). Oyuncu iki kadranla — gezegen yarıçapı ve yörünge periyodu — bir model eğri çizer ve gerçek verinin üstüne oturtmaya çalışır; artık (residual) grafiği sıfıra yaklaşınca "yakaladın". Sonra arşiv değeriyle karşılaştırır ve Kepler'in 3. yasasıyla yörünge yarıçapını, yıldız sıcaklığından denge sıcaklığını hesaplar.

**Öğretilen kavram:** Transit derinliği ≈ (R_gezegen/R_yıldız)² (Dünya-Güneş için ~84 ppm, Jüpiter için ~%1), periyot → yarı-büyük eksen (a³/P² = GM/4π²), model uydurma ve artık analizi, "yaşanabilir bölge" ≠ "yaşanabilir".

**Kaynak:** NASA Exoplanet Archive TAP: `https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,pl_orbper,pl_rade,pl_trandep,st_rad,st_teff,disc_year+from+ps+where+default_flag=1+and+tran_flag=1&format=json` (anahtarsız; **CORS tarayıcıdan doğrulanmalı** — açık değilse 100 gezegenlik gömülü snapshot). Yöntem: Winn 2010, "Transits and Occultations", arXiv:1001.2010. Wikipedia kartı: yıldız adıyla `tr.wikipedia.org/api/rest_v1/page/summary/...`.

**Boyut:** Gezegen.

**Maliyet:** Orta (ışık eğrisi üretimi + iki kadranlı uydurma arayüzü + TAP ayrıştırma; 3D teleskop nesnesi isteğe bağlı).

**Tuzak:** (1) Gerçek ışık eğrisi verisi değil *sentetik* eğri kullanıldığı açıkça yazılmalı ("gerçek parametrelerden üretilmiş"). (2) Limb darkening, eğiklik, eksantriklik ihmal ediliyor — derinlik formülü yaklaşıktır. (3) "Dünya benzeri" etiketini yarıçap benzerliğinden türetmemek; kütle/atmosfer bilinmeyebilir (`pl_bmasse` boş olabilir). (4) Arşivde aynı gezegen için birden çok satır var; `default_flag=1` filtresi şart, yoksa çelişkili değerler görünür.

---

## 7. Bulut Odası — Yeraltında Müon Say (Wilson odası + Anderson + Frisch-Smith)

**Oyuncunun yaptığı:** Kuantum boyutunda (ya da Tesis laboratuvarında) bir bulut odası. Oyuncu alkol buharı ve soğutma kadranlarını ayarlayarak aşırı doygunluğu "tutturur"; o anda izler belirmeye başlar: kalın-kısa (alfa), ince-kıvrık (beta), ince-dümdüz (müon). Oyuncu mıknatıs kadranını açar — izler kıvrılır; kurşun plaka ekler — Anderson'ın 1932 fotoğrafındaki gibi plakadan geçen parçacığın enerji kaybetmesinden yönünü, kıvrım yönünden yükünü okur. Sonra oyuncu "yükseklik" kadranıyla odayı dağ zirvesine, deniz seviyesine ve Tesis'in bulunduğu yeraltı derinliğine taşır; 1 dakikada saydığı müon sayısını üç kere kaydeder ve "neden hâlâ geliyorlar?" sorusuna zaman genişlemesi hesabıyla yanıt verir (2,2 µs ömür × 0,998c ≈ 660 m; ama 15 km'den geliyorlar → γ ≈ 20+).

**Öğretilen kavram:** Kozmik ışınlar ve ikincil müonlar; yük/momentum okuma (manyetik alanda kıvrılma yarıçapı); pozitronun keşfi; özel görelilikte zaman genişlemesinin *doğrudan gözlemi*; kayaç derinliğinin müon akısını azaltması (yeraltı laboratuvarlarının neden derinde kurulduğu — Tesis'in konumuna yeni bir anlam).

**Kaynak:** C.T.R. Wilson 1912, *Proc. R. Soc. A* 87:277 (Nobel 1927); Anderson 1933, "The Positive Electron", *Phys. Rev.* 43:491; Frisch & Smith 1963, "Measurement of the Relativistic Time Dilation Using µ-Mesons", *Am. J. Phys.* 31:342; Particle Data Group, "Cosmic Rays" derlemesi (deniz seviyesinde yatay dedektörde ~1 müon/cm²/dk). Wikipedia kartı: "Bulut odası", "Müon".

**Boyut:** Kuantum (parçacık/alan fiziği eşiği) — Başlangıç'a da uyar (kozmik ışınların kaynağı).

**Maliyet:** Orta (parçacık izi partikül sistemi mevcut sis parçacık altyapısıyla; kadran arayüzü; sayaç; Poisson rastgelelik).

**Tuzak:** (1) Müon akısı derinlikle çok hızlı düşer; oyun "Tesis'te 1/1000" gibi kesin rakam vermemeli — "kayacın kalınlığına göre yüzde birlere, binde birlere" demeli ve derinliği belirsiz bırakmalı (oyun kurgusu derinliği tanımlamıyor). (2) "Müonlar zaman genişlemesi *sayesinde* bize ulaşır" doğru; "Dünya'nın çerçevesinde ömürleri uzar, kendi çerçevelerinde mesafe kısalır" — iki bakış da verilmeli, biri "gerçek" diye sunulmamalı. (3) Bulut odasında gördüğün her iz "kozmik" değildir; radon alfa'ları baskındır — oyuncu türleri ayırt etmeyi öğrenmeli, "hepsi uzaydan" dememeli. (4) Pozitron "antimadde = negatif enerji/patlama" klişesine kaymamak.

---

## 8. Düşüncenin Hızı — Helmholtz'un Kronometresi (tepki süresi deneyi)

**Oyuncunun yaptığı:** Bilinç boyutunda bir deney masası. Oyuncu 20 denemede ışığa, 20 denemede sese tepki verir (tuş/dokunma); oyun `performance.now()` ile ms ölçer, histogram çizer, medyanı okutur. Üçüncü blok: "seçimli tepki" (sol ışık → A, sağ ışık → D). Oyuncu Donders'in çıkarma yöntemiyle "karar vermenin maliyetini" kendi verisinden hesaplar (seçimli − basit ≈ 50-150 ms). Son soru: "Gözden parmağa yol ~1,5 m; sinir iletim hızı 60-120 m/s olsa bile neden 200 ms?" → iletim değil *işleme* zaman alıyor.

**Öğretilen kavram:** Sinir iletim hızının sonlu olması (Helmholtz 1850, kurbağa siyatiği ~27 m/s — "düşünce anlık değildir" şokunun tarihi); işitsel tepkinin görselden ~30-40 ms hızlı olması (retina fototransdüksiyonu yavaş); tepki süresinin dağılım olması (tek sayı değil); Donders çıkarma mantığı. Mevcut "Eşik" mini oyunuyla (nöron eşiği) tamamlayıcı: orada tek nöron, burada tüm döngü.

**Kaynak:** Helmholtz 1850, *Archiv für Anatomie, Physiologie* ("Messungen über den zeitlichen Verlauf der Zuckung animalischer Muskeln..."); Donders 1868/1969, "On the speed of mental processes", *Acta Psychologica* 30:412 (çeviri); Kosinski 2013, "A Literature Review on Reaction Time" (Clemson Üniv. derlemesi; işitsel ~140-160 ms, görsel ~180-200 ms). Wikipedia kartı: "Tepki süresi", "Hermann von Helmholtz".

**Boyut:** Bilinç.

**Maliyet:** Küçük (DOM/canvas; ses için mevcut Web Audio; 150 satır).

**Tuzak:** (1) Ekran yenileme (60 Hz → 16,7 ms kuantalama) ve ses gecikmesi (10-50 ms) ölçüme eklenir; oyun "mutlak değer değil, karşılaştırma ölçüyorsun" demeli ve iki uyaranı da aynı gecikme zinciriyle vermeli. (2) Tanı/performans iması yok ("yavaşsın", "yorgunsun" yok; Lale nörologdu ama oyun doktor değil). (3) Konuşma sentezini uyaran olarak kullanmamak — gecikmesi değişken; kısa osilatör bip kullanmalı. (4) Çok hızlı tepkiler (<100 ms) "tahmin" olarak işaretlenmeli, veri dışı bırakılmalı.

---

## 9. Foucault Sarkacı — Tesis'in Enlemini Sarkaçla Bul

**Oyuncunun yaptığı:** Tesis'in merkez kuyusuna 20 m'lik bir sarkaç asılır (Motor Çekirdeği heykelinin yanı). Oyuncu sarkacı iple çekip yakarak (Foucault'nun ipi yakma tekniği) düzgün başlatır; zemindeki dereceli halka üzerinde salınım düzleminin yönünü her oyun-saatinde işaretler (oyun zamanı hızlandırılabilir). 4-6 işaretten saatlik dönüş hızını ölçer (Kapadokya'da ~9,4°/saat) ve ω = 15°/saat × sin(enlem) ilişkisinden enlemi hesaplar: sin φ = 9,4/15 → φ ≈ 38,6°. "Tesis'in nerede olduğunu Bakanlık söylemedi; sarkaç söyledi."

**Öğretilen kavram:** Dünya'nın dönüşünün yerel, laboratuvar içi kanıtı; dönen çerçevede Coriolis etkisi; enleme bağlılık (kutupta 24 saat, ekvatorda hiç dönmez; Kapadokya'da tam tur ~38,5 saat); ölçümden parametre çıkarma.

**Kaynak:** Foucault 1851, *Comptes Rendus* 32:135 ("Démonstration physique du mouvement de rotation de la Terre au moyen du pendule"); Panthéon deneyi: 67 m tel, 28 kg küre. Wikipedia kartı: "Foucault sarkacı".

**Boyut:** Tesis (Çekirdek kuyusu) — Yuva'ya köprü.

**Maliyet:** Küçük (3D sarkaç tek mesh + ip; zemin halkası texture; işaretleme arayüzü).

**Tuzak:** (1) Kötü başlatılan sarkaç elips çizer ve sahte presesyon üretir — Foucault'nun ip yakma ve Charron halkası çözümleri oyunda "neden" diye anlatılmalı; aksi halde oyuncu "ölçüm hep aynı" sanır. (2) Hızlandırılmış oyun zamanı sarkacın gerçek periyodunu (20 m için ~9 s) bozmamalı; iki ayrı saat (salınım ve dönüş) ekranda ayrı gösterilmeli. (3) "Sarkaç Dünya'nın döndüğünü kanıtlar" — doğru, ama "mutlak uzaya göre" tartışmasına (Mach) Anlam boyutunda bir cümlelik köprü vermek iyi; kesin dil kullanmamak.

---

## 10. Uzay Havası Panosu — Güneş Rüzgârı ve Kutup Işığı Sınırı (NOAA SWPC canlı)

**Oyuncunun yaptığı:** Gezegen boyutunun gözlem güvertesinde canlı Kp indeksi, güneş rüzgârı hızı ve Bz bileşeni gösterilir. Oyuncu "auroral oval" haritasında kendi eşiğini seçer; Kp değiştikçe ovalin güneye ne kadar indiğini görür ve "Türkiye'den ne zaman görülür?" sorusuna oval haritasından yanıt verir (yalnız Kp 8-9, G4-G5 — Mayıs 2024'te oldu). Tesis telsizinde parazit, gerçek Kp ile orantılı artar (ses katmanı). Mini görev: son 24 saatlik Bz grafiğinde "güneye dönüş" anlarını işaretleyip Kp artışıyla gecikmeli eşleştirmek.

**Öğretilen kavram:** Güneş rüzgârı-manyetosfer bağlaşımı (güneye dönük Bz = anahtar), Kp ölçeği (0-9, yarı-logaritmik, 3 saatlik, gezegensel), G-ölçeği (G1=Kp5 ... G5=Kp9), kutup ışığının enlem bağımlılığı, uydu/GPS/elektrik şebekesi etkileri.

**Kaynak:** NOAA SWPC ürünleri: `https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json`, `.../products/solar-wind/mag-1-day.json` (bz_gsm), `.../products/solar-wind/plasma-1-day.json` (hız, yoğunluk) — anahtarsız, HTTPS; **CORS doğrulanmalı** (tarayıcı panolarında yaygın kullanılıyor, muhtemelen açık). Ölçek tanımları: NOAA Space Weather Scales. Mayıs 2024 G5 fırtınası (Gannon fırtınası): NOAA SWPC bülteni; Türkiye'den gözlem haberleri. Wikipedia kartı: "Kp indeksi", "Kutup ışığı".

**Boyut:** Gezegen (ya da Yuva 2050 — altyapı kırılganlığı).

**Maliyet:** Küçük-orta (üç JSON, iki grafik, oval haritası için enlem eşik tablosu; telsiz parazit sesi mevcut ses motoruyla).

**Tuzak:** (1) Kp gezegensel ve 3 saatliktir; "şu an Kapadokya'da" demek yanlış — "son 3 saatlik küresel değer". (2) "Tahmini Kp" ön değerdir, sonradan düzeltilir. (3) Sağlık etkisi iddiası yok (baş ağrısı vb. bilimsel değil). (4) Kutup ışığını "Güneş'ten gelen parçacıklar doğrudan çarpar" diye anlatmak eksik — manyetosferden hızlandırılan elektronlar; Motor bunu düzeltmeli. (5) Veri boşlukları (DSCOVR kesintileri) olur; eksik veri "sis" olarak gösterilmeli, interpolasyon yapılmamalı.

---

## 11. Motor'un Kavanozu — Bayes ile Güncelle (epistemik deney)

**Oyuncunun yaptığı:** Anlam boyutunun agorasında iki kavanoz: biri 70 kırmızı/30 mavi, diğeri tersi. Motor birini gizlice seçer. Oyuncu tek tek top çeker ve her çekimden sonra kaydırıcıyla "A kavanozu olma olasılığım" değerini söyler. Oyun oyuncunun eğrisini Bayes'in eğrisiyle üst üste çizer; sonunda Brier skoruyla kalibrasyonu gösterir. İkinci sahne: "nadir hastalık testi" — oyuncu önce yüzdeyle tahmin eder, sonra 1000 kişilik "doğal sıklık" tablosunu kendisi doldurur ve iki cevabı arasındaki uçurumu görür. Motor'un "bilmediğini uydurmaz" ilkesi burada bir mekaniğe dönüşür: oyuncu da "bilmiyorum = 0,5 değil, belirsizlik aralığı" demeyi öğrenir.

**Öğretilen kavram:** Bayes teoremi, önsel/sonsal, kanıtın birikmesi, insanın tipik "tutuculuk" (yetersiz güncelleme) ve taban oranı ihmali; doğal sıklıkların yüzdelerden daha iyi anlaşılması; kalibrasyon. Felsefi köprü: Spinoza'nın "yeterli fikir"i ve Sagan'ın "olağanüstü iddia olağanüstü kanıt ister"i (ikisi de oyunda var) için somut bir araç.

**Kaynak:** Bayes & Price 1763, *Phil. Trans.* 53:370; Edwards 1968, "Conservatism in human information processing"; Kahneman & Tversky 1973, "On the psychology of prediction", *Psychol. Rev.* 80:237; Gigerenzer & Hoffrage 1995, "How to improve Bayesian reasoning without instruction: frequency formats", *Psychol. Rev.* 102:684. Wikipedia kartı: "Bayes teoremi", "Taban oranı yanılgısı".

**Boyut:** Anlam.

**Maliyet:** Küçük (DOM; olasılık hesabı birkaç satır; 1000 kişilik ızgara canvas).

**Tuzak:** (1) "Bayes tek doğru düşünme biçimidir" vaazı — önseller özneldir, model yanlış olabilir; Motor bunu da söylemeli. (2) Tıbbi test örneğinde gerçek bir hastalık adı ve gerçek oranlar kullanılacaksa güncel kaynakla; aksi halde kurgusal "Sis humması" ile anlatmak daha güvenli. (3) Oyuncunun "yanlış" güncellemesini utandırmamak — "insan beyni böyle çalışır" diye normalleştirip aracı vermek. (4) Yüzde ile sıklık formatını aynı ekranda karıştırmamak (asıl pedagojik nokta bu).

---

## 12. 2050'nin Sıcaklığı — Kendi Şehrini Modelle (Open-Meteo Climate + Archive)

**Oyuncunun yaptığı:** Yuva boyutunun 2050 kısmında bir iklim terminali. Oyuncu kendi şehrini haritadan seçer (ya da konum izni verir). Terminal iki şey çeker: ERA5 arşivinden 1961-1990 gerçek ortalaması ve CMIP6 HighResMIP modellerinden 2050 yıllık ortalaması (birden çok model). Oyuncu "yıllık ortalama" yerine "yaz en yüksek sıcaklık" ya da ">35°C gün sayısı" göstergesini kendisi seçer, model sayısını açıp kapatarak *yayılımı* (spread) görür ve "bu bir tahmin mi, projeksiyon mu?" sorusuna doğru yanıtı bulur. Sonra oyuncu 2050 yaz gününü 3D sahnede "yaşar": gökyüzü/ısı dalgalanması efekti modelden gelen sayıyla ölçeklenir (abartısız).

**Öğretilen kavram:** Hava ile iklim farkı; anomali (taban dönemine göre fark) ile mutlak sıcaklık farkı; model topluluğu (ensemble) ve belirsizlik; senaryo bağımlılığı (gelecek "kaderin" değil "emisyonun" fonksiyonu); yerel ölçekte uç günlerin ortalamadan daha hızlı değişmesi.

**Kaynak:** Open-Meteo Climate API: `https://climate-api.open-meteo.com/v1/climate?latitude=38.6&longitude=34.8&start_date=1950-01-01&end_date=2050-12-31&models=EC_Earth3P_HR,MRI_AGCM3_2_S,MPI_ESM1_2_XR&daily=temperature_2m_max` (anahtarsız, CORS açık, ticari olmayan kullanım serbest); Open-Meteo Archive (ERA5): `https://archive-api.open-meteo.com/v1/archive?...&start_date=1961-01-01&end_date=1990-12-31&daily=temperature_2m_mean`. Model arka planı: Haarsma ve ark. 2016, "High Resolution Model Intercomparison Project (HighResMIP v1.0)", *Geosci. Model Dev.* 9:4185. Çerçeve: IPCC AR6 WG1 (2021) Karar Vericiler İçin Özet. Wikipedia kartı: "İklim modeli", "CMIP".

**Boyut:** Yuva (2050).

**Maliyet:** Orta (iki API, günlük veriyi yıllık özetleme, çoklu model grafiği; sahne efekti mevcut hava olayı sistemiyle).

**Tuzak (en kritik):** (1) Open-Meteo'daki HighResMIP modelleri **tek ve yüksek emisyon senaryosu** (SSP5-8.5 benzeri zorlama) içerir; oyun bunu "olası gelecekler yelpazesinin üst ucu" diye etiketlemezse yanlış öğretir. Düşük senaryo için gömülü IPCC AR6 bölgesel aralık tablosu eklenmeli. (2) 1950-2014 "geçmiş" bölümü de model çıktısıdır, gözlem değil — gözlem için ERA5 arşivi ayrı çekilmeli; oyuncuya ikisi farklı renkle gösterilmeli. (3) Tek yılın (2050) tek değerini okumak gürültülüdür; 2041-2060 ortalaması gösterilmeli. (4) 3D sahne efekti felaket estetiğine kaçmamalı — veri ölçekli, sakin.

---

## Öncelik önerisi ve bağımlılıklar

| # | Fikir | Canlı API | CORS | Maliyet | İlk sürüme? |
|---|---|---|---|---|---|
| 1 | Galileo eğik düzlem | yok | — | küçük | evet |
| 2 | Eratosthenes gölgesi | Sunrise-Sunset | açık | küçük-orta | evet |
| 3 | Sismograf (USGS) | USGS GeoJSON | açık | küçük-orta | evet |
| 4 | Yarı ömür zarları | yok | — | küçük | evet |
| 5 | ISS yakala | wheretheiss.at | açık | küçük | evet |
| 6 | Transit avı | Exoplanet TAP | doğrulanmalı | orta | 2. dalga |
| 7 | Bulut odası / müon | yok | — | orta | 2. dalga |
| 8 | Tepki süresi | yok | — | küçük | evet |
| 9 | Foucault sarkacı | yok | — | küçük | evet |
| 10 | Uzay havası (NOAA) | SWPC JSON | doğrulanmalı | küçük-orta | 2. dalga |
| 11 | Bayes kavanozu | yok | — | küçük | evet |
| 12 | 2050 iklim terminali | Open-Meteo ×2 | açık | orta | 2. dalga |

Boyut dağılımı: Tesis 2 (3, 9) · Başlangıç/Kuantum 1 (7) · Gezegen 3 (5, 6, 10) · Bilinç 1 (8) · Anlam 1 (11) · Yuva 4 (1, 2, 4, 12). Başlangıç boyutu görece zayıf kaldı; istenirse 7 numaralı bulut odası Başlangıç'a ("kozmik ışınların kaynağı: süpernova kalıntıları") kaydırılabilir.

Ortak başarım fikri: "Kendi Elimle Ölçtüm" — 12 deneyden en az 6'sında oyuncunun ölçümü gerçek değere %10 içinde yaklaşınca açılır; sonuç ekranı oyuncunun tüm ölçüm-sapma çiftlerini tek grafikte gösterir.
