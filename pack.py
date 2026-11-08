# -*- coding: utf-8 -*-
"""Tamamen çevrimdışı, tek dosyalık paket: CDN scriptleri ve tüm asset'ler HTML'in içine gömülür."""
import io,os,re,base64,urllib.request,zipfile,mimetypes
SRC='varolus-denklemi.html';OUT_DIR='paket';os.makedirs(OUT_DIR,exist_ok=True)
html=io.open(SRC,encoding='utf-8').read()
def fetch(u):
    req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'});return urllib.request.urlopen(req,timeout=60).read().decode('utf-8')
def inline_script(m):
    u=m.group(1);js=fetch(u).replace('</script>','<\\/script>');return '<script>/* '+u.split('/npm/')[-1]+' */\n'+js+'\n</script>'
html,n=re.subn(r'<script src="(https://cdn\.jsdelivr\.net/[^"]+)"[^>]*></script>',inline_script,html);print('inlined scripts',n)
b64=io.open('assets/soldier.txt',encoding='ascii').read().strip()
old="fetch('assets/soldier.txt').then(r=>r.text())";assert old in html
html=html.replace(old,"Promise.resolve(window.__SOLDIER)")
def duri(name):
    p=os.path.join('assets',name);mt='image/webp' if name.endswith('.webp') else (mimetypes.guess_type(p)[0] or 'application/octet-stream')
    return 'data:'+mt+';base64,'+base64.b64encode(open(p,'rb').read()).decode('ascii')
cards={c[5:-5]:duri(c) for c in os.listdir('assets') if c.startswith('card-')}
html=html.replace('src="assets/card-${to}.webp"','src="${window.__CARDS[to]||\'\'}"')
html=html.replace('<script>','<script>window.__CARDS='+str(cards).replace("'",'"')+';window.__SOLDIER="'+b64+'";</script>\n<script>',1)
for name in sorted(set(re.findall(r'assets/([A-Za-z0-9_.-]+\.(?:webp|mp4))',html))):
    if not os.path.exists(os.path.join('assets',name)):continue
    html=html.replace('assets/'+name,duri(name))
print('left refs',re.findall(r'assets/[A-Za-z0-9_.${}-]+',html)[:5])
# --- yazı tiplerini göm (Google Fonts bağlantısı yerine); başarısız olursa bağlantılar kalır, sistem yazı tipine düşer
def inline_fonts(html):
    m=re.search(r'<link rel="stylesheet" href="(https://fonts\.googleapis\.com/css2[^"]+)">',html)
    if not m:return html,0
    UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
    css=urllib.request.urlopen(urllib.request.Request(m.group(1).replace('&amp;','&'),headers={'User-Agent':UA}),timeout=60).read().decode('utf-8')
    keep=[];n=0
    for sub,block in re.findall(r'/\*\s*([a-z-]+)\s*\*/\s*(@font-face\s*\{[^}]+\})',css):
        if sub not in('latin','latin-ext'):continue
        u=re.search(r'url\((https://[^)]+\.woff2)\)',block)
        if not u:continue
        data=urllib.request.urlopen(urllib.request.Request(u.group(1),headers={'User-Agent':UA}),timeout=60).read()
        keep.append(block.replace(u.group(1),'data:font/woff2;base64,'+base64.b64encode(data).decode('ascii')));n+=1
    if not n:return html,0
    html=html.replace(m.group(0),'<style>/* gömülü yazı tipleri: Cormorant Garamond, IBM Plex Sans, IBM Plex Mono (SIL OFL) */\n'+'\n'.join(keep)+'\n</style>')
    html=re.sub(r'<link rel="preconnect" href="https://fonts\.(?:googleapis|gstatic)\.com"[^>]*>\s*','',html)
    return html,n
try:
    html,nf=inline_fonts(html);print('inlined fonts',nf)
except Exception as ex:
    print('font inline skipped:',ex)
if '<meta charset' not in html[:400]:
    html='<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body style="margin:0">'+html+'</body></html>'
out=os.path.join(OUT_DIR,'Varolus-Denklemi.html');io.open(out,'w',encoding='utf-8').write(html)
readme='''VAROLUŞ DENKLEMİ — tek dosyalık tarayıcı oyunu

KURULUM (kurulum yok)
1. Zip dosyasına sağ tıklayıp "Tümünü ayıkla" deyin. Oyunu zip'in içinden açmayın; önce klasöre çıkarın.
2. Varolus-Denklemi.html dosyasını çift tıklayın. Windows'ta Oyunu-Baslat.bat, Mac/Linux'ta oyunu-baslat.sh da aynı işi yapar.
3. Dosya güncel bir tarayıcıda açılmalı: Chrome, Edge veya Firefox. Eski bir programla açılırsa dosyaya sağ tıklayıp
   "Birlikte aç" ile Chrome ya da Edge seçin.
4. İnternet gerekmez. Motor, müzik, karakterler, görseller ve yazı tipleri dosyanın içindedir.
   İlk açılış 5–15 saniye sürebilir (dosya yaklaşık 34 MB).
5. Başlık ekranında "Sesle başla" ile müzik, ambiyans ve seslendirme açılır.

GEREKSİNİMLER
- Windows 10/11, macOS veya Linux; WebGL destekleyen ekran kartı (son on yılın hemen her bilgisayarı).
- Yavaşlarsa üstteki kalite düğmesinden 1080p seçin; oyun kendisi de kaliteyi otomatik düşürür.
- Seslendirme tarayıcının Türkçe sesini kullanır. Türkçe ses yüklü değilse diyaloglar yalnız yazıyla akar.

KONTROLLER
WASD / ok tuşları: yürü · Shift: koş · Fare sürükle: kamera · Tekerlek: yakınlaş
E: etkileşim · 1/2/3: diyalog seçimi · F (basılı tut): Sis Feneri · P: fotoğraf modu · Esc: kapat
J ya da Günlük düğmesi: veriler, defter, dosya, harita, başarımlar
Kumanda: sol çubuk yürü, sağ çubuk kamera, A etkileşim. Dokunmatik: sol altta joystick, E, F ve kamera düğmeleri.

İNTERNET VARSA EK OLARAK ÇALIŞANLAR
- Gökyüzü Terminali (NASA günün görüntüsü), Wikipedia kaynak kartları
- Sismograf (USGS canlı depremler; internet yoksa kayıtlı örnek veri), ISS'yi Yakala (canlı konum)

PAYLAŞIMLI ÖZELLİKLER BU PAKETTE NASIL ÇALIŞIR
Pakette sunucu yoktur; bu yüzden paylaşımlı özellikler yerel bir arşivle çalışır. Motor bunu oyunda açıkça söyler.
- Yankı Taşları: her boyutta mürettebatın bıraktığı taşlar ve oyları görünür. Kendi taşınızı bırakınca bir kod çıkar
  (YT-XXX). Arkadaşınız bu kodu kendi oyunundaki taşa girerse taşınız onun sisinde de belirir; siz de onunkini girebilirsiniz.
- Günün Tohumu panosu: mürettebatın o günkü koşuları ve sizin süreniz. Süre kodunu (GT-XXXXXXX) arkadaşınıza
  gönderirseniz aynı günün panosunda yan yana görünürsünüz.
- Son istatistikleri: mürettebatın oyları, bu bilgisayardaki sonlar ve girdiğiniz arkadaş Yol Kartı kodları (VD-...).
- Tesisteki gözlemciler: önceki oturumlarınızın yürüyüş izleri soluk siluetler olarak dolaşır. Aynı bilgisayarda oyunu
  ikinci bir pencerede açarsanız iki pencere birbirini canlı görür.
İnternet üzerinden canlı, herkese açık pano ve taşlar yalnız claude.ai sürümünde vardır.

KAYIT
- İlerleme, dosyayı açtığınız tarayıcıda saklanır. Aynı bilgisayarda aynı tarayıcıyla açarsanız kaldığınız yerden sürer.
- Dosyayı başka bir klasöre taşırsanız ya da başka tarayıcı kullanırsanız oyun baştan başlar.
- Tarayıcı geçmişini/site verilerini silmek kaydı da siler.

SORUN GİDERME
- Siyah ekran: tarayıcıyı güncelleyin; tarayıcı ayarlarında "donanım hızlandırma" açık olsun.
- Ses yok: başlıkta "Sesle başla"yı seçin; tarayıcı sekmesinin sesi kapalı olmasın.
- .bat dosyası için Windows uyarı verirse kullanmanız gerekmez; html dosyasını çift tıklamak yeterlidir.

Açık kaynaklar ve veri kaynakları: başlık ekranındaki "Açık kaynaklar" düğmesi.
'''
io.open(os.path.join(OUT_DIR,'OKU-BENI.txt'),'w',encoding='utf-8-sig',newline='\r\n').write(readme)
bat='@echo off\r\nrem Varolus Denklemi: oyunu varsayilan tarayicida acar\r\nstart "" "%~dp0Varolus-Denklemi.html"\r\n'
io.open(os.path.join(OUT_DIR,'Oyunu-Baslat.bat'),'w',encoding='ascii',newline='').write(bat)
sh='#!/bin/sh\n# Varolus Denklemi: oyunu varsayilan tarayicida acar\nd="$(cd "$(dirname "$0")" && pwd)"\nf="$d/Varolus-Denklemi.html"\nif command -v xdg-open >/dev/null 2>&1; then xdg-open "$f"; else open "$f"; fi\n'
io.open(os.path.join(OUT_DIR,'oyunu-baslat.sh'),'w',encoding='ascii',newline='').write(sh)
z=zipfile.ZipFile('Varolus-Denklemi-Paket.zip','w',zipfile.ZIP_DEFLATED,compresslevel=9)
z.write(out,'Varolus-Denklemi/Varolus-Denklemi.html');z.write(os.path.join(OUT_DIR,'OKU-BENI.txt'),'Varolus-Denklemi/OKU-BENI.txt');z.write(os.path.join(OUT_DIR,'Oyunu-Baslat.bat'),'Varolus-Denklemi/Oyunu-Baslat.bat')
zi=zipfile.ZipInfo('Varolus-Denklemi/oyunu-baslat.sh');zi.external_attr=0o755<<16;zi.compress_type=zipfile.ZIP_DEFLATED;z.writestr(zi,sh);z.close()
print('html MB',round(os.path.getsize(out)/1e6,1),'zip MB',round(os.path.getsize('Varolus-Denklemi-Paket.zip')/1e6,1))
