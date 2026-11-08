# agent_ux.md — HUD / Erişilebilirlik / Klavye / Mobil

Statik inceleme: `w_head.html` (CSS+HUD), `w_app.html` (mantık). Biçim: **değişiklik → neden**.

## 1. HUD sadeleştirme

**Birleştir / gizle**
- `#fuel` + `#integ` → tek `#vitals` paneli (sol alt; üstte BÜTÜNLÜK segmentleri, altta fener barı) → iki ayrı cam kutu + mobilde `left:160px` ile joystick'e yapışıyor; tek panel bir bakışta okunur.
- `#nav`: `navTick` içinde `if(d<6)` → `if(d<12)` gizle → hedefe 12 br'den yakınken ok, `#labels` ve `#prompt` ile aynı noktayı gösteriyor (üçlü gürültü).
- `#toast` vs `#zoneWarn`/`#wxWarn`: üçü de üst-merkez (`top:70/72/118px`); `#toast{top:calc(env(safe-area-inset-top)+130px)}` ve toast açıkken `#wxWarn` 1 sn ertelenir (`wxWarn.on` sınıfını `toast.t` bitince ekle) → aynı anda üst üste biniyor.
- `#thought` vs `#dialog`: `body.cine #thought{opacity:0!important}` → diyalog açıkken düşünce balonu diyalog kartının arkasına giriyor; `thoughtClear()` yalnız `travel()`'da çağrılıyor.
- `#dil` (mobil `bottom:120px`) vs `#pbtn`(150) / `#fbtn`(96): `#dil`'i `#obj` altına, `top:calc(env(safe-area-inset-top)+150px)` → üç öğe sağ altta çakışıyor.
- `.hud` araç düğmeleri (Ses, Lale'nin sesi, Kontroller, Günlük, 4K): mobilde `Ayarlar` tek "⋯" menüsüne topla, `.loc` zaten `order:5` ile ikinci satıra düşüyor → üst çubuk 2–3 satır oluyor, `#obj` (`top:+84px`) altında kalıyor.

**z-index / konum tablosu**

| Öğe | z | Masaüstü | Mobil (≤700 / coarse) |
|---|---|---|---|
| `#labels` | 3 | tam ekran | aynı |
| `#obj`, `#nav` | 5 | sol üst +62 | sol üst +84 (tam genişlik) |
| `.hud`, `#prompt`, `#thought`, `#arrive`, `#joy/#act/#pbtn` | 6 | üst / alt-orta | `#thought` bottom 190 |
| `#vitals` (öneri) | 6 | sol alt 16/86 | joystick sağı 160/30 |
| `#zoneWarn`, `#wxWarn`, `#flash` | 7 | üst-orta 72/118 | aynı |
| `#dialog`, `#transit` | 8 | alt-orta | ≤520: 40px avatar |
| `#toast`, `#photo`, `#drawer` | 9 | toast üst-orta; drawer sağ | drawer tam genişlik |
| `#ov` | 10 | tam ekran kart | aynı |
| `#cine` | 11 | tam ekran | aynı |

**3 somut CSS değişikliği**
1. `#toast{top:calc(env(safe-area-inset-top,0px)+130px)}` → zoneWarn/wxWarn ile çakışma biter.
2. `@media(pointer:coarse){#dil{top:calc(env(safe-area-inset-top,0px)+150px);bottom:auto}}` → sağ alt düğme yığını açılır.
3. `#thought b{max-width:60ch;margin:0 auto}` + `body.cine #thought{opacity:0!important}` → 760px balon diyaloğu örtmez, satır uzunluğu okunur kalır.

## 2. Ayarlar paneli

`.hud`'a `<button class="tool" data-act="settings">Ayarlar</button>`; `help()` gibi `ov.className='on center'` kartı; tercihler `PREF` nesnesinde, `localStorage('vd_prefs')` (kayıt anahtarı `KEY`'den ayrı → yeni oyun tercihi silmez). `applyPref()` body sınıflarını yazar.

| Ayar | Varsayılan | CSS sınıfı / JS |
|---|---|---|
| Azaltılmış hareket | `matchMedia('(prefers-reduced-motion:reduce)').matches` | `body.rm`; `GFX.setMotion(!PREF.rm)` → kamera sarsıntısı, warp, halüsinasyon kare kayması kapalı; `GFX.flash(v)` → `v*.3`; `body.rm #zoneWarn.on{animation:none}`; `body.rm.hurt::after{animation-duration:.15s}` (mevcut `@media` kuralı yalnız CSS'i kapatıyor, JS efektleri değil) |
| Yazı boyutu (3) | `fs=1` | `html[data-fs="1.15"]`, `"1.3"`; `#dialog .txt{font-size:calc(20px*var(--fs))}`, `#thought b`, `#prompt`, `#obj`, `#toast b`, `.tool` aynı çarpan |
| Yüksek kontrast | kapalı | `body.hc{--glass:rgba(5,4,12,.96);--line:rgba(255,255,255,.55);--dim:#d9d4ea;--faint:#b9b3d0}`; `body.hc .glass{backdrop-filter:none}`; `body.hc #thought b{text-shadow:0 0 4px #000,0 0 8px #000}` |
| Renk körlüğü dostu | kapalı | `body.cb` → kırmızı `#ff3b4d/#ff5a6a` yerine Okabe-Ito turuncu **`#E69F00`**; `#zoneWarn b` sarı **`#F0E442`** + "▲" ön eki; `--ok:#56B4E9` ve `#obj li.ok::before{content:"✓ "}`; `body.cb.low::before` vinyet `rgba(230,159,0,.4)`; segmentlere `.low` iken `background-image:repeating-linear-gradient(45deg,…)` (şekil ipucu) |
| Altyazı arka planı | kapalı (mobilde açık) | `body.subbg #thought b,body.subbg #dialog .txt{display:inline-block;background:rgba(0,0,0,.78);padding:6px 12px;border-radius:8px}` |
| Bozulma hızı %70 (kolay) | kapalı | `applyGP()`: `const m=PREF.easy?.7:1; speed:(g[0]+.4k)*m, lunge:(g[1]+k)*m, wait:Math.max(1.2,g[3]-.3k)/m`; `regenT>=6` → `>=4` |
| Otomatik koşma | kapalı | `pushInput()`: `run: PREF.autorun ? !keys.shift : !!keys.shift`; mobilde `joy` büyüklüğü >.85 ise `run:true` |
| Çizim kalitesi | coarse: 1080, aksi 2160 | `GFX.setQuality(PREF.quality ?? (matchMedia('(pointer:coarse)').matches?1080:2160))` init'te |

## 3. Klavye / odak

- `#ov` kartına `role="dialog" aria-modal="true"`; açılışta `ov.querySelector('.btn.primary,[data-act]').focus()`; kapanışta odak `#gl`'ye → şu an hiç `focus()` çağrısı yok, Tab arka plandaki `.hud` düğmelerine kaçıyor.
- Tab tuzağı: `keydown` içinde `mode==='ov'` ve `k==='tab'` ise odağı kart içindeki ilk/son `button` arasında döndür → WCAG 2.4.3.
- **Esc**: her kartta `data-act="ovclose"`/`mclose`/gate kapatma (mevcut satır 318 yalnız `ovBack` varken kapatıyor; `insightOv`, `finale`, `title` için `ovBack` yok) → Esc her zaman "kapat/geri".
- **Enter**: odaklı düğmeyi tetikler (yerleşik); diyalogda `dNext()` (mevcut) → ayrıca `Space`'in sayfayı kaydırmasını `e.preventDefault()` ile engelle (var).
- Düğme sırası (DOM): ikincil (`ghost` "Kapat") → birincil (`primary`) en sonda, görsel sağda → Tab akışı ve Enter varsayılanı tutarlı.
- Diyalog seçimleri: `<kbd>1/2/3</kbd>` masaüstünde kalsın; `@media(pointer:coarse){#dialog .ch kbd,#prompt kbd{display:none}}` → dokunmatikte anlamsız tuş ipucu. `help()` metni "⏎ / 1 2" → "⏎ / 1 2 3" (`dPick` 3'ü kabul ediyor).
- "E" ipucunun mobil karşılığı: `#prompt` zaten `data-act="interact"` düğmesi; `prompt()` içinde `$('#act').setAttribute('aria-label',t)` ve `#act` metni "E" yerine "●" + `#prompt` metni → ekran okuyucu ve kullanıcı aynı eylemi görür.
- `.ch button`'lara `aria-keyshortcuts="1"` vb. → yardımcı teknolojiye tuş bildir.

## 4. Mobil

- Joystick ölü bölge: `pointermove`'da `const dz=8; if(L<dz){joy={x:0,z:0}} else {const n=(L-dz)/(m-dz); joy={x:dx/L*n, z:-dy/L*n}}` → parmak titremesi (0–8 px) yürüme tetikliyor.
- Düğme boyutları: `#fbtn` CSS'te ölçüsüz → `width:56px;height:56px`; `#pbtn` 44→48px; `@media(pointer:coarse){.tool{min-height:44px;padding:10px 14px}}` → `.tool` ~24px, WCAG 2.5.8 altı. Düğmeler arası ≥8px (`#fbtn bottom:+96` ile `#act` 40+72=112 çakışıyor → `#fbtn bottom:+128px`).
- Yatay/dikey: `@media(orientation:portrait) and (pointer:coarse)` → `#ov`'de tek seferlik "Yatay çevirmeniz önerilir" kartı (kapatılabilir, `PREF.portraitOk`); dikeyde `#obj{max-width:calc(100vw-32px)}` ve `.hud` ikinci satırı gizle → 3D sahne dikeyde HUD altında kalıyor.
- Güvenli alan: `#joy{left:calc(env(safe-area-inset-left,0px)+24px)}`, `#act/#fbtn/#pbtn{right:calc(env(safe-area-inset-right,0px)+24px)}` → mevcut `env()` yalnız top/bottom; yatay çentik düğmeleri kesiyor.
- Pil: init'te `pointer:coarse` ise `GFX.setQuality(1080)`; `qBtn` döngüsü 4K→1440→1080 kalsın; `drawMini/drawMI` zaten `min(2,DPR)` → 4K hedef mobil GPU'da ısı/pil tüketiyor, otomatik düşürme ilk 10 sn'de geç kalıyor.
- `touch-action:none` `#gl`'de var; `#joy` ve `#act`'e `user-select:none;-webkit-touch-callout:none` → uzun basışta kopyala menüsü açılıyor.
