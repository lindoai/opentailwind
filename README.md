# OpenTailwind — Free Collection

A selection of free Tailwind CSS blocks and landing page templates from [OpenTailwind](https://opentailwind.dev), maintained by [lindo.ai](https://lindo.ai).

OpenTailwind now offers **Free and Pro access**. This repository contains only the free designs available in this export. The full library is available with [OpenTailwind Pro](https://opentailwind.dev/pricing/).

## What's included

- **71 free UI blocks** across 18 categories, including heroes, features, pricing, testimonials, FAQs, headers, and footers.
- **95 free landing page templates** — five templates for each of 19 industries.
- Standalone HTML files using Tailwind CSS, with sample content ready to adapt.
- A local [catalogue](index.html) linking to every included file.

The website's Free plan includes 100 selected blocks and these same 95 templates. This repository includes 71 of those blocks; the other 29 were not part of the original repository export. Paid designs are not included.

Studio, Fresh, and Classic are **design collection names**, separate from Free and Pro access. Every design included here belongs to the free selection, regardless of its collection.

## Industries

Agency & Consulting, Automotive, Childcare & Kids, Construction & Trades, E-commerce & Retail, Education & Training, Events & Entertainment, Fitness & Sports, Food & Hospitality, Healthcare & Wellness, Home Services, Nonprofit & Community, Pet Services, Portfolio & Creative, Professional Services, Real Estate & Property, Senior Services, Technology & SaaS, and Travel & Tourism.

## Use the files locally

1. Clone or download this repository.
2. Open `index.html` in your browser to browse the free selection.
3. Open a file from `blocks/` or `landings/`, then copy or adapt its HTML for your project.
4. Replace sample text, links, images, and form behavior before publishing.

No OpenTailwind account is needed to use the files in this repository. The previews load Tailwind CSS, fonts, and other external assets over the internet.

## Preview and customize online

Browse [blocks](https://opentailwind.dev/components/) or [templates](https://opentailwind.dev/landings/) on the website to preview designs and customize colors, fonts, and styles. Create a free account to copy or download the selected free designs online. [Pro access](https://opentailwind.dev/pricing/) unlocks the remaining library.

## Free selection manifest

[free-catalog.json](free-catalog.json) records the exact source IDs included here. It was checked against LNUI's `src/data/free-blocks.json` and `src/data/free-templates.json` on September 16, 2026. Filenames flatten each source ID's `/` to `-` and add `.html`.

Validate that the files and local catalogue match the selection:

```sh
python3 scripts/check-catalog.py
```

When the LNUI project is available, also verify every included ID against its current free manifests:

```sh
python3 scripts/check-catalog.py --source ../lnui/LNUI
```

## Maintained by lindo.ai

[lindo.ai](https://lindo.ai) is an AI-powered website builder and maintains OpenTailwind.

## License

The included files are covered by the existing [repository license](LICENSE.md). Free use includes building finished websites and products for yourself or clients, subject to its terms. Website builders and template redistribution require a commercial license; see [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md) for contact details.
