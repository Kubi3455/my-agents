# Skill: Site Analysis

## Purpose
Sitenin mevcut yazılarını okuyarak ses, yapı, link ve taksonomi kurallarını `data/STYLE_GUIDE.md` içine çıkarmak.

## Serves Goals
- Ses tutarlılığı
- İç link ağı

## Inputs
- `https://www.firstevolvenextscale.com/wp-json/wp/v2/posts` (herkese açık, kimlik gerekmez)
- `/wp-json/wp/v2/categories`, `/wp-json/wp/v2/tags`
- Bir yazının HTML sayfası (SEO eklentisi/şema tespiti için)
- `MEMORY.md` → "Ses" bölümü (insan düzeltmeleri, analizden önceliklidir)

## Process
1. `python scripts/wp_client.py inventory` çalıştır (envanteri tazeler).
2. En yeni 8 yazının `content.rendered` alanını oku. **Yeni yazılar eski yazılardan daha ağırlıklıdır.** Site sesi değişiyorsa yeni sese uy.
3. Her yazı için ölç: kelime sayısı, H2/H3 sayısı, görsel sayısı, **gerçek** iç link sayısı (TOC `#` çapalarını sayma), dış link domain'leri, tablo/kod/FAQ varlığı, Gutenberg blok türleri.
4. Ses için 3 yazının ilk 3 paragrafını ve bölüm geçişlerini oku. Açılış kalıbını, sık geçiş ifadelerini, cümle uzunluğunu, zamir kullanımını not et.
5. Bir yazı sayfasının `<head>` kısmından SEO eklentisini (Rank Math/Yoast), title formatını, şema türlerini tespit et.
6. Sorunları listele (çift meta, çöp etiketler, utm'li linkler, eksik alt text vb.).
7. `data/STYLE_GUIDE.md` dosyasını güncelle; başa analiz tarihini yaz. MEMORY.md "Ses" kurallarını koru, üzerine yazma.

## Outputs
- `data/STYLE_GUIDE.md` (güncel)
- Journal: yeni tespit edilen site sorunları

## Quality Bar
- Her kural en az 2 yazıdan örnekle desteklenir
- Açılış kalıbı için en az 1 gerçek alıntı içerir
- Hedef sayılar (kelime, H2, link) ölçüme dayanır, tahmine değil

## Tools
- `scripts/wp_client.py inventory`
- `curl` / WebFetch (HTML head)

## Integration
- STYLE_GUIDE → ARTICLE_WRITING ve SEO_LINKING'in tek doğruluk kaynağı
- Envanter → TOPIC_SELECTION (tekrar önleme), SEO_LINKING (iç link adayları)
