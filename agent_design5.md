# Varoluş Denklemi — Kumanda, Lip-sync, Yankı Dizisi, Günün Tohumu, Kayıp Sinyal

Birimler önceki belgelerle aynı (yürüme 2.4, koşma 4.2, boyut ölçeği ±40, Bozulma Sahası yarıçapı R; sızıntı halkası R+4, uyarı halkası R+6). Yeni alanlar: `S.input`, `S.lip`, `S.mini.yanki`, `S.fuelBonus`, `S.daily`, `S.dailyBest`, `S.dailyName`, `S.lost`, `S.rec8`; `GAME.pad`, `GAME.minigames.yanki`, `GAME.daily`, `GAME.lost`.

## 1. Kumanda (Gamepad API)

**Algılama:** `gamepadconnected` → `S.input.pad=index`; her karede `navigator.getGamepads()[index]` okunur (yalnızca `mapping==='standard'`; değilse kumanda yok sayılır, HUD'da 2 sn "Kumanda düzeni tanınmadı"). `gamepaddisconnected` → hareket vektörü 0, fener bırakılır, `S.input.mode='kb'`.

| Giriş | Standart indeks | Eylem | Not |
|---|---|---|---|
| Sol çubuk | axes 0/1 | yürü | radyal deadzone 0.18; `n=((m−0.18)/0.82)^1.5`, yön korunur |
| Sağ çubuk | axes 2/3 | kamera | yatay 160 °/s, dikey 100 °/s tam itişte; eğri `^2`; invert yok; pitch sınırı fare ile aynı |
| LT / RT | buttons 6/7 | koş | `value ≥ 0.5` → Shift basılı sayılır |
| A | 0 | etkileşim / devam | E ve diyalog "devam" ile aynı |
| B | 1 | kapat / geri | Esc ile aynı; panel yoksa hiçbir şey yapmaz |
| X | 2 | Sis Feneri (basılı) | F basılı ile aynı; bırakınca kapanır |
| Y | 3 | fotoğraf | foto moduna gir/çek (mevcut tuşla aynı) |
| Start | 9 | günlük | J |
| Back | 8 | ayarlar | ayar paneli aç/kapat |
| D-pad ↑/↓ | 12/13 | diyalog seçimi (1-2-3) ve menü satırı | seçili satır vurgulanır, A onaylar |
| D-pad ←/→ | 14/15 | günlük/ayar sekmesi değiştir | mini oyunda ton girişi (bkz. §3) |

- Düğme kenarı: `pressed && !prevPressed` → tek tetik (A/B/Y/Start/Back/D-pad); X ve LT/RT durum olarak okunur. D-pad basılı tutulursa 400 ms sonra 120 ms aralıkla tekrar eder.
- Yürüme hızı `n·2.4` (koşarken `n·4.2`); dokunmatik joystick ile aynı hız eğrisi. Çubuk tam itişte klavye ile aynı hız: oyuncu kumandayla daha yavaş ya da hızlı olmaz.
- **Giriş modu:** `S.input={mode:'kb'|'pad'|'touch', lastPad:ts}`. Deadzone üstü çubuk veya herhangi düğme → `lastPad=now`. `now−lastPad<3000` → `mode='pad'`; aksi halde son klavye/fare/dokunma olayına göre. HUD ipuçları (etkileşim "E", fener "F", günlük "J", öğretici metinleri) pad modunda rozete döner: 18 px daire, 11 px harf; A #93e3a0, B #E63946, X #7fd6ff, Y #f3c870, Start/Back gri #9a9ab0 "≡"/"⧉". Mod değişince ipucu metni 0.2 sn fade ile değişir.
- **Titreşim:** `gamepad.vibrationActuator?.playEffect('dual-rumble',{duration,strongMagnitude,weakMagnitude})`. Vuruş: 120 ms, 0.6/0.6. Parça: 60 ms, 0.3/0.3. Yakalanma: 300 ms, 0.8/0.4. Actuator yoksa sessizce atlanır. Ayarlar'da tek anahtar "Kumanda titreşimi" (varsayılan açık; `S.input.rumble`).
- **Erişilebilirlik:** hassasiyet/eğri ayarı yok; tek deadzone 0.18 sabit. Hareket azaltma modunda kamera hızı aynı kalır (kullanıcı eylemi), sarsıntı zaten kapalı.
- Mobil + kumanda birlikteyse pad modunda dokunmatik joystick gizlenir (düğmeler kalır).

**Veri:** `S.input={mode,lastPad,pad,rumble}` (kalıcı: yalnızca `rumble`). `GAME.pad={dead:0.18,curve:1.5,camH:160,camV:100,hint:3000,rumble:{hit:[120,.6],frag:[60,.3],caught:[300,.8]}}`.

**Kabul:** (1) Standart kumandada sol çubuğu 0.17 itmek Arel'i kıpırdatmaz, 0.19 kıpırdatır; tam itiş hızı WASD ile ±%2 aynı. (2) A'ya basınca Mira diyalogu açılır, B kapatır; D-pad ↓ ikinci seçeneği vurgular, A onaylar. (3) Bir düğmeye bastıktan 3.0 sn sonra HUD "E" harfine geri döner; 2.9 sn'de hâlâ "A" rozetidir. (4) Vuruş alınca 120 ms titreşim; actuator olmayan kumandada hata yok (konsol temiz). (5) Kumanda çıkarılınca koşu/fener anında bırakılır, oyun 1 kare bile takılmaz.

## 2. Konuşma baş animasyonu (lip-sync)

- **Kaynak:** `SpeechSynthesisUtterance.onboundary` (`event.name==='word'`). Her kelimede darbe `p0 = clamp(0.55 + 0.45·min(event.charLength||4, 8)/8, 0, 1)`; `S.lip.p` anlık değeri `p(t)=p0·max(0, 1−t/0.18)` (lineer sönüm 180 ms). Yeni kelime gelirse `p=max(p, p0)`. `onend`/`onerror` → 0.25 sn'de 0'a.
- **Baş bone (konuşan NPC):** çene = baş x ekseni, açı `4°·p` (aşağı). Yatay salınım `3°·s·sin(π·t/0.18)` ile sadece darbe süresince; `s` kelime başına işaret değiştirir (+1/−1) → sağ-sol dönüşümlü. Dinleyici NPC ve Arel'de uygulanmaz. Kol/beden/omuz sabit; boyun transformu baş bone'un üstünde kalır.
- **Hareket azaltma:** salınım ±1°, çene 0–2°.
- **Olay yoksa** (ses kapalı, `speechSynthesis` yok, Safari gibi `onboundary` ateşlemeyen motor: utterance başladıktan 500 ms sonra darbe gelmezse): diyalog paneli açıkken sabit nod `1°·sin(2π·2·t)` (2 Hz, x ekseni); hareket azaltmada 0.4°. Panel kapanınca 0.3 sn'de sıfıra.
- **Zamanlama:** darbe `requestAnimationFrame` içinde güncellenir, 30 fps altında da sönüm süre tabanlıdır (kare sayımı yok).
- **Veri:** `S.lip={p, s, lastWord:ts, who}` (kalıcı değil). `GAME.lip={decay:.18, jaw:4, sway:3, nodHz:2, nodDeg:1, rm:{jaw:2, sway:1, nodDeg:.4}}`.

**Kabul:** (1) Sesli diyalogda her kelimede çene 0→≤4° açılıp 180 ms'de kapanır; kelime arası boşlukta 0°. (2) Ardışık iki kelimede baş önce +, sonra − yöne döner (en fazla 3°). (3) Ses kapalıyken konuşan NPC 2 Hz, 1° nod yapar; kol pozisyonu kare karşılaştırmasında değişmez. (4) Hareket azaltma açıkken genlikler 1°/2°/0.4°. (5) `onboundary` olmayan tarayıcıda 500 ms sonra nod moduna düşer; konsolda hata yok.

## 3. Yankı Dizisi mini oyunu (Anlam / `sisifos` noktası)

**Tetik:** `anlam` boyutunda `sisifos` (16,−6) noktasının ikinci cümlesi dinlendikten sonra panel açılır ("Kaya her seferinde aynı yoldan iner; Motor da aynı diziyi çalar. Tekrar et."). Sonraki ziyaretlerde noktanın E ipucu "Yankı Dizisi" olur; kazanıldıysa panel yalnız skor gösterir.

**Tonlar:** 1=261.6 Hz, 2=329.6, 3=392.0, 4=523.3 (sine, attack 10 ms, release 60 ms, −10 dB). Tempo 480 ms/ton (başlangıçtan başlangıca), ton süresi 260 ms. Oyuncu girişinde aynı ton 260 ms çalar.

**Turlar:** tur r∈{1..4}, dizi uzunluğu `L=2+r` (3,4,5,6). Dizi her turda sıfırdan üretilir: rastgele, aynı ton en fazla 2 kez art arda. Girdi süresi `T=L×1.6 s` (4.8/6.4/8.0/9.6 s), çalma bitiminden 300 ms sonra başlar. 4. tur bitince kazanılır.

**Girdi:** klavye 1-4; ekran düğmeleri (4 daire, 56 px, mobil 64 px); kumanda D-pad ←=1, ↑=2, →=3, ↓=4. Çalma sırasında girdi yok sayılır (daireler kilitli, %50 opak).

**Hata:** `wrong` (dizideki beklenen tondan farklı ton) ve `timeout` (T doldu). `S.mini.yanki.err` oturum içi sayaç; hata → aynı tur yeni diziyle tekrar; 3. hatada tur 1'e dönüş, sayaç 0, bu deneme **kaydedilmez** (`fails` artmaz, günlüğe yazılmaz). B/Esc ile çıkış: ilerleme silinir, kayıt yok.

**Durum makinesi** (`S.mini.yanki.state`):

| Durum | Giriş eylemi | Çıkış koşulu → sonraki |
|---|---|---|
| `intro` | başlık + `GAME.minigames.yanki.intro`, "Başla (A/E)" | A/E/tık → `play` (r=1, err=0); B/Esc → kapat |
| `play` | diziyi çal (L×480 ms), aktif daire parlar | son ton bitti +300 ms → `input` |
| `input` | zamanlayıcı T başlar, idx=0, çubuk azalır | her ton girişi → `judge`; T doldu → `fail(timeout)` |
| `judge` | anlık: `tone==seq[idx]` ? | eşit ve `idx+1<L` → idx++, `input` (zamanlayıcı **devam**); eşit ve `idx+1==L` → `next`; farklı → `fail(wrong)` |
| `next` | doğru daire 300 ms yeşil, kısa arpej | r<4 → 600 ms sonra `play` (r++); r==4 → `win` |
| `fail` | daire 400 ms kırmızı, `fail[type]` metni 1.4 s, err++ | err<3 → `play` (aynı r); err==3 → `play` (r=1, err=0) |
| `win` | girişim deseni 2.0 s tam parlaklık, `win` metni | 2.0 s → ödül yaz, kapat |

**Ödül (bir kez):** `S.fuelBonus += 1` (Sis Feneri deposu +1 sn kalıcı; depo = 12 + fuelBonus + görev bonusları; anında tam dolum), `S.mini.yanki.done=true`, başarım `echo_four` "Dört Yankı" (bilim, atom; koşul `mini.yanki.done`). Gizli başarım `clean_echo` "Temiz Yankı": kazanılan koşuda err==0 (`mini.yanki.clean`). Sema repliği 1.

**Görsel:** 4 daire pusula konumunda (yarıçap 90 px, mobil 72), tonun rengi: 1 #ff9152, 2 #93e3a0, 3 #7fd6ff, 4 #c9abff. Merkezde 160 px girişim deseni: iki kaynak, `I=cos²(π·d·sinθ/λ)`, `λ ∝ 1/f` aktif tona göre; sessizde %30 parlaklık. Üstte "Tur r/4", altta süre çubuğu 220×4 px (son 2 sn #E63946).

**Veri:** `S.mini.yanki={done,clean,best:r,state,r,seq,idx,err,t0}` (kalıcı: done, clean, best). `GAME.minigames.yanki={title,intro,win,fail:{wrong,timeout},freq:[261.6,329.6,392.0,523.3],tempo:480,tone:260,perItem:1.6,rounds:4,maxErr:3}`.

**Kabul:** (1) Tur 1 dizisi 3 ton, 4. tur 6 ton; girdi süresi 4.8→9.6 s. (2) 2. turda yanlış ton: kırmızı + "yanlış ton" metni, 1.4 s sonra 2. tur yeni diziyle; 3. hatada tur 1'e dönüş ve `fails` değişmez. (3) Süre dolunca `timeout` hatası; süre doğru ton girildiğinde sıfırlanmaz. (4) Kazanınca fener deposu 1 sn artar, tekrar oynayınca artmaz; `echo_four` toast'ı çıkar. (5) D-pad ← ile 1, ↓ ile 4 girilir; çalma sırasında basış yok sayılır.

## 4. Günün Tohumu (günlük meydan okuma)

**Tohum:** `day = Number(new Date().toISOString().slice(0,10).replace(/-/g,''))` (UTC; ör. 20261016). `realm = GAME.daily.realms[day % 6]`, liste `[baslangic,kuantum,gezegen,bilinc,anlam,yuva]`. `mod = GAME.daily.mods[Math.floor(day/7) % 5]`, liste `[karanlik,tekcan,kalin,sessiz,hizli]`. (20261016 → baslangic / karanlik.) Tüm oyuncular aynı gün aynı tohumu görür.

| Mod | Etki |
|---|---|
| karanlik | Sis Feneri devre dışı (F/X yok sayılır, HUD fener ögesi gizli) |
| tekcan | bütünlük 1 segment |
| kalin | sis yoğunluğu ×1.6, fog uzak mesafe ×0.6, nokta ışık sütunları %50 |
| sessiz | HUD uyarıları kapalı: saha kenarı, vuruş metni, nav oku; kalp sesi kalır |
| hizli | avcı yürüme/hamle hızı ×1.3, telegraph 0.6→0.5 sn |

**Başlangıç:** tesiste telsiz (`E`) menüsüne "Günün Tohumu" satırı (ilk parçadan sonra açılır: `frags.length ≥ 1`). Satır önizleme: boyut adı, mod adı, bugünkü en iyi süre (`S.dailyBest`), "Başla". Onay → 0.6 sn siyah, oyuncu boyutun `spawn`ına ışınlanır, 1.0 sn sonra kronometre `t0=performance.now()` başlar; HUD üst-orta mono 22 px "TOHUM · 00:00.0" + mod rozeti.
**Bitiş:** parça alınınca (`ZT.fragment`) kronometre durur, `ms=round(now−t0)`; 1.2 sn sonuç kartı (süre, bugünkü en iyi, sıra) → 3 sn sonra tesise dönüş (telsiz önünde).
**Kaçış/ölüm:** çıkış geçidi, Esc→"Vazgeç" ya da `daily.integ==0` → süre iptal, kayıt yok, 0.4 sn siyah, tesise dönüş; sınırsız tekrar.

**Ayrım kuralları (NG+ ve normal kaydı korumak için):**
- `S.daily={on:true, realm, mod, t0, day, integ}`; kalıcı kayda (`save()`) **yazılmaz**; sayfa yenilenirse koşu düşer.
- `daily.on` iken: `S.frags/facts/logs/hist/path/quests/wxLog/shots` hiçbir yazma almaz; parça envantere eklenmez; `S.integ` okunmaz/yazılmaz, hasar `daily.integ`'i düşürür (başlangıç: tekcan ise 1, değilse `S.integMax`); `playT` artmaz; başarım denetimi yalnız `daily_*` başarımlarına bakar.
- Boyut düzeni: `S.ngp`'den bağımsız **normal tur** yerleşimi (avcı sayısı, saha yarıçapı, parça konumu), yankı noktaları/kayıt/figürler/yol arkadaşı/atmosfer olayı/öğretici/halüsinasyon kapalı; sadece saha, avcılar ve parça aktif.
- Tesise dönüşte `S.daily={on:false}`; bütünlük, fener deposu ve konum koşu öncesi değerlerine döner (zaten dokunulmamıştır).

**Kayıt (db):** `daily/{self}` tek doküman: `{day, realm, mod, ms, name?}`. Yazma koşulu: `doc yok || doc.day !== day || ms < doc.ms`; dünkü doküman üzerine yazılır (kişi başı o gün için 1 doküman). `S.dailyBest={day,ms}` yerelde de tutulur (çevrimdışı HUD için); `S.dailyName` ≤12 karakter, isteğe bağlı, telsiz menüsünden girilir, dokümana `name` olarak gider. Bağlantı yoksa yerel en iyi gösterilir, pano "çevrimdışı".
**Pano:** günlük "Günlük" sekmesi: üstte tohum satırı ("16 Eki · Başlangıç · Karanlık"); `daily` koleksiyonu çekilir (≤200), `doc.day===day` filtrelenir, `ms` artan; ilk 10 satır (sıra, ad ya da "Anonim", `mm:ss.t`); altında "Sıran: k/N" (k = `ms<own` sayısı+1). Farklı günlerin dokümanları listelenmez. 30 sn önbellek; sekme açılınca yenilenir.

**Başarımlar:** `daily_first` "İlk Tohum" (bir koşu tamamlandı), gizli `daily_top` "Günün Birincisi" (pano 1. sıra).
**Veri:** `GAME.daily={realms:[...6], mods:{karanlik:{lantern:0},tekcan:{integ:1},kalin:{fog:1.6,far:.6},sessiz:{hud:0},hizli:{enemy:1.3}}, startDelay:1000}`.

**Kabul:** (1) Aynı UTC günde iki tarayıcı aynı boyut+modu gösterir; 20261016 → Başlangıç/Karanlık. (2) Koşu sırasında parça alınca `S.frags.length` değişmez, bütünlük segmenti koşu öncesiyle aynı; tesise dönülür. (3) İkinci koşuda daha kötü süre dokümanı değiştirmez; daha iyi süre değiştirir; ertesi gün ilk koşu dokümanı tamamen yeniler. (4) Pano yalnız bugünün dokümanlarını gösterir; oyuncunun sırası 10 dışındaysa "Sıran: 23/41" satırı görünür. (5) Sayfa yenilenince `S.daily.on=false`, normal kayıt bozulmamış (facts/frags/integ aynı). (6) tekcan modunda ilk vuruş koşuyu bitirir; karanlik'te X/F fener açmaz.

## 5. Kayıp Sinyal yan görevi

**Açılış:** telsiz menüsünde "Kayıp Sinyal" (koşul: `logs.length ≥ 3`). Seçilince Mira'nın 2 satırlık kaydı: Lale'nin taşıyıcı frekansında üç kayıp yankı var; "işaretle, geri dinleyeyim". `S.lost.on=true`. Sinyal ve nesneler yalnız `lost.on` iken var olur; daha önce boyutlarda görünmez.

**Yankı noktaları (yeni nesne, mevcut nokta değil):** 0.6 br yüksekliğinde ince anten direği, tepesinde 0.8 Hz yanıp sönen boyut rengi LED; ışık sütunu yok, haritada işaret yok, collider yok. Konum kuralı: her iki saha merkezine ≥ R+12, tüm nokta/figür/kayıtlara ≥ 10, orijine ≤ 36.

| Boyut | Konum | Sahalar | En yakın saha uzaklığı |
|---|---|---|---|
| baslangic | (30, 26) | (−30,24), (28,−26) | 52 |
| kuantum | (32, −26) | (−36,−16), (30,24) | 50 |
| gezegen | (−30, 26) | (32,26), (−30,−24) | 50 |

**Sinyal HUD** (sağ alt, 5 çubuk 6 px genişlik, yükseklik 8→20 px, boyut rengi; `d` = oyuncu-nokta yatay uzaklığı): d≤6→5, ≤12→4, ≤20→3, ≤30→2, ≤40→1, >40→HUD gizli, ses yok. Bip: 880 Hz sine, 40 ms, −18 dB; aralık `lerp(1.2, 0.25, (40−clamp(d,6,40))/34)` s. Zaten işaretli boyutta ve tesiste HUD yok. Diyalog/foto modunda bip susar. `sessiz`/Tohum modunda görev askıda.
**İşaretleme:** d ≤ 2.5 ve nokta görüş açısında → ipucu "E: İşaretle" (pad: A). E → 0.8 sn frekans süpürmesi 440→1760 Hz, LED sabit yanar, `lost.found[realm]=true`, HUD 2 sn "Yankı k/3", sinyal durur. Kumanda: 60 ms 0.3 titreşim.
**Tamamlama:** 3/3 → tesise ilk dönüşte telsiz LED'i yanar, menüde "Kayıt Sekiz" (dinleme ~40 sn; metin `GAME.lost.rec8.lines`, senarist yazar: Lale'nin üç yankıyı neden bıraktığı). Dinlenince `S.rec8=true`, `lost.done=true`, başarım `lost_signal` "Kayıp Sinyal" (hikâye, note; koşul `rec8`). Günlük "Kayıtlar" bölümüne "Kayıt Sekiz" eklenir (`seven_records` koşulu değişmez).
**NG+:** görev durumu korunur; tamamlanmışsa telsizde yalnız "Kayıt Sekiz'i tekrar dinle".

**Veri:** `S.lost={on, found:{baslangic,kuantum,gezegen}, done}` (kalıcı), `S.rec8` (kalıcı). `GAME.lost={unlock:{logs:3}, points:{baslangic:[30,26],kuantum:[32,-26],gezegen:[-30,26]}, bars:[6,12,20,30,40], beep:{hz:880,ms:40,min:.25,max:1.2}, mark:2.5, rec8:{lines:[]}}`.

**Kabul:** (1) Görev alınmadan boyutlarda direk ve HUD yok; alındıktan sonra üçünde direk var. (2) Noktaya 35 br'de 1 çubuk, 10 br'de 4 çubuk; bip aralığı 1.2 s'den 0.25 s'ye düşer, 41 br'de ses yok. (3) 2.5 br içinde E → işaret, "Yankı 1/3"; aynı boyuta tekrar girince HUD gizli. (4) Üçü işaretlenince telsizde "Kayıt Sekiz" belirir, dinlenince `lost_signal` toast'ı; `logs.length` 7'de kalmaz, günlükte sekizinci kayıt listelenir. (5) Günün Tohumu koşusunda direkler çizilmez ve bip çalmaz.
