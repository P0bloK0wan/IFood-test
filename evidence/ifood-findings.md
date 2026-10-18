# iFood — REA static reconstruction findings

## Artifact completeness

The supplied `originals/iFood.apk` is **truncated**, not a complete usable APK. SHA-256: `654feb3007d1d86cc51cf70774f7bf8e80222128a87df2b5583fd47cc47801d7`. Size: 35,830,416 bytes. It has valid ZIP local headers but no central directory/end-of-central-directory. Original bytes were preserved.

Original REA `inspect-android-package` failed loading ZIP; exact complete envelope: `ifood-package.json`. A bounded sequential parser (`recover_ifood.py`) recovered **258 complete entries**, individually validating declared uncompressed lengths and CRC32. It stopped at offset 35,657,728 on `classes4.dex`: declared payload 9,602,344 bytes, only 172,644 available. Recovery provenance, per-entry hashes and offsets: `ifood-recovery.json`. The derivative `../recovered/ifood-partial-recovered.apk` is explicitly partial, reconstructed, unsigned, and unsuitable as a faithful original APK.

## REA observations from recovered derivative

`ifood-recovered-package.json`: successful REA/JADX 0.7.1 `inspect-android-package`, Java 21; 35,986 classes in three complete DEX files. `ifood-classes.json`: successful `search-android-classes` query `br.com.ifood`, 1,506 matching class names.

- Package: `br.com.brainweb.ifood`; version **10.144.0**; version code **361014415**.
- minSdk 32; targetSdk/compileSdk 36.
- Manifest also declares required ABI/density split types; supplied artifact alone does not establish a complete install set.
- Main activity declaration: `br.com.ifood.activity.HomeActivity`.
- Evidence of UI modules: `HomeFragment`, `HomeCategoriesPageFragment`, `MerchantMenuFragment`, `MerchantMenuSearchFragment`, `MerchantProfileFragment`, `ItemDetailsFragment`, `CatalogItemAddObservationActivity`, `CartFragment`, `CartScreenFragment`, `DeliveryModeSelectorFragment`, `FavoriteRestaurantsFragment`, `OrderListFragment`, `LegacyOrderDetailsFragment`, `OrderEditingV2Fragment`, `AbortOrderFragment`, payment-card and driver-profile fragments. Focused exact names: `ifood-ui-classes.txt`.
- Deep-link declarations include `/delivery`, `/favoritos`, `/checkout`, `/migration-checkout`, `/inbox`, `/comer-fora`, `/dinein`, `/ajuda`, `/profile/credentials`, `/seguranca/dispositivos`.
- This supports a reconstruction scope of home/categories → merchant/menu → item/observation → cart/delivery/payment → local order tracking/history, plus favorites. **Class/route existence does not prove runtime layout, transitions, API semantics, or feature availability.**

## Supplemental ZIP-level observations (not additional REA claims)

- Kotlin metadata and AndroidX Compose, Fragment, navigation, data/view binding, Room, Retrofit and OkHttp metadata are present. Architecture is native Android/Kotlin with Compose and traditional views; no recoverable web app bundle was found in complete entries.
- Only two `.js` assets are present: Braze messaging bridge integrations. They are not the app's frontend.
- Missing from recovered portion: `resources.arsc`, `res/` layouts/drawables/fonts, ordinary restaurant/product photography, native library entries. Therefore precise typeface, spacing, brand palette, product catalog and full screen layouts cannot be reconstructed from this fragment.
- Font present: `assets/fontawesome-webfont.ttf` (icon font, not text font).
- Useful animations: `ifood-splash.lottie`, `cazetv_splash.lottie`, `favorite-empty-state.json`, `outline_cupom_aplicado.json`, `loading.json`, `success_purchase_tutorial_animation.lottie`, `uber-consent.lottie`, `uber-splash-animation.lottie`.
- iFood splash contains vector layers named `Logo`, `Seta`, `Mercado`, `Food`, `Farmácia`, `Bebidas`; colors include `#ed1b30` and `#eb0033` alongside illustration colors. This is animation evidence, **not a verified application-wide design token palette**; see `ifood-splash-colors.json`.

## Reconstruction constraints

No APK was executed, no account accessed, and no product API called. APK signatures and missing code/resources/splits were not verified. A functional local web prototype can implement the confirmed feature categories and familiar visual structure. Calling it visually identical or connected to real iFood deliveries/payments would exceed the available evidence.
