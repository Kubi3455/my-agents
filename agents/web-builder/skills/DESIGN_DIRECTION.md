# Skill: Design Direction

## Purpose
`frontend-design` skill'ini kullanarak firmaya özel, jenerik görünmeyen bir tasarım planı (token sistemi) çıkarmak. Bu plan, 21st.dev bileşenlerinin seçimine ve yeniden giydirilmesine yön verir.

## Serves Goals
- Benzer kalitede site üretmek
- Kaliteyi korumak (tutarlı görsel dil, erişilebilir renk/tipografi)

## Inputs
- Aktif firma dosyası ve belirlenen konsept (HEARTBEAT 3A, adım 1)
- `MEMORY.md` → "Denenmiş Tasarım Yönleri" (önceki firmalarda kullanılan kalıpları tekrar etmemek için)
- `knowledge/BRAND.md` (varsa)

## İki Kaynağın Rolü

| Kaynak | Ne sağlar |
|--------|-----------|
| `frontend-design` skill | Tasarım yönü: palet, tipografi, düzen, ilkeler, hero'nun rolü, elle yazılan bölümler, öz eleştiri |
| 21st.dev (COMPONENT_SELECTION) | Hazır, hareketli ve etkileşimli parçalar: imza bileşeni + destekleyiciler |

Kural: Yönü `frontend-design` belirler, 21st.dev bileşenleri bu yöne göre seçilir ve yeniden giydirilir.

## Process
1. `frontend-design` skill'ini yükle (Skill: `example-skills:frontend-design`) ve talimatlarını uygula.
2. Firmanın konusunu, kitlesini ve sayfanın ana işini tek cümlede yaz. Sektörün malzemelerini, dilini ve dünyasını not et.
3. Token sistemini çıkar:
   - **Renk:** 4-6 isimli hex değer (firma renkleri verildiyse onları temel al, kontrastı kontrol et)
   - **Tipografi:** 1-2 font ve rolleri, tip ölçeği
   - **Düzen:** tek cümlelik düzen konsepti + ASCII wireframe, hizalama kararı
   - **İlkeler:** bu sayfayı benzersiz kılan 2-3 ilke
4. **Hero'nun rolünü tanımla:** firmanın dünyasındaki en karakteristik şey ne ve nasıl gösterilecek? Bu tanım COMPONENT_SELECTION'a imza bileşeni arama kriteri olarak gider.
5. **Jeneriklik kontrolü:** Planı `frontend-design`'ın listelediği yapay zekâ varsayılanlarıyla (krem + terracotta, siyah + asit yeşili, SaaS kart kiti vb.) ve MEMORY'deki önceki firmalarla karşılaştır. Benzeyen kısmı revize et ve nedenini yaz. Firma bilgisi açıkça bu görünümlerden birini istiyorsa ona uy.
6. Planı firma raporunun "Tasarım planı" bölümüne yaz.

## Outputs
- Firma döngü raporunda "Tasarım planı" bölümü: token tablosu, wireframe, ilkeler, hero rolü, revizyon notları

## Quality Bar
- Palet 4-6 hex değerden oluşur ve metin/arka plan kontrastı WCAG AA'yı geçer.
- En az bir karar doğrudan firmanın sektöründen/dünyasından türetilmiş ve gerekçesi yazılmış.
- Plan, MEMORY'deki son 3 firmanın tasarım yönüyle aynı palet + font kombinasyonunu kullanmaz.

## Tools
- `example-skills:frontend-design` skill

## Integration
- Hero rolü ve token'lar → COMPONENT_SELECTION (arama ve puanlama kriteri)
- Token'lar → SITE_BUILD (Tailwind teması / CSS değişkenleri, bileşenlerin yeniden giydirilmesi)
- Kullanılan yön → MEMORY.md "Denenmiş Tasarım Yönleri"
