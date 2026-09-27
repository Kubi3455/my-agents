# Skill: Topic Selection

## Purpose
Sitenin nişine uyan, arama talebi olan, mevcut yazılarla çakışmayan ve iç link ağını güçlendiren günlük konuyu seçmek.

## Serves Goals
- Organik büyüme
- Düzenli yayın

## Inputs
- `data/TOPIC_LOG.md` (kuyruk + geçmiş odak kelimeler)
- `data/post-inventory.json` (mevcut yazılar)
- `data/imports/search-console/` (varsa)
- Web araması: son 14 günün AI agent / LLM tooling gelişmeleri, "People also ask", Reddit/HN'de tekrar eden sorunlar

## Process
1. **Kuyruk doluysa:** ilk konuyu al, web aramasıyla hâlâ güncel olduğunu ve konuyu doğrudan çözen yeni bir resmî doküman/sürüm olup olmadığını kontrol et. Güncelse 6. adıma geç.
2. **Kuyruk boşsa, aday üret (en az 10):**
   - **Küme genişletme:** Mevcut kümelerde eksik alt konular (ör. "agent loops" kümesi var → "LangGraph checkpointing", "CrewAI memory")
   - **Sorun odaklı:** Geliştiricilerin forumlarda sorduğu "how to fix / why does X" soruları (sitenin en güçlü formatı)
   - **Karşılaştırma:** "X vs Y" (sitede iyi performans gösteren format)
   - **Search Console:** Pozisyon 8–20 olup özel yazısı olmayan sorgular
3. Her adayı puanla (her biri 1–5):
   - Niş uyumu (agent/LLM/local AI mı?)
   - Arama niyeti netliği (long-tail, sorun çözen)
   - İç link potansiyeli (envanterde bağlanabilecek ≥3 yazı var mı?)
   - Güncellik
   - Rekabet edilebilirlik (ilk sayfada dev siteler + resmî dokümanlar mı dolu?)
4. Ele: odak kelimesi TOPIC_LOG veya envanterdeki bir yazıyla aynı/çok yakın olanlar (cannibalization).
5. En yüksek puanlı 5 konuyu kuyruğa ekle (odak kelime, küme, kategori, "neden şimdi").
6. Seçilen konu için **odak anahtar kelime** + 3–5 ikincil kelime + arama niyeti (informational / how-to / comparison) belirle.

## Outputs
- `data/TOPIC_LOG.md` güncellenmiş kuyruk
- Günlük paket için: konu, odak kelime, ikincil kelimeler, niyet, hedef kategori

## Quality Bar
- Odak kelime 3–6 kelimelik long-tail (tek kelimelik "AI agents" değil)
- Konu, sitenin mevcut bir yazısıyla aynı soruyu cevaplamıyor
- Envanterde en az 3 iç link adayı var

## Tools
- WebSearch / WebFetch
- `data/post-inventory.json`

## Integration
- Çıktı → ARTICLE_WRITING (brief) ve SEO_LINKING (odak kelime)
