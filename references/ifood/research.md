# iFood — visual and motion reference research

Research date: 2026-10-18. Target supplied Android package: `br.com.brainweb.ifood` 10.144.0 (361014415). The supplied APK is truncated. See `../../evidence/ifood-findings.md`. This folder contains reference materials only; no application was changed or launched.

## Evidence levels

- **A — original asset bytes:** extracted unchanged from complete, CRC-checked entries of the supplied APK. Original timeline, paths and keyframes are available. Runtime usage, renderer and lifecycle are not yet observed.
- **B — official static reference:** official store promotional screenshots, downloaded and visually inspected. These are marketing composites showing iPhone-like device frames even on Google Play, not native Android captures or complete app flows.
- **C — public engineering/process context:** official descriptions and historical engineer articles. They corroborate features/techniques but cannot establish current layout or precise motion.
- **Unknown:** no version-matched runtime capture. Never report guessed transition durations as measured original values.

## Primary public sources

1. [Official Google Play listing](https://play.google.com/store/apps/details?gl=BR&id=br.com.brainweb.ifood). Opened through web search; displayed update 2026-10-12. Seven 1080×2337 promotional PNGs downloaded to `screenshots/play-store-1.png` through `play-store-7.png`; exact source URLs and SHA-256 in `screenshot-sources.json`. Listing describes categories, search, bag checkout and order preparation/delivery tracking. The listing does not identify the version used in promotional captures.
2. [Official App Store listing](https://apps.apple.com/br/app/ifood-pedir-delivery-em-casa/id483017239). Opened successfully; search-provider snapshot displayed iOS 10.138.0 and version history. This differs from the supplied Android build and cannot validate Android geometry or transition timing.
3. [IFDS engineering/architecture article](https://tech.ifood.com.br/en/front-end/ifds-por-dentro-dos-padroes-de-engenharia-e-arquitetura-de-componentes-do-ifood-design-system/). Search indexed a primary iFood engineering article about connecting design/code through component standards. Direct fetch returned 403/internal errors, so **no token values, fonts or timing constants were obtained**. It is context, not a source for invented CSS tokens.
4. [Super fancy splashes! — Giovani Pereira](https://medium.com/macoclock/super-fancy-splashes-2f229a161155), **2020-12-22, historical iOS implementation**. Opened successfully. Describes secondary animated splash using Lottie, centered proportional artwork and cached date-selected seasonal animations. This explains why one bundled splash is not proof of the splash shown to every user/date. It is not evidence for current 2026 Android behavior.
5. [Official order flow explanation](https://institucional.ifood.com.br/institucional/como-funciona-um-pedido-do-ifood/) and [official coupons help](https://institucional.ifood.com.br/ajuda/cupons-e-descontos-do-ifood/). Primary pages found in search. Indexed excerpts corroborate item options/observations and selecting an eligible coupon. Direct opening returned 403, so these were not used as pixel or animation references.
6. [Official support article](https://institucional.ifood.com.br/clientes/suporte-do-ifood/). Indexed result describes an embedded official help short with profile/order entry points. Page returned 403; video was not viewed.
7. [Trailer linked from official Play listing](https://www.youtube.com/watch?v=P7ZGlXbIOio). ID verified from the listing thumbnail URL `https://i.ytimg.com/vi/P7ZGlXbIOio/hqdefault.jpg`. Video frames were not captured or measured. Secondary 2020–2021 tutorials surfaced in search and were intentionally not treated as version-matched motion evidence.

## Concrete UI reference matrix

| Surface | Observed reference | Measurable/visible facts | Confidence and missing evidence |
| --- | --- | --- | --- |
| Home header | Play screenshots 3 and 4 | White surface; centered address dropdown; notification bell at right; greeting below; purple Club link and coupon-count pill | B. No native pixel coordinate claim; promotional image scales/crops app. |
| Home categories | Play screenshots 3 and 4 | Two rows of four rounded light-grey icon tiles: restaurants, markets, pharmacies, drinks; Hits, Turbo, Shopping, Club. Pager indicator under grid. | B. Other categories and horizontal movement not observed. |
| Bottom navigation | Play screenshots 2–6 | Five items visible: Início, Busca, Hits, Pedidos, Perfil; small icon above label, white surface | B. This updates the older four-tab assumption; active appearance varies in composites. |
| Home content | Play screenshots 3 and 4 | Large promotional card below categories; pagination/progress marks; Últimas lojas section and Ver mais action | B. Exact aspect ratio of card should be extracted from the phone area, not full poster. |
| Promotion modal | Play screenshots 2, 5, 6 | Tall rounded colorful campaign card over dimmed home; white CTA near its bottom | B. Open/close gestures, backdrop opacity and motion timing unavailable. |
| Club | Play screenshot 6 | Purple/pastel-purple offer visual with faceted diamond illustration and CTA | B. Campaign-specific, not permanent brand-wide color specification. |
| Restaurant/menu/item | REA class names; official flow search excerpt | Restaurant menu/search, item detail, observation and cart exist | Static functionality evidence only. No complete current screenshot sequence. |
| Checkout/payment/coupon | REA class names; original coupon Lottie | Delivery-mode/cart/card modules exist; coupon outline geometry/timeline recovered | No current checkout layout, keyboard behavior or payment transitions observed. |
| Tracking/history | REA OrderList/OrderDetails; Play feature description | Order history/detail modules and preparation/delivery tracking supported | No verified current map route/driver/status animation or real ETA semantics. |
| Profile, favorites, search, error/empty states | REA names; favorites Lottie | Modules confirmed and one favorites animation recovered | Full screens/fonts/spacing missing. |

## Original motion asset matrix

All original JSON and `.lottie` containers are under `assets/`. Extracted nested JSON retains exact bytes. The source-member SHA-256 and parsed layer/shape inventories are in `motion-inventory.json`. Duration = `(op-ip)/fr`, not a wall-clock runtime measurement.

| Original member | Composition | FPS | Frame range | Nominal duration |
| --- | --- | ---: | --- | ---: |
| `assets/cazetv_splash.lottie` | 375×812 | 30 | 0–90 | 3.000000 s |
| `assets/favorite-empty-state.json` | 600×600 | 29.97 | 0–199 | 6.639973 s |
| `assets/ic_feed_anim.json` | 24×24 | 60 | 0–61 | 1.016667 s |
| `assets/ifood-splash.lottie` | 375×624 | 30 | 0–90 | 3.000000 s |
| `assets/loading.json` | 42×17 | 29.97 | 0–40 | 1.334668 s |
| `assets/outline_cupom_aplicado.json` | 240×40 | 30 | 0–106 | 3.533333 s |
| `assets/progress_bar_small.json` | 786×9 | 30 | 0–50 | 1.666667 s |
| `assets/success_purchase_tutorial_animation.lottie` | 750×888 | 30 | 0–385 | 12.833333 s |
| `assets/uber-consent.lottie` | 352×352 | 30 | 0–150 | 5.000000 s |
| `assets/uber-splash-animation.lottie` | 430×932 | 60 | 0–600 | 10.000000 s |

### Concrete motion observations

- **ifood-splash:** 30 fps; composition frames 0–90 (3.000 s); vector layers include Logo, Seta, d, eyes, F, i, Mercado, Food, Farmácia, Spray, Bebidas and Background. Arrow layer begins at frame 60 (2.000 s). Contains 54 path shapes, 6 rectangles, 61 fills and 63 transform groups, including nested assets. No external raster image required. Do not replace this with a generic pulsing text logo if claiming original artwork.
- **loading:** 42×17 composition with three 7×7 ellipse shapes, peach fill approximately `#fed298`. Opacity moves 30→100→30 with different starts: left begins at frame 0, middle frame 10, right frame 15. Composition lasts 40.0000016 frames at 29.9700012 fps. This particular original file is not a generic red bouncing-dot loader. Runtime recoloring is unknown.
- **outline_cupom_aplicado:** rounded closed outline, 1px dark `#141414` stroke; trim-path start animates 100→0 and offset 0→450 degrees across frames 0–60 (2.000 s), then composition continues to frame 106 (3.533 s). Bezier handles are embedded; do not substitute a guessed linear stroke.
- **progress_bar_small:** grey `#cccccc` base 786×9 with green approximately `#1fad68` path; morph keyframes at 0, 20, 40, with opacity fade boundaries at 0.5/1/39.5/40; composition 50 frames (1.667 s). This asset has no verified relation to food-order progress versus another tutorial.
- **favorite-empty-state:** 600×600, 199.000008 frames at 29.9700012 fps (~6.639973 s), 38 path shapes, 5 rectangles, fill/stroke/opacity structures across nested compositions. Loop policy not present as a confirmed native usage fact.
- **feed icon:** 24×24, 60 fps, 61 frames (~1.016667 s), 13 vector paths and trim-path structures. Could serve an animated icon, but its current screen usage is not established.
- **success purchase tutorial:** 750×888, 30 fps, 385 frames (12.833333 s), 1,125 path shapes and 33 merge-path operators. More complex than a success checkmark; browser renderer support must be checked before claiming faithful playback.
- **CazéTV seasonal splash:** 375×812, 30 fps, 90 frames; depends on extracted `images/2.webp`, preserved alongside JSON.
- **Uber-named assets are inside iFood:** consent 352×352/30fps/5s; splash 430×932/60fps/10s. They are iFood integration assets, **not evidence for the Uber standalone app splash**.

## What can and cannot be made identical

Byte-identical original Lottie payloads are now available. Replaying these at original speed, frame range, proportions and embedded easing is stronger than manually approximating them with CSS. Match selected rendered frames at a fixed viewport and DPR, accounting for SVG/Canvas differences, before describing rendered motion as equivalent. Native loop mode, playback speed overrides, theme recoloring, clipping, interaction triggers and end-of-animation navigation remain unobserved.

The following transitions are **unavailable as measured originals**: screen push/pop, bottom-sheet entrance/exit/spring, cart addition feedback, favorite-button tap, restaurant header collapse, search suggestion transitions, swipe carousel settling, checkout success navigation, map/driver movement, loading skeleton shimmer. Public stills cannot supply frame rate, easing or gesture interruption behavior. Any implemented transitions must be explicitly marked approximations until version-matched recordings or complete resources exist.

## Provenance verification

Source APK SHA-256: `654feb3007d1d86cc51cf70774f7bf8e80222128a87df2b5583fd47cc47801d7`. Recovered derivative and extraction provenance: `../../evidence/ifood-recovery.json`. This extraction only copies validated complete source entries; it does not repair missing classes/resources or certify APK signatures. `extract_motion.py` is reproducible and never executes app code. Store images are external official reference material; they are not extracted APK resources and should not be presented as recreated working screens.
