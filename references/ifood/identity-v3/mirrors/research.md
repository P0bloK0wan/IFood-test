# iFood font and wordmark mirrors — 2026-10-18

## Recommended assets

Eight valid WOFF2 files are saved here. Use `iFoodRCTextos-Regular.woff2` (400) and `iFoodRCTextos-Medium.woff2` (500) for UI text, and `iFoodRCTitulos-Medium.woff2` (500) / `iFoodRCTitulos-Bold.woff2` (700) for headings where the reference requires them. Light (300) and Bold (700) Textos, and Light/Regular Titulos, are also available. Total font payload: 226,688 bytes.

Source is explicitly a **public GitHub mirror**, not an official CDN download: [KalyssonRyan/Clone-Ifood, fixed commit](https://github.com/KalyssonRyan/Clone-Ifood/tree/7f8c3b8781d8853f3f07f6ba52541ef95d65357b/fonts). URLs were derived from that repository's published HTML/CSS. Downloaded files retain their original bytes; individual HTTP status, byte size, SHA-256, font tables and names are in `font-validation.json`. The `.woff` alternatives declared in its CSS returned 404; successful files are `.woff2`.

FontTools fully decompressed and decompiled all eight WOFF2 files with checksum checking enabled. Each has 355 glyphs and supports all the tested Portuguese accented letters. The names report **iFood RC Textos / iFood RC Titulos**, version **0.900**, copyright **2021 iFood.com Agência de Restaurantes Online S.A. All rights reserved**, manufacturer **Fabio Haag Type / VLF Design Ltda**, designer **Fabio Haag Type**. These are meaningful internal identity signals, although metadata alone is not proof of an official distribution chain. No reuse license was established. OS/2 embedding flags and copyright are recorded rather than being treated as license grants.

The [designer's primary case study](https://fabiohaagtype.com/en/ifood-font/) describes Tipo iFood as a custom family by Fabio Haag Type with FutureBrand and iFood; its text variant changes `a` and `g` for small-size legibility. The mirror files' designer metadata and paired Textos/Titulos families are consistent with this account. FontTools outline comparison confirms different `a` and `g` drawings between these two Regular files (see `glyph-comparison.json`). This supports the candidate selection, but does **not** prove that this 0.900/2021 build is byte-identical to the current native app or the version pictured in the case study. No typography binaries were recoverable from the supplied truncated APK for direct comparison.

## Full vector wordmark

`ifood-wordmark.svg` is the complete red iFood lettering plus smile, not a text approximation. It is 1,139 bytes, viewBox `0 0 1004 530.58`, with two vector paths colored `#ea1d2c`. SVG XML parsed successfully; no scripts or foreignObject elements are present. Source: [Istio's public case-study repository, fixed commit](https://github.com/istio/istio.io/blob/a03df1cfd4fda35a88a37b7a6486141c1c153bea/archive/v1.23/logos/ifood.svg). Its case-study index associates this logo with the official iFood website. Preserve its aspect ratio when displaying it. `logo-provenance.json` records exact source, Git blob SHA and SHA-256.

The [Wikimedia Commons logo page](https://commons.wikimedia.org/wiki/File:IFood_logo.svg) independently identifies the same full wordmark and title `ifood-43`, attributes the logo to iFood and cites logopng.com.br. The Commons page labels its own file PD-textlogo with a separate trademark notice; this is not a newly inferred license for our downloaded mirror. Wikimedia's original SVG download and API returned HTTP403, so no Wikimedia file was obtained and no block was bypassed. The actual local SVG came from the independently public Istio repository.

No app code, application dependencies, or published repository was modified. Brotli was installed only into `/tmp/ifood-font-tools` to enable FontTools WOFF2 validation.
