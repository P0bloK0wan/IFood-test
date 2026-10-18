# iFood public motion reference inventory — 2026-10-18

This bounded survey covers public references located through web search, official/author portfolios, and the already recovered APK assets. It is **not an exhaustive inventory of every animation shipped in every version or experiment**. A portfolio rendition is not the original executable Lottie JSON.

## Most useful new source: checkout waiting characters

[iFood Waiting Pages, Brão Barbosa's own portfolio](https://braobarbosa.com/project/ifood-waiting-pages) describes the animation between tapping Pay and receiving order confirmation. Eight variants use three context characters plus the iFood bag, walking in a loop. Stated contexts include restaurant, groceries, pharmacy, loyalty club, free delivery and Uber orders; the public evidence does not unambiguously name all eight variants. Authors: animation by Brão Barbosa and Edmar Almeida; illustration by Rentz, Edmar and Brão; Craft manager Cassius Fraga; director Isabel Araújo.

The [Behance case](https://www.behance.net/gallery/253365793/iFood-Waiting-Pages), published July 27, 2026, and [author LinkedIn post](https://www.linkedin.com/posts/braobarbosa_motiondesign-characteranimation-lottie-activity-7488987674847076353-8Dzn), whose downloaded HTML contains publication date July 31, 2026, independently identify the same project. The author states each native Lottie is approximately 30 KB. That is an author claim, not a locally measured JSON size.

**16 exact public GIF URLs** were obtained by following image links from the author's portfolio; see `public-gif-catalog.json`. First four are:

- https://braobarbosa.com/uploads/behance/01-ifood-waiting-pages/006.gif
- https://braobarbosa.com/uploads/20260915144758-6f2ae218d823.gif
- https://braobarbosa.com/uploads/behance/01-ifood-waiting-pages/012.gif
- https://braobarbosa.com/uploads/behance/01-ifood-waiting-pages/015.gif

The remaining twelve are separately linked character/loop studies, not evidence of twelve additional shipped checkout states. No URL was guessed. The web tool resolved them as image/gif but cannot render that media type. Direct HTTPS requests for the first two returned HTTP406, and were not retried with spoofed headers. Consequently none has a locally verified duration, dimensions or hash. Their visible page context is verified; their detailed frames are **not** observed in this survey.

The LinkedIn page was successfully saved as `linkedin-waiting.html`. It embeds public 640p/720p MP4 source URLs, preserved in `public-video-catalog.json`. Structured metadata declares PT3S and a 1280×720 display; its encoding URL identifies 30fps. Downloading the 720p source returned HTTP403, so no video file or frame measurement was obtained. Do not equate a three-second social preview with the native Lottie's measured cycle length.

## Other independently located public motion references

| Reference | Class and context | Verified available evidence / limits |
|---|---|---|
| [Ailo iFood — Brão Barbosa](https://braobarbosa.com/project/ailo-ifood) | Author case study, iFood AI assistant | First set of 15 animated expressions delivered as Lottie. Case video https://player.vimeo.com/video/1224435478 and onboarding https://player.vimeo.com/video/1224942311 . Not consumer checkout animation. |
| [iFood Ads Loading — Brão Barbosa](https://braobarbosa.com/project/ifood-ads-loading) | Author case study, advertiser portal | Cat archer targets apple on shopper, hit/drop/megaphone/reset. Author states four-second loop and 234 KB vector Lottie without rasters. Videos https://player.vimeo.com/video/1231767092 and https://player.vimeo.com/video/1231767091 . Not consumer-app checkout. |
| [Carol Teixeira, checkout loader post](https://pt.linkedin.com/posts/carolina-teixeira_j%C3%A1-pediu-seu-ifood-hoje-recentemente-alteramos-activity-7199195144091275264-F0oB) | Author account, earlier checkout implementation (2024) | Describes loading after finalizing the bag while order is generated; Edmar illustrations/key poses and Lottie implementation across Android/iOS. Public text confirms flow; source JSON not provided. |
| [iFood illustration system — redesign](https://www.behance.net/gallery/245903389/iFood-illustration-system-redesign) | Authors' product illustration system, 2022–2026 | April 6, 2026 case, authors Edmar Almeida, Andrés Cabrera, Carolina Teixeira, Brão Barbosa, Matheus Bomfim, Rentz. Indexed text available; opening returned403. |
| [iFood illustration system](https://www.behance.net/gallery/240708093/iFood-illustration-system) | Authors' earlier system case | Describes empty states and Meus Foods annual recap. Indexed evidence only; opening returned403. |
| [Super fancy splashes! — Giovani Pereira](https://medium.com/macoclock/super-fancy-splashes-2f229a161155) | iFood engineer's primary account, December22,2020 | Historical holiday splash; Lottie loaded in a secondary screen after static iOS launch image; cached remotely scheduled JSON; recommended under3s and embedded assets. Does not describe current app's complete timing. |
| [Groceries iFood — Bruno Parizotto](https://lottiefiles.com/pt/free-animation/groceries-ifood-W6VqqP6KLW) | Public community upload, official provenance unestablished | Page states groceries splash,15.4KB, Simple Lottie License. **Do not label original official** merely because title contains iFood. Direct fetch403; no source binary obtained. |
| [iFood Design&Motion — Vinicius MAIA](https://www.behance.net/gallery/130660241/iFood-Design-Motion) | Author campaign portfolio, November5,2021 | Advertising campaign/prototype videos (Betatype/Pizzou), not proof of consumer app motion. |
| [iFood 6ª Estrela](https://www.behance.net/gallery/158639307/iFood-6-Estrela) | Author campaign case, World Cup2022 | Mentions individually animated confetti and organic transitions, but in campaign film context; not a bag confirmation reference. |

## Original assets already available locally

`apk-motion-summary.json` references the existing ten complete animations recovered from the user's truncated iFood APK; originals are under `references/ifood/assets/`. These remain stronger evidence for exact executable motion than public video renditions. Relevant examples: iFood splash 3s/30fps; loading dots1.334668s/~29.97fps; coupon outline3.533333s/30fps; small progress1.666667s/30fps; favorite empty6.639973s/~29.97fps; feed icon1.016667s/60fps; purchase tutorial12.833333s/30fps. Exact dimensions and file paths are in the JSON.

`cazetv_splash/animations/animation.json` includes a precomposition layer named **confete** and another named **fitas**. This is original artwork recovered from the APK, but its source context is the CazéTV/FIFA2026 campaign splash. It does **not** establish that the same confetti appears in the bag. Reusing it there would be a chosen adaptation and should be described accordingly. Uber-consent and Uber-splash in this iFood APK are integration assets, not standalone Uber-app animations.

## Implementation implications

For order acceptance, the new source verifies a **contextual walking-character waiting state after Pay and before confirmation**. It does not substantiate an arbitrary fixed backend acceptance duration or all subsequent transition curves. The public Lottie JSON for these newer characters was not exposed in the fetched sources. A handcrafted imitation should not be called identical to the original file.

No public evidence located here verifies a specific original **confetti-in-bag** animation. Campaign confetti, generic LottieFiles confetti and other delivery brands' success animations are separate evidence and should not be misattributed to iFood. The parent task researches the original illustrated courier separately through the iFood Design Dribbble profile.

No app code, product dependencies, Git state or published site was modified. All direct requests used HTTPS with normal certificate verification.403/406 responses were recorded and respected. The first portfolio survey obtained URLs but no binaries; the subsequent official Dribbble survey below successfully obtained six media files.

## Verified downloads from the official iFood Design Dribbble profile

Source: https://dribbble.com/ifooddesign . Exact media URLs were read from the existing `courier/ifood-design.html`, specifically each shot's `data-video-teaser-large`, `data-animated-url`, or noscript image src. All six downloads returned HTTP200 and their bytes were preserved unchanged in `research/dribbble/`. `manifest.json` records source URLs, sizes, SHA-256 and full ffprobe output; separate `*-ffprobe.json` files also exist. These are **official design-team portfolio media**, not recovered native animation source code and not proof of the currently shipped consumer app.

| Shot / local file | Measured media | Observed motion and classification |
|---|---|---|
| [Restaurant Rating](https://dribbble.com/shots/7637059-Restaurant-Rating), `restaurant-rating.mp4` | 337,946B;800×600;30fps;383frames;12.766667s | Phone transitions from restaurant dashboard to reviews; expressive star changes from low to high rating. The page explicitly calls this a **rating concept transition for iFood for Restaurants**. Designer DanielMots, illustrator Edmar Almeida. Partner-app concept, not the consumer's post-order rating. |
| [Home screen main covers](https://dribbble.com/shots/6749537-Home-screen-main-covers), `home-main-covers.mp4` | 215,557B;800×600;60fps;290frames;4.833333s | Historical consumer home showcases horizontally changing time-of-day campaign covers, food imagery and changing surrounding presentation color. Observed café da manhã, afternoon, dinner and late-night themes. A portfolio presentation including a phone frame, not a standalone banner animation. |
| [Order Manager: Redesign Concept](https://dribbble.com/shots/6666774-Order-Manager-Redesign-Concept), `order-manager-concept.mp4` | 148,367B;800×600;60fps;232frames;3.866667s | Restaurant's desktop/tablet order cards switch between light/dark themes through left navigation. **Explicit redesign study**, Figma/Principle. Gabriela Neri for iFood; published **June21,2019**, verified from public page text. Not consumer checkout. |
| [Tab bar](https://dribbble.com/shots/6631314-Tab-bar), `tab-bar.mp4` | 144,189B;800×600;60fps;590frames;9.833333s | Consumer navigation switches home/search/orders/profile with active icon treatment; phone and surrounding colored backdrop are presentation elements. Page says consumer app interaction, Figma/Principle, Mariana Flamenbaum. Historical layout; current five-tab Hits navigation is not established by this older reference. |
| [Animation • Delivery app](https://dribbble.com/shots/9894657-Animation-Delivery-app), `delivery-app.gif` | 630,672B;1600×1200;74frames;30ms each;2.22s total | Map with route and delivery cards; red line accents pulse around an Entrega marker/card. Public page specifies **iFood Box flow**, design Dulce/@dulceakemi. It is not an animated red motorcycle courier sprite. |
| [iFood Loop Onboarding](https://dribbble.com/shots/7863300-iFood-Loop-Onboarding), `loop-onboarding.jpg` | 44,345B;400×300;JPEG;one frame | Static composition of three illustrated onboarding phone screens, pink background. Illustrator @meuri. **Not an animation**, despite Loop in the product name. Exact downloaded URL includes resize=400x0; no larger URL guessed. |

Three frames per video/GIF were extracted for inspection at approximately0%,33%,67% of duration; these derived JPEGs and `contact-sheet.jpg` are reference previews, separate from the unchanged downloaded files. Whole-file duration includes demonstration/presentation, and must not be mistaken for the duration of an individual native transition. Metadata on the currently fetched shot pages did not expose publication dates; June21,2019 above was available in the indexed Order Manager page. Other dates remain unverified rather than inferred from shot IDs.

The parent researcher separately obtained `courier/order-tracking.mp4` from shot6774843 and inspected it (15s,60fps). It is not duplicated here. The public portfolio catalog should keep consumer-app tracking/tab/home, restaurant-app rating/manager concepts, delivery-partner Box, and static Loop illustrations as distinct contexts.
