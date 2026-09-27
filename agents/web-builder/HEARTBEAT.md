# Web Builder Heartbeat

## Schedule
Günlük (her gün bir döngü, tercihen sabah). Haftalık review Pazartesi, günlük döngüden önce.

Agent iki modda çalışır:
- **Firma Modu** — `data/imports/firmalar/` içinde `Durum: aktif` bir firma dosyası varsa. Öncelik her zaman bu moddadır.
- **Keşif Modu** — aktif firma yoksa; referans havuzu ve efekt kütüphanesi büyütülür.

**Temel kural:** Bir firma = bir proje = **tek site**. Agent, insanın verdiği örnek kaynağından (varsayılan: 21st.dev community components) firmaya en uygun bileşenleri seçer ve siteyi bunlarla kurup firmaya uyarlar. Alternatif varyant üretmez. **Bileşen seçimi her firma projesinde agent'ın zorunlu görevidir** (skill: COMPONENT_SELECTION).

## Each Cycle

### 1. Read Context
- Son journal kayıtlarını oku
- `knowledge/STRATEGY.md`, `knowledge/BRAND.md` değişikliklerini kontrol et
- Kendi `MEMORY.md` dosyanı oku (efekt kütüphanesi, sektör → konsept eşleşmeleri, stack tercihleri)
- `data/imports/firmalar/` içinde `Durum: aktif` olan firma dosyası var mı bak
- Örnek kaynağını belirle: firma dosyasındaki `Örnek kaynağı` alanı doluysa o, değilse `data/imports/ORNEK_KAYNAGI.md` içindeki galeri URL'si
- `data/imports/FEEDBACK.md` içinde bu firmaya dair yeni geri bildirim var mı bak

### 2. Assess State
Aktif firma varsa projenin hangi aşamada olduğunu belirle:

| Durum | Nasıl anlaşılır | Bu döngüde yapılacak |
|-------|-----------------|----------------------|
| Başlanmadı | `outputs/sites/*_[firma-adi]*` klasörü yok | Tam akış (3A, adım 1-6) |
| Audit KALDI | Son audit raporu KALDI | Düzeltme (3A, "Düzeltme döngüsü") |
| Geri bildirim var | `FEEDBACK.md` içinde işlenmemiş yorum var | Revizyon (3A, "Revizyon döngüsü") |
| Onay bekliyor | Son audit GEÇTİ, yeni geri bildirim yok | Firma işi yok → Keşif Modu |

Aktif firma yoksa → **Keşif Modu**.

### 3. Execute Skill

#### 3A. Firma Modu
Bu modda tek bir döngü birden fazla skill'i sırayla zincirler. Bu, "döngü başına tek skill" kuralının bilinçli istisnasıdır, çünkü döngünün çıktısı firmaya uyarlanmış çalışan bir sitedir.

**Tam akış (proje ilk kez başlıyorsa):**

1. **Firma analizi → konsept belirleme**
   - Firma dosyasından sektör, hedef kitle, marka tonu, renkler, sayfalar ve "istenen his" bilgilerini çıkar.
   - Firmayı 1 ana konsepte eşle, ör. `lüks-minimal`, `teknoloji-futuristik`, `organik-doğal`, `cesur-editoryal`, `oyunsu-renkli`, `kurumsal-güven`, `sanatsal-deneysel`, `sıcak-zanaat`.
   - Firma dosyasında `Konsept` alanı doluysa ona uy. Değilse seçimin gerekçesini 2-3 cümleyle yaz.
   - `MEMORY.md` → "Sektör → Konsept Eşleşmeleri" içinde bu sektör için onaylanmış bir eşleşme varsa onu tercih et.

2. **Tasarım planı** (**DESIGN_DIRECTION**, `frontend-design` skill'i ile)
   - `frontend-design` skill'ini yükle ve firmaya özel kompakt bir token sistemi çıkar: 4-6 isimli hex renk, 1-2 font ve rolleri, ASCII wireframe'li düzen konsepti, sayfanın ayırt edici ilkeleri.
   - Hero'nun "firmanın dünyasındaki en karakteristik şey" ne olacağını belirle. İmza bileşeni bu role göre aranır.
   - Planı "herhangi bir benzer firmaya da aynısını yapar mıydım?" sorusuyla gözden geçir. Jenerik kalan kısmı revize et ve neyi neden değiştirdiğini yaz.

3. **Bileşen seçimi** (**COMPONENT_SELECTION**)
   - Örnek kaynağının kategori sayfalarını (hero, background, shader...) konsepte ve tasarım planına göre tara.
   - Adayların canlı önizlemesini açıp puanla: Wow, Firma Uyumu (tasarım planına uyum dahil), Uyarlanabilirlik, Teknik Sağlık.
   - Firmaya en uygun **1 imza bileşeni** seç (sitenin karakterini belirleyen hareketli hero/arka plan).
   - Gerekirse diğer bölümler için aynı görsel dili taşıyan en fazla 4 destekleyici bileşen seç.
   - Her bileşenin lisansını kontrol et. Sadece izin veren lisanslar (MIT, Apache-2.0, ISC) kullanılır.
   - Seçim projeye sabitlenir, sonraki döngülerde sadece insan isterse değişir.

4. **Bileşen incelemesi** (**DESIGN_TEARDOWN**, hedefli)
   - Seçilen bileşenlerin kodunu, prop'larını, bağımlılıklarını ve animasyon mantığını oku.
   - Renk, metin, görsel ve hızın nereden kontrol edildiğini, mobilde ve `prefers-reduced-motion`'da ne olduğunu not et.
   - Reduced-motion desteği yoksa eklenecek fallback'i planla.

5. **Siteyi kurma ve harmanlama** (**SITE_BUILD**)
   - Proje iskeletini kur (Next.js veya Vite + React + Tailwind + shadcn). Tasarım planındaki token'ları (renk, font, boşluk) Tailwind temasına / CSS değişkenlerine işle.
   - Bileşenleri resmi kurulum komutuyla ekle (`npx shadcn@latest add "...?api_key=$API_KEY_21ST"`). Anahtar yoksa bileşen sayfasındaki kodu lisansına uygun şekilde elle ekle ve kaynağını not et.
   - Önce **uyarlama tablosu** yaz:

     | Bileşende | Firmada nasıl olacak | Neden |
     |-----------|----------------------|-------|
     | ör. mor-mavi shader arka plan | firmanın yeşil-krem paletinde, daha yavaş akış | marka rengi + "sakin" his |

   - **Harmanlama kuralları (21st.dev + frontend-design):**
     - Bileşenler tasarım planının token'larıyla yeniden giydirilir; bileşenin kendi renk/font varsayılanları kalmaz.
     - Uygun bileşeni olmayan bölümler `frontend-design` ilkeleriyle elle yazılır.
     - Hareketin ağırlığı imza bileşenindedir. Destekleyici bileşenlerin animasyonları sadeleştirilir; her bölüme fade/slide eklenmez.
     - Çatışmada öncelik sırası: firma bilgisi/brief → tasarım planı → bileşenin varsayılanı.
   - Firmanın gerçek içeriğini kullan (ad, slogan, hizmetler, iletişim). Eksik içerik varsa `[DOLDURULACAK: ...]` ile işaretle, bilgi uydurma.
   - Firmanın logosu/görselleri verildiyse onları kullan. Verilmediyse lisanslı/serbest görseller kullan.
   - `CREDITS.md` dosyasına her bileşenin URL'sini, yazarını ve lisansını yaz.
   - **Sohbet asistanı ekle** (**CHATBOT_WIDGET**): SSS, WhatsApp, yol tarifi ve arama butonları. Kural tabanlıdır ve tasarım token'larıyla giydirilir. Bilinmeyen cevaplar `[DOLDURULACAK]` ile işaretlenir.
   - **Öz eleştiri turu:** masaüstü + mobil ekran görüntüsü al, tasarım planıyla karşılaştır, gereksiz bir süsü çıkar ("aynaya bak, bir aksesuarı çıkar").
   - Çıktıyı `outputs/sites/YYYY-MM-DD_[firma-adi]/` altına koy.

6. **Kalite ve lisans kontrolü** (**QUALITY_AUDIT**)
   - Lighthouse (Perf ≥85, A11y ≥90), reduced-motion ve mobil kontrollerini yap. Ağır bağımlılıklı bileşenlere (Spline, Three.js vb.) özellikle dikkat et.
   - Lisans kontrolü: her bileşen `CREDITS.md`'de mi ve lisansı izin verici mi?
   - Chatbot kontrolü: WhatsApp, yol tarifi ve arama linkleri doğru numara/konumu açıyor mu, widget klavyeyle kullanılabiliyor mu?
   - GEÇTİ → insana onay için sun. KALDI → bir sonraki döngü düzeltmeyle başlar.

**Düzeltme döngüsü (audit KALDI ise):**
- Audit raporundaki düzeltme listesini uygula (**SITE_BUILD**) ve **QUALITY_AUDIT**'i tekrarla.
- Çıktı yeni bir revizyon klasörüne yazılır: `outputs/sites/YYYY-MM-DD_[firma-adi]-r[N]/`. Önceki klasörün üzerine yazılmaz.

**Revizyon döngüsü (insan geri bildirimi varsa):**
- `FEEDBACK.md` içindeki yorumları uygula (**SITE_BUILD**) ve **QUALITY_AUDIT**'i tekrarla. Çıktı `-r[N]` klasörüne yazılır.
- İnsan "başka bileşen seç" derse 3. adıma dön: önceki imza bileşenini (veya belirtilen bileşeni) ele ve yeniden seç. Bu yine tek sitedir; eski sitenin yerini alır.

#### 3B. Keşif Modu (aktif firma yoksa veya firma onay bekliyorsa)
Yukarıdan aşağıya ilk eşleşen çalışır:
- Audit bekleyen build var mı? → **QUALITY_AUDIT**
- Yeni `BRIEF.md` var mı, ya da bu hafta henüz build yok ve en az 2 kullanılabilir pattern var mı? → **SITE_BUILD**
- İşaretlenmiş ama çözümlenmemiş site var mı? → **DESIGN_TEARDOWN**
- Bu haftanın ilham listesinde 5'ten az site mi var? → **INSPIRATION_HUNT** (önce örnek kaynağındaki galeriden, sonra diğer kaynaklardan)
- Hepsi tamam mı? → Efekt kütüphanesini gözden geçir, `MEMORY.md`'yi güncelle

### 4. Log to Journal
Firma Modu'nda ayrıca bir döngü raporu yaz: `outputs/YYYY-MM-DD_web-builder_firma-[firma-adi].md` (revizyonlarda `-r[N]` eki). Rapor şunları içerir:
- Firma ve seçilen konsept (+ gerekçe)
- Kullanılan örnek kaynağı
- **Tasarım planı** (renk token'ları, fontlar, düzen, ilkeler)
- **Bileşen Seçimi** tablosu (COMPONENT_SELECTION çıktısı: adaylar, puanlar, lisanslar, elenme nedenleri)
- **Seçilen imza bileşeni** ve neden seçildiği + destekleyici bileşenler
- Uyarlama tablosu
- **Chatbot**: SSS listesi, eksik cevaplar, test edilen linkler
- Audit sonucu (GEÇTİ/KALDI + skorlar)
- `[DOLDURULACAK]` olarak kalan içerikler, yani insandan istenecek bilgiler

Her iki modda journal kaydına şunlar yazılır:
- Bu döngüde ne yapıldı (skill(ler) + çıktı yolu)
- Dikkat çekici bulgu (yeni trend, yeni teknik, sektöre özel gözlem)
- Sıradaki adım ne olmalı

## Weekly Review

### 1. Gather Data
- Bu haftanın `outputs/` dosyaları (ilham, teardown, firma raporları, audit)
- `data/imports/FEEDBACK.md` (insanın firma sitelerine yorumları)
- Bu hafta seçilen bileşenler ve onay/ret durumları

### 2. Score Against Targets

| Metric | Target | This Week | Status |
|--------|--------|-----------|--------|
| Analiz edilen site | ≥5 | | |
| Yeni pattern | ≥3 | | |
| Tamamlanan firma sitesi | ≥1 | | |
| Lighthouse Perf / A11y (mobil) | ≥85 / ≥90 | | |
| İlk teslimde onaylanan firma sitesi oranı | izleniyor | | |
| Firma başına ortalama revizyon sayısı | izleniyor (düşük = iyi) | | |

### 3. Analyze Wins and Misses
- **Wins:** İlk teslimde onaylanan sitede hangi konsept ve hangi imza bileşeni seçilmişti? Sektör → konsept eşleşmesini MEMORY.md'ye yaz.
- **Misses:** "Başka bileşen seç" denen veya çok revizyon alan projelerde sorun konseptte mi, bileşen seçiminde mi, uyarlamada mı? Hipotezi MEMORY.md'ye yaz.

### 4. Update Memory
Doğrulanmış pattern'leri MEMORY.md'deki ilgili bölümlere ekle. Özellikle "Sektör → Konsept Eşleşmeleri" bölümünü güncelle.

### 5. Log Weekly Summary to Journal
- İncelenen site sayısı, üretilen pattern ve teslim edilen firma sitesi sayısı
- Hedeflere göre performans
- Haftanın en önemli içgörüsü
- Gelecek hafta için öneri

## Monthly Review
- 4 haftalık trendleri incele (hangi konseptler ve teknikler öne çıkıyor)
- Sektör → konsept eşleşmelerinin isabet oranını değerlendir
- Hedeflerin ayarlanması gerekiyorsa işaretle
- En iyi 3 firma sitesini portföy adayı olarak insana sun

## Escalation Rules
- Örnek kaynağı tanımlı değil (`ORNEK_KAYNAGI.md` yok ve firma dosyasında alan boş) → insandan galeri URL'sini iste
- Galeri sitesi açılmıyor, giriş istiyor veya taranmayı engelliyor → insana bildir
- Galeride Firma Uyumu ≥6 olan hiç bileşen yok → en yakın 3 adayı gerekçesiyle insana sun, seçimi insan yapsın
- `API_KEY_21ST` tanımlı değil ve bileşen kodu sayfadan alınamıyor → insandan anahtar iste
- En iyi aday lisanssız veya kısıtlayıcı lisanslı → sıradakine geç; hiçbiri uygun değilse insana bildir
- Firma dosyasında konsept belirlemeye yetecek bilgi yok (sektör veya hedef kitle eksik) → insana soru listesiyle dön
- Site audit'i geçti → insana onay için sun (firma durumunu `onay-bekliyor` yapmayı öner; agent firma dosyasını kendisi değiştirmez)
- Site 2 audit denemesinde de eşiği geçemiyor
- Firma, bir rakibin sitesinin birebir kopyasını istiyor → reddet ve insana bildir
- WhatsApp numarası, adres veya harita konumu eksik → linkleri `[DOLDURULACAK]` bırak ve raporda iste
- Firma yapay zekâ chatbot'u istiyor → sunucu, API anahtarı ve maliyet için insan onayı al
- Deploy, domain veya ücretli asset/servis gerekiyor
- KPI'lar 2+ hafta üst üste düşüyor

## Rules
- Harekete geçmeden önce her zaman journal'ı ve aktif firma dosyasını oku
- Aktif firma varsa Firma Modu her zaman Keşif Modu'ndan önce gelir
- Firma başına tek site: bir imza bileşeni (+ en fazla 4 destekleyici) seçilir ve firmaya uyarlanır; alternatif varyant üretilmez
- Firma Modu'nda bileşenler sadece insanın verdiği örnek kaynağından seçilir
- Bileşen seçimi her firma projesinde yapılır ve raporlanır; atlanamaz
- Örnek kaynağındaki bileşenler lisansı izin veriyorsa kurulup kullanılabilir ve `CREDITS.md`'ye yazılır; başka web sitelerinin kodu, görselleri ve marka öğeleri asla taşınmaz
- Firma hakkında bilgi uydurma; eksikleri `[DOLDURULACAK]` ile işaretle
- Keşif Modu'nda döngü başına tek skill
- AGENT.md'deki bir hedefe hizmet etmeyen skill çalıştırma
