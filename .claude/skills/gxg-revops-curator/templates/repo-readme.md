<!-- 
  TEMPLATE: GxG RevOps Playbook — корневой README.md
  Заполни {placeholders} реальными данными перед использованием.
  Запусти audit.py чтобы получить актуальные цифры для badges и coverage.
-->

<!-- BADGES — обновлять при каждом новом active скилле -->
![Skills](https://img.shields.io/badge/skills-{ACTIVE_COUNT}%20active-{COVERAGE_COLOR})
![Coverage](https://img.shields.io/badge/coverage-{COVERAGE_PCT}%25-{COVERAGE_COLOR})
![Domains](https://img.shields.io/badge/domains-10-blue)
![Updated](https://img.shields.io/badge/updated-{MONTH}%20{YEAR}-lightgrey)

# GxG RevOps Playbook

**Коллекция скиллов для Claude, покрывающая весь стек Revenue Operations.**

Каждый скилл — это готовый workflow: запустил, получил результат.
Не инструкции "как думать о RevOps" — а "как сделать прямо сейчас".

---

## Зачем

- ✅ **Скорость** — стандартные RevOps задачи решаются за один вызов скилла, без промпт-инжиниринга
- ✅ **Единый стандарт** — все в команде работают по одному GxG-подходу
- ✅ **Живая база знаний** — staging-область для доменного знания, которое ещё не стало скиллом
- ✅ **Полный стек** — {ACTIVE_COUNT} скиллов в {DOMAIN_COUNT} доменах от pipeline до CS ops

---

## Быстрый старт

**1.** Убедись что `gxg-revops-curator` активирован в твоём Claude.

**2.** Вызови любой скилл напрямую:
```
/scoring-leads
/forecasting-pipeline
/auditing-crm-data
```

**3.** Или попроси куратора найти нужное:
```
Нужен скилл для анализа churn — что есть в playbook?
```

---

## Что внутри

| Домен | Скиллов | Coverage | Описание |
|-------|---------|----------|---------|
| [pipeline](./pipeline/) | {N}/6 | {%}% | Управление воронкой, прогнозирование, стейдж-менеджмент |
| [demand-gen](./demand-gen/) | {N}/5 | {%}% | ICP, лид-скоринг, MQL/SQL-критерии, ABM |
| [sales-enablement](./sales-enablement/) | {N}/7 | {%}% | Плейбуки, battle cards, работа с возражениями |
| [crm-ops](./crm-ops/) | {N}/6 | {%}% | Salesforce/HubSpot, качество данных, автоматизация |
| [rev-analytics](./rev-analytics/) | {N}/5 | {%}% | KPI, атрибуция, дашборды, ARR/NRR/GRR |
| [cs-ops](./cs-ops/) | {N}/5 | {%}% | Health scoring, QBR, retention, expansion |
| [rev-tech](./rev-tech/) | {N}/4 | {%}% | Стек инструментов, интеграции, vendor eval |
| [pricing-packaging](./pricing-packaging/) | {N}/4 | {%}% | CPQ, тиры, deal desk, discount governance |
| [territory-quota](./territory-quota/) | {N}/4 | {%}% | Territories, квоты, ramp планы, компенсация |
| [mktg-ops](./mktg-ops/) | {N}/5 | {%}% | Campaign ops, automation, lead routing |
| **Итого** | **{ACTIVE}/{TARGET}** | **{COVERAGE_PCT}%** | |

---

## Структура репо

```
GxG RevOps Playbook/
├── README.md               ← здесь
├── INDEX.md                ← полный реестр всех скиллов
├── CONTRIBUTING.md         ← как добавить/улучшить скилл
├── _staging/               ← сырое знание → будущие скиллы
│   └── {note}.md
├── .claude/skills/
│   └── gxg-revops-curator/ ← мета-скилл для ведения этого репо
│
├── pipeline/               ← {N} скиллов
├── demand-gen/             ← {N} скиллов
├── sales-enablement/       ← {N} скиллов
├── crm-ops/                ← {N} скиллов
├── rev-analytics/          ← {N} скиллов
├── cs-ops/                 ← {N} скиллов
├── rev-tech/               ← {N} скиллов
├── pricing-packaging/      ← {N} скиллов
├── territory-quota/        ← {N} скиллов
└── mktg-ops/               ← {N} скиллов
```

---

## Добавить скилл или знание

**Быстро — добавь в staging** (займёт 2 минуты):
```
/gxg-revops-curator — добавь в staging: [опиши что знаешь]
```

**Полноценный скилл** — см. [CONTRIBUTING.md](./CONTRIBUTING.md).

Куратор поможет с таксономией, шаблоном и quality gates:
```
/gxg-revops-curator — хочу написать скилл для X
```

---

## Аудит и здоровье коллекции

```bash
# Полный аудит: скиллы + staging
python .claude/skills/gxg-revops-curator/scripts/audit.py --root .

# Только staging
python .claude/skills/gxg-revops-curator/scripts/audit.py --root . --staging-only

# Конкретный домен
python .claude/skills/gxg-revops-curator/scripts/audit.py --root . --domain pipeline
```

---

*Поддерживается `gxg-revops-curator` · Обновлено {MONTH} {YEAR}*
