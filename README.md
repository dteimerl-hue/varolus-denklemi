# Varoluş Denklemi

Tek dosyalık, tarayıcıda çalışan Türkçe 3B keşif oyunu (Three.js). Kapadokya'nın altındaki Kovuk Tesisi'nde fizikçi Dr. Arel Vey, dürüst yapay zekâ Motor ile birlikte altı boyutu gezer; bilmediği yerde uydurmayan bir makine, kaybedilen bir kardeşin ses kayıtları ve Bakanlık'ın baskısı arasında anlam arar.

- **Oyna (tarayıcıda):** `varolus-denklemi.html` dosyasını açın ya da GitHub Pages bağlantısını kullanın (depo ayarlarında Pages açıldığında `https://<kullanıcı>.github.io/varolus-denklemi/`).
- **Çevrimdışı paket:** Releases bölümündeki `Varolus-Denklemi-Paket.zip` — her şey (Three.js, görseller, yazı tipleri) tek HTML içinde gömülüdür, internet gerekmez. `OKU-BENI.txt` içinde kurulum ve kontroller yazar.

## İçerik (kısa)

Altı boyut (Başlangıç, Kuantum, Gezegen, Bilinç, Anlam, Yuva) + Çekirdek + gizli Bellek Sarayı; yedi mürettebat ve bir Bakanlık müfettişi; Lale'nin kayıtları; Bozulma düşmanları ve Sis Feneri; on bir mini deney (Eşik, Yörünge, Yankı Dizisi, Yarı Ömür, Galileo, Bayes, Helmholtz, Foucault, Bulut Odası, Sismograf, ISS); Tahmin Defteri, Bakanlık Raporu, Kayıt Dokuz, Yemekhane Gecesi, Yankı Taşları, Günün Tohumu, Hız Koşusu, Misafir modu, Arel'in Dosyası; dört son. Ayrıntılı envanter: `ozellikler.md`.

## Dosya yapısı

| Dosya | Ne |
|---|---|
| `w_head.html` | HTML iskeleti ve tüm CSS |
| `w_world.js` | 3B motor (Three.js r128): dünya, karakterler, ışık, efektler; `GFX` nesnesini dışa verir |
| `w_data.html` | Oyun verisi `GAME` (boyutlar, metinler, kişiler) ve senaryo paketleri `GAME.storyN` |
| `w_app.html` | Oyun mantığı: durum `S`, diyaloglar, mini oyunlar, günlük, sistemler |
| `build.py` | Dört parçayı `varolus-denklemi.html` olarak birleştirir, Node ile sözdizimi denetler, `test.html` üretir |
| `pack.py` | CDN scriptlerini, görselleri ve yazı tiplerini gömerek `paket/` ve zip üretir |
| `assets/` | Görseller (webp), karakter rig'i |
| `agent_story*.json`, `agent_*.md` | Senaryo ve tasarım metinleri (JSON'lar `w_data.html` içine enjekte edilmiştir) |
| `fikir_*.md` | Fikir havuzu (tasarım, anlatı, bilim, oyuncu) — henüz eklenmemiş fikirler buradan seçilir |

## Geliştirme

Gereksinimler: Python 3, Node.js (yalnız sözdizimi denetimi için), herhangi bir yerel HTTP sunucusu.

```bash
python build.py            # varolus-denklemi.html + test.html üretir
python -m http.server 8765 # http://localhost:8765/varolus-denklemi.html
python pack.py             # çevrimdışı paket: paket/ ve Varolus-Denklemi-Paket.zip (internet ister: CDN ve yazı tipleri indirilir)
```

Kural: oyun dört `w_*` parçasında geliştirilir; `varolus-denklemi.html` türetilmiş dosyadır, elle düzenlenmez, her değişiklikten sonra `build.py` ile yeniden üretilip birlikte commit edilir.

### Birlikte çalışma akışı

1. `main` korunur; her iş için dal açın: `git checkout -b ozellik/kisa-ad`.
2. Değişikliği yapın, `python build.py` çalıştırın, oyunu tarayıcıda deneyin (konsolda hata olmamalı).
3. Commit + push, GitHub'da Pull Request açın; diğer kişi gözden geçirip birleştirir.
4. Metin eklerken rakamları yazıyla yazın (seslendirme için), Motor bilmediğini uydurmaz, "sis" der.
5. Yeni sistemler için `w_app.html` içindeki `/* ---------- ... ---------- */` blok düzenini koruyun; durum alanlarını `fresh()` içine ve İkinci Tur `keep` listesine ekleyin.

## Veri kaynakları ve lisanslar

Açık kaynaklar listesi oyun içinde başlık ekranındaki "Açık kaynaklar" düğmesindedir (NASA APOD, USGS, wheretheiss.at, Wikipedia; Three.js MIT; yazı tipleri SIL OFL).
