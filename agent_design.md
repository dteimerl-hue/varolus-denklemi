# Varoluş Denklemi — Bozulma Sahası Tasarımı

Temel ilke: Ada genelinde Bozulma **pasif** (izler, titrer, 0 hız). Tehdit yalnızca **Bozulma Sahası** içinde ve sahadan sızan 4 birimlik "sızıntı" halkasında aktiftir. Tüm sayılar birim/saniye (oyuncu yürüme 2.4, koşma 4.2).

## 1. Saha İçi Davranış

- **Yerleşim:** Her adada 1 saha, merkez noktalardan en az 22 birim uzakta. Yarıçap R (bkz. tablo, 16–20). Saha karanlık küre + zemin çatlak dokusu.
- **Bozulma sayısı:** Sahada 2–3 (tablo). Saha dışındaki pasif Bozulmalar sahaya girmez, sadece oyuncuya dönük titrer.
- **Aktivasyon:** Oyuncu merkezden R içine girince **0.6 sn** sonra tüm saha Bozulmaları "Av" durumuna geçer. Çıkışta (R+4 "sızıntı" halkası dışında) **2 sn** sonra geri çekilme.
- **Av hızı:** Yürüyen oyuncuya karşı **3.0** (çarpan 1.25×yürüme), koşana yetişemez (koşma 4.2). Sürekli zorlama hamle ile yapılır.
- **Hamle (lunge):**
  - Menzil: oyuncu ≤ **5 birim** içindeyken tetiklenir.
  - Telegraph: **0.7 sn** — figür büzülür, kırmızı çizgiler sabitlenir, tiz "çatlak" sesi.
  - Hamle: **12 birim/sn**, **0.45 sn** (≈5.4 birim yol, düz çizgi, hedef telegraph başındaki konum + 0.3 sn tahmin).
  - Bekleme: hamle sonrası **1.8 sn** hareketsiz; bu pencere kaçış/püskürtme fırsatıdır.
  - Vuruş yarıçapı: oyuncudan **1.2 birim**.
- **Vuruş sonucu:** Bütünlük −1 segment, oyuncu geriye **2 birim** itilir, **0.4 sn** kontrol kilidi, **1.5 sn dokunulmazlık** (tüm Bozulmalardan). Bozulmalar aynı anda hamle yapamaz: aralarında en az **1.2 sn** fark.

## 2. Bütünlük Sayacı

- **3 segment**, HUD sol-alt, mavi-beyaz üç halka.
- Vuruş başına **−1**.
- **Yenilenme:** Saha dışında **6 sn/segment**; güvenli bölge (7 birim nokta/insan halkası) içinde **3 sn/segment**. Saha içinde yenilenme yok.
- **0 olunca:** "Yakalandı" → 1.2 sn animasyon → oyuncu adanın başlangıç noktasına döner. Toplanan parçalar korunur; saha Bozulmaları sıfırlanır.
- **Halüsinasyon tetiği:** Bütünlük **1**'e düşünce (her saha girişinde en fazla 1 kez).

## 3. Oyuncu Karşı Araçları

- **Sis Feneri (F):** Koni 45°, menzil **10 birim**. Koni içinde kalan Bozulma **0.5 sn** sonra püskürtülür: 8 birim geri çekilir, telegraph iptal olur, **3 sn** pasif. Yakıt: tam depo **12 sn**, saniyede 1 birim yanar; yenilenme yalnızca güvenli bölgede 2 birim/sn. Saha başına ideal kullanım 2–3 kısa (1–1.5 sn) basış.
- **Koşarak kaçma:** Koşma (4.2) Av hızını (3.0) aşar; tek risk hamle menzilinde kalmaktır. Hamleden kaçış: hamle başladıktan sonra 0.2 sn içinde yanal 90° dönüş → hamle ıskalar (düz çizgi).
- **Geri çekilme kuralı:** Oyuncu R+4 dışına çıkınca 2 sn sonra Bozulmalar **4 birim/sn** ile saha merkezine döner, kovalamaz. Sızıntı halkasında (R ile R+4 arası) hamle yapabilir, Av hızı yarıya düşer (1.5).
- **Safe ring:** Saha içinde **geçerli değil**. Saha sınırı güvenli bölgelerle kesişemez (yerleşim kuralı). Saha dışı noktalar normal davranır.

## 4. Parça Toplama

- Parça saha merkezinde, 1.5 birim yarıçaplı ışık sütunu.
- **Etkileşim:** E tuşu **2 sn basılı tutma**, hareket serbest değil (durur), kesilirse ilerleme sıfırlanır. Vuruş alınca kesilir.
- **Öfke dalgası:** Parça alınınca **4 sn** boyunca tüm saha Bozulmaları: Av hızı **4.0**, telegraph **0.5 sn**, bekleme **1.2 sn**. Sonra normal. Saha artık "boşalmış": karanlık %50 azalır, Bozulmalar pasife döner ve o adada bir daha aktive olmaz.
- **Ödül:** Her ada 1 parça; **6 parça** → Çekirdek'te "Kayıt Yedi" açılır (Lale'nin son kaydı). 3 parça → Sis Feneri deposu 12→16 sn (ara ödül).

## 5. Zorluk Eğrisi

| Boyut (içgörü) | Saha R | Bozulma | Av hızı | Hamle hızı | Telegraph | Bekleme |
|---|---|---|---|---|---|---|
| 1 (0) | 16 | 2 | 2.6 | 10 | 0.9 | 2.2 |
| 2 (1) | 17 | 2 | 2.8 | 11 | 0.8 | 2.0 |
| 3 (2) | 18 | 2 | 3.0 | 12 | 0.7 | 1.8 |
| 4 (3) | 18 | 3 | 3.0 | 12 | 0.7 | 1.8 |
| 5 (4) | 19 | 3 | 3.2 | 13 | 0.6 | 1.6 |
| 6 (5) | 20 | 3 | 3.4 | 14 | 0.55 | 1.5 |

Av hızı her zaman koşma (4.2) altında kalır; 6. boyutta yürüme ile kaçış imkânsızdır.

## 6. Geri Bildirim

- **Sahaya giriş:** HUD ortası-üst, 2 sn: "BOZULMA SAHASI — bütünlük düşüyor" (renk #E63946 üzerine siyah gölge, 0.3 sn titreme). Bütünlük sayacı ortaya kayar, kırmızıya döner.
- **Ses:** Saha içi kalp atışı 70 bpm, bütünlük 2'de 100 bpm, 1'de 130 bpm + düşük frekanslı uğultu. Telegraph: tiz cam çatlağı (0.7 sn). Hamle: hava kesme "whoosh". Püskürtme: boğuk çığlık.
- **Ekran kenarı:** Bütünlük 3→2: kenarlarda %15 kırmızı-siyah damar vinyeti; 1: %35 + 0.5 sn aralıkla chromatic aberration nabzı. Hamle vuruşu: 0.2 sn beyaz-kırmızı flaş + 0.3 sn kamera sarsıntısı (genlik 0.4).
- **Yakalanma animasyonu:** **1.2 sn** — figürler oyuncuyu sarar, ekran siyaha çatlar; 0.4 sn siyah; başlangıçta yeniden doğuş (bütünlük 3).

## 7. Halüsinasyon Sahnesi

- **Süre:** 9 sn (son 1.5 sn solma).
- **Kontrol:** Kilit yok; yürüme/koşma serbest, Sis Feneri **devre dışı** (F basınca cızırtı). Gerçek Bozulmalar bu sürede **duraklar** (hamle yok), böylece sahne cezaya dönüşmez.
- **Kopyalar:** Oyuncunun 4 çarpık kopyası (siyah silüet, kırmızı gözler, 1.3× boy) 10 birim uzakta belirir, **2.0** hızla yaklaşır, 2 birimde durur ve titreyerek izler; **dokunmaz**, hasar vermez. Oyuncu içinden geçebilir.
- **Ekran:** Gri-kırmızı ters renk, 0.3 sn'de bir kare kayması, Lale'nin ses kaydından ters çalınan 2 sn'lik cümleler.
- **Çıkış:** 9 sn dolunca veya oyuncu sahadan çıkınca (R+4) anında biter; kopyalar 0.5 sn'de dağılır, Sis Feneri geri gelir, gerçek Bozulmalar 1 sn sonra tekrar aktif. Halüsinasyon sonrası bütünlük yenilenmesi 3 sn hızlandırılır (saha dışı 6→3 sn ilk segment için).
