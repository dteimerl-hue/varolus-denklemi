# -*- coding: utf-8 -*-
"""GitHub'a yayınlama yardımcısı (gh CLI olmadan).

Git Credential Manager ile github.com için kayıtlı oturumu kullanır:
  1) depoyu oluşturur (yoksa)      2) ortak çalışanı davet eder
  3) GitHub Pages'i açar (main / kök)  4) remote ekler ve main dalını iter
  5) sürüm (release) oluşturup paket zip'ini yükler

Kullanım:  python yayinla.py [--repo varolus-denklemi] [--collab Mertstoy] [--tag v29] [--private]
Önce bir kez:  git credential-manager github login
"""
import argparse,json,os,subprocess,sys,urllib.request,urllib.error,io
P=argparse.ArgumentParser();P.add_argument('--repo',default='varolus-denklemi');P.add_argument('--collab',default='Mertstoy');P.add_argument('--tag',default='v29');P.add_argument('--private',action='store_true');P.add_argument('--zip',default='Varolus-Denklemi-Paket.zip');A=P.parse_args()
def cred():
    env=dict(os.environ,GCM_INTERACTIVE='never',GIT_TERMINAL_PROMPT='0')
    r=subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\n\n',capture_output=True,text=True,env=env)
    d=dict(l.split('=',1) for l in r.stdout.splitlines() if '=' in l)
    if not d.get('password'):sys.exit('GitHub oturumu bulunamadı. Önce şunu çalıştırın:  git credential-manager github login')
    return d.get('username'),d['password']
USER_HINT,TOK=cred()
def api(method,path,body=None,raw=None,ctype='application/json',ok=(200,201,204,202)):
    url=path if path.startswith('http') else 'https://api.github.com'+path
    data=raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
    req=urllib.request.Request(url,data=data,method=method,headers={'Authorization':'token '+TOK,'Accept':'application/vnd.github+json','User-Agent':'varolus-yayinla','Content-Type':ctype,'X-GitHub-Api-Version':'2022-11-28'})
    try:
        with urllib.request.urlopen(req,timeout=120) as r:
            t=r.read().decode('utf-8','replace');return r.status,(json.loads(t) if t.strip().startswith(('{','[')) else t)
    except urllib.error.HTTPError as e:
        t=e.read().decode('utf-8','replace')
        try:j=json.loads(t)
        except Exception:j={'message':t[:200]}
        return e.code,j
st,me=api('GET','/user');assert st==200,('kullanıcı okunamadı',st,me.get('message'))
LOGIN=me['login'];print('GitHub hesabı:',LOGIN)
# 1) depo
st,r=api('GET',f'/repos/{LOGIN}/{A.repo}')
if st==404:
    st,r=api('POST','/user/repos',{'name':A.repo,'description':'Varoluş Denklemi — tek dosyalık Türkçe 3B keşif oyunu (Three.js)','private':A.private,'has_issues':True,'has_wiki':False,'auto_init':False})
    assert st==201,('depo oluşturulamadı',st,r.get('message'));print('depo oluşturuldu:',r['html_url'])
else:
    assert st==200,('depo sorgusu',st,r.get('message'));print('depo zaten var:',r['html_url'])
HTML=r['html_url'];CLONE=r['clone_url']
# 2) ortak çalışan
if A.collab:
    st,r2=api('PUT',f'/repos/{LOGIN}/{A.repo}/collaborators/{A.collab}',{'permission':'push'})
    print('ortak çalışan:',A.collab,'→',{201:'davet gönderildi',204:'zaten ekli'}.get(st,f'hata {st}: {r2.get("message") if isinstance(r2,dict) else r2}'))
# 3) remote + push
def git(*a,check=True):
    r=subprocess.run(['git',*a],capture_output=True,text=True);
    if check and r.returncode:print(r.stderr.strip()[:400]);sys.exit('git hatası: '+' '.join(a))
    return r.stdout.strip()
remotes=git('remote')
if 'origin' not in remotes.split():git('remote','add','origin',CLONE)
else:git('remote','set-url','origin',CLONE)
print('itiliyor…');git('push','-u','origin','main');print('main dalı itildi')
# 4) Pages
st,r3=api('GET',f'/repos/{LOGIN}/{A.repo}/pages')
if st==404:
    st,r3=api('POST',f'/repos/{LOGIN}/{A.repo}/pages',{'source':{'branch':'main','path':'/'}})
    print('Pages:',{201:'açıldı'}.get(st,f'hata {st}: {r3.get("message") if isinstance(r3,dict) else r3}'))
else:print('Pages zaten açık' if st==200 else f'Pages sorgusu {st}')
PAGES=f'https://{LOGIN.lower()}.github.io/{A.repo}/'
# 5) sürüm + zip
if os.path.exists(A.zip):
    st,rel=api('GET',f'/repos/{LOGIN}/{A.repo}/releases/tags/{A.tag}')
    if st==404:
        st,rel=api('POST',f'/repos/{LOGIN}/{A.repo}/releases',{'tag_name':A.tag,'name':'Varoluş Denklemi '+A.tag,'body':'Çevrimdışı tek dosyalık paket. Zip\'i klasöre çıkarın, Varolus-Denklemi.html dosyasını çift tıklayın; ayrıntılar OKU-BENI.txt içinde.','draft':False,'prerelease':False})
        assert st==201,('sürüm oluşturulamadı',st,rel.get('message'))
        print('sürüm oluşturuldu:',rel['html_url'])
    else:print('sürüm zaten var:',rel['html_url'])
    if not any(a.get('name')==os.path.basename(A.zip) for a in rel.get('assets',[])):
        up=rel['upload_url'].split('{')[0]+'?name='+os.path.basename(A.zip)
        with open(A.zip,'rb') as f:data=f.read()
        st,r4=api('POST',up,raw=data,ctype='application/zip')
        print('zip yüklendi' if st==201 else f'zip yüklenemedi {st}: {r4.get("message") if isinstance(r4,dict) else r4}')
    else:print('zip zaten yüklü')
print('\nBİTTİ\n depo   :',HTML,'\n oyun   :',PAGES,'(Pages birkaç dakika içinde yayına girer)\n sürüm  :',HTML+'/releases',f'\n {A.collab} daveti e-postasına ve github.com bildirimlerine düşer; kabul edince yazma yetkisiyle çalışabilir.')
