# QA-3 · Statik denetim (w_app.html / w_world.js / w_data.html / w_head.html)

Yöntem: kod okunarak (çalıştırılmadan) incelendi; GAME verisi sandbox'ta değerlendirilip alan adları ile çapraz kontrol edildi (realm7 = `bellek`: 3 nokta, 2 figür, 1 kayıt, 3 mektup, zone+zoneText, mirror, comp yok, wx yok). `$('#…')` ile çağrılan tüm kimlikler w_head.html'de var; app'ta kullanılan tüm `GFX.*`, `AUD.*`, `MUS.*` metotları tanımlı. `load()` sonrası `S=Object.assign(fresh(),saved)` ile üst seviye eksik alanlar tamamlanıyor (eski kayıt uyumluluğu bu düzeyde sağlam; sadece iç içe nesnelerde derin birleştirme yok). "Olası" işaretli olanlar kesinleşmemiş tahmindir. Not: dosya denetim sırasında başka bir ajan tarafından değiştirildi (CHAT, note(), keep listesine letters/rec8 eklendi); bulgular son hâle göre doğrulandı.

## A. Çökme

1. **Çekirdek'te yakalanınca `r.spawn` TypeError (ve yanlış yere ışınlama)** — w_app.html, anahtar: `GFX.respawn(S.lastSafe||r.spawn)`
   `caughtNow()` içinde `r=R[cur]`; `cur==='cekirdek'` iken `R.cekirdek` yok → `S.lastSafe` null ise `undefined.spawn` ile çöker. `stormTick()` süre bitince `caughtNow()` çağırıyor, yani fırtınada süre dolan her oyuncu bu yola giriyor. `lastSafe` null değilse de önceki boyutun koordinatlarına (başka bir dünyanın noktasına) ışınlanıyor.
   Düzeltme: `GFX.respawn(S.lastSafe||(r?r.spawn:(cur==='cekirdek'?[0,16]:[0,12])))` ve `travel()` tamamlanınca `if(to==='cekirdek')S.lastSafe=null;`.

2. **`thought(undefined)` → `t.length` TypeError (olası)** — w_app.html, anahtar: `const dur=Math.min(9000,2600+t.length*45)`
   `thought()` metni doğrulamıyor; `thought(p.after[pr][0],…)`, `thought(sl[0],…)`, `thought(L[i++],'Motor')` gibi veri-güdümlü çağrılarda boş dizi/eksik alan gelirse ana tick içinde fırlatır (tick try/catch'siz; bir kez çöken `setInterval` sonraki turlarda da hata üretir).
   Düzeltme: fonksiyonun başına `if(!t||typeof t!=='string')return;` ekle.

3. **CHAT.step `speechSynthesis` global guard'sız (olası, düşük)** — w_app.html, anahtar: `!speechSynthesis.speaking)VOX.speak(L.t,L.who)`
   VOX her yerde `'speechSynthesis' in window` ile korunurken burada çıplak referans var; Web Speech olmayan WebView/eski tarayıcıda ReferenceError. `CHAT.tick()` try/catch içinde olduğu için oyun çökmez ama o tur `MUS.motif` atlanır.
   Düzeltme: `VOX.on&&('speechSynthesis' in window)&&!speechSynthesis.speaking`.

## B. Veri kaybı

4. **İkinci Tur (NG+) başarımları, sonları ve Tohum rekorlarını siliyor** — w_app.html, anahtar: `const keep={notes:S.notes,noteKeys:S.noteKeys,chat:S.chat,letters:S.letters,rec8:S.rec8,`
   `startTour2()` `S=Object.assign(fresh(),keep)` yapıyor; `ach`, `endings`, `dailyBest`, `wiki`, `lookMods` keep'te yok. Sonuç: `ending_each` (3 son) başarımı pratikte alınamaz (her turda `endings` sıfırlanır), NG+ başında ilk `achCheck()` ile tour2/letters_all/lost_signal/echo_four/mini_both/photo5… toast fırtınası ve zaman damgaları kaybı, günlük rekorlar silinir, Arel'in görünüm ödülleri (`lookMods`) kaybolur.
   Düzeltme: keep'e `ach:S.ach,endings:S.endings,dailyBest:S.dailyBest,wiki:S.wiki,lookMods:S.lookMods` ekle.

5. **NG+ sonrası `started:false` → yeniden açılışta giriş sineması tekrar oynuyor** — w_app.html, anahtar: `tour:2,ngIntro:false,trips:{}}`
   `fresh()` `started:false` veriyor, keep listesi `started` içermiyor; sayfa yenilenince başlık "Simülasyonu başlat" der ve `cinema()` (ilk giriş filmi) yeniden oynar; ayrıca `ROOM.init()` ve `MUS.realm('hub')` enterWorld dışından başlatılmadığı için NG+'ı başlıktan açan oyuncuda presence çalışmaz.
   Düzeltme: keep'e `started:true` ekle (ve startTour2 içinde `ROOM.init();`).

## C. Oynanış

6. **Çekirdek'e ikinci girişte Sis Fırtınası hiç başlamıyor; Bozulmalar da vuramıyor** — w_app.html, anahtar: `if(to==='cekirdek'&&!S.coreCine){S.coreCine=true;cinema2()}` ve `GFX.onCatch((n,kind)=>{if(mode!=='play')return;const r=R[cur];if(!r)return;`
   Fırtına yalnızca `halWas` (coreHal halüsinasyonu bittiğinde) üzerinden tetikleniyor. Oyuncu fırtınayı bitirmeden çıkar/sayfayı yenilerse `coreCine` ve `coreHal` zaten true → ne sinema ne hal → `halWas` false → `startStorm` asla çağrılmaz; `coreDef()` yine zone + 3 avcı üretir ama HUD/süre yok, `stormDone` hiç set edilmez. Üstüne `onCatch` `R[cur]` yokken erken döner: Çekirdek avcıları hiçbir zaman vuramaz/yakalayamaz.
   Düzeltme: travel tamamlanınca `if(to==='cekirdek'&&S.coreHal&&!S.stormDone)setTimeout(startStorm,1500);` ve onCatch'te `const r=R[cur]||(cur==='cekirdek'?{}:null);if(!r)return;`.

7. **`halWas` boyutlar arası sızıyor** — w_app.html, anahtar: `GFX.hallucOff();clearTimeout(halCap);document.body.classList.remove('low');dlg=null;renderDlg()`
   `travel()` halüsinasyonu kapatıyor ama `halWas`'ı sıfırlamıyor; yeni boyuta varışta tick `halWas&&!GFX.halActive()` görüp sahte `cmp('hallucination')` repliği atıyor; Çekirdek'e taşınan sızıntı fırtınayı sinema/hal sırasından önce başlatabiliyor.
   Düzeltme: travel başındaki `wxOn=null;` yanına `halWas=false;` ekle.

8. **Kumandayla ER=EPR kalibrasyonu (mode 'gate') yapılamıyor → boyutlara girilemiyor** — w_app.html, anahtar: `if(dn(0)){if(mode==='dialog')dNext();else if(mode==='play')interact(GFX.near)`
   GPAD.poll'da `gate` modu için hiçbir dal yok: A hiçbir şey yapmaz, B `Escape` ile iptal eder, D-pad odak gezdirme yalnız ov/title/drawer'da. İlk ziyarette her boyut `openGate()` zorunlu (`!S.cal||(VAR[e.to]&&!S.cal2[e.to])`), dolayısıyla salt-kumanda oyuncusu tesiste kilitli kalır. Klavyede de Enter/ok tuşu bağlı değil (sadece Tab+slider).
   Düzeltme: poll'a `else if(mode==='gate'&&gate&&!gate.ok){fireGate()}` ve D-pad sol/sağ → `gate.mu=Math.max(-1,Math.min(1,gate.mu∓.05));drawMI()`, yukarı/aşağı → `gate.t±.05`.

9. **Kumanda koparsa Sis Feneri açık kalıyor, yakıt boşalıyor** — w_app.html, anahtar: `sleep(){if(!this.on)return;this.on=false;document.body.classList.remove('gp')`
   X basılıyken (`xHeld`) `gamepaddisconnected` → `sleep()` çağrılır ama sentetik `keyup f` gönderilmez; `keys.f` true kalır, tick her 250 ms yakıt düşürür, `GFX.lantern` açık kalır (gerçek F tuşuna basılana dek).
   Düzeltme: sleep'e `if(this.xHeld){this.xHeld=false;document.dispatchEvent(new KeyboardEvent('keyup',{key:'f',bubbles:true}))}` ekle.

10. **VOX çakışması: `thought()` diyalog sesini kesiyor** — w_app.html, anahtar: `if(prio>=2||who)VOX.speak(t,id)}TQ.until=now+dur`
    `VOX.speak` her çağrıda `this.stop()` ile `speechSynthesis.cancel()` yapıyor. `thought()` mod kontrolü yapmadığından diyalog sırasında tetiklenen zamanlayıcılar (varış `setTimeout(()=>thought(ar),3600)`, `thought(sl[0],…),4200`, `playHal` adımları 2,3 sn'de bir, NG+ giriş döngüsü `thought(L[i++],'Motor')`, `questFound` 800 ms, TQ kuyruğundan geri oynatma) konuşulan satırı yarıda keser ve Arel/Motor sesiyle üstüne konuşur.
    Düzeltme: `thought()` başına `if(mode==='dialog'){if(!TQ.q.some(x=>x.t===t))TQ.q.push({t,who,prio});return}` (kuyruğa ertele).

11. **Bellek kaydı "Lale'nin kaydı 7/6" gösteriyor** — w_app.html, anahtar: `Lale’nin kaydı ${Object.keys(S.logs).length}/6` (finale), `toast('Lale’nin kaydı',\`${Object.keys(S.logs).length}/6\`)`, `['Lale’nin kayıtları',Object.keys(S.logs).length,6]` (Arşiv)
    realm7'nin 1 kaydı var ve `S.logs.bellek` yazılıyor; `fragCount()` gibi bir dışlama kayıt sayımında yok → finale/totem notu, log toast'u ve Arşiv çubuğu (%116) 7/6 olabilir.
    Düzeltme: `const logCount=()=>GAME.realms.filter(r=>S.logs[r.id]).length;` tanımlayıp bu üç yerde kullan.

12. **Günün Tohumu 'karanlık' modunda yakıt sıfırlanması etkisiz** — w_app.html, anahtar: `S.fuel=6+S.facts.filter(f=>f.realm===to).length*4+(S.fuelBonus||0)`
    `travel()` tamamlanışında `DAILY.arrive()` (fuel=0) çağrıldıktan sonra bu satır yakıtı yeniden dolduruyor; klavye `karanlik` kontrolü feneri engellediği için HUD'da dolu depo görünür ama F çalışmaz (çelişkili). Kumanda `key('f')` yolu da aynı guard'dan geçiyor, sorun yok.
    Düzeltme: satırı `if(!(S.daily&&S.daily.on&&S.daily.mod==='karanlik'))S.fuel=…` yap ya da `DAILY.arrive()` çağrısını yakıt satırının sonrasına taşı.

13. **Fırtına giriş replikleri boyut değişince de akıyor** — w_app.html, anahtar: `L.forEach((t,i)=>setTimeout(()=>thought(t,null,3),i*2600))`
    `startStorm` 3-4 zamanlayıcı kuruyor; oyuncu Dönüş Geçidi'yle hub'a dönerse `storm=null` olur ama zamanlayıcılar hub'da "Sis yükseliyor. Lale'ye ulaş." der (ve VOX konuşur). Aynı durum `endStorm(win)` dizisinde.
    Düzeltme: zamanlayıcıları `storm.tm=[]` dizisine koy, `travel()`'daki `if(storm){…}` bloğunda `storm.tm.forEach(clearTimeout)`.

14. **Kumandayla giriş sineması atlanamıyor** — w_app.html, anahtar: `if(dn(1)){if(mode==='mini'&&mini)closeMini();else key('Escape')}`
    Escape sentetik olarak gönderilse de klavye işleyicisi `mode==='cine'` için `enter|escape` → `endCinema()` yapıyor; evet çalışır. Ancak A (dn(0)) `cine` modunda hiçbir şey yapmıyor; sadece B ile atlanıyor. Olası/kozmetik; yine de `else if(mode==='cine')endCinema()` eklenebilir.

## D. Erişilebilirlik / kozmetik

15. **Odak tuzağı yalnız `mode==='ov'`: mini oyunlar (Yankı Dizisi, Eşik, Yörünge) ve geçit kalibrasyonu kapsam dışı** — w_app.html, anahtar: `if(k==='tab'&&mode==='ov'){const bs=[...document.querySelectorAll('#ov button,#ov input,#ov a')]`
    `openMini`/`renderYanki`/`renderGate` `mode='mini'|'gate'` kullanıyor; Tab, overlay'in arkasındaki HUD düğmelerine (ses, kalite, günlük…) kaçıyor; ayrıca bu üç render odak taşımıyor (`fb.focus()` yok), klavye kullanıcısı overlay'e hiç giremiyor.
    Düzeltme: koşulu `(mode==='ov'||mode==='mini'||mode==='gate')` yap; `renderMini`, `renderYanki`, `renderGate` sonunda `const fb=ov.querySelector('button,input');fb&&fb.focus();`.

16. **Yankı Dizisi pedleri `disabled` olunca odak kayboluyor** — w_app.html, anahtar: `data-act="ytone" data-i="${i}" style="--c:${col[i]}" ${can?'':'disabled'}`
    Motor çalarken (st='play'/'next') pedler disabled → odaklı ped odağı `body`'ye düşürür; her turda klavye kullanıcısı yeniden Tab'lamak zorunda (1-4 tuşları çalışıyor ama ekran okuyucu bağlamı kaybolur).
    Düzeltme: `disabled` yerine `aria-disabled="${!can}"` kullan (YK.press zaten `st!=='input'` ise yok sayıyor) ve `st==='input'` olunca `document.querySelector('.ypads button')?.focus()`.

17. **Overlay kapanınca odak tetikleyen öğeye dönmüyor** — w_app.html, anahtar: `function closeOv(back){armed=false;VOX.stop();`
    `closeOv`/`closeMini`/`endCinema2` sonrasında `activeElement` kaldırılan düğme olduğu için odak `body`'ye düşer; telsiz menüsü, akış haritası, mektup/ending kartı kapanınca ekran okuyucu konumunu yitirir.
    Düzeltme: overlay açan fonksiyonlarda `ovOpener=document.activeElement`, closeOv/closeMini sonunda `ovOpener&&ovOpener.focus&&ovOpener.focus();ovOpener=null`.

18. **Yeni overlay'lerde `role="dialog" aria-modal` yok** — w_app.html, anahtar: `ov.innerHTML=\`<div class="card glass"><p class="eyebrow" style="color:#ffb347">Kovuk Tesisi · telsiz</p>`
    Yalnız Ayarlar kartı `role="dialog" aria-modal="true"` taşıyor; radioMenu, openFlow, finaleSaray, renderYanki/renderMini, openApod kartları taşımıyor → ekran okuyucu arka plandaki HUD'u okumaya devam eder.
    Düzeltme: bu kartların kök `<div class="card glass"` açılışına `role="dialog" aria-modal="true" aria-labelledby` ekle (en kolayı `$('#ov')` için `.className='on …'` atayan yerlerde `ov.setAttribute('role','dialog');ov.setAttribute('aria-modal','true')`).

19. **Fotoğraf modu `pbars` bayrağı sıfırlanmıyor** — w_app.html, anahtar: `document.body.classList.remove('photo','bars');$('#photo').hidden=true`
    `photoOff` sınıfı kaldırıyor ama modül değişkeni `pbars` true kalıyor; bir sonraki P'de düğme `aria-pressed=true` gösterirken bantlar kapalı, ilk tıklama "kapatır" (görünürde hiçbir şey olmaz).
    Düzeltme: photoOff içine `pbars=false;const pb=document.querySelector('[data-act="pbar"]');pb&&pb.setAttribute('aria-pressed','false');`.

20. **Sarayın Kapısı sonunda "İçgörü alındı 6/6" ve görev paneli overlay arkasında açık** — w_app.html, anahtar: `toast('İçgörü alındı',\`${doneCount()}/6 · ${PATHS[k].name} yolu\`)` ve finaleSaray `onEnd` içinde `mode='ov'`
    Bellek'in içgörüsü `doneCount()`'a girmediğinden toast "6/6" tekrar eder; `finaleSaray` onEnd'de `mode='ov'` yaptıktan sonra `dNext` `objectives()` çağırıp `#obj`'yi görünür bırakır (overlay arkasında). Kozmetik.
    Düzeltme: toast'ta `cur==='bellek'?'Yedinci içgörü':\`${doneCount()}/6\`` ve finaleSaray onEnd sonunda `$('#obj').hidden=true`.

21. **NG+'da mektuplar korunurken sekme metni çelişiyor (olası)** — w_app.html, anahtar: `gate7Open()?'Bellek Sarayı’nın üç odasında.':'Yedinci geçit henüz kapalı: altı parça ve Kayıt Sekiz gerek.'`
    keep listesi artık `letters` ve `rec8` taşıyor ama `frags` sıfırlanıyor; Mektuplar sekmesi "3/3 okundu" ile "Yedinci geçit henüz kapalı" satırını aynı anda gösteriyor. Tasarım kararıysa metni "İkinci turda altı parçayı yeniden topla" diye özelleştir.
    Düzeltme: `S.tour>=2&&!gate7Open()?'İkinci tur: altı parçayı yeniden topla.':…`.

## Kontrol edilip sorun bulunmayanlar (kısa)
- `GAME.realms` varsayımları: `doneCount`, `fragCount`(bellek dışlanır), `renderMap`, `sealed` döngüsü, `navTarget`, `hubDef` Çekirdek kilidi yedinci boyuttan etkilenmiyor; `realmDef`/`objectives`/`insightOv` realm7 alanlarıyla (points/figures/zone/zoneText/hal/insight/mirror/letters) uyumlu. `wxTick`/`cmp` bellek'te `comp` yokken güvenli.
- VOX: aynı anda iki utterance olmuyor (`speak` önce `stop`); sorun yalnız 10 numaradaki "kim kimi kesiyor" meselesi. CHAT banter `speechSynthesis.speaking` ile yol veriyor.
- GPAD ile klavye `pushInput()`'ta toplanıyor, `prev` dizisi ilk turda güvenli, `poll` try/catch'li.
- Eski kayıt: `fresh()` ile üst düzey birleştirme var; `S.sinyal` her zaman `{on,found}` olarak yaratılıyor; `S.daily` yarım kalmışsa `enterWorld` sıfırlıyor (tekcan/karanlık etkileri ilk boyut yolculuğunda temizleniyor).
- Zamanlayıcılar: `cmp`, `wikiCard`, `DAILY.arrive` toast'u, `interact frag → playHal`, `flowArel` mod/boyut kontrollü; `closeMini` YK zamanlayıcılarını temizliyor; `travel` `storm`, `wxOn`, `cmpT`, `halCap`, `mirrorSaid/Tip`, CHAT'i temizliyor (eksik olan yalnız `halWas`, bkz. 7).
