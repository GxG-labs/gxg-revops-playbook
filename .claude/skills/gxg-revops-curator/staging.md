# Curator — Staging Workflows

Подробные инструкции по работе со staging-областью (`_staging/`).
SKILL.md маршрутизирует сюда при staging-запросах.

---

## Когда использовать staging

**Добавляй в staging, когда:**
- Есть полезное доменное знание, но нет времени делать полноценный скилл прямо сейчас
- Знание неполное — нужно больше примеров или контекста
- Непонятно, в какой домен это идёт
- Источник — сырые заметки (митинг, документ, разговор), требующие обработки

**Не добавляй в staging:**
- Ссылки на внешние ресурсы без GxG-специфичного контекста
- Общеизвестные RevOps-концепции без GxG-применения
- Дубликаты существующих active-скиллов

---

## Scan Staging

**Trigger:** "scan staging", "что в staging", "staging status"

1. Найти все `.md` файлы в `_staging/` кроме `README.md` и `_template.md`
2. Прочитать фронтматтер каждого: `title`, `domain`, `status`, `skill_candidate`, `added`
3. Вычислить `days_in_staging = today - added`
4. Оценить готовность к скиллу (0–3):
   - +1 если `skill_candidate: yes`
   - +1 если раздел "Знание" > 100 слов
   - +1 если "Вопросы без ответа" пусты или отмечены как решённые
5. Вывести таблицу:

```
| Note | Domain | Status | Days | Readiness | Action |
|------|--------|--------|------|-----------|--------|
| {title} | {domain} | {status} | {n} | {0-3}★ | {promote|refine|park|review} |
```

Флаги-предупреждения:
- ⏰ `ready` > 30 дней → "пора продвигать"
- 🗑️  `parked` > 90 дней → "пересмотреть или удалить"
- 📝 `raw` > 14 дней без изменений → "нужен refining"

---

## Refine Note

**Trigger:** "refine {note}", "help me structure {note}", "доработай заметку {note}"

Цель: превратить `raw` → `refining` → `ready`

1. Прочитать заметку
2. Определить:
   - Правильный ли домен?
   - Есть ли конкретные примеры (G4 requirement)?
   - Есть ли open questions, которые блокируют скилл?
3. Предложить структуру для раздела "Знание":
   - Основной workflow / процесс
   - GxG-специфичные параметры (пороги, критерии, решения)
   - Примеры (хотя бы 2)
4. Задать уточняющие вопросы по open questions
5. Обновить `status: refining` и добавить заметки в раздел "Заметки куратора"
6. Если после рефайнинга готово → предложить promote

---

## Promote Note to Skill

**Trigger:** "promote {note}", "make skill from {note}", "promote {slug} to skill"

1. Прочитать staging-заметку
2. Проверить readiness:
   - Есть конкретный workflow/процесс?
   - Есть ≥2 примера (или можно извлечь из знания)?
   - Нет блокирующих open questions?
   - Если нет → предложить refine сначала
3. Определить `domain` и `slug` (использовать `skill_candidate_slug` из фронтматтера или предложить)
4. Scaffoldить скилл из `templates/new-skill.md` используя знание из заметки:
   - Описание берётся из "Контекст" + Description Optimizer
   - Инструкции — из "Знание"
   - Примеры — из примеров в заметке или создать на основе знания
   - Out of scope — из "Вопросы без ответа" (чего не знаем = out of scope пока)
5. Запустить G1–G7 gate check
6. Сохранить скилл в `{domain}/{slug}/SKILL.md` со статусом `draft`
7. Переместить staging-заметку: добавить в фронтматтер `promoted_to: {domain}/{slug}` и `status: promoted`
8. Обновить INDEX.md
9. **README freshness check** ← автоматически после promote
   Скилл стал active — запусти §README Freshness Check из lifecycle.md.

---

## Park Note

**Trigger:** "park {note}", "not ready yet {note}", "запаркуй {note}"

1. Обновить `status: parked` в фронтматтере
2. Добавить в "Заметки куратора":
   ```
   Запарковано: {date}
   Причина: {почему не превращать в скилл сейчас}
   Триггер для возврата: {что должно измениться, чтобы вернуться к этому}
   ```
3. Не удалять — оставить в `_staging/`

---

## Add to Staging

**Trigger:** "add to staging", "сохрани это в staging", "добавь в базу знаний"

1. Уточнить:
   - Домен (или предложить)
   - Источник (meeting-notes / doc / conversation / research)
   - `skill_candidate`: yes / no / maybe
2. Предложить slug на основе содержимого
3. Создать `_staging/{slug}.md` из `_template.md`
4. Заполнить знание из предоставленного контента
5. Установить `status: raw`
6. Сообщить: "Добавлено в staging. Запусти scan staging чтобы увидеть полную картину."

---

## Staging Health Rules

| Rule | Action |
|------|--------|
| `ready` > 30 дней | Напомнить о promote при следующем scan |
| `parked` > 90 дней | Предложить удалить или reconsider |
| `raw` > 14 дней | Предложить refine или park |
| >20 заметок в staging | Предупредить — staging переполнен, нужна чистка |
| >5 `ready`-заметок | Срочно: много готового знания без скиллов |
