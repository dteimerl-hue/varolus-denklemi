# Varoluş Denklemi — 12 anlatı/içerik fikri (v21 üstüne)

Sıralama: en güçlü duygusal etki önce. Her fikir mevcut envanterle (ozellikler.md v21, GAME.people, GAME.core, story2–8, realm7) çakışmayacak şekilde seçildi; mevcut Kayıt 0–8, üç mektup, Ayna Bozulma, İkinci Tur, vardiya/chatter, epiloglar ve Bakanlık telsizi bilinerek yazıldı.

"Satır" = diyalog/metin satırı (JSON dizisindeki tek string ≈ 1 satır). Kod satırı dahil değildir.

---

## 1. Oyuncunun Kendi Kaydı — "Kayıt Dokuz"
Çekirdek'ten sonra (ya da Sessizlik sonunda) Arel telsize kendi kaydını bırakır: oyuncu 5 soru-şablonundan (Lale'ye, Motor'a, tanıklara, geleceğe, kendine) birini seçer ve her satırı iki-üç hazır parçadan kurar; metin oyuncunun gerçek tercihleriyle (yol, dinlenen kayıt sayısı, kaçan Bozulma, günlük notları) otomatik doldurulur. Kayıt yalnızca o oyuncunun localStorage'ında kalır; İkinci Tur'da Lale'nin eski kabininden "Kayıt Dokuz" olarak geri çalınır, bu kez Lale'nin sesiyle değil Arel'in sesiyle.
- **Tema:** hatırlama + yas (yas, alınan değil bırakılan bir şeye dönüşür); bilgi-sorumluluk (Lale "doldurma; taşı" demişti — oyuncu taşıdığını kaydeder).
- **İçerik:** ~90 satır (5 şablon × ~12 parça + 25 bağlama bağlı dolgu + 5 Lale/Motor tepkisi).
- **Risk:** Oyuncu "yazarlığı"nın tonu bozma riski orta; hazır parçalarla sınırlandırılmalı. Tekrar riski düşük (her oyun farklı). Web Speech ile Arel'in sesiyle okunması duygusal yükü taşır.

## 2. Lale Hayattayken — "Haliç Sabahı" (oynanabilir flashback)
Kayıt Sıfır'ın tamamlayıcısı: İstanbul 2026, tanıdan iki gün sonra, tek bir sabah; oyuncu bu kez Lale olarak yürür (evden Haliç kıyısına, oradan Nil'in laboratuvarına). Motor yok, sis yok, Bozulma yok; yalnızca Lale'nin kafasında kelimelerin yer yer "sis"e dönüştüğü kısa anlar (altyazıda bir kelime boşluk olarak gelir, oyuncu üç seçenekten doğrusunu seçmeye çalışır — yanlışsa sahne devam eder, kimse düzeltmez). Sabah, Arel'i aramaya karar verip aramamasıyla biter; telefon ekranında Arel'in adı, sonra kapanır.
- **Tema:** dürüstlük (söylememe kararının içinden görülmesi), hatırlama (kelime kaybının birinci şahıs deneyimi), yas (kaybı yaşarken yaşayan kişi).
- **İçerik:** ~140 satır (Lale iç ses 50, Nil diyaloğu 30, sokak/ev NPC'leri 25, kelime-boşluk mini sistemi için 20 çift, final 15). Ayrıca yeni küçük ortam (Haliç kıyısı + lab) gerekir — prosedürel su ve mevcut Three.js su/gökyüzü yeterli.
- **Risk:** Ton bozulması riski yüksek: Lale'nin yankısı şimdiye dek hep dolaylıydı; doğrudan oynanabilir olunca gizemini kaybedebilir. Çözüm: 8–10 dakika, tek sahne, müzik yok, yalnızca ses. Kilidi İkinci Tur + Kayıt Sıfır'a bağlanmalı.

## 3. Mürettebattan Biri Ayrılıyor — "Sema'nın Çantası"
Telsiz evre 2'de ("dış tanıklar derhal ayrılsın") Sema, tesis hekimi olarak Bakanlık listesine imza atar ve gitmeye karar verir: Lale'ye verdiği sözü tuttu, görevi bitti. Oyuncu Sema'yı asansörde yakalar; onu tutmak için bir sebep değil, bir cümle gerekir (üç seçenek: Lale'nin adı, kendi korkusu, hiçbir şey söylememek). İki seçenekte Sema gider; tesiste yeri boşalır, vardiya satırları ve epilog değişir, Çekirdek'teki "who" listesinden düşer ve finaldeki "dört yabancı" cümlesi "üç" olur. Üçüncü seçenekte kalır ama Arel'e "beni tutan sen değildin" der.
- **Tema:** dürüstlük (gitmek de dürüst bir cevap), yas (yasın içindeki insanların da yorulması), bilgi-sorumluluk (Sema'nın sözünü tutmanın bedeli).
- **İçerik:** ~75 satır (asansör sahnesi 20, gidiş/kalış dalları 2×12, boşalan tesis için diğer mürettebattan 7×2 satır, epilog varyantları 3×3, Çekirdek finali 4 satır değişiklik).
- **Risk:** Mevcut finale ve epilog JSON'una dokunur (kırılganlık orta). Tekrar riski düşük. Oyuncunun suçluluk hissi istenen etki; ama "yanlış cevap verdim" hissi oluşmamalı — her dal bir cevap olarak yazılmalı.

## 4. Motor'un Gözünden — "Sis Günlüğü" bölümü
Çekirdek'ten önce kısa bir ara bölüm: ekran Motor'un iç görünümüne döner (siyah-beyaz, yalnızca kenar çizgileri, HUD yok). Oyuncu Motor'dur; Arel'i dışarıdan izler, onun yürüdüğü yolu tahmin etmesi istenir (Bakanlık'ın "tahminle doldur" emrinin tersine çevrilmiş hâli). Her tahmin ekranda "güven: %" olarak görünür; Motor bilmediği yerde sis gösterir, yani oyuncu "bilmiyorum" seçeneğini kullanmadan ilerleyemez. Bölüm, Motor'un Arel'in Lale'ye bakışını hesaplamayı reddettiği tek bir cümleyle biter: "Bu bölge ölçülmedi. Doldurmayacağım."
- **Tema:** dürüstlük (Motor'un dürüstlüğünü oyuncu uygulamak zorunda kalır), bilgi-sorumluluk (tahmin etmemenin bedeli ve onuru).
- **İçerik:** ~60 satır (Motor iç ses 25, tahmin kartları 15, Bakanlık karşı sesi 8, Arel'in dışarıdan duyulan 12 satırı).
- **Risk:** Ton bozulması düşük-orta: Motor konuşkanlaşırsa "dürüst makine" gizemi dağılır — Motor satırları kısa, nötr, sayı ağırlıklı kalmalı. Görsel kod yükü (farklı render modu) orta.

## 5. Sahte Lale — "Dolgu Algoritması"
Bakanlık'ın gönderdiği dolgu algoritması (telsiz evre 1) Motor'a sızar; Bilinç boyutundan sonra tesiste ikinci bir Lale yankısı belirir: daha sıcak, daha tam, kestiği yerleri "hatırlayan", sorulara cevap veren. Oyuncu iki yankıyla konuşabilir; sahte olanın tek kusuru hiç "bilmiyorum" dememesidir. Oyuncu hangisini Çekirdek'e götüreceğini seçer; sahteyi seçerse Kayıt Yedi'nin kilidi açılmaz ve Sis Fırtınası'nda yankı dağılır, ekranda "Kayıt yedi: bu sesi ben bırakmadım" yazar.
- **Tema:** dürüstlük (tamam olmak ile doğru olmak arasındaki fark), hatırlama (idealize edilen hatıra vs kesik hatıra), yas (teselli olan yalanın cazibesi).
- **İçerik:** ~85 satır (sahte Lale 35 — gerçek Lale'nin satırlarının "düzeltilmiş" varyantları, gerçek Lale'nin 10 yeni tepkisi, Mira/Sema'nın fark etme satırları 12, iki finale dallanma 20, Bakanlık 8).
- **Risk:** Tekrar riski orta (iki Lale'nin satırları birbirine yakın olmalı ama ayırt edilebilir). Ton riski orta: "kötü ikiz" klişesine kaymamalı; sahte Lale kötü değil, yalnızca fazla iyi olmalı. Oyuncunun yanlış seçimi cezadan çok hüzün olarak yazılmalı.

## 6. Bakanlık Müfettişi — "Dr. Işık Tan"
Telsiz evre 2'de teslim ekibiyle bir kişi erken iner: Işık Tan, Bakanlık'ın bilim danışmanı, eski kozmolog, Arel'in Nobel'den önceki doktora arkadaşı. Düşman değildir; "sisi doldur" emrini yazan kişi odur ve bunu savunur: "Halk sis görmek istemiyor, cevap istiyor; cevap vermeyen bilim bütçesini kaybeder." Tesiste dolaşır, mürettebatla ayrı ayrı konuşur (Mira'yla kavga, Kaan'la eski tanışıklık, Hatice Nine'yle beklenmedik yakınlık). Oyuncu ona Motor'u gösterebilir: bir veri noktasına birlikte bakılır ve Işık ilk kez "bilmiyoruz" cümlesini kurar ya da kurmaz — Köprü sonunda Bakanlık'ın geri çekilmesinin yüzü olur.
- **Tema:** bilgi-sorumluluk (bilimin topluma borcu: cevap mı, dürüstlük mü), dürüstlük (karşı tezin inandırıcı savunusu).
- **İçerik:** ~110 satır (giriş 10, Arel diyaloğu 3 evre × 12, mürettebatla 7 × 5, Motor'a bakış sahnesi 15, üç son için epilog 3 × 4, idle 6).
- **Risk:** Ton riski orta: siyasi karikatüre dönüşmemeli; Işık haklı olduğu yerlerde haklı bırakılmalı. Yeni karakter modeli (Mixamo rig + look) gerekir. Mevcut telsiz metinleriyle tutarlılık şart.

## 7. Tanıkların Çatışması — "Yemekhane Gecesi"
Dört tanık (Rıza, Deniz, Zeynep, Hatice) aynı masada; oyuncu sahneye dışarıdan girer. Zeynep ölümün yanında olmanın anlamsızlığını, Hatice toprağın sabrını, Rıza izsiz silinmeyi, Deniz belirlenmişliği savunur ve birbirlerini incitirler ("Sen yoğun bakımda ölüm görüyorsun, ben kırk yıl denizde ölüm gördüm; farkı ne?"). Oyuncu araya girmez; yalnızca kimin yanına oturacağını seçer ve o kişinin bakış açısından sahnenin geri kalanını dinler (diğerlerinin sesi sisli/boğuk). Sahne uzlaşmadan biter; ertesi gün her tanığın idle satırları bir derece değişmiştir.
- **Tema:** anlam (anlamın insanlar "arasında" kurulması — ama çatışarak), hatırlama (herkesin kendi kaybını merkeze koyması).
- **İçerik:** ~70 satır (ortak sahne 25, dört bakış açısı × 8 "boğuk" varyant, ertesi gün 4 × 2).
- **Risk:** Ton riski düşük-orta: tanıklar şimdiye dek nazikti; çatışma ölçülü ve yorgunluktan doğmalı, öfkeden değil. Tekrar riski düşük. Mevcut chatter sistemiyle (story8) teknik olarak uyumlu.

## 8. Çocuk Oyuncu Modu — "Deniz'in Defteri"
Ayarlardan açılan ayrı anlatı katmanı (10–14 yaş): oyuncu Arel değil, Deniz'dir; tesiste misafir olarak dolaşır, boyutlara Arel'in peşinden girer. Bozulma yok, Bakanlık telsizi yok, Lale'nin kayıtları Deniz'e kapalı (yalnızca "Arel abi bir şey dinliyor" olarak görünür). Veri noktaları aynı bilimsel içerikle ama Deniz'in sorusu ve sınav formatıyla; her boyutun sonunda Deniz defterine bir soru yazar (oyuncu üç sorudan seçer) ve Lale Hoca'nın "sor" cümlesi motif olarak döner. Son: Deniz ilk deneyini kurar (Köprü epiloğundaki cümlenin oynanabilir hâli).
- **Tema:** bilgi-sorumluluk (soru sormanın kendisi bir sorumluluk), hatırlama (Lale'yi tanımadan ondan bir şey taşımak).
- **İçerik:** ~200 satır (6 boyut × ~25 Deniz varyantı + 30 tesis + 20 final). En pahalı fikir; ama mevcut fact/figure altyapısını yeniden kullanır.
- **Risk:** Ton bozulması riski yüksek değil ama "ikinci bir oyun" riski var: iki anlatı katmanının birbirini sulandırmaması için Deniz katmanı yas temasına dokunmamalı. Tekrar riski orta (aynı boyutlar iki kez yazılır).

## 9. Gerçek Zamanlı Saat — "Yetmiş İki Saat" modu
İsteğe bağlı mod: Bakanlık'ın 72 saati oyuncunun gerçek saatine bağlanır (localStorage'da başlangıç damgası; oyun kapalıyken de akar). Telsiz evreleri gerçek 24 saatlik aralıklarla gelir; Kaan'ın sayımı, mürettebatın vardiya satırları ve tesis ışıkları gerçek saate göre değişir (gece 03:00'te tesiste yalnızca Zeynep uyanıktır, nöbet alışkanlığı). Süre dolduğunda Çekirdek'e girilmemişse Bakanlık elektriği keser ve beşinci bir son açılır: "Karanlık" — Motor kapanır, Lale'nin yankısı dinlenmemiş kalır, Arel'in defterine Motor'un son cümlesi düşer.
- **Tema:** bilgi-sorumluluk (ertelemenin bedeli), yas (zamanın yasa aldırmadan akması).
- **İçerik:** ~55 satır (saate bağlı mürettebat 7 × 4, gece sahneleri 10, Karanlık sonu 12, uyarı/mod açıklaması 5).
- **Risk:** Oyuncuyu cezalandırma riski yüksek; yalnızca açıkça seçilen mod olmalı ve Günün Tohumu'na bağlanabilir. Tekrar riski düşük. Ton: gece 03:00 Zeynep sahnesi oyunun en sessiz anı olabilir — kıymetli.

## 10. Mektup Yazma — "Cevap Postası"
Zeynep, Lale'ye mektup yazmıştı ve "cevabı seninle gelmiş" demişti; Rıza'ya mektup gelmişti. Oyuncu her tanığa bir boyuttan sonra mektup yazabilir: Defter sekmesinde üç cümle, her cümle ilgili boyutun veri noktalarından / figür diyaloglarından türetilmiş 4 seçenekle kurulur. Tanık mektubu bir sonraki boyut dönüşünde okumuş olur ve yalnızca mektupta geçen şeye tepki verir (epilog metni de mektup içeriğine göre bir cümle değişir). Yazılmayan mektup da bir cevaptır: tanık "yazmadın, olsun" der ve sorusunu kendi taşır.
- **Tema:** anlam (anlamın iki insan arasında kurulması — bu kez oyuncunun eliyle), dürüstlük (yalnızca ölçülen şeyin yazılabilmesi).
- **İçerik:** ~120 satır (4 tanık × 6 boyut × 4 seçenek = 96 cümle parçası + 4 × 5 tepki + 4 "yazmadın" satırı).
- **Risk:** Tekrar riski orta: seçenekler mevcut "after" satırlarını yankılamamalı, onları tamamlamalı. Ton düşük risk. Letters sekmesi zaten var (Bellek Sarayı); UI yeniden kullanılır.

## 11. Nil'in Odası — Lale'nin Meslektaşından Üçüncü Bakış
Nil (Bilinç boyutundaki figür, Lale'nin nörolog arkadaşı) tesise gelmez ama Motor'da bir kayıt odası açılır: Lale'nin kesip attığı değil, Nil'in sakladığı dört ses — Lale'nin hastalarına filmini anlatırken, Nil'le tartışırken, bir vaka toplantısında ve Arel hakkında konuşurken. Bunlar Lale'nin Arel'e bırakmadığı, bırakmayı düşünmediği "üçüncü şahıs" Lale'sidir: daha sert, daha komik, bazen haksız. Oyuncu dördünü dinleyince Çekirdek'teki yankı bir satır ekler: "Nil sana neyi dinletti? Peki. O da bendim."
- **Tema:** hatırlama (bir insanın yalnızca bize bıraktığı kadar olmaması), yas (idealize etmeden hatırlamak), dürüstlük (Lale'nin kusurlarıyla görülmesi).
- **İçerik:** ~50 satır (4 kayıt × 8 + Nil'in 8 çerçeve satırı + Çekirdek'e 3 ek + Sema'nın 3 tepkisi).
- **Risk:** Tekrar riski düşük-orta (Kayıt 0–8 ile farklı ton: üçüncü şahıs). Ton riski düşük; en ucuz ve en "yetişkin" fikirlerden biri. Kayıt Yedi'nin ağırlığını gölgelememeli — kilit, Kayıt Yedi'den sonra açılmalı.

## 12. Boyut Sekiz — "Yankı Odası" (dinleme boyutu)
Yedinci geçidin ardında, İkinci Tur'da açılan sekizinci alan: bilim yok, figür yok, Bozulma yok. Oyuncu yalnızca yürür ve oyunun tüm diyaloglarından rastgele seçilen cümleler, konuşan kişinin motifiyle, mesafeye göre sisli gelir; durup dinleyince cümle netleşir ve kim söylediği ekranda belirir. Odanın tek etkileşimi "sustur"dur: oyuncu bir sesi kalıcı olarak kapatabilir ve bir daha açamaz (localStorage). Çıkışta Motor, kaç sesin susturulduğunu söyler ve bir cümle ekler: "Ben hiçbirini silmedim; sen seçtin."
- **Tema:** hatırlama (hatırlamanın seçici olması, unutmanın bir eylem olması), bilgi-sorumluluk (silmenin geri alınamazlığı).
- **İçerik:** ~20 yeni satır (mevcut diyalog havuzunu yeniden kullanır: Motor 8, giriş/çıkış 8, başarım 4).
- **Risk:** Ton riski düşük; tekrar riski düşük (içerik mevcuttur). Oyuncuyu "yanlış sesi kapattım" pişmanlığına itme riski — istenen etki ama bir uyarı metni şart. Teknik maliyet düşük (TTS + motif sistemi hazır).

---

## Önceliklendirme özeti

| # | Fikir | Satır | Duygusal etki | Risk | Maliyet/etki |
|---|---|---|---|---|---|
| 1 | Kayıt Dokuz (oyuncu kaydı) | 90 | çok yüksek | orta | iyi |
| 2 | Haliç Sabahı (Lale flashback) | 140 | çok yüksek | yüksek | orta |
| 3 | Sema'nın Çantası (ayrılış) | 75 | yüksek | orta | iyi |
| 4 | Sis Günlüğü (Motor POV) | 60 | yüksek | düşük-orta | iyi |
| 5 | Dolgu Algoritması (sahte Lale) | 85 | yüksek | orta | orta |
| 6 | Dr. Işık Tan (müfettiş) | 110 | orta-yüksek | orta | orta |
| 7 | Yemekhane Gecesi (tanık çatışması) | 70 | orta-yüksek | düşük-orta | iyi |
| 8 | Deniz'in Defteri (çocuk modu) | 200 | orta | orta | zayıf |
| 9 | Yetmiş İki Saat (gerçek zaman) | 55 | orta | yüksek (ceza) | orta |
| 10 | Cevap Postası (mektup yazma) | 120 | orta | düşük | orta |
| 11 | Nil'in Odası | 50 | yüksek | düşük | çok iyi |
| 12 | Yankı Odası (boyut 8) | 20 | orta | düşük | çok iyi |

Önerilen ilk paket (≈ 200 satır): 11 + 4 + 1 + 12 — en düşük riskle en yüksek etki; hepsi mevcut TTS, motif, Defter ve kayıt altyapısını yeniden kullanır.
