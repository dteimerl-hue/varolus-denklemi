# Varoluş Denklemi — 12 yeni mekanik/sistem fikri

Sıralama: değer/maliyet oranı en yüksekten en düşüğe. Hiçbiri mevcut envanterde (ozellikler.md v21) yok; her biri yeni bir oyun döngüsü getirir (epistemik bahis, bakım, inşa, zaman, sosyal, çıkarım, meta). Maliyet ölçeği tek dosya Three.js + sunucusuz (yalnız localStorage ve artifact db) kısıtına göredir.

---

## 1. Tahmin Defteri: Kalibrasyon Bahsi
**Döngü:** Her boyuta girmeden önce Motor üç soru sorar ("Mars'ta su izi bulacak mısın? Yüzde kaç eminsin?"); oyuncu seçenek + güven yüzdesi girer. Veri noktaları toplandıkça Motor tahmini gerçekle karşılaştırır ve Brier puanı verir; iyi kalibre oyuncu "Dürüst Gözlemci" rütbesi kazanır, aşırı özgüven ise Motor'dan nazik ama acımasız bir yorum alır. Eğlencesi: bilgi değil, kendi bilgisizliğini bilmek ödüllendirilir; yeniden oynamada oyuncu tahminlerini düzeltmeye çalışır.
**Tema bağı:** Motor'un "bilmediğini uydurmama" ilkesini oyuncuya aktarır; oyuncu da dürüst makine olmayı öğrenir.
**Maliyet:** Küçük — mevcut veri noktası ve mini sınav altyapısına boyut başına 3 soruluk JSON, bir kaydırıcı arayüzü ve Brier hesabı.
**Bağımlılık/risk:** Sorular gerçek bilim kaynaklı veri noktalarına bağlı olmalı; cevap Wikipedia kartından önceden sızarsa bahis anlamsızlaşır (sorular kart açılmadan sorulmalı).

## 2. Bakanlık Raporu: Dürüstlük Muhasebesi
**Döngü:** Her evre sonunda Bakanlık rapor ister; oyuncu bulgular hakkında üç şık arasında seçer: gerçeği yaz (kaynak kesilir), süsle (yakıt/kolaylık gelir), sakla (kimse bilmez). Motor her raporu kaydeder ve yalanlar birikince tutarsızlıklar ortaya çıkar: mürettebat sohbeti değişir, Bakanlık "önceki raporunla çelişiyor" der, sonlar kaymaya başlar. Eğlencesi: kısa vadeli kazanç ile uzun vadeli güven arasında gerçek bir ikilem; tek bir "ahlak puanı" yerine çelişki kataloğu.
**Tema bağı:** Dürüst makine ile baskı altındaki insan arasındaki gerilimi oyuncunun ellerine koyar.
**Maliyet:** Küçük — rapor diyalog ağacı, localStorage'da yalan listesi ve mevcut mürettebat/son dallanmasına 2-3 koşul.
**Bağımlılık/risk:** Sonuçlar görünür olmazsa sistem süs kalır; her yalanın en az bir somut geri dönüşü (diyalog, kaynak, son) yazılmalı.

## 3. Hatırlama Provası: Günlük Erozyonu
**Döngü:** Defter girdileri ve veri kartları zamanla sislenir (harfler silinir, cümleler boşluğa döner); oyuncu bir girdiyi "prova" ederse (kısa boşluk doldurma, aralıklı tekrar) girdi yeniden netleşir ve bir sonraki erozyon daha geç gelir. Kayıtları korumak için oyuncu neyi hatırlamaya değer bulduğunu seçmek zorunda kalır; her şey korunamaz. Eğlencesi: envanter yönetimi gibi ama envanter oyuncunun belleğidir; bakım döngüsü oyuna doğal bir ritim verir.
**Tema bağı:** Hatırlama verilmiş bir şey değil bir eylemdir; Lale'nin kayıtları oyuncu onları tekrar tekrar dinlediği sürece yaşar.
**Maliyet:** Küçük-orta — her girdiye zaman damgası ve "netlik" değeri, metin maskeleme fonksiyonu ve bir boşluk doldurma mini arayüzü.
**Bağımlılık/risk:** Kolay mod ve erişilebilirlik ayarlarında erozyonu kapatma seçeneği şart; aksi halde ceza gibi hissedilir.

## 4. Gerçek Zaman Vardiyası
**Döngü:** Tesis gerçek saat ve takvimle yaşar: gece 00-06 arası yalnız Hatice Nine ve telsiz uyanıktır, ay evresine göre sis yoğunluğu değişir, oyuncu uzun süre gelmezse Defter'de "Arel'in yokluğu" notları ve mürettebat mesajları birikir. Bazı tanıklar ve bir mektup yalnızca belirli gerçek saat aralığında ortaya çıkar. Eğlencesi: dünya oyuncudan bağımsız yaşar, geri dönmek keşfe dönüşür (Animal Crossing ritmi, Outer Wilds merakı).
**Tema bağı:** Lale'nin yokluğunda geçen zaman ile oyuncunun oyundan uzak geçirdiği zaman üst üste biner.
**Maliyet:** Küçük — Date() tabanlı koşullar, localStorage'da son ziyaret damgası, mevcut vardiya satırlarına saat filtresi.
**Bağımlılık/risk:** Saat kandırılabilir ve gece oynamayan oyuncu içerik kaçırabilir; zaman kilitli her içeriğe 7 günlük gerçek süre sonra alternatif açılış konmalı.

## 5. Lale'ye Sesli Mesaj
**Döngü:** Çekirdek yakınında bir kayıt cihazı; oyuncu mikrofona 1-2 cümle söyler, Web Speech tanıma metne çevirir ve Arel'in sesiyle Defter'e işlenir. Son sahnede Lale'nin yankısı oyuncunun kendi cümlesine cevap verir (anahtar kelime eşleşmesiyle 6-8 varyant), Kayıt Yedi'ye oyuncunun sözü eklenir. Eğlencesi: oyuncunun kendi sözü oyunun kanonuna girer; tek seferlik ama unutulmaz.
**Tema bağı:** Oyun boyunca yalnız dinlenen Lale'ye ilk kez cevap verilir; hatırlama iki yönlü olur.
**Maliyet:** Küçük — SpeechRecognition API (Web Speech sentezi zaten var), anahtar kelime tablosu, klavye alternatifi.
**Bağımlılık/risk:** Tanıma Chrome dışı tarayıcılarda ve çevrimdışı pakette çalışmayabilir; yazarak girme her zaman açık kalmalı, ses verisi cihaz dışına çıkmamalı.

## 6. Tanıklık Panosu: Çıkarım Tahtası
**Döngü:** Mevcut 7 tanık ve kesik kayıt parçaları, Yedinci Geçit'in neden mühürlendiğini anlatan tek bir olay örgüsünün parçalarıdır; oyuncu bir mantar panoda kim/ne zaman/nerede kartlarını iplerle bağlar. Obra Dinn kuralı: yalnızca üç bağ aynı anda doğru olduğunda pano "kilitlenir" ve onaylanır, tek tek doğrulama yoktur; bu yüzden tahmin değil çıkarım gerekir. Eğlencesi: dağınık yan görevler bir cinayet masasına dönüşür; dürüst makine ipucu vermez ama çelişkiyi işaretler.
**Tema bağı:** Sisin içinde parçalardan bütünü yeniden kurmak oyunun kendisidir; Motor "bilmiyorum" der, oyuncu bilmek zorundadır.
**Maliyet:** Orta — pano arayüzü (sürükle-bırak, çizgi), 12-15 kartlık doğruluk matrisi, mevcut tanık metinlerinin olay örgüsüne göre yeniden yazılması.
**Bağımlılık/risk:** Tanık metinleri tutarlı tek bir zaman çizelgesi olarak yeniden yazılmazsa pano çözülemez olur; senaryo revizyonu kod kadar iş.

## 7. Fener Ağı: Kalıcı Işık İnşası
**Döngü:** Oyuncu Bozulma Sahaları'nda sınırlı sayıda ışık direği diker; direkler arası 20 m'den kısaysa koridor "aydınlanır" ve Bozulma oraya giremez, uzunsa sis geri dolar. Direkler turlar arası kalır ama yakıt ister; oyuncu rotasını planlayıp bir aydınlık ağ kurar, NG+'da ağı yarım kalmış bulur. Eğlencesi: Death Stranding yapı paylaşımı tadında, keşif alanı yavaş yavaş evcilleşir ve her direk bir karardır.
**Tema bağı:** Sis bilinmeyenin, ışık hatırlananın haritasıdır; oyuncu kendi bilgisini mekâna işler.
**Maliyet:** Orta — direk yerleştirme (raycast), graf bağlantı hesabı, Bozulma yol bulmasına "aydınlık yasak" maskesi, localStorage'da direk listesi.
**Bağımlılık/risk:** Mevcut Sis Feneri yakıt ekonomisiyle çakışır; iki kaynak tek havuza bağlanmalı, yoksa dengesizlik olur.

## 8. Motor'u Öğretmek: Kanıt Grafiği
**Döngü:** Motor başlangıçta birçok soruya "bilmiyorum" der; oyuncu toplanan veri noktalarını kanıt olarak bir iddiaya bağlar ("Evren genişliyor" ← Hubble verisi). Yeterli kanıt bağlanınca Motor o konuda konuşmaya başlar ve yeni diyalog/kapı açılır; çelişen kanıt bağlanırsa Motor "çelişki var" der ve ikisini de askıya alır. Eğlencesi: diyalog ağacını oyuncu inşa eder; makine gerçekten öğreniyor hissi verir.
**Tema bağı:** Dürüst makinenin bilgisi ancak oyuncunun getirdiği kanıt kadardır; uydurmanın alternatifi somutlaşır.
**Maliyet:** Orta — iddia/kanıt JSON grafiği (30-40 düğüm), bağlama arayüzü, Motor diyaloglarına "bilinen iddia" koşulu.
**Bağımlılık/risk:** Bilimsel iddiaların kanıt zincirleri gerçekle tutarlı yazılmalı; yanlış bir zincir oyunun "gerçek bilim" sözünü bozar.

## 9. Yankı Taşları: Sessiz Sosyal Katman
**Döngü:** Oyuncu sisin bir noktasına "yankı taşı" bırakır; mesaj 60-80 sabit kelime karosundan 3 karoyla kurulur ("dikkat / sis / aşağıda", "Lale / burada / konuştu"). Diğer oyuncular aynı koordinatta taşı bulur, dokununca Motor'un sesiyle okunur, "doğru çıktı" oyu verebilir; en çok oylanan taşlar kalıcılaşır. Eğlencesi: Dark Souls mesajlarının sıcaklığı, serbest metin olmadan; yalnız oynanan oyun sessizce kalabalıklaşır.
**Tema bağı:** Başka oyuncuların hatırladıkları sisin içinde ize dönüşür; hatırlama ortaklaşır.
**Maliyet:** Orta — artifact db'ye koordinat + 3 karo + oy kaydı, yakınlık sorgusu, karo seçici arayüz.
**Bağımlılık/risk:** Artifact db yalnız artifact sürümünde var, çevrimdışı pakette özellik kaybolur; karo sözlüğü sabit olduğu için moderasyon gerekmez ama hacim sınırı (ör. boyut başına 200 taş) konmalı.

## 10. Geri Sarma Bedeli
**Döngü:** Oyuncu 8 saniye geri sarabilir (Bozulma saldırısından, düşüşten kaçmak için); her sarım Defter'den rastgele bir cümleyi siler ya da bir veri kartını sisler. Tehlikeyi geri almak ucuz, hatırlamak pahalıdır; oyuncu neyi feda ettiğini sarım sonrası görür. Eğlencesi: zaman manipülasyonunun sahiplik hissi (Prince of Persia) ama bedel hikâyenin kendisidir.
**Tema bağı:** Her geri alış bir unutuştur; sise karşı zaman kazanmak belleğe mal olur.
**Maliyet:** Orta — oyuncu/düşman transform ve durum halka tamponu (8 sn × 60 kare), geri oynatma, Defter silme kancası.
**Bağımlılık/risk:** Bozulma durum makinesi ve mini oyun zamanlayıcılarıyla senkron bozulabilir; ilk sürümde mini oyun içinde devre dışı bırakılmalı.

## 11. Lale'nin Bahçesi: Bellek Bahçesi
**Döngü:** Tesis'te bir toprak parçası; toplanan kesik kayıt parçaları "tohum" olur, oyuncu bunları 3×3 ızgaraya dizer ve yan yana gelen parçaların anlam bağına göre bitkiler farklı büyür (gerçek zamanla, saatler içinde). Çiçek açan bitki bir mektup satırı verir; komşuluk doğru kurulursa gizli dördüncü mektup oluşur. Eğlencesi: düzenleme/inşa döngüsü yavaş ve meditatif; oyuncu oyuna dönüp "ne açmış" diye bakar.
**Tema bağı:** Lale nörologdu, bahçe onun bellek kuramının somut hali; büyüyen her bitki bir hatırlamadır.
**Maliyet:** Orta — ızgara yerleştirme, komşuluk kuralları tablosu, prosedürel bitki geometrisi (L-system), localStorage zaman damgası.
**Bağımlılık/risk:** Kesik kayıt parçalarının anlamsal etiketlenmesi gerekir; gerçek zaman beklemesi sabırsız oyuncu için "hızlandır" seçeneğiyle dengelenmeli.

## 12. Saha Tasarımcısı: Kodla Paylaş
**Döngü:** Oyuncu sade bir editörde kendi Bozulma Sahası'nı kurar (sis yoğunluğu, 3-6 Bozulma, veri noktası yerleri, bir kayıt parçası), oynayıp test eder ve 40-60 karakterlik bir koda sıkıştırır. Kod URL'ye ya da panoya yazılır; başka oyuncu yapıştırınca saha prosedürel olarak aynı şekilde kurulur, en iyi süre küresel panoya girer. Eğlencesi: sunucusuz kullanıcı içeriği, Mario Maker'ın en küçük hali; tasarımcı ile oyuncu rolleri yer değiştirir.
**Tema bağı:** Oyuncu kendi sisini kurar ve başkasının sisine girer; hatırlamanın öznelliği oyun mekaniğine dönüşür.
**Maliyet:** Büyük — yerleştirme editörü, saha serileştirme/çözme, prosedürel kurulumun tüm düşman ve zone kodundan ayrıştırılması.
**Bağımlılık/risk:** Mevcut zone kodu elle yerleşimle yazılmışsa ayrıştırma yüksek maliyetli; kod formatı bir kez yayınlandıktan sonra geri uyumluluk sürdürülmeli.

---

### Hızlı özet tablosu

| # | Fikir | Döngü türü | Maliyet |
|---|-------|-----------|---------|
| 1 | Tahmin Defteri | Epistemik bahis | Küçük |
| 2 | Bakanlık Raporu | Sonuçlu seçim / itibar | Küçük |
| 3 | Hatırlama Provası | Bakım / aralıklı tekrar | Küçük-orta |
| 4 | Gerçek Zaman Vardiyası | Gerçek zaman | Küçük |
| 5 | Lale'ye Sesli Mesaj | Meta / kişisel iz | Küçük |
| 6 | Tanıklık Panosu | Çıkarım | Orta |
| 7 | Fener Ağı | İnşa / kalıcı dünya | Orta |
| 8 | Motor'u Öğretmek | Bilgi grafiği inşası | Orta |
| 9 | Yankı Taşları | Asenkron sosyal | Orta |
| 10 | Geri Sarma Bedeli | Zaman manipülasyonu | Orta |
| 11 | Lale'nin Bahçesi | Düzenleme / gerçek zaman büyüme | Orta |
| 12 | Saha Tasarımcısı | Kullanıcı içeriği / prosedürel | Büyük |
