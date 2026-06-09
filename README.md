![Skills](https://img.shields.io/badge/skills-1%20active-yellow)
![Coverage](https://img.shields.io/badge/coverage-2%25-red)
![Domains](https://img.shields.io/badge/domains-10-blue)
![Updated](https://img.shields.io/badge/updated-June%202026-lightgrey)

# GxG RevOps Playbook

**Коллекция скиллов для Claude, покрывающая весь стек Revenue Operations.**

Каждый скилл — это готовый workflow: запустил, получил результат.
Не инструкции "как думать о RevOps" — а "как сделать прямо сейчас".

---

## Зачем

- ✅ **Скорость** — стандартные RevOps задачи решаются за один вызов скилла, без промпт-инжиниринга
- ✅ **Единый стандарт** — все в команде работают по одному GxG-подходу
- ✅ **Живая база знаний** — staging-область для доменного знания, которое ещё не стало скиллом
- ✅ **Полный стек** — цель: 51 скилл в 10 доменах от pipeline до CS ops

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
| [pipeline](./pipeline/) | 0/6 | 0% | Управление воронкой, прогнозирование, стейдж-менеджмент |
| [demand-gen](./demand-gen/) | 0/5 | 0% | ICP, лид-скоринг, MQL/SQL-критерии, ABM |
| [sales-enablement](./sales-enablement/) | 1/7 | 14% | Плейбуки, battle cards, работа с возражениями |
| [crm-ops](./crm-ops/) | 0/6 | 0% | Salesforce/HubSpot, качество данных, автоматизация |
| [rev-analytics](./rev-analytics/) | 0/5 | 0% | KPI, атрибуция, дашборды, ARR/NRR/GRR |
| [cs-ops](./cs-ops/) | 0/5 | 0% | Health scoring, QBR, retention, expansion |
| [rev-tech](./rev-tech/) | 0/4 | 0% | Стек инструментов, интеграции, vendor eval |
| [pricing-packaging](./pricing-packaging/) | 0/4 | 0% | CPQ, тиры, deal desk, discount governance |
| [territory-quota](./territory-quota/) | 0/4 | 0% | Territories, квоты, ramp планы, компенсация |
| [mktg-ops](./mktg-ops/) | 0/5 | 0% | Campaign ops, automation, lead routing |
| **Итого** | **1/51** | **2%** | |

---

## Структура репо

```
GxG RevOps Playbook/
├── README.md               ← здесь
├── INDEX.md                ← полный реестр всех скиллов
├── CONTRIBUTING.md         ← как добавить/улучшить скилл
├── _staging/               ← сырое знание → будущие скиллы
├── .claude/skills/
│   └── gxg-revops-curator/ ← мета-скилл для ведения этого репо
├── pipeline/
├── demand-gen/
├── sales-enablement/
├── crm-ops/
├── rev-analytics/
├── cs-ops/
├── rev-tech/
├── pricing-packaging/
├── territory-quota/
└── mktg-ops/
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

*Поддерживается `gxg-revops-curator` · Обновлено June 2026*
