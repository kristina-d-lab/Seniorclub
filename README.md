# Seniorclub — многоязычный сайт (fi/en/ru)

Статический сайт без фреймворков и сборки: 48 страниц (16 × 3 языка) + корневой
редирект, общие CSS/JS/картинки в `/assets`. Хостинг — Vercel, репозиторий — GitHub.

## Структура

```
/index.html           → определяет язык браузера и перекидывает на /fi/, /en/ или /ru/
/404.html             → страница «не найдено» (Vercel подхватывает автоматически)
/fi/  /en/  /ru/      → страницы по языкам (index.html, mumili.html, ota-yhteytta.html, …)
/assets/css/style.css → все стили
/assets/js/main.js    → бургер-меню, дропдауны, форма контактов
/assets/images/       → логотип, фото, флаги, favicon, og-image
/robots.txt, /sitemap.xml
/vercel.json          → правила адресов, 301-редиректы со старого сайта, заголовки кеширования
/preview.py           → локальный просмотр с теми же правилами адресов, что на Vercel
```

## Адреса страниц

На сайте используются «красивые» адреса, такие же, как на старом seniorclub.fi:

```
/fi/                     /en/                     /ru/
/fi/mumili/              /en/mumili/              /ru/mumili/
/fi/seniori-samurai/     …                        …
```

Файлы при этом лежат как `fi/mumili.html` — `vercel.json` переписывает адрес
`/fi/mumili/` → `fi/mumili.html`. Все внутренние ссылки, canonical, hreflang и
sitemap.xml используют именно эти адреса.

Старые адреса старого сайта (например `/mumili/`, `/en/seniors-friendship-club/`,
`/fi/aikataulu/`) отдают 301 на новые — позиции в Google сохраняются.

## Локальный просмотр

Открывать `index.html` двойным кликом **не получится** (ссылки абсолютные).
Вместо этого в папке сайта:

```bash
python3 preview.py
```
и открыть http://localhost:8000/

## Публикация (через сайт GitHub, без git-команд)

1. github.com → репозиторий `kristina-d-lab/Seniorclub` → **Add file → Upload files**
2. Перетащить содержимое папки сайта (папки `fi`, `en`, `ru`, `assets` и файлы
   `index.html`, `404.html`, `vercel.json`, `robots.txt`, `sitemap.xml`, `README.md`, `preview.py`)
3. Подтвердить замену → **Commit changes**
4. Vercel передеплоит сам за 1–2 минуты.

Настройки проекта на Vercel: Framework Preset **Other**, Build Command и Output
Directory — пустые.

## Свой домен

Vercel → проект → **Settings → Domains** → добавить `seniorclub.fi` и `www.seniorclub.fi`
→ прописать у регистратора DNS-записи, которые покажет Vercel. Canonical-адреса в
коде уже указывают на `https://www.seniorclub.fi/…`.

После подключения домена:
- Google Search Console → добавить сайт → отправить `https://www.seniorclub.fi/sitemap.xml`
- проверить структурированные данные: https://search.google.com/test/rich-results

## Что можно донастроить

- **Соцсети в футере** — сейчас показан только Facebook (единственная реальная ссылка).
  Остальные включаются в `build_gen/templates.py` → `SOCIAL_LINKS` (иконки для
  YouTube, Instagram, X, Telegram, Threads уже готовы), либо вручную в HTML.
- **Форма «Ota yhteyttä»** — открывает почтовый клиент с заполненным письмом
  (рабочий вариант без сервера). Для «тихой» отправки можно подключить
  Formspree / Web3Forms: заменить обработчик в `assets/js/main.js`.
- **Уведомление о cookies** не нужно — сайт не ставит cookies и не использует аналитику.
  Если добавите Google Analytics, потребуется баннер согласия.

## SEO, что уже сделано

- title / meta description на каждой странице с локальными ключами (Espoo, Helsinki, 60+)
- canonical + hreflang (fi/en/ru/x-default) на каждой странице и в sitemap.xml
- Open Graph / Twitter Card с картинкой 1200×630
- schema.org: `NGO` (организация, адрес, аудитория 60+) на всех страницах,
  `Course` с расписанием на страницах программ
- robots.txt, sitemap.xml, 301-редиректы со старых адресов
- favicon / apple-touch-icon, theme-color, `notranslate` (у сайта свои 3 языка)
