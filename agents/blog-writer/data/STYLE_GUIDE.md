# Style Guide: firstevolvenextscale.com

> 2026-09-27 tarihinde 21 yazının REST API üzerinden analiziyle çıkarıldı (SITE_ANALYSIS skill'i).
> Yazılar İngilizce yazılır; bu rehber Türkçe'dir. Haftalık review'da yeni yazılarla güncellenir.

## Site Kimliği
- **Site adı:** First Evolve Next Scale
- **Taban URL (API için):** `https://www.firstevolvenextscale.com` (www'suz adres yönlendiriyor; yönlendirmede Authorization header düşer, her zaman www kullan)
- **Niş (son 2 ay):** AI agent'lar, multi-agent framework'ler (CrewAI, LangGraph, AutoGPT), agent debugging/loop sorunları, human-in-the-loop, local LLM (Ollama, llama.cpp, Instructor)
- **Eski/geniş konular:** AI araç listeleri, AI eğitim/sertifika, LLM'ler nasıl çalışır, AI donanım
- **Hedef okur:** Pratik yapan geliştirici / teknik meraklı; "no code overload" vaadiyle başlangıç-orta seviye

## Ses ve Ton
- **Birinci tekil şahıs, deneyimden konuşan geliştirici.** Açılış bir itiraf ya da yaşanmış bir sorunla başlar:
  - "I spent an embarrassing number of hours last month debugging a pipeline that kept choking on a single stray comma."
- İkinci paragraf okuru içeri alır: "If you've run a local LLM through Ollama… you already know this pain."
- Üçüncü paragraf vaadi verir: "Here's how it actually works, where it breaks, and when you need something stronger."
- Konuşma dili, kısaltmalar serbest (it's, doesn't, you'll). Hafif ironi var ama abartı ve hype yok.
- Kalıplaşmış geçişler: "Here's the confusing part:", "The catch:", "Which is exactly the problem X was built to remove."
- Dürüstlük: araçların **sınırlarını** ve "when it's not enough" bölümünü mutlaka yaz. Artı/eksi listeleri kullanılır.

### Kaçınılacaklar
- "In today's fast-paced world", "delve", "unlock the power", "game-changer", "revolutionize" gibi yapay zekâ kokan klişeler
- Kanıtsız istatistik, uydurma alıntı, var olmayan kütüphane fonksiyonu
- Paragraf başına 4 cümleden fazla

## İnsan Sesi: Gerçek Bir AI Uzmanı Gibi Yaz (ZORUNLU)

> Kullanıcı kuralı (2026-09-27): Yazılar, sahada agent ve LLM sistemleri kurmuş, samimi konuşan gerçek bir AI mühendisinin kaleminden çıkmış gibi olmalı. **Yapay zekâ yazmış hissi kesinlikle olmamalı.** Bu bölüm diğer tüm stil kurallarından önceliklidir.

### Persona
- Yıllardır LLM uygulamaları, agent pipeline'ları ve local model kurulumları yapan pratisyen bir mühendis. Akademisyen ya da pazarlamacı değil.
- Okura, kahve içerken bir meslektaşa anlatır gibi konuşur: "you", "I", "we" serbest. Arada kısa espri ya da hafif sitem ("json.loads() did not appreciate the commentary").
- **Görüşü vardır ve söyler:** "Honestly, I'd skip X for this." / "I'd reach for Y unless you need Z." Her şeye "it depends" demez. Ama neden öyle düşündüğünü de açıklar.
- Neyi bilmediğini ya da neyin kendisini şaşırttığını kabul eder: "I didn't expect this to matter as much as it did."

### Uzmanlık Sinyalleri (her yazıda en az 4 tanesi)
- Dokümanda yazmayan **pratik detay**: bir parametrenin varsayılanı neden sorun çıkarır, hangi hata mesajını görürsün, neyi loglarsın
- **Trade-off** tartışması: hız ile doğruluk, maliyet ile kontrol, basitlik ile esneklik
- "Bunu denedim, işe yaramadı çünkü…" tarzı başarısızlık anlatısı
- Gerçek hata mesajı, config satırı veya komut (doğrulanmış)
- Yaygın tavsiyeye kibarca itiraz: "You'll see people recommend X. It works, until…"
- Kenar durum ya da ölçek sorunu: "Fine for 10 requests. At 10k, here's what breaks."

### Yapay Zekâ Kokusunu Yok Etme Kuralları
**Ritim (en önemli):**
- Cümle uzunluğunu bilinçli değiştir. Uzun bir açıklamanın ardından kısa bir cümle gelsin. Böyle.
- Paragraf uzunlukları eşit olmasın: bazen tek cümle, bazen dört.
- Her bölüm aynı kalıpla başlamasın (tanım → açıklama → örnek dizisini sürekli tekrarlama).

**Yasak kalıplar (bulursan yeniden yaz):**
- "It's not just X, it's Y" / "X isn't about A. It's about B." karşıtlıkları
- Üçlü sıralama alışkanlığı ("fast, reliable, and scalable"): en fazla bir kez
- "Whether you're a beginner or a seasoned pro…", "Let's dive in", "In this article we will explore", "buckle up"
- "Moreover", "Furthermore", "Additionally", "In conclusion", "It's worth noting that", "It's important to remember"
- "delve", "tapestry", "landscape", "realm", "robust", "seamless", "leverage", "harness", "elevate", "empower", "navigate the complexities", "ever-evolving", "crucial", "pivotal"
- Her bölümün sonunda o bölümü özetleyen cümle
- Conclusion'da yazıyı madde madde tekrar etmek (onun yerine: kişisel tavsiye + bir sonraki adım)
- Her maddesi kalın başlık + iki nokta ile başlayan listeler (en fazla bir liste böyle olabilir)
- Em dash (—): yazı başına en fazla 3 (site ara sıra kullanıyor, abartma)
- Aşırı temkinli dil ("may potentially", "can help to") ve her iddianın yumuşatılması
- Emoji

**Yapılacaklar:**
- Kısaltmalar: it's, don't, you'll, I'd, that's
- Doğal dolgu ve geçişler: "Here's the thing.", "Quick aside:", "Anyway,", "Okay, so", "The annoying part?"
- Arada soru sor, cevabı hemen ver
- Somut ol: "a 7B model on a laptop with 16 GB RAM", "a 3-agent CrewAI setup". Soyut "various models" deme
- Bazen parantez içi kişisel yorum yap (ki bunu insanlar yapar)
- Kod öncesi "neden", kod sonrası "nerede patlar" anlat

### Dürüstlük Sınırı
Persona deneyimden konuşur ama **uydurma olgu yazmaz**: sahte müşteri/şirket adı, sahte benchmark rakamı, sahte alıntı yok. Anekdotlar genel ve makul olmalı ("last month a pipeline kept choking on…"). Rakam verilecekse kaynağı `sources.md`'de olmalı ya da "roughly", "in my runs" gibi açıkça kişisel gözlem diye çerçevelenmeli.

### İnsan Sesi Testi (yayından önce, 8/8 olmalı)
1. Yasak kalıp/kelime taraması temiz mi?
2. Art arda 3 cümle aynı uzunlukta mı? (varsa kır)
3. En az 4 uzmanlık sinyali var mı?
4. En az 2 açık görüş/tavsiye cümlesi ("I'd…", "Skip…") var mı?
5. Conclusion özet değil de tavsiye mi?
6. Açılış gerçek bir durumla mı başlıyor (tanımla değil)?
7. Yüksek sesle okununca "bir insan böyle konuşur mu?" hissi veriyor mu?
8. Bir meslektaş okusa "bunu sahada çalışmış biri yazmış" der mi?

## Yapı (yeni yazılar için hedef)
| Öğe | Hedef |
|-----|-------|
| Uzunluk | 1.800–2.800 kelime (son dönem yazıların aralığı) |
| Başlık | `[Anahtar konu]: [Somut vaat]` + çoğu zaman sonunda yıl ("… 2026"). ≤ 65 karakter tercih edilir |
| Slug | Kısa, anahtar kelime odaklı, yılsız (`debugging-multi-agent-workflows`) |
| Açılış | 3 kısa paragraf: hikâye → okurun acısı → vaat |
| TOC | Otomatik (Easy TOC eklentisi). Elle TOC yazma |
| H2 | 7–11 adet; H3 ile alt kırılım |
| Kod | Teknik konularda `wp-block-code` blokları; çalışır, kısa, yorumlu Python |
| Tablo | En az 1 karşılaştırma tablosu (X vs Y, mod karşılaştırma vb.) |
| Artı/Eksi | Araç konusunda "Pros of X / Cons of X" H3'leri |
| "Common Pitfalls" | Teknik yazılarda sonlara yakın bir bölüm |
| Sonuç | `## Conclusion`: kısa, tekrar değil, sonraki adım öner |
| FAQ | `## FAQ` + 3–5 soru H3 olarak (People Also Ask tarzı). Rank Math FAQ şeması için uygun |

## Gutenberg Blok Biçimi
İçerik HTML'i Gutenberg blok yorumlarıyla yazılır ki editörde düzenlenebilir kalsın:
```html
<!-- wp:paragraph --><p>…</p><!-- /wp:paragraph -->
<!-- wp:heading --><h2 class="wp-block-heading">…</h2><!-- /wp:heading -->
<!-- wp:heading {"level":3} --><h3 class="wp-block-heading">…</h3><!-- /wp:heading -->
<!-- wp:code --><pre class="wp-block-code"><code>…</code></pre><!-- /wp:code -->
<!-- wp:table --><figure class="wp-block-table"><table>…</table></figure><!-- /wp:table -->
<!-- wp:list --><ul class="wp-block-list"><li>…</li></ul><!-- /wp:list -->
<!-- wp:quote --><blockquote class="wp-block-quote"><p>…</p></blockquote><!-- /wp:quote -->
<!-- wp:separator --><hr class="wp-block-separator has-alpha-channel-opacity"/><!-- /wp:separator -->
```

## Görseller
- Ana görsel (featured) + yazı içi **2–3 görsel** (son yazılarda yalnızca 1 görsel var; eski yazılar 3–9 arası. Hedef bunu artırmak)
- Alt metin: açıklayıcı cümle + odak anahtar kelime doğal şekilde. Örnek: "Structured outputs in local LLMs using Instructor and Python, showing an Ollama model, Pydantic validation, and structured JSON extraction workflow."
- Dosya adı: `anahtar-kelime-aciklama.png` (boşluksuz, küçük harf)

## Linkler
- **Mevcut durum zayıf:** yazı başına yalnızca 1–2 gerçek iç link var. **Hedef: 4–6 bağlamsal iç link.**
- İç link anchor'ları doğal cümle içinde: "running local LLMs with Ollama"
- Dış linkler: **resmî dokümantasyon** (docs.crewai.com, docs.langchain.com, docs.ollama.com, python.useinstructor.com). Hedef 2–4
- Dış linklerden `utm_*` parametrelerini temizle (mevcut bir yazıda `?utm_source=chatgpt.com` kalmış)

## Taksonomi
- **Kategoriler:** AI (5), AI Education (11), AI Software (8), AI Technology (6). Yeni kategori açma. `Uncategorized` ve `Resources` kullanma
- **Etiketler (sahip kararı 2026-09-28):** Her yazıya SEO çalışmasıyla birlikte **yazıya özel tam 10 etiket**. İçerik: odak anahtar kelime, slug'daki ana ifade, ikincil anahtar kelimeler, yazıda geçen araç/framework adları, arama niyeti ifadeleri. Aynı adda (büyük/küçük harf fark etmez) etiket varsa o kullanılır, yenisi açılmaz. Etiketler Title Case, 1–4 kelime. Tag arşivleri Rank Math'te `noindex`, yani çok etiket ince içerik cezası yaratmaz

## SEO Altyapısı
- **Rank Math** kurulu (Article/BlogPosting, BreadcrumbList şeması otomatik)
- SEO title formatı: `%title% | First Evolve Next Scale`
- **Bilinen sorun (insana bildir):** Sayfalarda iki `<meta name="description">` var (tema/eklenti çakışması). Ajan düzeltemez; journal'a yazıldı.
