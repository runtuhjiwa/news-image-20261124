[![Competition](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/runtuhjiwa/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/runtuhjiwa/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# news-image-20261124

Sum up 24 November 2026's world news in one image — a make.fun entry.

`entry.png` is a five-panel news-magazine front page ("THE WORLD — Tuesday, 24 November 2026") summing up the day's five biggest world stories. `main.py` copies it to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`) and validates the PNG magic bytes, IHDR chunk, dimensions and file size.

## The five stories

1. **Tankers ablaze in Hormuz** — Iran's Revolutionary Guard Corps said three oil tankers caught fire after striking naval mines in the Strait of Hormuz while under US military escort; the claim was carried by IRNA early on Tuesday 24 November and could not be independently verified, with US Central Command yet to respond.
2. **Huang is back** — Nvidia's board unanimously reinstated co-founder Jensen Huang as president and CEO with immediate effect, less than two weeks after he resigned on 12 November; shares jumped about 31% to $165.05 and Wall Street rebounded on Tuesday 24 November.
3. **Zaporizhzhia hit** — An overnight Russian strike on residential areas of Zaporizhzhia killed 2 people and wounded 40, including four children, regional governor Mykhailo Semikin said on Tuesday 24 November; a private house was destroyed and a five-storey apartment block partly destroyed.
4. **Hamas security chief killed** — Israeli airstrikes killed Naeem Abu Nahel, the director of Hamas' internal security apparatus in Gaza, in western Gaza City on Tuesday 24 November; at least seven Palestinians were killed, including two police officers, medics and police said.
5. **Nuclear satellite alarm** — NATO Secretary General Mark Rutte said the alliance will defend against threats in space after German media reported Russia may launch a nuclear-armed satellite, dubbed "Sputnik-S", within 60 days; Chancellor Friedrich Merz called the reports a sign of the escalation Russia is prepared to pursue.

## Notes on sourcing

Each panel was checked against reporting dated Tuesday 24 November 2026
(Reuters, IRNA via the press, Nvidia's own announcement, NATO's Berlin press
conference). Two points of care: the Hormuz tanker story is presented as
Iran's claim, because it could not be independently verified when reported;
and the fifth panel is the NATO space warning, not the COP31 collapse — the
COP31 talks ended without a deal on Sunday 22 November, so they belong to
that day's news, not this one.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png`.
