# Varoluş Denklemi — Bellek Sarayı (gizli yedinci boyut), Ayna Bozulma, Mektuplar

Birimler önceki belgelerle aynı (yürüme 2.4, koşma 4.2, ada r 52, oynanabilir ±40; mevcut avcı `GP={speed:2.8,lunge:11,tele:.8,wait:2}`, fener itişi `dp<11 && cs>.8 → 3 sn`). Yeni alanlar: `S.letters{id:ts}`, `S.mirror{on,hits,resets}`, `S.bellek{unlocked:ts}`, `S.ending='saray'`; `GAME.mirror`, `GAME.letters`. Yeni prop alanı: `at:[x,z]` + `ring:R` (+`a0` derece) → `min/max` yerine odaya sabit halka yerleşimi: açı `i·360/n + a0`, radyal titreşim ±0.4 br, tohum `ground.seed+i`. `at` yoksa eski radyal yerleşim.

**Kilit:** boyut `hidden:true`; tesiste yedinci geçit `{id:'bellek',to:'bellek',name:'Bellek Sarayı',hex:'#ff9ec4',pos:[0,-30],hidden:true}` yalnızca `fragCount()≥6 && S.rec7` iken çizilir ve kalibre edilir (`S.bellek.unlocked=ts`, toast "Yedinci geçit: Bellek Sarayı"). Öncesinde aynı noktada 12 sn'de bir 0.2 sn pembe titreme (ipucu). NG+'da kilit devredilir (ilk turda açıldıysa açık kalır).

## 1. `world` bloğu (palet: sıcak amber #ffb070 / soluk pembe #ff9ec4 / lacivert #2a2448)

```js
{id:"bellek",name:"Bellek Sarayı",sub:"Lale'nin hipokampusunun içi",hex:"#ff9ec4",loc:"üç oda, bir koridor, bir gece",spawn:[0,26],hidden:true,
 world:{ground:{seed:71,c1:"#2a2448",c2:"#3a2e54",c3:"#5a3a4e",r:52,h:.5,ridge:2,c4:"#e8b6c0",rough:.4},
  atmo:{top:"#0a0a2e",hor:"#b36a4a",sun:"#ffb070"},
  light:{sky:"#ffb37a",ground:"#1a1230",hemi:.9,sun:"#ffd0a0",sunI:1.3,dir:[-40,22,30]},
  fog:{c:"#140e2a",n:36,f:150},rim:{color:"#ff9ec4",i:.9},grade:{sat:1.15,vig:.6,grain:.03,con:1.08},dust:"#ffc9d6",
  sky:{world:"bilinc",stage:"dmn",pos:[0,22,-120],scale:1.3},
  props:[
   // ada geneli
   {type:"pillar",n:16,hex:"#d9b38c",min:36,max:44,solid:.7,s0:.9,s1:1.2},
   {type:"shelf",n:10,hex:"#f3c870",min:10,max:34,s0:.8,s1:1.2},
   {type:"tree",n:8,hex:"#6a3a5a",min:30,max:42,solid:.6},
   {type:"grass",n:28,hex:"#ffb3c6",min:5,max:40},
   {type:"crystal",n:8,hex:"#ffc078",min:20,max:40,s0:.5,s1:.9},
   {type:"rock",n:6,hex:"#2a2448",min:38,max:44,solid:1.2},
   // oda 1 · Mutfak [28,0]
   {type:"pillar",n:8,at:[28,0],ring:6,hex:"#e0a070",solid:.7,s0:.8,s1:.9},
   {type:"crate",n:4,at:[28,0],ring:3,a0:45,hex:"#8a5a3a",solid:.9},
   {type:"shelf",n:3,at:[28,0],ring:4.5,a0:0,hex:"#f3c870",s0:.9,s1:1},
   {type:"console",n:1,at:[28,0],ring:2,a0:180,hex:"#ffb070",solid:1},
   // oda 2 · Hastane koridoru [-14,-24]
   {type:"pillar",n:10,at:[-14,-24],ring:6,hex:"#cfd4dc",solid:.7,s0:1,s1:1.15},
   {type:"crate",n:3,at:[-14,-24],ring:4,a0:30,hex:"#e6e9ee",solid:.9},
   {type:"cable",n:6,at:[-14,-24],ring:5,a0:15,s0:1,s1:1},
   {type:"console",n:2,at:[-14,-24],ring:3,a0:90,hex:"#7fd6ff",solid:1},
   // oda 3 · Kapadokya gecesi [-14,24]
   {type:"rock",n:8,at:[-14,24],ring:6,hex:"#c08a60",solid:1.1,s0:.8,s1:1.4},
   {type:"crystal",n:5,at:[-14,24],ring:4,a0:36,hex:"#ff9ec4",s0:.4,s1:.7},
   {type:"grass",n:10,at:[-14,24],ring:5,hex:"#ffd9a0"}]},
 zone:{pos:[0,-8],r:16,name:"Aynanın Odası",hunters:0,mirror:true}
```

Oda kimliği ışıkla pekişir: her oda merkezinde 1 PointLight (r 9, i 1.2): Mutfak #ffb070, Koridor #cfe6ff (0.9 Hz, ±0.15 titreyen floresan), Kapadokya #ff9ec4 + yerde 1.5 br yarıçaplı ateş parıltısı (crystal s0 .4). `zone.hunters:0` → `spawnHunters()` atlanır; `zone.mirror:true` → §3.

## 2. Yerleşim (oda merkezleri r 28, 0° / 120° / 240°)

| Öğe | id | Konum (x,z) | Not |
|---|---|---|---|
| Doğuş | — | [0,26] | ada standardı |
| Dönüş geçidi | exit | [0,34] | hex #f3c870 |
| Bozulma Sahası | zone | merkez [0,-8], r 16 | sızıntı halkası 20, uyarı 22 |
| Kesik parça | frag | [0,-8] | saha merkezi (motor varsayılanı) |
| Ayna Bozulma başlangıcı | mirror | [-10,-20] | saha içinde (merkeze 15.6) |
| Oda 1 Mutfak | — | [28,0] | pillar halkası r 6 |
| Oda 2 Hastane koridoru | — | [-14,-24] | saha merkezine 21.4 (uyarı halkası içinde, kasıtlı) |
| Oda 3 Kapadokya gecesi | — | [-14,24] | doğuşa 14.1 |
| Nokta 1 | yerhucre · "Yer Hücreleri" | [25,-3] | O'Keefe 1971; annesinin mutfağı |
| Nokta 2 | replay · "Gece Yeniden Oynatma" | [-18,-27] | Wilson–McNaughton 1994: uykuda 20× hızlı tekrar (aynanın bilimi) |
| Nokta 3 | hm · "H.M.'nin Boşluğu" | [-17,21] | Molaison 1953; yeni anı kaydedemeyen adam |
| Mektup 1 | m_mutfak | [31,3] | odaya 4.2 |
| Mektup 2 | m_koridor | [-10,-27] | saha merkezine 21.5 |
| Mektup 3 | m_gece | [-11,27] | doğuşa 11.0 |
| Figür 1 | milner · Brenda Milner (1918– · nöropsikolog) | [10,12] | wander 3, hex #f3c870 |
| Figür 2 | laleyanki · Lale (yankı) | [-6,12] | wander 0, hex #ff7cb9; her mektupta 1 satır açılır (0/3: yalnız bakar) |
| Kayıt | log · "Kayıt: MR Günü" | [22,-20] | `S.logs.bellek`; saha merkezine 25 |

Çakışma kuralı: etkileşimli öğeler arası ≥5 br (en yakın çift: Mektup 2 – Nokta 2, 8.0), hiçbiri saha içinde değil (parça hariç), hepsi r ≤ 32. Nav oku: mektup 3/3 değilse en yakın okunmamış mektup; 3/3 ise dönüş geçidi.

## 3. Ayna Bozulma (`GAME.mirror`)

```js
GAME.mirror={hz:10,len:150,start:[-10,-20],moveEps:.02,stillWin:.5,stillEps:.2,vmax:4.6,catchup:8.4,hitR:1.2,inv:1.5,push:2.5,repel:3,resetR:25,opacity:.55,trail:[.2,.12,.06]}
```

- **Etkinleşme:** kopya `start`'ta doğar, parıltılı ve hareketsiz. Oyuncu sahaya ilk girişte (`zoneActive`) `S.mirror.on=true` → kayıt başlar ve ada genelinde aktif kalır (geçitten çıkınca kapanır, tampon silinir). Sahada başka avcı yok.
- **Kayıt tamponu:** 100 ms tik (10 Hz). Tikte oyuncu yer değiştirmesi ≥ `moveEps` ise `{x,z,yaw}` örneği kuyruğa girer; durgun tiklerde örnek **girmez**. Kuyruk 150 örnek (= 15 sn hareket). Kuyruk dolunca her yeni örnek en eskisini düşürür ve kopya düşen örneğe 100 ms lineer enterpolasyonla gider. Sonuç: kopya tam olarak "15 sn hareket" geridedir; oyuncu durunca örnek gelmez, kopya durur.
- **Durma tanımı:** son 0.5 sn toplam yer değiştirme < 0.2 br → `still=true`; kopyanın animasyonu idle'a geçer (0.2 sn blend), nefes sesi susar. Diyalog/mektup/foto modu zaten durgun sayılır.
- **Hız sınırı:** kopya hızı ≤ `vmax` 4.6 (örnek aralığı >0.46 br ise gecikir, açık birikir). Birikim > 5 br → 0.5 sn, `catchup` 8.4 br/sn ile yetişir; sırasında 0.3 sn beyaz-pembe parıltı (sıçrama okunur).
- **Dolum süresi:** kuyruk 150'ye ulaşmadan kopya `start`'ta bekler. Yani ilk 15 sn hareket güvenli; HUD'da sahaya girişte 1 satır: "Ayna seni kaydediyor." (3 sn).
- **Temas:** mesafe ≤ 1.2 → vuruş: `S.integ−1`, dokunulmazlık 1.5 sn, oyuncu kopyadan 2.5 br itilir (0.3 sn), sarsıntı 0.4 / 0.3 sn, kumanda 120 ms 0.6. Kopya sıfırlanmaz, tekrar sürer. Bütünlük **3 segment** (`integMax` bu boyutta 3'e kırpılır, yörünge bonusu uygulanmaz). 0 → 1.2 sn yakalanma, 0.4 sn siyah; doğuşa dönüş, tampon boş, kopya `start`'ta, `S.caught++`, `S.mirror.resets++`; parça alındıysa korunur.
- **Sis Feneri:** F basılı, kopya ≤ 11 br ve koni içinde (`cs>.8`) → 3 sn donma: gelen örnekler düşer (kopya "o parçayı unutur"), görsel opaklık .55→.2, 3 sn sonunda kalan açık `catchup` kuralıyla kapanır. Fener deposu normal tüketir; donmadayken tekrar fener süreyi uzatmaz (1 sn bekleme).
- **Kaçış:** oyuncu–kopya mesafesi > 25 br → kopya 0.5 sn solar, kuyruk silinir, `start`'a döner, yeniden 150 örnek bekler (`S.mirror.resets++`). Koşarak düz 6 sn yeterli (4.2×6=25.2).
- **Görsel/ses:** Arel mesh'i, `scale.x=−1` (aynalı), tek renk #ff7cb9, opaklık .55, lacivert rim; 0.1 sn aralıkla 3 artık görüntü (.2/.12/.06). Yürüyüş animasyonu örnek hızından. Ses: oyuncunun adım sesi tersten, −10 dB, yöne göre pan; ≤ 6 br'de kalp vuruşu 100 bpm, ≤ 3 br 130 bpm. Hareket azaltma: artık görüntü yok, parıltı yok.
- **Kayıt / NG+:** `S.mirror={on,hits,resets}` kalıcı değil (boyut çıkışında sıfır). NG+: `len:120` (12 sn), `hitR:1.4`, `repel:2`.
- **Öğretilen davranış:** okumak için dur (kopya durur), parçayı almak için sahaya git-dön (15 sn tampon → gidiş-dönüş yolu üst üste gelmez; yolu çeşitle), Fener acil çıkış.

## 4. Mektuplar (`GAME.letters`)

- **Nesne:** 0.5×0.35×0.04 br kutu (zarf), emissive #ff7cb9 (0.8), yerden 0.9 br, ±0.08 br / 0.8 Hz salınım, 20°/sn dönüş; PointLight #ff9ec4 i .6 r 5. Etkileşim r 2.2; HUD "E · Mektup". Okunduktan sonra kalır: opaklık .4, ışık .15, etiket "okundu".
- **Okuma:** E → diyalog paneli, `who:'f'` Lale sesi (`voices.lale`), 4 satır (~25 sn), devam E. Bitince `S.letters[id]=ts`, toast "Mektup n/3", HUD istatistik satırına ` · mektup n/3` eklenir. Okuma sırasında oyuncu durgundur → kopya durur; panel kapanınca 1 sn ek dokunulmazlık (ayna 1.2 br içindeyse geri itilir, vuruş yok).

| id | Başlık | Oda | İçerik (hikâye ajanına özet, ≤4 satır) |
|---|---|---|---|
| m_mutfak | "Annemin Mutfağı" | Mutfak | Kokunun hipokampusa en kısa yolu; sekiz yaşında Arel sandalyede; "seni ilk orada kaydettim" |
| m_koridor | "Koridor, Gece 3" | Hastane | Son haftanın koridoru; floresan; Sema'ya verilen talimat; "görülmek istemedim, kaydedilmek istedim" |
| m_gece | "Kapadokya, Perseidler" | Kapadokya gecesi | Motor fikrinin doğduğu gece; 400 metre altı seçimi; "beni ben yapan şey nereye gider" sorusunun ilk hali |

- **Günlük "Mektuplar" sekmesi:** üstte "n/3"; 3 kart (mobil 1 sütun), kartta oda ikonu (24 px, pembe), başlık, boyut-içi tarih, tam metin; okunmamış kart %30 opak + "???". Tekrar dinle düğmesi (TTS). Sekme kilit açılana kadar günlükte görünmez.
- **3/3 ödülü:** toast "Sarayın Kapısı açıldı" (gizli-başarım sesi, üçüncü nota E6); Lale yankısı 3. satırını söyler; Çekirdek totemine **4. seçenek** `{t:"Sarayın kapısını aç. Lale'nin belleğinde kal.", req:'letters3'}` eklenir (3/3 değilse seçenek çizilmez). Sonuç: `S.ending='saray'`, `endings.saray={title:"Saray"}`: Arel Motor'u kapatmaz, açmaz; Bellek Sarayı'nı tek oda olarak kilitler ve dışarıdan yalnız oraya girer; tanıklar gider, Mira raporu "tamamlanmadı" yazar. Sonlar paneli 4 kart; başarım `four_endings` "Dört Son" (gizli, `endings.length==4`, hikâye). `three_endings` değişmez.

## 5. Kabul kriterleri

1. `fragCount()<6 || !S.rec7` iken tesiste [0,-30]'da geçit yoktur (yalnız 12 sn'de bir 0.2 sn pembe titreme); koşul sağlanınca geçit çizilir, kalibre edilir ve Bellek Sarayı'na [0,26]'da doğulur; dönüş geçidi [0,34]'tedir.
2. Sahaya girmeden önce kopya [-10,-20]'de kıpırdamaz; girişten sonra 15 sn boyunca hareket edip duran oyuncunun kopyası, oyuncu durduktan en geç 0.2 sn sonra durur ve oyuncunun tam 15 sn önceki yolunu ±0.3 br sapmayla izler.
3. Oyuncu sahada 3 sn durur, sonra 10 sn koşarsa kopya o 3 sn boyunca hiç ilerlemez (örnek sayısı artmaz); kopya oyuncuya 1.2 br'ye girince bütünlük 3→2, 1.5 sn içinde ikinci vuruş olmaz, oyuncu 2.5 br itilir.
4. Fener koni içinde kopyayı 3 sn dondurur; donma bitince kopya en çok 0.5 sn'de ve 8.4 br/sn'yi aşmadan yoluna döner. Düz koşuyla kopya 25 br'den uzaklaşınca 0.5 sn'de solar ve [-10,-20]'de bekler; `S.mirror.resets` 1 artar.
5. Üç mektup [31,3], [-10,-27], [-11,27]'de E ile Lale sesiyle okunur; her okumada HUD "mektup n/3" artar, günlük "Mektuplar" sekmesinde kart dolar; okuma sırasında kopya durur ve okuma bitince 1 sn vuruş olmaz.
6. Mektup 3/3 iken Çekirdek toteminde 4. seçenek görünür ve seçilince `S.ending='saray'`, sonlar paneli 4 kart gösterir; 2/3 iken seçenek çizilmez ve totem 3 seçeneklidir. Tüm oda prop'ları (`at/ring`) kendi merkezine ±0.4 br toleransla r 6 (pillar) halkasında doğar; hiçbir prop doğuş, geçit, nokta, mektup, kayıt ve figür konumlarına 2 br'den yakın değildir (çakışırsa 0.5 br adımla dışa itilir).
