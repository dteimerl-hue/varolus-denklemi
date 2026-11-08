# Varoluş Denklemi — Yol Arkadaşı, Tanık Görevleri, Mini Oyunlar, Atmosfer

Birimler: yürüme 2.4, koşma 4.2 birim/sn. Mira tesiste kalır (geçit/telsiz); altı boyuta altı kişi.

## 1. Yol Arkadaşı Sistemi

| Boyut | Kişi | Neden |
|---|---|---|
| baslangic | kaan | Gün doğumu sayan astronot ilk ışığı görmeli |
| kuantum | deniz | Determinizm kaygısı; "it from bit" onun sınav sorusu |
| gezegen | riza | Soluk Mavi Nokta → Haliç imzası |
| bilinc | zeynep | Son nefes sorusu; nöron/DMN onun servisinin fiziği |
| anlam | sema | Uçan Adam'ı Lale'den dinledi; "Çekirdek" sözünü taşıyor |
| yuva | hatice | Toprak/ceviz; torunu Yusuf bu boyutun figürü |

**Hareket:** hedef mesafe 3.5, durma 2.5, oyuncunun 30° arkasında-sağında. Yürüme 2.4. Mesafe > 7 olunca koşar (4.6, yetişir). Mesafe > 22 ya da görüş dışıysa kamera arkasına ışınlanır (0.3 sn soluklaşma). Oyuncu 6 sn kesintisiz koşarsa arkadaş koşuyu bırakır, 1 replik söyler, ışınlanma kuralıyla yetişir; kovalama hissi oluşmaz.

**Diyalogda:** arkadaş oyuncudan 2.0 birim yanda, konuşana 35° dönük durur; dinleme animasyonu.

**Bozulma Sahası:** R+6 halkasında durur ve uyarır; R+4 sızıntı halkasını asla geçmez; oyuncu çıkınca 2 sn sonra takip sürer. Oyuncu yakalanınca (bütünlük 0) arkadaş spawn noktasında bekler.

**Halüsinasyonda:** HAL kopyası zaten o kişiyi içeriyor; gerçek arkadaş donar, silüeti 0.6 sn gri-gürültüye döner, kopya konuşur. Bitince gerçek arkadaş 1 replik; oyuncuya 2.5 sn fener yakıtı iade edilir.

**Replik tetikleyicileri (kişi başı 13, senarist yazar):**

| Tetik | Adet |
|---|---|
| Varış (geçit çıkışı +2 sn) | 1 |
| İlk yankı noktası dinlendi | 1 |
| Figürle konuşma sonrası (figür başı 1) | 2 |
| Saha kenarı uyarısı (R+6; ikinci girişte farklı metin) | 2 |
| Parça alındı (ZT.fragment sonrası, sahadan çıkınca) | 1 |
| Yakalandıktan sonra | 1 |
| Halüsinasyon sonrası | 1 |
| 6 sn koşma | 1 |
| Atmosfer olayı başlangıcı | 1 |
| Boşta (45–70 sn aralıkla, sırayla) | 2 |
| Çıkış geçidi (geçide 6 birim) | 1 |

## 2. Tanık Görevleri

Görev tesiste alınır; hedef nokta/figür dinlenince "cevap bulundu" damgası; verene teslim → ödül + 1 tepki repliği. Hedef boyut, kişinin eşlik ettiği boyuttan farklıdır.

| ID | Açılış (içgörü) | Veren | Soru (özet) | Hedef | Ödül |
|---|---|---|---|---|---|
| T01 | 0 | riza | "Bir ömür iz bırakmadan silinir mi?" | yuva / zirkon | Günlük sayfası |
| T02 | 0 | deniz | "Belirlenmiş olmak anlamsız mı?" | anlam / spinoza | Fener yakıtı deposu +4 sn (12→16) |
| T03 | 1 | zeynep | "Son nefeste giden şey nereye gider?" | kuantum / lattice | Bütünlük maks +1 (3→4) |
| T04 | 2 | hatice | "Emeğin değeri kalır mı?" | baslangic / cmb | Aksesuar: yün atkı (Hatice ördü) |
| T05 | 3 | kaan | "Neden hâlâ gün doğumu sayıyorum?" | yuva / elif | Aksesuar: ISS ekspedisyon rozeti |
| T06 | 4 | sema | "'Çekirdek'e varınca' ne demekti?" | bilinc / nil | Bütünlük maks +1 (4→5) |
| T07 | 5 | mira | "Motor unutuyor mu, saklıyor mu?" | gezegen / cheyava | Aksesuar: Mira'nın iş eldiveni + günlük sayfası |

HUD: görev alınınca haritada soru işareti; teslimde kişinin üzerinde ünlem. Aksesuarlar Arel'in `look` nesnesine yazılır (scarf/badge/gloves alanları mevcut).

## 3. İki Yeni Mini Oyun

Ortak: tek ekran, 10–20 sn, kalibrasyon paneliyle aynı çerçeve; sonuç 1.5 sn animasyon.

### 3a. Bilinç — "Eşik" (tetik: bilinc / `neuron` noktası, ikinci cümle dinlendikten sonra panel açılır)

- **UI:** üç sinaps ağırlığı kaydırıcısı w1,w2,w3 ∈ [0, 12] mV; zamanlama kaydırıcısı Δt ∈ [0, 20] ms (ardışık sinapslar arası gecikme); sağda zar potansiyeli izi (−70 çizgisi, −55 eşik çizgisi kesikli, −45 kırmızı bant).
- **Formül:** τ = 10 ms. V_tepe = −70 + w1 + w2·e^(−Δt/τ) + w3·e^(−2Δt/τ).
- **Kazanma:** −55 ≤ V_tepe ≤ −45 → aksiyon potansiyeli animasyonu (+30 mV'a fırlar, 1 ms).
- **Hata mesajları:** (1) V_tepe < −55: "Eşik altı: hece çıkmadı." (2) V_tepe > −45: "Aşırı uyarım: depolarizasyon bloğu." (3) Δt > 15 ve w1+w2+w3 ≥ 15 ama V_tepe < −55: "Zamanlama: sinyaller birbirini beklemedi."
- **Deneme:** sınırsız; 3 başarısızdan sonra ipucu ("5 ms'de ikinci sinyalin %61'i kalır").
- **Ödül:** fener deposu +3 sn (kalıcı), anında tam dolum; Zeynep repliği 1.

### 3b. Gezegen — "Yörünge" (tetik: gezegen / `enceladus` noktası; Ayşe'yle konuşulmuşsa panelde "Clipper JOI" konsolu açılır)

- **UI:** Δv kaydırıcısı [0, 1.5] km/s (yakıt sınırı 1.0, üstü kırmızı); açı θ ∈ [0°, 60°]; Jüpiter diski, 1.0–1.4 RJ yeşil halka; "YAK" ile 8 sn yörünge çizimi.
- **Model (iki cisim):** μ = 1.267×10⁸ km³/s², RJ = 71.492 km, v∞ = 5.6 km/s. r_p = (0.6 + 0.02·θ) RJ. v_p = √(v∞² + 2μ/r_p); yakma sonrası v' = v_p − Δv. e = r_p·v'²/μ − 1.
- **Kazanma:** 1.0 ≤ r_p/RJ ≤ 1.4 ve e < 1 ve Δv ≤ 1.0. (Örnek: θ = 30° → r_p = 1.2 RJ, kaçış hızı 54.35 km/s, v_p = 54.64 → Δv ≥ 0.29 yeterli.)
- **Hata mesajları:** (1) r_p < 1.0: "Perijüpiter çok alçak: Clipper kayboldu." (2) r_p > 1.4: "Pencere kaçtı: uzaktan geçtin." (3) e ≥ 1 veya Δv > 1.0: "Yakalanmadı: hiperbolik" / "Yakıt bitti."
- **Deneme:** 3 hak; tükenince Ayşe ipucu verir, 60 sn sonra yenilenir.
- **Ödül:** bütünlük maks +1 (kalıcı) ve sahadaki kesik parçanın yeri haritada işaretlenir; Rıza repliği 1.

## 4. Atmosfer Olayları

Aralık 90–150 sn, süre 20–30 sn, 3 sn geçiş; olay başında 1 arkadaş repliği. Sis 0–1 (fog.n/f çarpanı), ışık (sunI×), parçacık sayısı.

| Boyut | Olay | Sis | Işık | Parçacık | Koşma | Bozulma |
|---|---|---|---|---|---|---|
| baslangic | Foton fırtınası | 0.75 | 1.6 (beyaz-turuncu patlama) | 900 ışık benekleri | 4.2→3.6 | Saha aktif; görüş 14 birime iner |
| kuantum | Çökme dalgası | 0.3 | 0.8, 2 Hz titreşim | 400 kırık çizgi | Değişmez; zemin 0.15 birim titrer | Bozulmalar 0.4 sn görünmez (her 4 sn), telegraph görünür kalır |
| gezegen | Toz fırtınası | 0.85 | 0.55 (kızıl) | 1500 toz | 4.2→3.4 | Saha aktif; sızıntı halkası R+4→R+6 |
| bilinc | Nöbet | 0.4 | 1.3, 1.2 Hz kırmızı nabız | 700 nöron kıvılcımı, hızı ×2 | 4.2→4.6 (adrenalin) | Av hızı 3.0→3.4, bekleme 1.8→1.4 sn |
| anlam | Gölge tutulması | 0.5 | 0.35 (gün ışığı söner, rim ×2) | 200 kül | Değişmez | Pasif Bozulmalar oyuncuya döner, hareket etmez |
| yuva | Meteor + aurora | 0.2 | 0.9, aurora yeşil-mor 0.5 Hz dalga | 60 meteor izi + 300 aurora şeridi | 4.2→4.4 | Saha pasifleşir; parça alma için fırsat penceresi |

HUD'da olay ikonu; boyut başına en fazla 3 olay; parça alındıktan sonra sıklık yarıya iner.
