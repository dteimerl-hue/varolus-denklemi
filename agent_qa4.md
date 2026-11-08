# QA-4 · Statik denetim — QA-3 sonrası eklenen sistemler

Kapsam: CHAT, defter erozyonu (clarity/fogText/rehearse), MUS.motif, Tahmin Defteri, Bakanlık Raporu, Kayıt Dokuz, Sema dalı, SEIS, Yarı Ömür, ISS, Yol Kartı/Sisi Tahmin Et, EGGS, Sis Günlüğü (motor), Nil'in Odası, Galileo, Hız Koşusu, Sahte Lale, Bayes, CLOCK, Misafir modu, hubHint, autoQuality. QA-3 bulguları tekrarlanmadı. Doğrulananlar: `load()` kayıtları `Object.assign(fresh(),saved)` ile birleştiriyor (eski kayıtta `pred/predRes/notes` yokluğu çökertmiyor); `#ov` elemanında `role="dialog" aria-modal` başlıkta tanımlı; `thought('')` korumalı; `hubDef` Sema/Lale'yi `semaGone/laleGone` ile süzüyor; `interact()` her yerde `GFX.near` kullanıyor; Tahmin Defteri nokta id'leri gerçek nokta id'leriyle eşleşiyor; `codeMake/codeParse` bit düzeni ve sağlama toplamı tutarlı; `GUEST.tick` ile `SPEED.hud` aynı `#speed` elemanını paylaşsa da aynı tik içinde sıralı yazdıkları ve `S.speed`/`S.guest` birlikte olamadığı için çakışmıyor; IIFE içinde tanımdan önce `const` kullanımı (TDZ) bulunmadı (tüm yeni `const` nesneleri yalnızca çalışma zamanında, boot sonrasında çağrılıyor).

Öncelik: A çökme > B kilitlenme/veri kaybı > C oynanış > D erişilebilirlik/kozmetik. "(olası)" ile işaretlenenler kod yolundan kesin türetilemeyen, koşula bağlı bulgulardır.

## A. Çökme

1. **(olası) Prova sırasında defter kırpılırsa `n.ts` TypeError** — w_app.html, anahtar: `function rehAnswer(i){const E=(GAME.story11||{}).erode||{};const n=S.notes[reh.i];`
   Neden: `rehearse()` dizin saklıyor; overlay açıkken zamanlayıcıyla gelen bir `note()` (`CLOCK.away` 5 sn gecikmeli `note(k)`, `setTimeout(()=>note('start'),4000)`, `note('realm')` 3,5 sn) `S.notes.length>60` olunca `splice` ile baştan siliyor → dizin kayar; 60 sınırında `S.notes[reh.i]` undefined olur ve `n.ts` okunurken çöker.
   Düzeltme: `reh` içinde dizin yerine not nesnesini (`n`) sakla; `rehAnswer` başında `if(!n)return` koy.

## B. Kilitlenme / veri kaybı

2. **Sis Günlüğü'nden Esc ile çıkınca `body.motorview`, `motor` ve MUS bölge modu takılı kalıyor** — w_app.html, anahtar: `document.body.classList.add('motorview');thoughtClear();MUS.setZone(true)`
   Neden: `motorChapter` `ovBack='play'` kuruyor; Esc → `closeOv()` yalnızca `#ov`'u boşaltıp `mode='play'` yapıyor. `motor` null'lanmıyor, `motorview` sınıfı ve `MUS.setZone(true)` geri alınmıyor; oyuncu "Motor'un gözü" filtresiyle ve bölge müziğiyle dolaşmaya devam ediyor, Çekirdek'e tekrar girene kadar düzelmiyor.
   Düzeltme: `closeOv` başına `if(motor){motor=null;document.body.classList.remove('motorview');MUS.setZone(false)}` ekle (benzer şekilde `reh=null;guess=null;predGate=null;rec9Sel=null`).

3. **Hız Koşusu onaysız `S=fresh()` ile başarımları, sonları, defteri ve görünümü siliyor** — w_app.html, anahtar: `function speedStart(cat){const c=S.cal;S=fresh();S.cal=c;`
   Neden: Başlıkta "Baştan başla" iki aşamalı (`armed`) onay istiyor; `speedcat` tek tıkla kayıt üzerine yazıyor (`save()`). `startTour2`'nin aksine `ach, endings, dailyBest, notes, noteKeys, wiki, lookMods, guessDone, eggs, chat` taşınmıyor; `S.lookMods` kaybı yeniden yüklemede Arel'in görünümünü sıfırlıyor. Koşu bittiğinde `achCheck` yalnızca boş `S.ach` üstünde çalışıyor.
   Düzeltme: `speedStart` içinde `startTour2`'deki kalıcı alanları (`ach, endings, dailyBest, notes, noteKeys, wiki, lookMods, eggs, guessDone, chat`) `keep` ile taşı ve `speedcat` düğmesine `armed` tarzı ikinci tık onayı ekle.

4. **İkinci Tur `motorSeen`'i taşıyıp `motorFilled`'ı sıfırlıyor → "motor_honest" başarımı herkese açılıyor** — w_app.html, anahtar: `motorSeen:S.motorSeen,nil:S.nil,nilDone:S.nilDone` ve `c:()=>S.motorSeen&&!S.motorFilled`
   Neden: `startTour2` keep listesinde `motorSeen` var, `motorFilled` yok; `fresh()` onu 0 yapıyor. Tur 2'de ilk `achCheck` (her 4 sn, Çekirdek'te) üç bölgeyi "dolduran" oyuncuya da dürüstlük başarımını veriyor. Aynı listede `semaGone/semaStay` taşınırken `laleGone/fakeGone/fakeChosen` taşınmıyor: Sema Tur 2'de yok, "giden" gerçek Lale geri geliyor (olası tasarım kararı; tutarlılık için not).
   Düzeltme: keep'e `motorFilled:S.motorFilled` ekle; Lale/Sema politikasını eşitle (ya ikisini de taşı ya da ikisini de sıfırla).

5. **(olası) Misafir sayacı duvar saatiyle çalışıyor; kayıt yüklenince süre anında doluyor** — w_app.html, anahtar: `const left=Math.max(0,600-(Date.now()-g.t0)/1000)`
   Neden: `S.guest.t0` `Date.now()` olarak kaydediliyor ve `save()` ile diske yazılıyor. Sekmeyi kapatıp "Kaldığın yerden devam et" diyen misafir, oyun süresi (`S.playT`) 2 dakikayken "On dakika doldu" mesajıyla karşılaşıyor; sekme arka plandayken de sayaç akıyor.
   Düzeltme: `S.guest={t0:S.playT||0}` ve `left=600-((S.playT||0)-g.t0)` kullan.

6. **(olası) SEIS/ISS yüklemesi beklerken açılan başka overlay'in üzerine yazılıyor** — w_app.html, anahtar: `await SEIS.load();if(mode!=='ov')return;if(!SEIS.task)SEIS.newTask();renderSeis()`
   Neden: Oyuncu "Kapat" deyip (mode `play`) 8 sn'lik fetch bitmeden telsiz/rapor/Kayıt Dokuz gibi başka bir `mode='ov'` ekranı açarsa koşul geçiyor ve `renderSeis()` o ekranın `innerHTML`'ini siliyor; rapor/Kayıt Dokuz kaydedilmeden kayboluyor (`reportOv` tekrar sorulur ama `rec9Sel` kaybolur).
   Düzeltme: `openSeis/openIss` başında `const tok=++ovToken` tut, `await` sonrası `if(mode!=='ov'||tok!==ovToken)return`.

7. **(olası) `GUEST.said` oturum boyunca sıfırlanmıyor** — w_app.html, anahtar: `const GUEST={said:{},tick(){`
   Neden: Modül düzeyi nesne; "Baştan başla" sonrası ikinci misafir koşusunda `point/figure/zone/exit` ipuçları hiç söylenmiyor. Ayrıca veri `steps.arrive` tanımlı ama hiçbir `say('arrive')` çağrısı yok.
   Düzeltme: `guestStart` içinde `GUEST.said={}`; Yuva'ya varışta (`travel('yuva')` sonrası) `say('arrive')` çağır.

## C. Oynanış

8. **Çekmecedeki kod kutusuna yazarken tuşlar oyuna gidiyor (E konuşma, P fotoğraf, WASD yürüme)** — w_app.html, anahtar: `document.addEventListener('keydown',e=>{const k=e.key.toLowerCase();if(k==='tab'&&(mode==='ov'` ve `<input id="gcode" placeholder="VD-XXXX-XXXXX"`
   Neden: Tohum sekmesi `mode==='play'` iken açılıyor; keydown dinleyicisinde `e.target` için INPUT/TEXTAREA koruması yok. Kod alfabesinde E, P, W, A, S, D, F var: "VD-…E…" yazarken `interact(GFX.near)` tetikleniyor (yakındaki NPC ile diyalog açılıp çekmece kapanıyor), P fotoğraf modunu açıyor, WASD Arel'i yürütüyor.
   Düzeltme: Her iki keydown dinleyicisinin başına `if(e.target&&/^(INPUT|TEXTAREA)$/.test(e.target.tagName)&&e.key!=='Escape')return;` ekle.

9. **Tahmin Defteri'nde 18 sorunun hepsinde doğru şık ilk sırada** — w_data.html, anahtar: `"predict": {"intro": "Tahmin Defteri. Boyuta girmeden üç soru`
   Neden: Tüm sorularda `"a": 0`; şıklar karıştırılmadan basıldığı için (`q.opts.map((o,i)=>…data-i="${i}"`) hep ilk şık doğru. Brier/kalibrasyon başarımı ("calibrated") ilk şık + %95 ile garanti ediliyor.
   Düzeltme: Veride `a` değerlerini çeşitlendir ya da `renderPredict`'te şıkları deterministik tohumla (`q.id`) karıştırıp `a`'yı eşle.

10. **Anlam boyutunda p2 ve p3 aynı noktaya bağlı; iki sonuç aynı anda çözülüyor** — w_data.html, anahtar: `{"id": "p3", "point": "sisifos"`
    Neden: Anlam'ın iki noktası var (`ucan, sisifos`); p3 de `sisifos`'a bağlanmış. `predictResolve` iki soruyu aynı anda çözüyor, iki `thought` 1800 ms'de çakışıyor (ikincisi birinciyi bastırıyor) ve "yanılma" geri bildirimi tek görünüyor.
    Düzeltme: p3'ü `"point": "ucan"` yap ya da `predictResolve`'da aynı noktadaki ikinci düşünceyi +3000 ms geciktir.

11. **`removeNpc` sonrası etiket ve yakınlık kalıntısı** — w_app.html, anahtar: `GFX.removeNpc('lale2');thought(R13.motor` (ayrıca `GFX.removeNpc('lale')`, `GFX.removeNpc('sema')`); w_world.js, anahtar: `if(hide||!l.ent.obj.visible)`
    Neden: `buildLabels` listesi sadece `travel`'da yeniden kuruluyor; dünya etiket döngüsü `obj.visible` (hâlâ true) ve `ent.pos`'a bakıyor → kaybolan NPC'nin "Lale · yankı · tam" etiketi havada asılı kalıyor. `removeNpc` `near=null` yapıp `nearCb`'yi çağırmıyor; uygulamadaki `near` eski nesnede kaldığından `prompt()` "Lale ile konuş" yazısını göstermeye devam ediyor (E basınca `GFX.near` null olduğundan tepki yok; dokunmatik E düğmesi de `GFX.near` kullandığı için güvenli).
    Düzeltme: Uygulamada `removeNpc` çağrılarının ardından `buildLabels()` çağır; w_world `removeNpc` içinde `if(near===n){near=null;nearCb&&nearCb(null)}`.

12. **SEIS eşik kaydırıcısı her `input` olayında tüm overlay'i yeniden çiziyor** — w_app.html, anahtar: `const thr=$('#seisthr');if(thr)thr.addEventListener('input',()=>{SEIS.thr=+thr.value;$('#seisthrv').textContent=SEIS.thr`
    Neden: `renderSeis()` `innerHTML`'i değiştirince sürüklenen kaydırıcı DOM'dan kalkıyor; fare sürüklemesi ilk adımda kopuyor, klavye kullanıcısında odak `body`'ye düşüp ilk düğmeye atlıyor (her ok tuşunda bir adım, sonra odak kaybı). Depremler `<li data-act="seispick">` olduğundan klavyeyle hiç seçilemiyor; harita tıklaması dışında konum tahmini yolu yok.
    Düzeltme: `input`'ta yalnız `$('#seisthrv')`, deprem sayısı ve `SEIS.draw()`+liste parçasını güncelle (tam render'ı `change`'e bırak); `li`'lere `role="button" tabindex="0"` ve Enter/Space işleyicisi ekle.

13. **Sisi Tahmin Et kodu normalize edilmeden anahtar oluyor; zayıf sağlama toplamı** — w_app.html, anahtar: `guess={code:code.toUpperCase(),p,qs,i:0,`
    Neden: `S.guessDone` anahtarı ham girdiden (`"vd-ab12-…"` / `"VDAB12…"` / boşluklu) üretiliyor; aynı kod farklı yazımla tekrar "çözülmüş" sayılıyor, "kod çözüldü" sayacı şişiyor. `codeParse` 5 bitlik sağlama (1/32) kullandığından yanlış yazılan kodların ~%3'ü geçip anlamsız sorular üretiyor (olası).
    Düzeltme: Anahtar olarak `codeParse` ile temizlenmiş `t` (VD+8+1) kullan; sağlamayı 2 karaktere (10 bit) çıkar.

14. **(olası) Dolunay/yeni ay sis çarpanı tüm boyutlara sızıyor ve geri alınmıyor** — w_app.html, anahtar: `if(m>.47&&m<.53){if(GFX.setFogMul)GFX.setFogMul(.85);if(key(`
    Neden: `CLOCK.tick` yalnız hub'da koşuyor ama `fogX` dünya genelinde kalıcı; yeni ayda (1.2) boyutlardaki Bozulma görüş mesafesi değişiyor, dolunayda hafifliyor. Aynı tikte `document.body.classList.toggle('night',hr<6)` de sadece hub'da güncellendiğinden 05:59'da girilen boyutta "gece" sınıfı saat 06'dan sonra da kalıyor.
    Düzeltme: Koşul dışında `GFX.setFogMul(1)` çağır ve `travel` sonunda `fogX`'i boyut için sıfırla; `night` toggle'ını `cur` koşulunun dışına al.

15. **(olası) `vd_last` oturum başında yazılıyor; uzaklık günleri oturum süresi kadar şişiyor ve taze koşulara "uzaktaydın" notu düşüyor** — w_app.html, anahtar: `localStorage.setItem('vd_last',String(Date.now()))}catch(e){`
    Neden: `CLOCK.away` yalnız `enterWorld`'de çalışıyor; 3 saat oynayıp 22 saat sonra dönen oyuncu "away1" alıyor. `speedStart/guestStart` da `enterWorld` çağırdığından, eski `vd_last` 1 günden eskiyse yeni Hız Koşusu'nun 5. saniyesinde "Deftere yazıldı" ve `S.awayCrew={}` ile mürettebat "nerelerdeydin" repliklerine geçiyor.
    Düzeltme: `vd_last`'ı `save()` içinde (ya da `visibilitychange`'de) güncelle; `away()` içinde `if(S.speed||S.guest)return`.

16. **(olası) CHAT hub'a dönüşte eski NPC nesneleriyle devam ediyor** — w_app.html, anahtar: `if(this.cur){if(this.pause){this.pause=false;this.lineAt=now}if(now<this.lineAt)return;this.step();return}`
    Neden: Boyuta gidip dönünce ada yeniden kuruluyor; `this.cur.A/B` eski adaya ait, `GFX.meet` yeni adada hiç çağrılmıyor. Sohbet ortasından, NPC'ler birbirine dönmeden ve yan yana olmadan devam ediyor; baloncuk `GFX.island.npcs.find` ile yeni nesneye bağlanıyor ama `end()`'deki `unmeet` artık anlamsız.
    Düzeltme: `tick` başındaki `cur!=='hub'` dalında `this.end()` çağır (pause yerine iptal).

## D. Erişilebilirlik / kozmetik

17. **Kayıt Dokuz cümle ekranı odak yönetmiyor** — w_app.html, anahtar: `const prev=slots.map((s,i)=>rec9Sel.pick[i]!=null?rec9Fill(s[rec9Sel.pick[i]]):'…').join(' ');`
    Neden: İlk ekran (`Kime?`) ilk düğmeye odaklanıyor, ikinci dal her `r9p` tıklamasında `innerHTML`'i yeniliyor ve `.focus()` çağırmıyor → odak `body`'ye düşüyor; Tab tuzağı sonraki Tab'da listenin başına atıyor, klavye kullanıcısı seçtiği cümleden kopuyor. "Kaydet" `disabled` olduğundan Tab listesinde de yok.
    Düzeltme: Render sonunda `const b=ov.querySelector('[data-act="r9p"].sel')||ov.querySelector('button');if(b&&!ov.contains(document.activeElement))b.focus()`.

18. **ISS yörünge izi hep boylam 0'da çiziliyor** — w_app.html, anahtar: `x.lineTo(...this.xy(lat,((i*1.0)+ (this.now.lon-0))%360-180>180?0:0,w,h))`
    Neden: Üçlü ifade her iki dalda da `0` döndürüyor; iz, haritanın ortasında dikey bir sinüs çizgisi olarak görünüyor ve istasyonun gerçek yoluyla ilgisi yok (tahmin görevini yanıltıyor).
    Düzeltme: `this.xy(lat,((this.now.lon+(i-180)*1.02)+540)%360-180,w,h)` gibi gerçek boylam kaydırması kullan.

19. **(olası) Erozyon öncesi notlarda `at`/`ts` yoksa netlik NaN** — w_app.html, anahtar: `const age=(S.playT||0)-(n.ts==null?n.at:n.ts);`
    Neden: `ts` eksikliği `at`'a düşürülüyor ama eski `note()` sürümünde `at` de yoksa `age=NaN` → `clarity` NaN; `fogText(t,NaN)` sessizce düz metin döndürüyor, "Prova et" asla görünmüyor ve bu notlar hiç silinmiyor (tasarımla çelişiyor, çökmüyor).
    Düzeltme: `load()` sonrası `S.notes.forEach(n=>{n.at??=0;n.ts??=n.at;n.reh??=0})` göçü ekle.

20. **"Prova et" düğmesi 5 harften kısa kelimeli notta sessizce hiçbir şey yapmıyor** — w_app.html, anahtar: `.filter(x=>x[0].length>=5);if(!ws.length)return;`
    Neden: Düğme `clarity<.98` olan her notta basılıyor; uygun kelime yoksa `rehearse` erken dönüyor, çekmece açık kalıyor, geri bildirim yok.
    Düzeltme: `renderNotes`'ta düğmeyi `n.t.split(' ').some(w=>w.replace(/[.,;:!?…]+$/,'').length>=5)` koşuluna bağla ya da eşiği 4'e indir.

21. **Hız Koşusu menüsü başlık ekranında Esc ile kapanmıyor; Tab tuzağı başlıkta yok** — w_app.html, anahtar: `function speedMenu(){const SP=(GAME.story12||{}).speed||{};const b=SPEED.best();const ov=$('#ov');ov.className='on center';`
    Neden: `mode` `'title'` kalıyor; keydown'daki Esc dalı yalnız `mode==='ov'` için `ovclose` tıklıyor, Tab tuzağı da `ov/mini/gate` ile sınırlı. Klavye kullanıcısı "Vazgeç"e ulaşmak için düğmeleri dolaşıp HUD'a kayabiliyor.
    Düzeltme: Esc dalına `||mode==='title'` ekle (yalnız `[data-act="ovclose"]` varsa) ve Tab tuzağı koşuluna `mode==='title'` dahil et.

22. **(olası) Tahmin kartında her şık tıklaması odağı ilk şıkka taşıyor** — w_app.html, anahtar: `const fb=ov.querySelector('button');if(fb&&!ov.contains(document.activeElement))fb.focus()}` (renderPredict)
    Neden: Tıklanan düğme `innerHTML` ile yok olunca `activeElement` body oluyor ve koruma ilk soruya odaklıyor; üçüncü sorunun güven düğmesine basan klavye kullanıcısı tekrar birinci soruya dönüyor.
    Düzeltme: Render öncesi `const id=document.activeElement&&document.activeElement.dataset` ile `q/i/c` değerlerini sakla, render sonrası aynı `data-*` eşleşen düğmeye odaklan.
