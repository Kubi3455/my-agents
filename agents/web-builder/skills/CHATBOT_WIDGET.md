# Skill: Chatbot Widget

## Purpose
Her firma sitesine; SSS cevaplayan, WhatsApp'a bağlayan, telefonla arama ve haritada yol tarifi açan, sitenin tasarımıyla uyumlu bir sohbet asistanı eklemek.

## Serves Goals
- Benzer kalitede site üretmek (firma sitesinin standart parçası)
- Kaliteyi korumak (erişilebilir, performansı düşürmeyen widget)

## Tür
**Varsayılan: kural tabanlı asistan.** Yapay zekâ ve sunucu kullanmaz, sabit maliyeti yoktur, her hostingde çalışır, sadece firmanın onayladığı bilgileri söyler.
- Yapay zekâ chatbot'u (Claude API vb.) **sadece insan açıkça isterse** yapılır. Sunucu tarafı kod, API anahtarı ve maliyet gerektirdiği için önce insana devredilir (bkz. Escalation).

## Inputs
- Aktif firma dosyası: `SSS`, `WhatsApp`, `Telefon`, `Adres`, `Harita konumu`, `Çalışma saatleri` alanları
- Tasarım planı (DESIGN_DIRECTION): renkler, fontlar, köşe/gölge dili
- 21st.dev'de uygun bir sohbet/chat UI bileşeni varsa COMPONENT_SELECTION'da destekleyici bileşen olarak değerlendirilebilir

## Process
1. **Veriyi hazırla:** `chatbot-data.json` (veya `.ts`) dosyası oluştur. İçerik: SSS listesi (soru, cevap, anahtar kelimeler), iletişim bilgileri, çalışma saatleri. Tüm metinler bu tek dosyada durur, firma sonradan kolayca düzenleyebilir.
2. **SSS içeriği:**
   - Firma dosyasında `SSS` verildiyse aynen kullan.
   - Verilmediyse firma bilgilerinden **sadece kesin olarak bilinenlerden** 4-6 soru-cevap türet (ör. "Nerede bulunuyorsunuz?", "Çalışma saatleriniz?", "Hangi hizmetleri veriyorsunuz?").
   - Bilinmeyen cevaplar (fiyat, süre, garanti vb.) uydurulmaz; `[DOLDURULACAK]` ile işaretlenir ve raporda insandan istenir.
3. **Arayüz akışı:**
   - Sağ altta sabit bir buton (tasarım token'larıyla giydirilmiş), açılınca kısa bir karşılama mesajı.
   - **Hızlı butonlar:** SSS başlıkları + "WhatsApp'tan yaz" + "Yol tarifi al" + "Ara".
   - Serbest metin kutusu: yazılan soru SSS anahtar kelimeleriyle eşleştirilir (küçük harfe çevirme ve Türkçe karakter normalizasyonu ile). Eşleşme yoksa: "Bu konuda en doğru bilgiyi ekibimiz verir" mesajıyla WhatsApp ve Ara butonları gösterilir.
4. **Aksiyon linkleri:**
   - WhatsApp: `https://wa.me/90XXXXXXXXXX?text=<encodeURIComponent("Merhaba, web sitenizden yazıyorum...")>` (numara ülke koduyla, boşluk ve `+` olmadan)
   - Yol tarifi: `https://www.google.com/maps/dir/?api=1&destination=<enlem,boylam veya encode edilmiş adres>`. Mobilde Google Maps / Apple Maps uygulamasını açar, API anahtarı gerektirmez.
   - Arama: `tel:+90XXXXXXXXXX`
   - Tüm dış linkler `target="_blank" rel="noopener"` ile açılır.
5. **İsteğe bağlı gömülü harita (iletişim bölümü):** `https://www.google.com/maps?q=<adres>&output=embed` iframe. Performans için "Haritayı göster" tıklamasıyla ya da görünür olunca yüklenir (lazy), sayfa açılışında yüklenmez.
6. **Erişilebilirlik ve performans:**
   - Buton `aria-label`'lı, klavye ile açılıp kapanabilir (Esc kapatır), odak widget içinde yönetilir.
   - Widget JS'i hafif tutulur; dış chat servisi scripti eklenmez.
   - `prefers-reduced-motion` açıkken açılma animasyonu kapatılır.
   - Mobilde imza bileşeninin veya önemli CTA'ların üstünü kapatmaz.
7. **Opsiyonel sabit WhatsApp kısayolu:** Firma isterse widget'tan ayrı küçük bir WhatsApp butonu eklenebilir. Varsayılan: sadece widget içinde (ekranda iki yüzen buton olmaması için).

## Outputs
- Site içinde `components/chat-widget/` (UI) + `chatbot-data.*` (içerik)
- Firma raporunda "Chatbot" bölümü: SSS listesi, eksik (`[DOLDURULACAK]`) cevaplar, test edilen linkler

## Quality Bar
- Tüm SSS cevapları firma dosyasındaki bilgilere dayanır; uydurma bilgi yoktur.
- WhatsApp, yol tarifi ve arama linkleri gerçek cihazda / tarayıcıda test edilmiş olmalı (doğru numara ve konum açılıyor).
- Widget Lighthouse Performance skorunu 3 puandan fazla düşürmez; A11y ≥90 korunur.
- Widget görsel olarak sitenin tasarım planına uyar (hazır chat servisi görünümü taşımaz).

## Tools
- React + Tailwind (sitenin stack'i), Playwright (link ve etkileşim testi)

## Integration
- SITE_BUILD'in parçası olarak kurulur (HEARTBEAT 3A, adım 5)
- QUALITY_AUDIT linkleri, klavye erişimini ve performans etkisini kontrol eder
- Yapay zekâ chatbot'u istenirse → insana handoff (sunucu, API anahtarı, maliyet onayı)
