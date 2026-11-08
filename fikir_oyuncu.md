# Varoluş Denklemi — oyuncu/topluluk gözüyle 12 fikir

Bakış açısı: oyunu bir akşam bitirip arkadaşına WhatsApp'tan link atan, Reddit'te "bunu oynayın" diyen, bir YouTuber'ın 40 dakikalık videosunu izleyip "ben de sonumu göreyim" diyen oyuncu. Kaynak: `ozellikler.md` (v21). Maliyet ölçeği: **küçük** (bir akşam, mevcut sistemlere ek), **orta** (birkaç gün, yeni UI/akış), **büyük** (haftalar, metin/varlık üretimi). Kısıtlar: tek HTML, sunucusuz, artifact db yalnızca küçük veri (pano/sonlar), localStorage.

---

## 1. Yol Kartı — paylaşılabilir son posteri
Oyun bittiğinde seçilen son (Gözlemci/Köprü/Sessizlik/Sarayın Kapısı), totem cevabı, oynanış süresi, açılan başarım sayısı ve o yola özel bir Lale cümlesiyle 1080×1350 (Instagram/WhatsApp oranı) bir kart üretilir; canvas ile çizilir, "indir" ve Web Share API ile tek dokunuşla paylaşılır. Kartın üstünde oyuncunun Arel'i (kıyafet/saç/ayakkabı varyasyonu) ve küresel son yüzdesi ("oyuncuların %31'i Köprü'yü seçti") yer alır; başarımlarla açılan çerçeveler (Sis Fırtınası'nı geçen için fırtına çerçevesi vb.) kartı kişiselleştirir. Mevcut fotoğraf modu (filtre, şerit, indirme) zaten canvas çıkışı yaptığı için büyük kısmı hazır.
- **Oyuncu ihtiyacı:** "Benim sonum buydu, seninki ne?" — kendini ifade + arkadaşı kışkırtma (Wordle kutucukları etkisi).
- **Maliyet:** küçük. Canvas + mevcut fotoğraf modu altyapısı; artifact db'ye yazma gerekmez, son yüzdesi zaten okunuyor.
- **Kötüye kullanım riski:** düşük. Kartta serbest metin alanı yok (oyuncu adı eklenecekse 12 karakter + küçük kaba söz listesi filtresi ya da hiç ad koyma; kartı "Arel Vey" imzalı tut).

## 2. "Sisi Tahmin Et" — son kodu ile sosyal tahmin
Oyun sonunda 8–10 karakterlik bir kod üretilir (`VD-K3-7B2X` gibi): seçilen son, 6 boyuttaki yol seçimleri, totem cevabı ve mini sınav profili base32 ile sıkıştırılmış. Arkadaş kodu Tohum sekmesine girince "Arkadaşın Bilinç boyutunda hangi yolu seçti?" tipi 5 soruluk tahmin oyunu açılır; doğru tahmin sayısına göre "Sisi Okuyan" başarımı ve iki profilin yan yana karşılaştırması ("ikiniz de Anlam'da Sessizlik'i seçtiniz"). Sohbet grubunda kod alışverişi başlı başına bir oyun olur.
- **Oyuncu ihtiyacı:** paylaşım bahanesi + "beni ne kadar tanıyorsun" sosyal kancası; oyunu bitirmemiş arkadaşı merak ettirir.
- **Maliyet:** küçük–orta. Kod yalnızca enum değerleri taşır (sunucu yok, URL hash'ine de gömülebilir: `#kod=...`); tahmin UI'si Tohum sekmesine ek bir panel.
- **Kötüye kullanım riski:** çok düşük. Kod serbest metin içermez; geçersiz kod sessizce reddedilir. Tek dikkat: kod, ismen "spoiler" taşıdığından tahmin ekranında sonu doğrudan yazdırmayıp soru formunda sunmak.

## 3. Hız Koşusu modu ve bölüm zamanlayıcısı
Ana menüde "Hız Koşusu": oyun içi zaman (IGT) ekranın köşesinde, her geçit/boyut çıkışında split ("Kuantum 6:42, önceki en iyi −0:18"), diyalog atlama ve kalibrasyon mini-arayüzünü hızlandırma serbest. Kategoriler: **Any% (herhangi bir son)**, **Tüm Veriler** (18 veri noktası + 6 kayıt parçası), **Yedi Geçit** (Bellek Sarayı dahil). Koşu sonunda doğrulama kodu (süre + kategori + seed + basit checksum) ve Yol Kartı'nın hız koşusu versiyonu. Günün Tohumu'ndaki "Hızlı Sis" koşulu zaten var; bu onun kalıcı ve kategorili hali.
- **Oyuncu ihtiyacı:** geri dönüş sebebi (bitirdikten sonra ne yapacağım?), YouTube/Twitch içerik üretimi, konuşma oyunu topluluklarında "hikâye oyununu 20 dakikada bitirdim" videoları.
- **Maliyet:** orta. Zamanlayıcı ve split'ler küçük; diyalog atlama ve mini oyunların atlanabilir/hızlı versiyonları orta; küresel pano eklenecekse artifact db'de kategori başına en iyi 20 kayıt (küçük veri).
- **Kötüye kullanım riski:** orta. İstemci tarafı süre sahtelenebilir; checksum sadece kazara bozulmayı yakalar. Çözüm: küresel panoyu "güven temelli" diye etiketle, kayıt eklerken video linki iste (yalnızca YouTube/Twitch domain'i), ya da panoyu tamamen yerel tut ve paylaşımı karta bırak. Aşırı uç süreleri (< teorik minimum) otomatik ele.

## 4. Özel Tohum linki — "benim dünyamda oyna"
Günün Tohumu'nun kardeşi: oyuncu kendi koşul setini (Işıksız + Kalın Sis + Tek Can) ve bir seed'i seçer, oyun bir URL üretir (`...#tohum=KALIN-SIS-4471&kosul=IK,TC`). Linke tıklayan arkadaş aynı Bozulma davranışını, aynı hava olaylarını, aynı halüsinasyon sırasını görür; bitirince ikisinin sonucu (süre, bütünlük kaybı, toplanan veri) aynı ekranda karşılaştırılır. "Hatice Nine'nin tohumu" gibi 5–6 hazır isimli tohum ile başlangıç verilebilir.
- **Oyuncu ihtiyacı:** asenkron rekabet; "aynı şeyi yaşadık mı?" sohbeti; Reddit'te "bu tohum çok zor, deneyin" gönderileri.
- **Maliyet:** küçük. Seed sistemi ve 5 koşul mevcut; eklenen şey URL parametresi okuma/yazma ve sonuç karşılaştırma ekranı. Sunucu yok.
- **Kötüye kullanım riski:** düşük. URL yalnızca seed + koşul bayrakları; bilinmeyen parametreler yoksayılır. Tohum adı serbest metinse (isteğe bağlı) 20 karakter ve filtre; yoksa yalnızca otomatik üretilmiş ad.

## 5. Misafir modu — 10 dakikalık "Kovuk'a bir bakış"
Linkle gelen ve 3 saatlik oyuna girmeyecek arkadaş için: tek boyut (Kuantum ya da Yuva — en görsel olanı), geçit önceden kalibre, Motor'un 20 saniyelik tanıtımı, 1 veri noktası, 1 tarihi figür diyaloğu, kısa bir Bozulma karşılaşması ve mini sınav; sonunda "Bu bir boyuttu, altı tane daha ve bir Çekirdek var" + kaydı tam oyuna taşıma. Süre sayacı görünür (kalan ~10 dk), mobilde varsayılan giriş bu mod olmalı.
- **Oyuncu ihtiyacı:** düşük taahhütle tatma; paylaşan kişinin "sadece 10 dakika ver" diyebilmesi; mobilde linke tıklayanın beyaz ekrana değil oyuna düşmesi.
- **Maliyet:** orta. İçerik hazır, iş akışı budama: boyut seçimi, atlanan sistemler (günlük sekmeleri gizli, Tohum yok), misafir→tam oyun kayıt aktarımı (localStorage'da bayrak).
- **Kötüye kullanım riski:** yok. Tek tasarım riski: misafir modu "tam oyun bu kadar mı?" izlenimi bırakırsa dönüşüm düşer; sonda Çekirdek'ten 10 saniyelik görsel tease koy.

## 6. Eşlik modu — ikinci oyuncu Motor olur
Aynı cihazda asimetrik kanepe ko-op: birinci oyuncu Arel'i yürütür, ikinci oyuncu (ikinci kumanda ya da klavyenin sağ tarafı / telefon dokunmatiği) Motor'un gözüdür: Sis Fenerini yönlendirir, Bozulma yaklaşınca ekranın kenarını titreştirir, Sis Akış Haritası'nı canlı okur ve mini sınavlarda "ipucu" hakkını kullanır. Motor "bilmediğini uydurmaz" — ikinci oyuncu da yalnızca gördüğünü söyleyebilir; iki kişinin konuşması oyunun teması olur. Çocuk-ebeveyn ve çift oynaması için ideal.
- **Oyuncu ihtiyacı:** oyunu birlikte deneyimleme (konuşma oyunlarını eşiyle/çocuğuyla oynayanlar büyük segment); izleyen kişiye rol vermek.
- **Maliyet:** orta–büyük. İkinci girdi haritası (kumanda desteği var), fener kontrolünün ayrılması, Motor rolüne özel 20–30 satır diyalog ve bir HUD; ağ yok.
- **Kötüye kullanım riski:** yok. Denge riski: ikinci oyuncu feneri sürekli tutarsa Bozulma kolaylaşır; yakıtı ikinci oyuncuya da sınırlı ver.

## 7. Oynanış karnesi — "Arel'in Dosyası"
Son ekranında ve Günlük'te yeni bir sayfa: toplam süre, boyut sırası, mini sınav doğruluğu (ve hangi boyutta en çok yanıldığı), Bozulma'dan kaçış/yakalanma sayısı, fener yakıtı kullanımı, en uzun konuşulan tarihi figür, toplanan Lale kayıtları (x/8), yol dağılımı (Köprü 3 / Gözlemci 2 / Sessizlik 1) ve her satırın karşısında küresel ortalama. En sonda tek cümlelik "Motor'un yorumu" (kural tabanlı: "Veriyi topladın ama sınavlarda acele ettin"). Yol Kartı'ndan daha derin, "ikinci tur" için hedef verir.
- **Oyuncu ihtiyacı:** kendini görme ve kıyaslama; NG+ için somut neden ("Kuantum'da 3 yanlış, bir daha gir"); Reddit'te ekran görüntüsü paylaşımı.
- **Maliyet:** küçük–orta. İstatistiklerin çoğu zaten tutuluyor (başarımlar, Günün Tohumu panosu, son istatistikleri); eksik sayaçlar + bir sayfa UI. Küresel ortalamalar artifact db'ye 10–12 toplam sayaç (çok küçük veri).
- **Kötüye kullanım riski:** düşük. Küresel sayaçlara sahte değer basılabilir; istemciden yalnızca +1/+süre ekle, aykırı değerleri (süre > 24 sa) at.

## 8. Yankı Taşı — şablonla iz bırakma (Dark Souls usulü)
Her boyutta bir "yankı taşı": oyuncu üç parçalı şablondan cümle kurar — [özne: "Sis / Bozulma / Lale'nin sesi / Motor / Bu veri"] + [fiil: "burada bekliyor / yalan söylemiyor / beni şaşırttı / ilerde tehlikeli / ağlattı"] + [isteğe bağlı boyut etiketi]. Diğer oyuncuların yankıları (zaten var olan "oda varlığı hayaletleri" gibi) taşın yanında belirir; beğeni = "Yankıla". Serbest metin yok, bu yüzden moderasyon gerekmez ama ifade alanı vardır; Türkçe çekimler şablonda hazır.
- **Oyuncu ihtiyacı:** yalnız bir oyunda başkalarının varlığını hissetmek; "ben de buradaydım" demek; duygusal anları (Lale kayıtları) başkalarıyla sessizce paylaşmak.
- **Maliyet:** orta. Şablon UI + artifact db'de boyut başına en fazla 150 kayıt (küçük: her kayıt 3 enum + sayaç), eski kayıtları döndür; hayalet sistemi görsel olarak yeniden kullanılır.
- **Kötüye kullanım riski:** düşük (şablon sayesinde). Kalan risk: şablon kombinasyonlarının çift anlamlı çıkması — listeyi yazarken kombinasyonların tamamını bir kez okuyun; spam için cihaz başına günde 3 yankı sınırı (localStorage) ve db'de aynı kombinasyonu tekrar yerine sayaçla tut.

## 9. Sözleşmeler — isimli zorluk sunumları
Günün Tohumu'ndaki 5 koşulu kalıcı, anlatıya bağlı paketlere dönüştür: **Gözlemci Sözleşmesi** (kolay mod + otomatik koşma + bol yakıt), **Köprü Sözleşmesi** (varsayılan), **Sessizlik Sözleşmesi** (Sessiz + Kalın Sis: Motor konuşmaz, yalnızca sis gösterir), **Lale'nin Sözü** (Tek Can + Işıksız: ölünce kayıt silinir, Lale'nin son kaydı yalnızca burada açılır). Her sözleşme Yol Kartı'nda mühür olarak görünür; "Lale'nin Sözü" bitirenler için ayrı küresel sayaç ("bugüne kadar 212 kişi").
- **Oyuncu ihtiyacı:** zorluk seçimini kimliğe çevirme ("ben Sessizlik'te bitirdim"), geri dönüş sebebi, erişilebilirlik tarafında ise kolay modu utandırmadan sunma.
- **Maliyet:** küçük. Koşullar ve kolay mod mevcut; eklenen şey paketleme, isimler, 1 özel kayıt ve kart mührü.
- **Kötüye kullanım riski:** yok. Tasarım notu: "Lale'nin Sözü"nde kayıt silinmesi hikâye kaybı demek; silmeden önce iki kez onay ve Yol Kartı'nı otomatik üret ki eli boş kalmasın.

## 10. Paskalya yumurtaları — Kovuk'un küçük sırları
Birkaç ucuz, konuşulacak sürpriz: (a) NASA APOD terminaline oyuncunun bugünkü tarihinin yanında doğum gününü girince o günün APOD'u ve Motor'un "senin günün böyle görünüyormuş" satırı; (b) gerçek saatte 03:00–04:00 arası oynayanlara Hatice Nine'nin farklı bir vardiya satırı ve telsizde bir "uykusuz" sinyali; (c) Perseid/Geminid gibi gerçek meteor yağmuru tarihlerinde gökyüzünde daha fazla kayan yıldız + Deniz'in yorumu; (d) Motor Çekirdeği heykeline 7 kez tıklayınca Kayıt Sıfır'ın mırıltılı versiyonu; (e) ana menüde belirli tuş dizisi ile "Motor dürüstlük modu": tüm sis uyarıları yüzde olarak görünür. Hiçbiri ilerlemeyi etkilemez, hepsi ekran görüntüsü/short'luk.
- **Oyuncu ihtiyacı:** keşif ve "bunu biliyor muydunuz" paylaşımı; YouTuber'lara ikinci video malzemesi; oyunun canlı hissetmesi.
- **Maliyet:** küçük (her biri birkaç satır; APOD zaten var, meteor tarihleri sabit liste). Toplamı bir akşam.
- **Kötüye kullanım riski:** yok. Dikkat: tarih/saat tabanlı olanlar cihaz saatine bağlı; yanlış saat dilimi sürprizi kaçırır, bu da sorun değil. Doğum günü girişi localStorage'da kalsın, hiçbir yere gönderilmesin.

## 11. İngilizce altyazı katmanı
Tüm diyalogları değil, önce **UI + veri noktaları + Lale kayıtları + yol seçimi/son metinleri** için İngilizce altyazı; mürettebat ortam sohbetleri ve heykel yorumları ikinci dalga. Seslendirme Türkçe kalır (Web Speech Türkçe ses), altyazı İngilizce seçilebilir — "altyazılı film" hissi, çeviri maliyetini yarıya indirir. Tarayıcı dili İngilizse ilk açılışta soru sorulur. Wikipedia kaynak kartları dile göre `en.`/`tr.` seçer.
- **Oyuncu ihtiyacı:** Türkçe bilmeyen arkadaşa/yurt dışındaki akrabaya gönderebilmek; itch.io ve Reddit'te (r/WebGames, r/indiegames) erişim; YouTuber'ların uluslararası izleyicisi.
- **Maliyet:** büyük. Metin hacmi (6 boyut × veri + diyalog + 8 kayıt + mektuplar + sonlar) ciddi; katmanlı yaklaşımla ilk dalga orta. Tek dosya kalmalı: metinler `{tr, en}` sözlüğünde, dosya boyutu artar (sıkıştırma ile kabul edilebilir).
- **Kötüye kullanım riski:** yok. Kalite riski: Lale'nin kayıtları ve düşünür diyalogları makine çevirisiyle düzleşir; en azından bu iki kümeyi insan eliyle çevirin, aksi halde paylaşan oyuncunun "ama Türkçesi çok daha iyi" demesi gerekir.

## 12. Cep kalitesi — mobil ilk 60 saniye
Linklerin çoğu telefonda açılacak. Hedef: (a) dikey ekran desteği (en azından menü, günlük, kart; oyun yatay kilit uyarısı), (b) cihaza göre otomatik kalite: `deviceMemory`/GPU tespiti ile 720p ön ayarı, yansımalı su ve lens flare kapalı, parçacık sayısı yarım; (c) yükleme ekranında ilerleme çubuğu ve 1 cümlelik "Kovuk'a iniliyor" (beyaz ekran = kapatılan sekme); (d) dokunmatik joystick'e ek olarak "dokun-git" (noktaya dokunarak yürüme) ve büyük F (fener) düğmesi; (e) pil tasarruf modu (30 fps). Yol Kartı, Sisi Tahmin Et ve Misafir modu mobilde kusursuz olmalı; bunlar paylaşım döngüsünün mobil halkası.
- **Oyuncu ihtiyacı:** linke tıklayan arkadaşın ilk dakikada kaçmaması; otobüste/yatakta Misafir modu; paylaşılan kartın telefondan üretilmesi.
- **Maliyet:** orta. Kalite ayarları ve dokunmatik mevcut; eklenen otomatik tespit, dikey düzen ve yükleme ekranı. Test maliyeti (gerçek cihazlar) asıl zaman gideri.
- **Kötüye kullanım riski:** yok. Teknik risk: iOS Safari'de Web Speech ve ses otomatik başlamaz; ilk dokunuşta "sesi aç" düğmesi şart, yoksa oyun sessiz sanılır.

---

## İlk 10 dakikada kaybedilebilecek oyuncu — 5 gözlem

1. **İsim seli.** İlk üç dakikada Arel, Motor, Lale, Bakanlık ve 7 mürettebat ismi + "Kovuk Tesisi", "Bozulma", "Sis" terimleri geliyor. Yeni oyuncu kimin canlı, kimin kayıt, kimin düşman olduğunu ayırt edemez. Öneri: ilk 5 dakikada en fazla 3 isim (Arel, Motor, Lale); mürettebatı Günlük > İnsanlar sekmesine ilk kez girince tanıt; ismi ilk geçen her karakter için 2 saniyelik ekran etiketi.
2. **"Nereye gideceğim?"** Tesiste 6 geçit, Çekirdek, 3 terminal ve heykel aynı anda açık. Serbest keşif güzel ama ilk oyuncu için bir ok lazım: Başlangıç geçidi parlasın, diğerleri sisle kapalı gibi görünsün; Motor tek cümleyle "önce Başlangıç" desin. Geçit kalibrasyonu (ER=EPR arayüzü) ilk engel — başarısız olursa "neden?" belirsiz; ilk kalibrasyonu otomatik ya da yönlendirmeli yap, ikinciden itibaren gerçek.
3. **Bozulma ile ilk karşılaşma ne demek?** Oyuncu ilk kez yakalandığında ölüm mü, görüntü mü, ceza mı anlaşılmıyor; bütünlük segmentleri ve Sis Feneri'nin (F, yakıt) ilişkisi anlatılmadan düşman geliyor. Öneri: ilk Bozulma'yı Rehber içinde kaçılamayacak kadar yavaş yap, fener yakıtının bitişini ve bütünlük kaybını tek bir cümleyle ("Sis Feneri Bozulma'yı iter; yakıtı Sis Akış Haritası'ndan gör") göster.
4. **Sessiz ve kekeme açılış.** Tarayıcı ses politikası yüzünden Web Speech ve prosedürel müzik ilk tıklamaya kadar çalmaz; oyuncu "ses yok mu?" der. Varsayılan 2160 çizim kalitesi orta cihazda ilk 30 saniyeyi takılmalı yapar — "oyun bozuk" izlenimi. Öneri: ilk etkileşimde "Sesi aç" düğmesi, 2 saniyelik FPS ölçümüyle otomatik kalite düşürme, yükleme çubuğu.
5. **Yol seçimi ve günlük sekmeleri anlamsız.** İlk boyutun sonunda Köprü/Gözlemci/Sessizlik seçimi geliyor ama bu kelimelerin ne yaptığı (son mu, diyalog mu, zorluk mu) söylenmiyor; oyuncu rastgele seçip "yanlış mı yaptım?" kaygısıyla kalıyor. Günlük 10 sekmeyle açılıyor, çoğu boş. Öneri: ilk yol seçiminde her seçeneğin altına tek satır sonuç ipucu ve "geri dönülebilir/dönülemez" bilgisi; Günlük sekmelerini ilgili sistem ilk kez tetiklendiğinde aç (ilk 10 dakikada Veriler + Defter + Görevler yeter).
