# Varoluş Denklemi — QA Turu 2 (statik inceleme)

Kapsam: `w_app.html`, `w_world.js`, `w_data.html`, `w_head.html`. Tarayıcı kullanılmadı; bulgular kod okuması ve veri eşleştirmesine dayanır.

## 1. Hata adayları

**H1 — Lale'nin kaydı dinlenemiyor (ReferenceError).** `w_app.html › interact()` log dalı: `const lines=l.lines.map(...)` — `l` hiçbir yerde tanımlı değil; `w_world.js` log entitesi de `lines` taşımıyor. Tekrar: herhangi bir boyutta kayıt işaretine yaklaş, E'ye bas → konsolda hata, diyalog açılmaz, `S.logs` hiç dolmaz (mühür ve "6/6 kayıt" imkânsız). Düzeltme: `const lines=(R[cur].logs.find(x=>x.id===e.id)||{lines:[]}).lines.map(t=>({who:'l',t}));`

**H2 — Nokta hedefli tanık görevleri tamamlanamıyor.** `interact()` point dalı: `questFound('p:'+e.id)` `if(!e.done)` bloğunun içinde. Görev verildiğinde nokta zaten dinlenmişse (q_mira `cmb` unlock=5, q_hatice `stars` unlock=2, q_zeynep `lattice`, q_riza `sisifos`, q_deniz `dot`) cevap asla "bulunmaz". Figür hedefleri (`f:elif`, `f:nil`) bloğun dışında olduğu için çalışıyor. Tekrar: Başlangıç'ı bitir, 5 içgörü sonra Mira'dan görevi al, `cmb`'ye dön → hiçbir şey olmaz. Düzeltme: `questFound('p:'+e.id)` çağrısını `if(!e.done){...}` bloğunun dışına, `onEnd` sonuna taşı.

**H3 — Yakıt bonusu her varışta siliniyor.** `travel()` varış callback'i: önce `S.fuel+=S.fuelBonus` sonra `S.fuel=6+facts*4` ile ezer. Eşik mini oyunu (+3) ve q_deniz ödülü (+4) etkisiz. Düzeltme: `S.fuel=6+S.facts.filter(f=>f.realm===to).length*4+(S.fuelBonus||0);` (önceki `S.fuel+=` satırını sil).

**H4 — Seçim tuşu yol sayacını şişiriyor.** `dPick()` seçim yapıldıktan sonra da 1/2/3 ile tekrar çağrılabiliyor; her basış `S.path[...]++`. Tekrar: seçimli diyalogda 1'e beş kez bas → Yol sekmesinde +5. Düzeltme: `if(!L.ch||dlg.pick!=null)return;`

**H5 — Final müziği ilk gösterimde çalmıyor.** `finale()`: `if(S.ending)MUS.ending(S.ending)` satırı `S.ending=ek` atamasından önce. Totem seçildikten sonraki ilk final ekranı sessiz; ancak "Yeni simülasyon"a tıklanıp yeniden render olunca başlar. Düzeltme: `S.ending=ek;save();MUS.ending(ek);` (üstteki koşullu çağrıyı sil).

**H6 — Mini oyun tek şansta kaybediliyor (mod çakışması).** `interact()` point `onEnd`: `setTimeout(()=>{if(mode==='play')openMini(mg)},900)`. 900 ms içinde yol arkadaşına E basılırsa (`near` sıklıkla o) mode='dialog' olur, mini açılmaz; nokta `done` olduğu için bir daha tetiklenmez. "Vazgeç" de aynı: `S.mini` yazılmaz ama nokta bitmiştir. Düzeltme: point dalının başına `if(e.done&&mg&&!S.mini[mg]){openMini(mg);return}` benzeri yeniden açma yolu ekle (mg hesabını dalın başına al).

**H7 — Görünmez avcı saldırısı (Kuantum "Çökme Dalgası").** `w_world.js › weatherStep()` `hideGlitch` ile bozulmaları gizler; `glitchStep()` `active` koşulu havayı bilmez. `wxTick()` saha aktifken hava başlatmaz ama hava sürerken sahaya girilebilir. Tekrar: Kuantum'da hava uyarısı çıkınca sahaya koş → görünmeyen avcılar vurur. Düzeltme: `glitchStep` içinde `const active=glitchOn&&!locked&&halT<=0&&n.hunter&&Z&&isl.zoneActive&&!(WX&&WX.hideGlitch&&WX.k>.3);`

**H8 — Geçit kalibrasyonunda müzik kesiliyor.** `MUS.realm('gate')`: `GAME.audio.realms` içinde `gate` yok; `spec()` null → `stopLayer` sonra sessizlik. Düzeltme: `realm()` içinde `const sp=this.spec(id)||(id==='gate'?this.spec(cur):null);` ya da `w_data.html`'e `audio.realms.gate` ekle.

**H9 — "Görünüm" ödülü kalıcı değil, sıfırlamada ise kalıyor.** `questReward()` `GAME.people.arel.look`'u yerinde değiştirir; `S`'e yazılmaz → sayfa yenilenince eldiven/rozet/atkı kaybolur; "Baştan başla" sonrası ise `S=fresh()` olsa da look değişmiş kalır. Düzeltme: `fresh()`'e `lookMods:{}` ekle, ödülde `S.lookMods[rw.k]=rw.v`, boot'ta `GFX.setPlayerLook(Object.assign({},GAME.people.arel.look,S.lookMods))`.

**H10 — Travel sırasında temizlenmeyen zamanlayıcılar.** `travel()` yalnızca `halCap`'i temizler; `cmpT`, `thought.t`, `wxTick` içindeki `W.arel`/`cmp('weather')`/`wxWarn` 2.5–7 s timeout'ları ve nokta→mini 900 ms timeout'u yaşamaya devam eder. Tekrar: hava uyarısı çıkar çıkmaz dönüş geçidine gir → Platform'da eski boyutun yol arkadaşı adına replik düşer. Düzeltme: `travel()` başına `clearTimeout(cmpT);clearTimeout(thought.t);$('#thought').classList.remove('on');` ekle (ve wx timeout'larını `wxT` dizisinde tutup burada temizle).

**H11 — Fotoğraf modu ölü arayüz.** `w_head.html` `#photo`, `#pbtn` (dokunmatikte görünür 📷), `data-act="photo|photooff|pfilt|pbar|pshot"` ve "P" etiketi var; `w_app.html` click handler'ında bu act'ler ve `GFX` API'sinde foto fonksiyonu yok. Düzeltme: `#pbtn` ve `#photo` bloklarını kaldır ya da `if(a==='photo'){document.body.classList.toggle('photo');return}` ile en azından gizle/göster bağla.

**H12 — Mobilde Sis Feneri yok; E tuşu basılı tutma diyalogu uçuruyor.** Fener yalnızca `keydown 'f'`; `w_head.html`'de dokunmatik F düğmesi yok, Kontroller metni de söylemiyor. Ayrıca `keydown` `e.repeat` kontrolü yapmadığı için E basılı tutulunca `dNext()` satırları atlar. Düzeltme: keydown başına `if(e.repeat)return;`; head'e `<button id="fBtn" class="touch" data-act="lantern">F</button>` ekleyip `pointerdown/up` ile `GFX.lantern(true/false)` bağla.

Küçük notlar: `fresh()`'te `trips, lastDom, lastDone, laleHint, helped, coreCine, gt` yok (kod `||` ile tolere ediyor, ama şema belgesi olarak eksik); Arşiv "Kalibrasyonlar" sayacı Kuantum ilk kalibre edilirse 7/6 olabilir (`Object.keys(S.cal2).length+(S.cal?1:0)` → `Math.min(6,…)`); `TTS.stop()` yalnızca `dNext()`'te — `renderDlg()` `!dlg` dalına da `TTS.stop()` ekle; `page` ödülü (`S.pages`) hiçbir yerde gösterilmiyor; yol arkadaşı `near` hesabında +2.4 cezaya rağmen geçit yarıçapının (4.2) dış 0.6 m'sinde geçidi geçiyor — `e.follow?4:0` yap; `S.integMax` HUD segmentleri `integHUD()`'da doğru yeniden kuruluyor, sorun yok.

## 2. Oynanış sürtünmeleri

1. **HUD kalabalığı:** sol üstte konum+noktalar+yol düğmesi+görev kutusu, sağ üstte zaman genişlemesi, sol altta bütünlük+yakıt, ortada nav oku, üstte saha/hava uyarıları, altta düşünce+toast+prompt. Mobilde `#integ` (left:160) joystick'in hemen yanında. Görev kutusunu varsayılan kapalı/katlanır yap, uyarıları tek şeride topla.
2. **Tek `#thought` kanalı:** hava Arel replikleri, yol arkadaşı idle (45 s) + Arel yankısı (4.2 s), halüsinasyon satırları ve saha metinleri birbirini eziyor. Kuyruk ya da öncelik ekle.
3. **Kalibrasyon beş kez aynı uzun metin:** VAR'lı her boyutta aynı Jafferis paragrafı; sadece `note` değişiyor. İkinci kalibrasyondan itibaren kısa sürüm göster.
4. **Görev hedefi işaretsiz:** `navTarget()` görev hedefini bilmiyor; oyuncu `hint`'i hatırlamak zorunda. Verilmiş görevin hedef noktasını nav'a ikinci öncelik olarak ekle.
5. **Parça sonrası yığılma:** frag alınır → öfke (hunter hız 4) + 2.5 s sonra halüsinasyon + "low" vinyet + kalp atışı blip. Halüsinasyonu saha dışına çıkınca tetikle.
6. **Ses varsayılan kapalı:** MUS ve TTS düğme basılmadan hiç duyulmuyor; başlık ekranında "Sesle başlat" seçeneği yok.
7. **Mini oyun habersiz ve geri dönüşsüz:** nokta diyalogu kapanır kapanmaz tam ekran deney açılıyor; "Vazgeç" sonrası ulaşılamıyor (H6).
8. **Görev listesindeki sabit uyarı:** "Bozulma Sahası'na girince saldırırlar" her boyutta kalıcı satır; ilk sahadan sonra kaldır.

## 3. Yeni Oyun+ (İkinci Tur)

Açılış: `finale()` düğmelerine `data-act="ng"` ekle; click'te `const p=S;S=fresh();S.ng=(p.ng||0)+1;S.prevEnding=p.ending;S.cal=true;S.cal2=p.cal2;S.facts=p.facts;save();cinema();`. `fresh()`'e `ng:0,prevEnding:null,lookMods:{}` ekle.

1. **Saha yarıçapı +40%, karanlık ring daha geniş** — `realmDef()`: `zone:{...r.zone,r:(r.zone.r||17)*(S.ng?1.4:1)}`.
2. **Avcı 3→4 ve bir kademe sert GPT** — `realmDef()` hunter `length:(S.ng?4:(n<3?2:3))`; `applyGP()` indeks `Math.min(5,doneCount()+S.ng)`.
3. **Parçalar ve kayıtlar farklı yerde** — `w_data.html` her realm'e `zone.pos2`, `logs[].pos2`; `realmDef()` `pos:S.ng&&l.pos2||l.pos`. Ayrıca `glitches[0]` yerine `glitches[1]` kullan.
4. **Gizli 7. parça (Platform mağarası)** — `hubDef()` `S.ng` iken `frag` entitesi döndürsün (`w_world.js load()` frag'ı yalnızca zone içinde kuruyor; `def.frag` için ayrı dal ekle). `interact()` frag dalında `cur==='hub'` ise `GAME.story.record7.hidden` satırları; `fragCount()>=7` olunca Çekirdek'te `record7.effect2`.
5. **Tanıklar önceki sona göre konuşur** — `w_data.html people[id].ng={kopru:[…],gozlemci:[…],sessizlik:[…]}`; `interact()` hub dalı başında `if(S.ng&&p.ng&&!(S.told[id]||{}).ng){lines=p.ng[S.prevEnding].map(...);S.told[id].ng=true}`; `updLabels()` ünlem koşuluna aynı testi ekle.
6. **Hava daha sık ve sahada da başlar** — `wxTick()` `wxNext=now+(S.ng?40:90)+…`, `z.active` erken dönüşünü `S.ng` için kaldır (H7 düzeltmesiyle birlikte).
7. **Kuantum da kalibre ister, gürültü her geçitte** — `openGate()` `NOISE=(v.noise||0)+(S.ng?.06:0)`; `VAR.kuantum={peak:2.5,thr:.8,note:'…'}`; `interact()` gate koşulu `!S.cal2[e.to]` (cal kısayolunu NG'de kapat).

Final kartında `S.ng` için "İkinci tur · önceki yol: …" satırı (`finale()` not paragrafı) ve totem `close` metninin alternatifi (`GAME.core.totem.opts[i].close2`).
