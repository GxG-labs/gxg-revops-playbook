# Curator — README Workflows

Создание и обновление README.md для репозитория GxG RevOps Playbook.
Основано на анализе 500+ топ GitHub-репозиториев (awesome-readme, 20k+ ⭐).

---

## Два типа README в этом репо

| Файл | Назначение | Аудитория |
|------|-----------|-----------|
| `README.md` (корень) | Главная страница репо — что это, зачем, как начать | Новые участники, RevOps команда |
| `{domain}/README.md` | Обзор домена — что внутри, coverage, метрики | Те, кто работает с конкретным доменом |

Этот модуль покрывает оба типа. Разные шаблоны — см. ниже.

---

## Когда обновлять README

| Триггер | Что обновить |
|---------|-------------|
| Добавлен новый скилл | Badges (счётчик скиллов), Coverage таблица в корневом README |
| Изменилась структура папок | Раздел Structure |
| Новый домен добавлен | Domains таблица, Structure |
| Coverage target достигнут | Badges, Coverage таблица |
| Изменился workflow (как контрибьютить) | Quick Start, Contributing |
| Переименован домен | Все ссылки на домен по всему README |
| Раз в квартал (routine) | Badges, Coverage, "What's New" |

---

## Create: корневой README.md

**Trigger:** "создай README", "напиши README для репо", "readme для playbook"

### Анатомия README для knowledge/playbook репо

Порядок секций — строгий. Каждая секция обоснована данными из топ-репозиториев.

```
1. Banner/Logo              ← первое впечатление, 42% больше звёзд с визуалом
2. Badges                   ← моментальные сигналы доверия (4-7 макс)
3. One-liner                ← ≤10 слов, что это
4. Why (value prop)         ← 3-5 bullets: какие проблемы решает
5. Quick Start              ← как использовать за ≤3 шага
6. What's Inside            ← домены + coverage map
7. Skill count / Stats      ← прогресс и momentum
8. How to Use               ← как запускать скиллы
9. How to Contribute        ← CONTRIBUTING ссылка + 4 шага
10. Structure               ← дерево папок
11. License / Credits       ← если нужно
```

### Правила написания

**Первый экран (above the fold)** — содержит badges + one-liner + why. Читатель решает "интересно / нет" за 5 секунд.

**Язык** — активный залог, императив. "Run `/skill-name`", не "Skills can be run by..."

**Длина** — для knowledge repo оптимально 400–900 слов. Детали — в domain README.

**Ссылки** — все relative (`./pipeline/README.md`), не absolute URLs.

**Таблицы** — для coverage map и структуры. Для обычного текста — нет.

**Emoji** — умеренно, только как visual anchor в заголовках или bullets (не в теле текста).

### Badges для knowledge репо

Стандартные code-badges (build, npm) не подходят. Используем content-badges:

```markdown
![Skills](https://img.shields.io/badge/skills-{N}%20active-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-{N}%25-{color})
![Domains](https://img.shields.io/badge/domains-10-blue)
![Updated](https://img.shields.io/badge/updated-{month}%20{year}-lightgrey)
```

Color logic для coverage badge:
- ≥80% → `brightgreen`
- 60–79% → `yellow`
- 40–59% → `orange`
- <40% → `red`

Максимум 5 badges. Лишние — шум.

---

## Create: domain README.md

**Trigger:** "напиши README для домена X", "обнови readme pipeline"

### Структура domain README

```
1. Domain name + scope (1 абзац)
2. Coverage map (таблица: skill | status | description)
3. Key metrics (3-5 важнейших KPI этого домена)
4. Stack references (инструменты GxG в этом домене)
5. Coverage targets
6. Notes (GxG-специфичный контекст)
```

Короче корневого — фокус на навигации внутри домена.

---

## Update: обновление существующего README

**Trigger:** "обнови README", "update readme", "актуализируй readme"

### Шаги

1. Прочитать текущий README
2. Запустить audit (`scripts/audit.py`) чтобы получить актуальные цифры
3. Определить что устарело:
   - Счётчик скиллов в badges
   - Coverage таблица
   - Структура папок
   - Ссылки (нет broken links?)
4. Обновить только изменившееся — не переписывать весь документ
5. Сообщить что изменилось (diff summary)

### Частые обновления

**Badges** — обновлять при каждом добавлении скилла:
```
Было: ![Skills](https://img.shields.io/badge/skills-3%20active-red)
Стало: ![Skills](https://img.shields.io/badge/skills-7%20active-orange)
```

**Coverage таблица** — брать цифры из audit.py, не вручную.

**"What's New"** секция (если есть) — ротировать: хранить последние 3 события, остальное — в CHANGELOG.

---

## README Quality Score

10-балльная шкала (адаптирована для knowledge repo):

| # | Критерий | Балл |
|---|---------|------|
| 1 | 4–5 content badges (skills count, coverage, domains, updated) | /1 |
| 2 | One-liner ≤10 слов описывает суть | /1 |
| 3 | Visual элемент (banner, architecture diagram, coverage таблица) | /1 |
| 4 | Quick Start — как начать за ≤3 шага | /1 |
| 5 | Domains таблица с coverage % и ссылками | /1 |
| 6 | Конкретный пример использования скилла | /1 |
| 7 | Ссылка на CONTRIBUTING.md + краткие шаги | /1 |
| 8 | Folder structure актуальная | /1 |
| 9 | Нет broken links | /1 |
| 10 | Написан для новичка (не требует контекста) | /1 |

**8–10** → Excellent ✅ | **6–7** → Good ⚠️ | **<6** → Needs work 🔧

---

## Anti-patterns (из анализа реальных репо)

| Anti-pattern | Почему плохо | Как исправить |
|-------------|-------------|--------------|
| Wall of text без структуры | Читатель уходит за 3 сек | Добавить headers, bullets, таблицы |
| Устаревшие цифры в badges | Подрывает доверие | Auto-генерация из audit.py |
| "This repo contains..." как первая строка | Weak opener, не описывает value | Начинать с benefit, не с description |
| TOC без якорных ссылок | Не работает навигация | Проверить, что все `#` anchors существуют |
| Структура папок вручную | Быстро устаревает | Генерировать из `tree` при обновлении |
| Contributing в 1 строку | Отпугивает контрибьюторов | Минимум 4 шага + ссылка на CONTRIBUTING.md |
| README как единственная документация | Слишком длинный | README = hub, детали — в domain README |

---

## Пример: корневой README.md для GxG RevOps Playbook

Используй `templates/repo-readme.md` как основу. Шаги:

1. Прочитать `templates/repo-readme.md`
2. Запустить audit.py, получить актуальные цифры
3. Заполнить `{placeholders}` реальными данными
4. Сохранить как `README.md` в корне репо
5. Запустить README Quality Score — должно быть ≥8/10

---

## Out of Scope

Этот модуль НЕ:
- Создаёт README для отдельных скиллов (там SKILL.md, не README)
- Генерирует GitHub Pages или сайт документации
- Управляет CHANGELOG.md (это отдельный workflow)
