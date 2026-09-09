# Seniorclub — многоязычный сайт (fi/en/ru)

Статический сайт, без фреймворков и сборки. 49 HTML-страниц (16 на язык + редирект),
общие CSS/JS/картинки в `/assets`.

## Структура

```
/index.html          → редирект на /fi/
/fi/  /en/  /ru/      → страницы по языкам (index.html, mumili.html, ota-yhteytta.html, …)
/assets/css/style.css → все стили
/assets/js/main.js    → бургер-меню, дропдауны, форма контактов
/assets/images/       → логотип, фото, флаги
```

## Публикация на GitHub

Репозиторий уже готов локально (`git init` + первый коммит сделаны). Дальше:

1. Создай пустой репозиторий на github.com (**без** README/.gitignore — они не нужны, у нас уже есть)
2. В папке с сайтом выполни:

```bash
git remote add origin https://github.com/<твой-логин>/<название-репозитория>.git
git push -u origin main
```

Если попросит логин — используй Personal Access Token вместо пароля
(GitHub → Settings → Developer settings → Personal access tokens).

## Публикация на Vercel

Проще всего — через сайт Vercel, без командной строки:

1. vercel.com → **Add New → Project**
2. **Import Git Repository** → выбери репозиторий, который только что запушила
3. Framework Preset: **Other** (это статический HTML, сборка не нужна)
4. Build Command и Output Directory — оставь пустыми (или Output Directory: `.`)
5. **Deploy**

Через минуту сайт будет доступен на `https://<название>.vercel.app`.

В комплекте уже лежит `vercel.json` — он включает чистые адреса
(`/fi/mumili` вместо `/fi/mumili.html`), чтобы ссылки были такими же, как на живом
seniorclub.fi.

### Свой домен

Vercel → проект → **Settings → Domains** → добавить `seniorclub.fi` (или поддомен) →
прописать DNS-записи, которые покажет Vercel, у регистратора домена.

## Дальше

- Форма на странице «Ota yhteyttä» сейчас открывает почтовый клиент (mailto) —
  рабочий вариант без сервера. Если понадобится тихая отправка без открытия
  почты, можно подключить Formspree/Netlify Forms или простую serverless-функцию.
- Соцсети в футере: реальна пока только ссылка на Facebook, остальные — заглушки (`#`),
  подставить ссылки, когда появятся аккаунты.
