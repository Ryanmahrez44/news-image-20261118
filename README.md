# The World in One Day — Wednesday, 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Ryanmahrez44/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Ryanmahrez44/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image summing up the world news of **Wednesday, 18 November 2026**,
built for the [make.fun "Sum up 18 November's world news in one image"
bounty](https://make.fun/bounty/news-image-20261118). A newspaper front
page, drawn programmatically with Python PIL — crisp text, no photos, no
AI-generated imagery.

## What the image shows

Six stories, chosen for consequence and breadth across regions and fields:

1. **Iran Hits U.S. Base in Kuwait, Strikes Bahrain Again** (Middle East)
   — Tehran's drones target Ali Al Salem air base and Bahrain again, a day
   after U.S. jets struck a missile site on Iran's Qeshm Island; both Gulf
   states report interceptions.
2. **Trump Lands in Shenzhen; Xi and Putin Meet** (Diplomacy) — the three
   leaders prepare trilateral talks at the APEC summit, set for Thursday.
3. **Nvidia Board Rules Out Huang's Return** (Technology) — chair Harvey
   Jones says the board will not reinstate its co-founder; CFO Colette
   Kress stays interim chief.
4. **EU Proposes €45bn Ukraine Loan for 2027** (Europe) — €20bn for the
   budget and €25bn for arms, repaid only once Russia pays reparations.
5. **Fed Minutes Point to More Hikes** (Economy) — nearly all officials
   expect further rises if inflation stays hot; the October hold was 10–2.
6. **GTA VI Unlocks First in New Zealand** (Culture) — the game goes live
   region by region from midnight local time; early reviews arrive.

Every headline is faithful to the reporting of 18 November 2026; nothing
is invented, no quotes or figures were made up. Sources: live news wires
and news round-ups of 18 November 2026 (see BUILD_REPORT.md).

## How it works

- `build_image.py` — the PIL script that draws `entry.png` (1024×1024,
  ~151 KB). Run it to re-render the image.
- `main.ts` — the entrypoint (Node 22, standard library only). It copies
  `entry.png` to the output directory, so both runs produce byte-identical
  output:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
