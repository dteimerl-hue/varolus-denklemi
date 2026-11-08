# Sis Akışı — algoritmik felsefe (algorithmic-art geçişi)

**Hareket:** *Sis Akışı* (Fog Drift). Bilinmeyenin görselleştirilmesi: Motor'un "bilmediği yerde sis gösterir" kuralı, bir akış alanı olarak kodlanır.

**İlke.** Her boyutun zemini üstünde, tohumlanmış bir gürültü alanı (fbm, 3 oktav) yön belirler; 1.400 foton bu alanı izler, ömürleri bitince adanın rastgele bir noktasında yeniden doğar. Hiçbir karede desen aynı değildir; yine de aynı tohum aynı akışı doğurur. Güzellik son karede değil, süreçtedir: parçacıklar yavaşça yükselip alçalır, hava olayları (foton fırtınası, çökme dalgası, nöbet) akış hızını ve parlaklığı çarpar, saha içinde sis kırmızıya kayar.

**Hesaplamalı malzeme.** Yön = fbm(x·0,045 + tohum, z·0,045, t·0,06) · 4π; hız 1,6 birim/sn; yükseklik zemin + 0,4 + sin(t·0,7 + i)·0,9. Renk boyutun rengidir, parlaklık 0,35–1,0 arasında tohumdan türer. Toplamsal karışım, derinlik yazmadan; parçacıklar birbirine değdikçe ışık birikir, "yoğunluk haritası" kendiliğinden oluşur.

**Gök katmanı.** Aynı felsefe gökte iki hızda yaşar: kayan yıldızlar (12 iz, 70–140 birim/sn, 0,5–1,1 sn ömür) ve yere yakın fotonlar (36 iz, 3–10 birim/sn). Meteor yağmurunda bekleme süreleri 0,6 ile çarpılır; aurora perdeleri (5 düzlem, köşe z = sin(x·0,08 + t·0,9) · 4) yeşilden mora kayar.

**Zanaat.** Parametreler sayısız yinelemeyle seçildi: parçacık sayısı GPU'yu zorlamadan "canlı" okunacak kadar; hız, yürüyen oyuncunun gözünde akışın fark edilip takip edilmeyeceği kadar yavaş; opaklık 0,55 ± 0,25 nefes gibi. Ustalık, rastgeleliği görünmez kılmakta değil, onu niyetli göstermektedir.
