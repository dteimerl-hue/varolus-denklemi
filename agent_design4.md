# Varoluş Denklemi — Başarımlar, Sis Fırtınası, Öğretici, Eş-varlık

Birimler önceki belgelerle aynı (yürüme 2.4, koşma 4.2). Yeni alanlar: `S.ach{id:ts}`, `S.storm{tries,done}`, `S.tut{step,skipped}`, `S.ghostId`.

## 1. Başarımlar (20)

| id | Ad | Koşul (S alanı, eşik) | Gizli | Kategori | İkon |
|---|---|---|---|---|---|
| first_card | İlk Kart | `facts.length ≥ 1` | hayır | keşif | note |
| six_gates | Altı Kapı | `hist` içinde 6 farklı boyut varışı | hayır | keşif | star |
| full_archive | Tam Arşiv | `facts.length ≥ 37` | hayır | keşif | eye |
| seven_records | Yedi Kayıt | `logs.length ≥ 6 && rec7` | hayır | keşif | spiral |
| three_frames | Üç Kare | `shots ≥ 3` | hayır | keşif | eye |
| six_skies | Altı Gök | `wxLog` içinde 6 farklı `dim` | **evet** | keşif | drop |
| first_cut | İlk Kesik | `frags.length ≥ 1` | hayır | hayatta kalma | shield |
| six_cuts | Altı Parça | `frags.length ≥ 6` | hayır | hayatta kalma | shield |
| untouched | Dokunulmadan | parça alındı, o sahada vuruş 0 (`hist` saha kaydı `hit:0`) | **evet** | hayatta kalma | fire |
| storm_first | Sis Fırtınası | `storm.done && storm.tries == 1` | hayır | hayatta kalma | fire |
| five_rings | Beş Halka | `integMax ≥ 5` | hayır | hayatta kalma | shield |
| two_trials | İki Deney | `mini.esik && mini.yorunge` | hayır | bilim | atom |
| clean_threshold | Temiz Eşik | `mini.esik.fail == 0` | **evet** | bilim | atom |
| clipper_joi | Clipper JOI | `mini.yorunge.joi == true` | hayır | bilim | atom |
| seven_witness | Yedi Tanık | 7 `quests` teslim | hayır | hikâye | note |
| three_endings | Üç Son | `endings.length == 3` | hayır | hikâye | star |
| one_path | Tek Yol | `path` tek köşe ≥ 6, diğer ikisi 0 | **evet** | hikâye | spiral |
| round_two | Tur II | `ngp == 1` | hayır | ikinci tur | clock |
| record_zero | Kayıt Sıfır | `rec0` | **evet** | ikinci tur | leaf |
| second_breath | İkinci Nefes | NG+ sonu, tur `playT ≤ 2400` sn | **evet** | ikinci tur | clock |

Kontrol: `checkAch()` her `save()` sonrası ve 2 sn'de bir. **Toast:** sağ üst, 260×56 px, 3.2 sn, 0.3 sn fade; 24 px SVG ikon (kategori rengi) + ad. Ses: sine E5→B5, 0.25 sn, −14 dB; gizlide üçüncü nota E6. Aynı anda tek toast, ardışıklar 0.6 sn arayla; diyalog/foto modunda bekler. **Günlük "Başarımlar" sekmesi:** üstte "n/20"; 5 kategori halkası (donut 48 px, kalınlık 6; keşif #7fd6ff, hayatta kalma #E63946, bilim #93e3a0, hikâye #c9abff, ikinci tur #f3c870, içinde "k/m"). Kazanılan: dolu ikon + tarih; kazanılmamış %30 opak; gizli kazanılmamış: kilit + "???". Mobil 2 sütun.

## 2. Çekirdek set-piece "Sis Fırtınası"

**Tetik:** `coreHal` son satırı kapanıp 1.5 sn solma bitince. Oyuncu halüsinasyon bitiş konumunda (merkezden ~30 br); Lale merkezden 6 br'de, üstünde 3 br yarıçaplı altın ışık sütunu. Yol arkadaşı yok; Sis Feneri aktif, depo tam, yenilenme yok; koşma serbest.

- **Süre:** 45 sn (yol ~24–36 br: koşarak 8 sn, yürüyerek 15 sn; baskı sis + avcıdan gelir).
- **Avcılar:** 5; merkez etrafında r=24 halkasında 72° aralıkla, ilk avcı oyuncu→Lale doğrultusundan 36° kaydırılmış (hiçbiri yolda doğmaz). Av hızı 3.6, hamle 14 br/sn (0.45 sn), telegraph 0.6 sn, bekleme 1.5 sn, eşzamanlı hamle aralığı 1.0 sn. Lale'nin 3 br halkasına giremezler; fener püskürtmesi geçerli.
- **Sis:** `f(t)=smoothstep(0,30,t)` → 0→1 **30 sn**, 15 sn tavanda; f=1'de görüş 9 br (fog çarpanı 0.25).
- **Işık:** çarpan 1.0→0.35 lineer 30 sn; Lale'nin sütunu etkilenmez (tek referans).
- **Sarsıntı:** t≥10 sn sürekli genlik 0.08 (4 Hz), f ile 0.15'e; vuruşta +0.4, 0.3 sn.
- **HUD:** üst-orta "SİS · 00:45" mono 22 px #f3c870, altında 220×4 px sis çubuğu. Son 10 sn: #E63946, saniyede 0.1 sn titreme. Bütünlük sayacı ortada, kırmızı.
- **Başarısızlık:** bütünlük 0 **veya** süre doldu → 1.2 sn yakalanma, 0.4 sn siyah; başlangıç konumu, süre/sis sıfır, bütünlük tam, avcılar halkaya; `storm.tries++`. **Kolaylaştırma (sessiz):** 3. denemeden süre 60 sn, avcı 4, sis tavanı 0.8; 5. denemeden Lale'nin sütunu 8 br, nav oku Lale'yi gösterir, telegraph 0.8 sn.
- **Bitiş:** Lale'ye ≤3 br → avcılar 0.5 sn'de dağılır, sis 2 sn'de 0.3'e, ışık 1.0'a; `storm.done=true`; `finale` başlar.
- **Müzik:** core `pad` −6 dB; `noise` f ile 0→−8 dB; `bass` 60→72 bpm (0→30 sn); kalp 70/100/130 bpm bütünlükle; son 10 sn `arp` susar. Bitişte pad 0 dB + tek nota A3 (4 sn, reverb wet 0.6).

**İkinci Tur:** süre 40 sn, avcı 6 (60°), hamle 16, telegraph 0.5, sis 25 sn'de tavana, kolaylaştırma 4. denemeden; HUD "SİS · II".

## 3. Öğretici (ilk 3 dakika)

Metin alt-orta, 13 px, 0.3 sn fade; her adımda sağ altta "Atla (Esc)". Tetik sağlanınca 0.8 sn sonra kapanır; zaman aşımında adım bitmiş sayılır. Art arda 2 "Atla" → tüm rehber kapanır (`tut.skipped=true`). Oynanış yarıda kesilmez.

| # | Tetik | Metin (≤70) | Zaman aşımı |
|---|---|---|---|
| 1 | 4 br yürüdü | WASD ile yürü. Sis seni bekler; acele etme. | 20 sn |
| 2 | Shift 1.5 sn basılı | Shift: koş. Nefesin değil, sabrın biter. | 25 sn |
| 3 | kamera 60° döndü | Fareyle bak. Çoğu şey arkanda durur. | 15 sn |
| 4 | Mira ile konuştu | E: Mira'yla konuş. Geçit onun elinde. | 60 sn |
| 5 | günlük açıldı (J) | J: günlük. Dinlediğin her şey buraya yazılır. | 40 sn |
| 6 | geçit paneline girdi | Geçide yaklaş, E. İlk kapı: Başlangıç. | 90 sn |
| 7 | bir boyuta vardı | Işık sütunları yankı noktası. Yaklaş, dinle. | 60 sn |
| 8 | ilk noktayı dinledi | Bir kart düştü. Kaynağı günlükte; küreden uzak dur. | 45 sn |

Adım 4 ve 6'da nav oku hedefe döner. Bütçe: 1–6 tesiste ~100 sn, 7–8 ilk boyutta ~60 sn. NG+'da açılmaz. **Mobil:** tuş yerine düğme adı ("Sol çubukla yürü", "Koş düğmesi", "Sağ yarıyı kaydır", "E düğmesi"); 2. tetik koş düğmesi 1.5 sn, 3. tetik sağ yarıda 60° kaydırma; metin joystick üstünde (alt 120 px), 14 px; "Atla" 44×44 px; adım 8'e "F: Sis Feneri" satırı (QA H12).

## 4. Eş-varlık (room)

- **Görsel:** Arel mesh'i tek renk, opaklık 0.35, gölge/ayak izi/isim yok. Renk: `ghostId` hash → 6 boyut renginden biri; Tur II oyuncusu altın #f3c870. Animasyon hızdan türetilir. Oyuncuya ≤2 br yaklaşınca opaklık 0.1. Collider ve E etkileşimi yok.
- **Güncelleme:** istemci **250 ms**'de bir `{x,z,yaw,v,ngp}` yayınlar (sabitken 2 sn'de bir); alıcı 250 ms lineer enterpolasyon; 1.5 sn paket yoksa solar, 5 sn'de silinir.
- **Mesafe filtresi:** ≤30 br tam; 30–40 br 1 sn'de solar; >40 çizilmez. **Maks 6** hayalet (en yakın 6).
- **Boyutlarda görünmeme:** yalnızca `cur==='hub'`; geçit kalibrasyonu, boyutlar, Çekirdek, intro ve finale'de asla. Diyalog ve fotoğraf modunda gizlenir.
- **Yanlış kullanım:** sunucu konumu tesis yarıçapı 42 içine kırpar; paketler arası hız >6 br/sn → düşer; oturum başına rastgele `ghostId`, kişisel veri ve metin kanalı yok; 5 dk hareketsiz → silinir; oda 24 kişi (fazlası yalnız izler); IP başına 1 yayıncı. Ayar: "Hayaletleri gizle". Bağlantı yoksa sistem sessizce kapalı, HUD uyarısı yok.
