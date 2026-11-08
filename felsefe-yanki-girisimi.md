# Yankı Girişimi

**Felsefe:** Anlam, tek bir sesin içinde değil, seslerin birbirine çarptığı yerde doğar. Dört kaynak, dört ton; her biri yalnızken düz bir halka, birlikteyken bir desen. Hatırlamak, dağılmış halkaları tekrar üst üste getirmektir.

**Algoritmik ifade:** Tuval dört noktadan yayılan dairesel dalgalardan kuruludur. Her kaynak kendi frekansını taşır (pentatonik oran: 1, 5/4, 3/2, 2) ve çalındığı anda genliği 1'e sıçrayıp üstel sönümle (yarı ömür 600 ms) kaybolur. Piksel yoğunluğu dört dalganın toplamının karesidir: aynı fazda çakışan tepeler parlak düğümler, zıt fazlar karanlık boşluklar üretir. Oyuncunun doğru tonu, Motor'un dizisiyle aynı kaynağı tekrar uyandırdığında desen eski halini geri "hatırlar"; yanlış ton, dördüncü bir faz kayması ekleyerek deseni bulandırır.

**Zaman:** Her kare, önceki karenin %92'sini taşır. Bu ağır bellek, ekranı bir süre önce duyulanın hayaletiyle doldurur; işitsel çalışma belleğinin dört öğelik sınırı (Cowan) burada görünür olur: beş kaynağın hayaleti aynı anda tutulamaz, desen kendini siler. Tur ilerledikçe sönüm kısalır; dizi uzadıkça görsel de belleğini kaybeder.

**Tohumlu değişim:** Kaynak konumları, turun tohumu ile altın açı (137,5°) üzerinde döndürülür; aynı tur aynı deseni verir, her oyun oturumu farklı yerleşim görür. Renk, genlik toplamından türetilir: sıcak amber (doğru), soğuk lila (bekleme), kızıl (hata).

**Zanaat:** Algoritma 2D canvas üzerinde 96×96 örnekleme ızgarasıyla hesaplanır ve bilineer ölçeklenir; 60 fps'de 1 ms altında kalır. Her sabit, sayısız denemeyle kulağa ve göze aynı anda hizalanmış, ustalıkla işlenmiş bir bütünün parçasıdır: tempo 480 ms, ton 260 ms, sönüm 600 ms, hafıza 0,92.

*(Not: Bu felsefe oyun içinde p5.js yerine saf canvas ile, Yankı Dizisi mini oyununun arka planı olarak uygulanmıştır.)*
