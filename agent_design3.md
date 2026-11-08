# Varoluş Denklemi — İkinci Tur, Fotoğraf Modu, Harita Sekmesi, Küresel Son Panosu

Birimler önceki belgelerle aynı (yürüme 2.4, koşma 4.2). Veri kartı = dinlenmiş nokta/figür/kayıt; toplam 37 (baslangic 6, kuantum 7, gezegen 6, bilinc 6, anlam 6, yuva 6).

## 1. İkinci Tur (New Game+)

**Açılış:** Üç sondan herhangi biri görüldükten sonra son kartında "İkinci Tur" düğmesi. `S.ngp` 0→1 (3. ve sonraki turlar 1'de sabit kalır; değiştiriciler büyümez). Her tur yeni `S.runId`.

| Korunur | Sıfırlanır |
|---|---|
| `facts` (günlük/harita dolu kalır, gri "önceki tur" damgası) | `insight` (0; kapılar yeniden açılır) |
| `looks` (atkı, rozet, eldiven) | `frags` (6 parça yeniden) |
| `integMax` (3–5) ve `fuelBonus` (12/16 sn) | `quests` (T01–T07 yeniden; T03/T06 ödülü bütünlük yerine günlük sayfası, çünkü maks zaten korunmuş) |
| `endings[]` (görülen sonlar birikir), `rec7` | `path` sayaçları (gozlemci/kopru/sessizlik → 0) |

**6 değiştirici (tablo değerlerine uygulanır):**

| # | Alan | Tur 1 | Tur 2 |
|---|---|---|---|
| 1 | Saha yarıçapı R | 16–20 | +3 → 19–23 (sızıntı halkası R+4 sabit) |
| 2 | Avcı sayısı | 2–3 | +1 → 3–4 (eşzamanlı hamle aralığı 1.2 sn korunur) |
| 3 | Hamle hızı / telegraph | 10–14 / 0.9–0.55 sn | +2 → 12–16 / telegraph −0.1 sn (min 0.45) |
| 4 | Parça konumu | saha merkezi | merkezden 6–8 birim rastgele (seed = runId), ışık sütunu 1.5→1.0 birim |
| 5 | Gizli 7. parça | yok | **Tesiste**, Lale'nin odası (hub, Mira konsolu arkası). Koşul: 6 parça + 7 görev teslim + Tur 1'de Kayıt Yedi dinlenmiş. Açar: "Kayıt Sıfır" (Lale'nin ilk kaydı, 5 satır) |
| 6 | Yenilenme | saha dışı 6 sn, güvenli 3 sn | 8 sn / 4 sn; halüsinasyon sonrası hızlandırma korunur |

**Sonlar:** Üç son aynı kalır. Kayıt Sıfır dinlenmişse totem sorusuna 3. seçenek eklenir ("Defteri Lale'ye geri ver") ve seçilen sona 4 cümlelik epilog bağlanır; epilog `endings[]`'de tur 1'de görülen sona atıf yapar (ör. Gözlemci→Köprü: "Bir kez izledin; bu kez konuştun.").

**HUD:** Sağ üst "TUR II" rozeti (11 px, #f3c870, %70 opaklık); bütünlük halkaları altın kenarlı; parça sayacı "n/7" (7. dilim kilitliyken kesik çizgili). Saha girişi uyarısı "BOZULMA SAHASI · II".

## 2. Fotoğraf Modu (P)

- **Durma:** Oyun tamamen duraklar (dt=0, Bozulma telegraph/hamle dahil). Realm pad −6 dB sürer, event bus susar. HUD, diyalog ve altyazı gizlenir; Arel, arkadaş, Bozulma ve hava parçacıkları dondurulmuş görünür. **H** Arel'i gizler.
- **Kamera (yörünge):** Hedef Arel göğsü (y+1.4). Yaw sınırsız; pitch −20°…+75°; mesafe 1.5–14 birim (tekerlek/pinch, adım 0.5); kamera zemin+0.3'ün altına inmez. WASD/ok: hedefi 4 birim yarıçap içinde kaydırır. Mobil: tek parmak döndür, iki parmak zoom, çift dokun hedefi sıfırlar.
- **FOV:** Kaydırıcı 24–90, varsayılan 50, adım 1.
- **Filtreler (grade ön ayarı):** 1 **Motor** (boyutun kendi grade'i), 2 **Sis** (sat 0.3, con 1.15, grain 0.08, vig 0.75), 3 **Lale** (sat 1.1, sıcak tint #f3c870 %12, vig 0.5, grain 0.02). Sayı tuşları/düğme ile geçiş, 0.3 sn fade.
- **Letterbox:** L tuşu döngü: yok → 2.35:1 → 1:1 (kare). Bantlar #000, %100 opak.
- **Kayıt:** Enter/"Kaydet" → canvas 1920×1080 (mobilde ekran çözünürlüğü, maks 2× DPR), PNG. Dosya adı `varolus_{boyutId}_{YYYYMMDD-HHMMSS}_{filtre}.png` (ör. `varolus_kuantum_20261012-203015_sis.png`). `S.photos`++ (Harita sekmesinde sayaç).
- **Mobil düğme:** HUD sağ alt kamera ikonu 44×44 px; mod içinde alt şerit: filtre · FOV · letterbox · kaydet · çık.
- **Çıkış:** P veya Esc; kamera 0.4 sn'de döner, 1 sn dokunulmazlık (saha içindeyse). Halüsinasyon ve yakalanma sırasında açılmaz.

## 3. Günlük "Harita" Sekmesi

Hepsi inline SVG, `viewBox="0 0 360 H"`, `width="100%"`, tek sütun, 12 px boşluk; etiket 11 px, metin #e8e4ff, eksen #4a4a6e, boş durum metni ortada 12 px italik. Boyut renkleri: baslangic #ff9152, kuantum #7fd6ff, gezegen #93e3a0, bilinc #ff7cb9, anlam #c9abff, yuva #6f9dff.

| # | Grafik | Kaynak | Tür / Boyut | Renk kuralı | Boş durum |
|---|---|---|---|---|---|
| 1 | Boyut başına veri kartı | `S.facts` (id → boyut) | 6 yatay çubuk, 360×180, çubuk 20 px | dolu kısım boyut hex'i, kalan #2a2850; sağda "n/6" | "Henüz kart yok. Bir yankı noktasında E'ye bas." |
| 2 | Yol üçgeni | `S.path` {gozlemci,kopru,sessizlik} sayaçları | ternary, 360×300; nokta = barisentrik ağırlık merkezi, r=6 | köşeler: Gözlemci #7fd6ff, Köprü #93e3a0, Sessizlik #c9abff; nokta en ağır köşe rengi | "Yol henüz çizilmedi. Tesiste biriyle konuş." |
| 3 | Bütünlük–zaman | `S.timeline` (5 sn'de bir {t, integ, zone}; son 10 dk, 120 örnek) | çizgi, 360×120 | çizgi o anki boyut hex'i; saha içi aralıklar #E63946 %20 arka plan; `integMax` kesik yatay çizgi | "Sayaç henüz sınanmadı." |
| 4 | Parça halkası | `S.frags` (6, NG+'da 7) | donut çap 160, kalınlık 18 | dilim = parçanın boyut hex'i; boş #2a2850; 7. dilim #f3c870 kesikli; merkez "n/6" | "Kesik parça yok. Karanlık küreleri ara." |
| 5 | Olay ufku süresi | `S.weatherLog` [{dim, kind, dur}] | yığılmış yatay çubuk (boyut başına toplam sn, 0–90), 360×180 | boyut hex'i %60 opak; olay adı çubuk içinde | "Hava hâlâ sakin." |

Sekme altı: "Fotoğraf: n · Tur: I/II". Tooltip yok; tüm değerler sabit etiket (dokunmatik uyumlu).

## 4. Küresel Son İstatistiği Panosu

**Depo:** Tek paylaşılan belge `stats` {gozlemci, kopru, sessizlik, total, cardsSum, rec7Count, updatedAt}; ayrıca `runs/{runId}` (30 gün saklanır).

**Yazma (bir kez):** Son kartı açıldığı anda, `S.reported=false` ise: `{runId, ending, cards(0–37), rec7(0/1), ngp, playSec}` gönderilir; başarılıysa `S.reported=true` ve `localStorage.vd_reported[runId]=1`. Sunucu: `runId` zaten varsa 409 → istemci sessizce yoksayar. Her tur yeni runId → NG+ ayrı oyun sayılır (istenen davranış).

**Gösterim:** Son kartı altında 3 yüzde çubuğu (220×8 px; Gözlemci #7fd6ff, Köprü #93e3a0, Sessizlik #c9abff), kendi sonun kalın. Altında: "Ortalama veri kartı 24/37" (cardsSum/total) · "Kayıt Yedi'yi dinleyenler %38". 2 sn içinde gelmezse önbellekteki değer, "~" ile.

**Veri yoksa:** fetch hatası veya `total<10` → çubuk yerine "Sayaçlar henüz sessiz — ilk tanıklardan birisin." (`total` 1–9 ise "n kişi" yazılır, yüzde gösterilmez.)

**Kötüye kullanım / çift sayım:** runId tek kullanım (sunucu reddeder); `playSec ≥ 600` ve `cards ≤ 37` şema doğrulaması, `ending` enum; IP başına 5 yazma/saat; yalnızca sayaç artışı (okuma herkese, silme yok). Pano "yaklaşık" etiketli; kişisel veri yok.
