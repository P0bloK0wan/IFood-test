# iFood identity v3 — bounded public-source asset research

Date: 2026-10-18. Scope: official visual identity resources, no application/repository changes. All network requests used HTTPS with normal TLS validation. No authentication, anti-bot bypass, guessed font paths, or font-mirror downloads.

## Ready to integrate: five real CDN artworks

The following files were downloaded directly from `static.ifood-static.com.br`, returned HTTP 200/image/png, decoded and verified with Pillow, visually inspected, and hashed. All have transparent backgrounds. Exact bytes, dimensions, URLs and SHA-256 are recorded in `asset-provenance.json`.

| File | Dimensions | Appearance | Status versus current native-app icon |
| --- | --- | --- | --- |
| `restaurant.png` | 229×160 | Cutout cheeseburger photograph | Real iFood landing artwork; differs from small 3D hamburger in current Play screenshot |
| `market.png` | 235×177 | Red grocery cart with vegetables | Real iFood landing artwork; different composition from native category tile |
| `pharmacy.png` | 100×86 | Light-blue medicine case with pink cross | Real iFood landing artwork; useful replacement for generic icon |
| `drinks.png` | 139×95 | Glasses of beer and cola | Real iFood landing artwork; native screenshot has bottles instead |
| `petshop.png` | 135×77 | Bowl of dog biscuits | Additional real category artwork; not one of the eight initial requested tiles |

URLs were discovered in [public HTML references](https://github.com/KalyssonRyan/Clone-Ifood/blob/7f8c3b8781d8853f3f07f6ba52541ef95d65357b/index.html), corroborated by [another public reference](https://github.com/FernandoTakao/Ifood/blob/40cc914fdb01f6f27132bddf6a0b6066a0fc70d4/static/index.html). The GitHub pages are third-party discovery aids, **not the final asset source**. Downloads used the exact URLs cited there:

- https://static.ifood-static.com.br/image/upload/f_auto/webapp/landingV2/restaurant.png
- https://static.ifood-static.com.br/image/upload/f_auto/webapp/landingV2/market.png
- https://static.ifood-static.com.br/image/upload/f_auto/webapp/landingV2/pharmacy.png
- https://static.ifood-static.com.br/image/upload/f_auto/webapp/landingV2/drinks.png
- https://static.ifood-static.com.br/image/upload/f_auto/webapp/landingV2/petshop.png

These are better provenance than generic substitutes, but substituting them still does **not** establish pixel-identical native category artwork. The exact eight current native icons remain visible only in previously archived promotional screenshots.

## Typography: primary evidence, binary unavailable

[The typeface designer's public case](https://fabiohaagtype.com/en/ifood-font/) was readable through the web tool. It identifies **Tipo iFood**, collaboration with FutureBrand and iFood, and a dedicated Text variant with different `a` and `g` shapes for small-size legibility. The case is official evidence from the creator, not a community token approximation.

Searches for iFood RC Textos/Titulos found third-party repositories and font mirrors. Their CSS references local font files, not verifiable official CDN URLs. None was copied as an authenticated official font. No official RC Textos/Titulos font binary was downloaded. Do not relabel Inter or another fallback as Tipo iFood, and do not infer the current Android font from an older website's font family name.

## Logo and remaining categories

- An official-host logo PNG URL, `https://static.ifood.com.br/webapp/images/logo-smile-512x512.png`, was discovered in a [public project reference](https://github.com/PedroHenriqueBarros/iFood-Project/blob/bd4b591149d6a8e57401c752153e61d4cf07e8c0/README.md). Fetch returned 403; no file was saved or substituted.
- SVG search found third-party logo libraries and mirrors, not an independently verified current official SVG file. No new logo SVG was saved.
- No public verified direct assets for **Hits, Turbo, Shopping, Clube** were located in this bounded search.
- Original vector logo artwork remains present in the already extracted `../assets/ifood-splash/animations/data.json`. It is original APK data; this research did not alter or trace/rebuild it as a new logo.

## Screenshots and coverage

Previously downloaded official Play Store references remain in `../screenshots/play-store-1.png` through `play-store-7.png`; see `../research.md`. They show home, category grid and promotional overlays, not a complete restaurant/product/bag/orders/profile sequence.

[Official order-flow article](https://institucional.ifood.com.br/institucional/como-funciona-um-pedido-do-ifood/) was found, but direct and web-tool opening returned 403 during this research. No guessed `tela1` URL was attempted. Search indexed its feature descriptions, which cannot establish exact pixel layouts. The official [2025 culture PDF](https://carreiras-cdn.ifood.com.br/assets/2025/12/DECK-DE-CULTURA-IFOOD_2025.pdf) surfaced in search with an app-home illustration; downloading returned 403, so it was not available as a local screenshot source. No new version-matched restaurant/product/bag/orders/profile screenshots were acquired.

## Failed reads and boundaries

`www.ifood.com.br`, `institucional.ifood.com.br`, `beneficios.ifood.com.br`, the culture PDF, designer-page direct download and its linked image returned HTTP 403. Records for the initial home requests are in `initial-fetches.json`; asset success/failure records are in `asset-provenance.json`. These were website/network responses, not automatic approval-review rejections. Requests were not retried through proxies, downgraded to HTTP, or made with TLS verification disabled.

## Integration guidance

Use the four relevant CDN images for restaurants/markets/pharmacies/drinks if the goal is an improvement using authentic published brand material. Keep the native-artwork mismatch recorded. The exact four other native category artworks and font binaries still require a complete APK resource set, authorized published assets, or version-matched screen/reference files. Do not treat this research as completion of the user's requested full visual identity.
