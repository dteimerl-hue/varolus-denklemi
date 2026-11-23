# Doğal Mg/Ca karbonat mineralleri (huntit–hidromanyezit, dolomit) üzerine deneysel makaleler

> **ÖNEMLİ ORTAM KISITI (önce okuyun):** Bu oturumda ağ erişimi kısıtlıydı. `curl` ve WebFetch ile şu alan adlarının tamamı reddedildi (proxy 403 / ENOTFOUND): `api.crossref.org`, `doi.org`, `www.mdpi.com`, `pmc.ncbi.nlm.nih.gov`, `www.ncbi.nlm.nih.gov`, `europepmc.org`, `dergipark.org.tr`, `pdfs.semanticscholar.org`, `en.wikipedia.org` ve denenen diğer tüm yayıncı siteleri. Yalnızca WebSearch (arama motoru özetleri) çalıştı.
> Sonuçlar:
> 1. **Hiçbir PDF indirilemedi** — `pdfs/` klasörü boş.
> 2. **Crossref/doi.org doğrulaması yapılamadı** — bibliyografik veriler yalnızca arama sonuçlarından (PubMed, MDPI, doi.org başlıkları) alındı.
> 3. **Makalelerin tam metni okunamadı** — özetler kelimesi kelimesine alınamadı; aşağıdaki sayısal sonuçlar yalnızca arama özetlerinde geçen parçalardır.
> Bu notlar tek başına sunum yazmaya **yetmez**; ağ izni verildikten sonra (en az `www.mdpi.com`, `pmc.ncbi.nlm.nih.gov`, `api.crossref.org`, `doi.org`) tam metinlerin okunması gerekir. Aşağıda "Gaps" başlıkları eksikleri tek tek listeler.

Seçilen 2 makale:
- **Makale 1 (huntit–hidromanyezit, alev geciktirici dolgu):** Yılmaz Atay ve ark., *Materials* 2025, 18(11), 2652.
- **Makale 2 (dolomit, kalsinasyon + CO2 tutma):** Alalade ve ark., *C – Journal of Carbon Research* 2025, 11(2), 37.

---

## Soru 1 — Tam bibliyografik veri, DOI doğrulaması, APA 7 kaynakça

### Takeaway
İki makalenin başlık, dergi, cilt/sayı/makale numarası ve DOI bilgileri arama sonuçlarında (PubMed, MDPI, doi.org başlıkları) tutarlı biçimde görünüyor; ancak Crossref API'ye erişilemediği için resmî doğrulama YAPILAMADI ve yazar sırası/yazım biçimi son kez kontrol edilmelidir.

### Cited Findings
**Makale 1**
- Başlık: "Novel Flame-Retardant Wood-Polymer Composites by Using Inorganic Mineral Huntite and Hydromagnesite: An Aspect of Application in Electrical Engineering" — [doi.org](https://doi.org/10.3390/ma18112652)
- Dergi/cilt/sayı/makale no: *Materials* 2025, 18(11), 2652; DOI 10.3390/ma18112652 (arama özeti) — [MDPI](https://www.mdpi.com/1996-1944/18/11/2652)
- Yazarlar (arama özetine göre): Gül Yılmaz Atay, Joanna L. Wilk-Jakubowski, Volodymyr Loboichenko; PMID 40508650, PMCID PMC12156906 — [PubMed](https://pubmed.ncbi.nlm.nih.gov/40508650/)
- Tarihler (arama özetine göre): gönderim 26 Mart 2025, revizyon 16 Mayıs 2025, kabul 20 Mayıs 2025, yayın 5 Haziran 2025 — [PubMed](https://pubmed.ncbi.nlm.nih.gov/40508650/)
- APA 7 (yazar sırası Crossref'ten doğrulanamadı):
  Yılmaz Atay, G., Wilk-Jakubowski, J. L., & Loboichenko, V. (2025). Novel flame-retardant wood-polymer composites by using inorganic mineral huntite and hydromagnesite: An aspect of application in electrical engineering. *Materials, 18*(11), Article 2652. https://doi.org/10.3390/ma18112652

**Makale 2**
- Başlık: "Moderate-Temperature Carbon Capture Using Thermally Pre-Treated Dolomite: A Novel Approach" — [doi.org](https://doi.org/10.3390/c11020037)
- Dergi/cilt/sayı/makale no: *C* (Journal of Carbon Research) 2025, 11(2), 37; DOI 10.3390/c11020037; yayın tarihi 5 Haziran 2025 — [MDPI](https://www.mdpi.com/2311-5629/11/2/37)
- Yazarlar (arama özetinde verilen atıf biçimi): Alalade, I.G.; Morales-Mendoza, J.E.; Jasso-Salcedo, A.B.; Domínguez-Arvizu, J.L.; Hernández-Majalca, B.C.; Salami, H.A.; Bueno-Escobedo, J.L.; Ibarra-Rodriguez, L.I.; López-Ortiz, A.; Collins-Martínez, V.H. — [MDPI](https://www.mdpi.com/2311-5629/11/2/37)
- Yazarların kurumu: Centro de Investigación en Materiales Avanzados (CIMAV), Meksika (arama özeti) — [MDPI](https://www.mdpi.com/2311-5629/11/2/37)
- İlk yazarın açık adı: Iyiade Gbolahan Alalade; sorumlu grup: Virginia H. Collins-Martínez — [SciProfiles](https://sciprofiles.com/profile/4419406); [SciProfiles](https://sciprofiles.com/profile/1252644)
- APA 7 (Crossref'ten doğrulanamadı):
  Alalade, I. G., Morales-Mendoza, J. E., Jasso-Salcedo, A. B., Domínguez-Arvizu, J. L., Hernández-Majalca, B. C., Salami, H. A., Bueno-Escobedo, J. L., Ibarra-Rodriguez, L. I., López-Ortiz, A., & Collins-Martínez, V. H. (2025). Moderate-temperature carbon capture using thermally pre-treated dolomite: A novel approach. *C, 11*(2), Article 37. https://doi.org/10.3390/c11020037

### Inferences
- Her iki DOI de arama motorunda doi.org adresi olarak doğru başlıkla listelendiği için DOI'lerin çözümlendiği büyük olasılıkla doğrudur; ancak bu, istenen Crossref doğrulamasının yerini tutmaz.
- MDPI dergilerinde sayfa aralığı yoktur, makale numarası kullanılır (2652 ve 37); APA 7'de "Article 2652" biçimi uygundur.

### Gaps
- Crossref API (`api.crossref.org`) ve `doi.org` bu ortamdan erişilemedi; DOI çözümlemesi ve metadata resmî olarak DOĞRULANAMADI.
- Makale 1'de yazar sırası ve ikinci yazarın adının tam yazımı (Joanna L. / Jacek Łukasz Wilk-Jakubowski?) doğrulanamadı — arama özeti "Joanna L." veriyor; makalenin ilk sayfasından kontrol edilmeli.
- Makale 2'de yazarların tam adları (ilk yazar dışında) ve bazı soyadlardaki aksanlar (ör. Ibarra-Rodríguez) doğrulanamadı.

---

## Soru 2 — Açık erişim durumu, PDF bağlantısı, indirme

### Takeaway
İki makale de MDPI dergisinde yayımlanmış olup açık erişimli görünüyor, fakat bu ortamdan hiçbir PDF İNDİRİLEMEDİ (tüm yayıncı/arşiv alan adları ağ politikası tarafından engelli); `pdfs/` klasörü boştur.

### Cited Findings
- Makale 1 MDPI'de ve PubMed Central'da (PMC12156906) tam metin olarak yer alıyor — [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12156906/); [MDPI](https://www.mdpi.com/1996-1944/18/11/2652)
- Makale 1 için Semantic Scholar'da PDF kopyası listeleniyor — [Semantic Scholar PDF](https://pdfs.semanticscholar.org/52c4/987f37d787e9276c298f128f04db67a80b35.pdf)
- Makale 2 MDPI'de yayımlanmış; hakem raporları sayfası da açık — [MDPI](https://www.mdpi.com/2311-5629/11/2/37); [MDPI review report](https://www.mdpi.com/2311-5629/11/2/37/review_report)

### Inferences
- MDPI'nin standart PDF adres kalıbına göre beklenen doğrudan PDF adresleri (DENENEMEDİ, tahmini kalıp): `https://www.mdpi.com/1996-1944/18/11/2652/pdf` ve `https://www.mdpi.com/2311-5629/11/2/37/pdf`.
- MDPI makaleleri normalde CC BY 4.0 lisansıyla yayımlanır; bu iki makale için lisans metni sayfadan okunamadığı için kesin lisans doğrulanmadı.
- İndirme mümkün olduğunda önerilen dosya adları: `pdfs/karbonat_1_huntit_hidromanyezit.pdf` ve `pdfs/karbonat_2_dolomit.pdf`.

### Gaps
- **PDF indirme başarısız.** `curl` ile `www.mdpi.com`, `pmc.ncbi.nlm.nih.gov`, `europepmc.org`, `doi.org`, `dergipark.org.tr`, `zenodo.org`, `core.ac.uk`, `web.archive.org` vb. hepsi proxy tarafından reddedildi (yalnızca github.com / pypi.org erişilebilir). Ağ ayarlarında bu alan adlarına izin verilmesi gerekir.
- Lisans (CC BY 4.0) sayfadan doğrulanamadı.
- Alternatif aday olarak incelenen DergiPark makalesi (Aras, Ç., Demirata Öztürk, B., Sözgen Başkan, K. (2022). Enrichment of Magnesite and Usage to Obtain Magnesium Fluoride. *JOTCSA, 9*(2), 621–630, DOI 10.18596/jotcsa.1070017 — [DergiPark](https://dergipark.org.tr/en/pub/jotcsa/article/1070017)) de aynı nedenle indirilemedi; manyezit istenirse yedek adaydır.

---

## Soru 3 — Mineraller: formül, yapı, özellikler, yataklar, kullanım alanları

### Takeaway
Huntit (Mg3Ca(CO3)4) ve hidromanyezit doğada karışım hâlinde bulunur, Türkiye'de Denizli yöresinden çıkarılır ve halojensiz alev geciktirici dolgu olarak ticari kullanılır; dolomit (CaMg(CO3)2) rombohedral (trigonal) bir karbonattır, sertliği 3,5–4, özgül ağırlığı ≈2,85'tir ve MgO/refrakter kaynağıdır.

### Cited Findings
**Huntit – hidromanyezit**
- Huntitin formülü Mg3Ca(CO3)4 (CaMg3(CO3)4); karbonat sınıfında, dolomit grubunda sayılır — [Wikipedia: Huntite](https://en.wikipedia.org/wiki/Huntite)
- Büyük huntit yatakları Türkiye ve Yunanistan'dadır ve alev geciktirici özelliği nedeniyle ticari olarak işletilir — [Wikipedia: Huntite](https://en.wikipedia.org/wiki/Huntite)
- Türkiye'de huntit, Denizli'den hidromanyezit ile doğal karışım hâlinde elde edilir — [PMC10387843](https://pmc.ncbi.nlm.nih.gov/articles/PMC10387843/)
- Alev geciktirici olarak kullanılacak huntitin %33–35 MgO, %15–17 CaO ve %45–50 kızdırma kaybı içermesi istenir — [ResearchGate: Enrichment of huntite ore](https://www.researchgate.net/publication/376202527_ENRICHMENT_OF_HUNTITE_ORE_BASED_ON_ITS_CHARACTERIZATION)
- Hidromanyezit formülü bir Türk çalışmasında Mg4(OH)2(CO3)3·3H2O olarak verilmiş; yaygın mineralojik formül ise Mg5(CO3)4(OH)2·4H2O'dur (kaynaklar arasında yazım farkı var) — [ResearchGate](https://www.researchgate.net/publication/260342950_Preparation_and_Characterization_of_PolyanilineTurkish_Huntite-Hydromagnesite_Composites); [Wikipedia: Hydromagnesite](https://en.wikipedia.org/wiki/Hydromagnesite)
- EVA içinde huntit/hidromanyezit, benzer dolgu oranında Al(OH)3'ten daha yüksek oksijen indeksi vermiştir (%40'a karşı %35) — [ResearchGate: fire retardant effects of huntite](https://www.researchgate.net/publication/256969521_The_fire_retardant_effects_of_huntite_in_natural_mixtures_with_hydromagnesite)
- HH; düşük maliyetli, halojensiz, düşük duman ve asit gazı salımlı bir alev geciktirici olarak tanımlanır — [PMC12156906](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12156906/)

**Dolomit**
- Dolomit susuz bir karbonat mineralidir, ideal formülü CaMg(CO3)2 — [Wikipedia: Dolomite (mineral)](https://en.wikipedia.org/wiki/Dolomite_(mineral))
- Kristal sistemi rombohedral (trigonal); Mohs sertliği 3,5–4 — [Britannica](https://www.britannica.com/science/dolomite-mineral)
- Özgül ağırlık: 2,84–2,86 (Wikipedia), 2,85 ± 0,01 (Britannica) — [Wikipedia](https://en.wikipedia.org/wiki/Dolomite_(mineral)); [Britannica](https://www.britannica.com/science/dolomite-mineral)
- Dolomit, magnezyum metali ve refrakter tuğlaların bileşeni olan magnezya (MgO) kaynağıdır — [geology.com](https://geology.com/minerals/dolomite.shtml)
- Refrakterlerin korunmasında kalsine, refrakter ham maddesi olarak ise sinter dolomit biçiminde kullanılır — [IspatGuru](https://www.ispatguru.com/dolomite-a-useful-mineral/)
- Dolomit yaklaşık 700 °C'de doğrudan MgO ve CaO'ya ayrışır; oluşan "dolomitik kalsit" kireçtaşından daha düşük sıcaklıkta dekarbonate olur (Valverde ve ark., PCCP 2015) — [RSC](https://pubs.rsc.org/en/content/articlelanding/2015/cp/c5cp05596b)
- Türkiye'de yaklaşık 16 milyar ton dolomit ve 110 milyon ton manyezit rezervi olduğu bildirilmiştir (JOTCSA 2022 makalesinin girişi) — [DergiPark](https://dergipark.org.tr/en/pub/jotcsa/article/1070017)

### Inferences
- HH'nin alev geciktirici etkisi, ısıyla endotermik bozunup su buharı ve CO2 salması ve geride MgO/CaO kalıntısı bırakmasına dayanır (ATH/MDH ile aynı mekanizma sınıfı); bu, yukarıdaki "halojensiz, düşük dumanlı" tanımıyla tutarlıdır.
- Dolomitin kalsinasyon ürünü CaO·MgO'dur; CaO CO2 tutan aktif fazdır, MgO ise sinterleşmeyi engelleyen inert iskelet görevi görür — Makale 2'nin "CaO–MgO fazları" bulgusuyla tutarlı.

### Gaps
- Aşağıdaki genel mineral verileri bu oturumda bir kaynaktan DOĞRULANAMADI (Wikipedia/mindat'a erişim yok); sunuma koymadan önce mindat.org veya Wikipedia'dan teyit edilmelidir. Hatırlanan (doğrulanmamış) değerler:
  - Huntit: trigonal sistem, beyaz renkli, çok ince taneli/toprağımsı, Mohs sertliği ≈1–2, yoğunluk ≈2,7 g/cm³; ≈450–800 °C aralığında CO2 vererek bozunur.
  - Hidromanyezit: monoklinik, beyaz/renksiz, sertlik ≈3,5, yoğunluk ≈2,2 g/cm³; ≈220–550 °C aralığında önce su, sonra CO2 vererek bozunur.
  - Dolomit: renk beyaz/gri/pembe, camsı–inci parlaklık, {10-11} mükemmel dilinim, soğuk seyreltik HCl'de zayıf köpürme; iki basamaklı bozunma (CO2 atmosferinde önce MgCO3 bileşeni, sonra CaCO3).
- Türkiye'deki huntit–hidromanyezit rezerv tonajı ve dolomit yataklarının il bazında dağılımı için güvenilir kaynak bulunamadı.

---

## Soru 4 — Çalışmalar: amaç, numune kaynağı, işlemler, karakterizasyon, sonuçlar

### Takeaway
Makale 1, PP matrisine MDF atığı ve huntit–hidromanyezit ekleyerek alev geciktirici ahşap-polimer kompozit üretmiş; HH yanmazlığı belirgin artırmış ama kırılganlığı artırıp mekanik dayanımı düşürmüştür. Makale 2, doğal dolomiti 900 °C'de havada kalsine edip 650 °C'de argonda ön işleme tabi tutarak 0,477 g CO2/g kapasiteli, 15 çevrim sonunda %84 kapasite koruyan bir sorbent elde etmiştir.

### Cited Findings
**Makale 1 (huntit–hidromanyezit, WPC)**
- Amaç: yanmazlık özelliğiyle bilinen huntit–hidromanyezit minerali kullanılarak alev geciktirici ahşap-polimer kompozit üretmek — [PMC12156906](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12156906/)
- Malzemeler/işlem: matris polipropilen; takviye MDF atığı ve huntit–hidromanyezit; karıştırma çift vidalı ekstrüderle yapılmış — [PMC12156906](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12156906/)
- Test numuneleri sıcak pres (compression molding) ile hazırlanmış — [doi.org](https://doi.org/10.3390/ma18112652)
- Yanma testi: UL 94 dikey yanma testi; anahtar kelimeler arasında mekanik özellikler ve elektrik mühendisliği var — [PubMed](https://pubmed.ncbi.nlm.nih.gov/40508650/)
- Bulgu: HH ilavesiyle kompozitler belirgin alev geciktiricilik kazanmıştır — [PMC12156906](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12156906/)
- Bulgu: HH ilavesi, kırılganlığı artırdığı için polimer-ahşap-mineral kompozitin mekanik dayanımını düşürmüştür — [doi.org](https://doi.org/10.3390/ma18112652)
- Bağlam (aynı grubun ilişkili çalışmaları, bu makalenin sonucu DEĞİL): PP'de %40 HH ile UL94 V0; %60 dolguda elastisite modülü 1215 → 3362 MPa — [SPE Polymers 2026](https://4spepublications.onlinelibrary.wiley.com/doi/10.1002/pls2.70036); [Vietnam J. Chem. 2024](https://onlinelibrary.wiley.com/doi/10.1002/vjch.202300157)

**Makale 2 (dolomit, CO2 tutma)**
- Amaç: bütünleşik karbon tutma ve dönüştürme (yüksek saflıkta hidrojen üretimi) için ucuz, ısıl kararlı, orta sıcaklıkta rejenere edilebilen CaO esaslı sorbent geliştirmek — [MDPI](https://www.mdpi.com/2311-5629/11/2/37)
- İşlemler: doğal dolomit kuvars fırında ortam havasında 900 °C'de kalsine edilmiş, ardından inert (argon) akışında 650 °C'de ısıl ön işlem (aktivasyon) uygulanmış — [ResearchGate](https://www.researchgate.net/publication/392454631_Moderate-Temperature_Carbon_Capture_Using_Thermally_Pre-Treated_Dolomite_A_Novel_Approach); [SciProfiles](https://sciprofiles.com/profile/4419406)
- Karakterizasyon: XRD, SEM-EDS, BET, TGA — [MDPI](https://mdpi.com/2311-5629/11/2/37)
- En iyi numune: 900 °C'de 60 dk kalsine edilip argonda aktive edilen "PCD60Act"; en yüksek CO2 tutma 0,477 g CO2/g sorbent — [doi.org](https://doi.org/10.3390/c11020037)
- Çevrim kararlılığı: %90 CO2 ile 650 °C'de 15 çevrim sonunda 0,38 g CO2/g sorbent; %84 kapasite korunumu — [doi.org](https://doi.org/10.3390/c11020037)
- XRD: 15 tutma–rejenerasyon çevriminden sonra ana CaO–MgO fazları tamamen rejenere olmuş; 15 çevrim sonrası MgO kristalit boyutu 29 nm — [doi.org](https://doi.org/10.3390/c11020037)
- Açıklama: üstün sonuçlar, ısıl ön işlemler sırasında dolomitte oluşan kristal kusurlarına bağlanmış — [MDPI](https://www.mdpi.com/2311-5629/11/2/37)
- Sonuç: ısıl ön işlemli dolomit esaslı sorbent (PCD60Act), orta sıcaklıklarda verimli CO2 tutma için başarıyla geliştirilmiştir — [MDPI](https://www.mdpi.com/2311-5629/11/2/37)

### Inferences
- Makale 1'in başlığındaki "elektrik mühendisliği" vurgusu ve anahtar kelimeler, kompozitin kablo/elektrik ekipmanı gibi yangın güvenliği gerektiren uygulamalar için değerlendirildiğini düşündürür; elektriksel ölçüm yapılıp yapılmadığı doğrulanamadı.
- Makale 2'de 0,38/0,477 ≈ %80 eder; makalede bildirilen %84, muhtemelen çevrim koşullarındaki (ör. %90 CO2) ilk çevrim kapasitesine göre hesaplanmıştır — tam metinden kontrol edilmeli.
- "PCD60Act" adı muhtemelen "pre-calcined dolomite, 60 min, activated" kısaltmasıdır (çıkarım).

### Gaps
- **Makale 1:** HH'nin tedarikçisi/ocağı (Türkiye-Denizli olup olmadığı), kimyasal bileşimi ve tane boyutu; PP ve MDF atığı özellikleri; formülasyon tablosu (ağırlıkça % oranlar); ekstrüder ve pres parametreleri (sıcaklık, devir, basınç, süre); uygulanan mekanik test standartları ve sayısal değerler (çekme, eğilme, darbe, sertlik); UL 94 sınıfları (V-0/V-1/V-2) ve yanma süreleri; LOI, TGA, SEM yapılıp yapılmadığı — tam metne erişilemediği için BULUNAMADI.
- **Makale 2:** Dolomitin çıkarıldığı yer (muhtemelen Meksika — doğrulanmadı) ve kimyasal bileşimi; tane boyutu/öğütme; denenen diğer kalsinasyon süreleri ve numune kodları; gaz debileri, CO2 derişimleri, karbonatlaşma/rejenerasyon sıcaklık-süre programı; BET yüzey alanı ve gözenek verileri; CaO kristalit boyutları — BULUNAMADI.
- Her iki çalışmada da öğütme/eleme gibi ön hazırlık adımları doğrulanamadı.

---

## Soru 5 — Özet (verbatim) ve 3–5 önemli şekil/tablo

### Takeaway
Hiçbir makalenin özeti kelimesi kelimesine ALINAMADI ve şekil/tablo başlıkları görülemedi; yalnızca arama özetlerinde geçen tek cümlelik parçalar mevcut.

### Cited Findings
- Makale 1 özetinden arama sonucunda görünen parça: "In this study, a flame-retardant wood-polymer composite was produced using huntite-hydromagnesite mineral, recognized for its non-flammability properties." — [PMC12156906](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12156906/)
- Makale 1'den arama sonucunda görünen parça: "It was concluded that the composites gained significant flame retardancy with the addition of huntite hydromagnesite." — [PMC12156906](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12156906/)
- Makale 2'den arama sonucunda görünen parça: "The dolomite sample calcined at 900 °C for 60 min, and after being activated under an inert atmosphere (argon), labeled PCD60Act, exhibited the highest CO2 uptake of 0.477 gCO2/gsorbent." — [doi.org](https://doi.org/10.3390/c11020037)
- Makale 2'den arama sonucunda görünen parça: "These remarkable results are explained by the crystalline defects generated during the thermal pre-treatments of the dolomite." — [MDPI](https://www.mdpi.com/2311-5629/11/2/37)
- Makale 2'de bir XRD difraktogramı şekli vardır: 15 çevrim sonrası PCD60Act'in CaO–MgO fazlarının tamamen rejenere olduğunu gösterir — [doi.org](https://doi.org/10.3390/c11020037)

### Inferences
- Yukarıdaki cümleler arama motoru özetlerinden alınmıştır; kelimesi kelimesine doğruluğu ve özetin mi yoksa metnin başka bir bölümünün mü parçası olduğu kesin değildir. Sunumda "özet" olarak kullanılmamalı; özet doğrudan makalenin ilk sayfasından kopyalanmalıdır.

### Gaps
- Her iki makalenin tam özeti (verbatim) alınamadı — tam metin sayfalarına erişim engelli.
- Şekil ve tablo listesi/başlıkları (Makale 1: formülasyon tablosu, UL 94 tablosu, mekanik sonuç grafikleri, SEM görüntüleri; Makale 2: XRD desenleri, TGA tutma eğrileri, çevrim grafiği, SEM-EDS, BET tablosu gibi beklenenler) DOĞRULANAMADI; bunlar yalnızca beklenti olup makaleden teyit edilmelidir.
- İkinci slayt için gereken ilk sayfa görüntüsü üretilemedi (PDF yok).
