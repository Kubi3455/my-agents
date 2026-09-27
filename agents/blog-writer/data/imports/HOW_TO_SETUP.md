# Kurulum (bir kerelik, insan yapar)

## 1. WordPress Application Password
1. WP Admin → **Users → Profile** → en altta **Application Passwords**
2. Ad: `blog-writer-agent` → **Add New Application Password**
3. Çıkan parolayı (boşluklu hâliyle) kopyala. **Bir daha gösterilmez.**
4. Kullanıcının rolü en az **Author** olmalı (Editor önerilir: etiket oluşturabilmesi için)

> LiteSpeed / güvenlik eklentisi (Wordfence vb.) REST API'yi veya Application Passwords'ü kapatmışsa açılmalı.

## 2. Ortam değişkenleri
Değerleri hiçbir dosyaya yazma. Windows (kalıcı, kullanıcı düzeyi):
```powershell
[Environment]::SetEnvironmentVariable("WP_USER", "kullanici-adi", "User")
[Environment]::SetEnvironmentVariable("WP_APP_PASSWORD", "xxxx xxxx xxxx xxxx xxxx xxxx", "User")
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-...", "User")
```
Bulut rutini için aynı üç değişken rutinin **environment/secrets** ayarına girilir.

## 3. Rank Math meta alanlarını REST'e aç
Rank Math, SEO başlığı/açıklaması/odak kelimeyi varsayılan olarak REST API'den yazdırmaz.
**Code Snippets** eklentisiyle (veya child theme `functions.php`) şu snippet'i ekle:

```php
add_action( 'init', function () {
    foreach ( [ 'rank_math_title', 'rank_math_description', 'rank_math_focus_keyword' ] as $key ) {
        register_post_meta( 'post', $key, [
            'show_in_rest'  => true,
            'single'        => true,
            'type'          => 'string',
            'auth_callback' => function () { return current_user_can( 'edit_posts' ); },
        ] );
    }
} );
```
Doğrulama: `python agents/blog-writer/scripts/wp_client.py check` → `rank math meta: OK`

## 4. Sosyal medya (Jetpack Social, ücretsiz)
1. WP Admin → Plugins → Add New → **Jetpack Social** → kur, etkinleştir, WordPress.com hesabıyla bağla
2. Jetpack → **Social** → Connections:
   - **Facebook** → yalnızca **Sayfa** seçilebilir (kişisel profil desteklenmez)
   - **Instagram Business** → Instagram hesabı Professional (Business/Creator) olmalı ve bir Facebook Sayfasına bağlı olmalı
   - **LinkedIn** → kişisel profil
3. Her bağlantıda "Share to this account by default" açık olsun
4. Doğrulama: `python agents/blog-writer/scripts/wp_client.py check` → `jetpack social message: OK`
5. Paylaşım **yalnızca "Yayınla"ya bastığında** olur. Yayınlamadan önce editörün sağ panelindeki Jetpack Social bölümünde ajanın yazdığı metni görüp düzenleyebilirsin.

## 5. Search Console (haftalık, opsiyonel ama önerilir)
Search Console → Performance → son 28 gün → Export → CSV →
`agents/blog-writer/data/imports/search-console/YYYY-MM-DD_queries.csv`

## 6. Bilinen site sorunu (senin düzeltmen gerekir)
Yazı sayfalarında **iki** `<meta name="description">` var (biri temadan/başka bir eklentiden, biri Rank Math'ten).
Tema ayarlarında SEO/meta özelliğini kapat ki yalnızca Rank Math'inki kalsın.
