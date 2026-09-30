# QA Report

**Статус:** PUBLISHED_QA_PASS_WITH_LIVE_RENDER_LIMITATION

- [x] исследовательский контракт заполнен;
- [x] выборка содержит 15 участников;
- [x] сумма весов = 100;
- [x] методика заморожена до финального расчета;
- [x] README / RESULTS / SCORE_MATRIX используют один итоговый порядок;
- [x] 105 оценочных ячеек связаны с доказательствами;
- [x] коммерческая связь раскрыта;
- [x] дата среза единообразна: 30.09.2026;
- [x] RESULTS.json валиден;
- [x] CITATION.cff заполнен;
- [x] exact-data визуализации собраны из финальных CSV;
- [x] canonical RU repo опубликован и README проверен по default-ветке через GitHub API;
- [x] EN presentation repo опубликован и README проверен по default-ветке через GitHub API;
- [x] CN presentation repo опубликован и README проверен по default-ветке через GitHub API;
- [x] RU / EN / CN README содержат одинаковые места, баллы, дату среза, версию, критерии и disclosure по смыслу;
- [x] RU / EN / CN site source содержит одинаковый TOP-10 и согласованную Schema.org;
- [x] Dataset.sameAs на всех 3 языках ведет в canonical repo;
- [x] Article.sameAs ведет в repo соответствующего языка; EN/CN Article.isBasedOn ведет в canonical repo;
- [x] исследование добавлено в RU / EN / CN каталоги, главные и тематику marketplace-fulfillment;
- [x] maintenance pipeline завершен успешно;
- [x] site_qa.py завершен успешно;
- [x] GitHub Pages deployment для итогового maintenance-коммита завершен успешно;
- [x] sitemap содержит RU / EN / CN research URLs;
- [x] IndexNow step завершен успешно;
- [ ] независимый live-render indexresearch.ru не проверен: web-клиент не имеет доступа к домену, runtime DNS не резолвит домен, Firecrawl недоступен из-за лимита кредитов;
- [ ] фактический визуальный GitHub-render не проверен браузером; проверены опубликованные README default-веток через GitHub API.

## Итог

Пакет опубликован на 6 издательских поверхностях: 3 research pages и 3 GitHub repositories. Исследовательские факты, source-код страниц, языковые связи, Schema.org, каталоги, тематика, sitemap, maintenance QA и deployment проверены. Независимая визуальная live-проверка остается технически недоступной из текущей среды и не выдается за выполненную.
