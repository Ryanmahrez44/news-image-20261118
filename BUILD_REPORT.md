# BUILD REPORT — news-image-20261118

## Entry
- Bounty: "Sum up 18 November's world news in one image"
  (https://make.fun/bounty/news-image-20261118, $250, top 50 paid)
- Deadline: Fri 20 Nov 2026 07:00 WIB
- Image: `entry.png` — 1024×1024 px, 151,202 bytes (limit: 1 MiB, 1024×1024)
- Entrypoint: `main.ts` (Node 22, stdlib only — `node:fs`, `node:path`)
- Method: the repo holds the image; `main.ts` copies it to the output
  directory. The image was drawn programmatically with Python PIL
  (`build_image.py`), never AI-generated, so no text is garbled.
- Built by reusing the news-image-20261119 generator and adapting it to
  the verified news of 18 November 2026.

## The six stories (all verified from live news of 18 Nov 2026)
Chosen for consequence and breadth across regions and fields:

1. **Iran Hits U.S. Base in Kuwait, Strikes Bahrain Again** (Middle East,
   lead) — Iran's army said its drones struck US air defences and launch
   systems at Ali Al Salem Air Base in Kuwait; Bahrain said its air
   defences repelled several Iranian attacks before dawn. A day earlier,
   US jets struck an IRGC missile launch site on Qeshm Island. Kuwait
   and Bahrain reported interceptions and no damage or casualties.
   Sources: Reuters via telegraph.ng, The National via titobaronmedia.com,
   geopolitiki.com, thecurtain.online (all 18 Nov 2026).
2. **Trump Lands in Shenzhen; Xi and Putin Meet** (Diplomacy, Asia) —
   Donald Trump landed in Shenzhen on Wednesday; Xi Jinping and Vladimir
   Putin met on the APEC margins, with trilateral talks set for Thursday
   and no published agenda. Sources: NPR
   (npr.org/2026/11/18/nx-s1-6045518/trump-china-xi-putin), Open Chronicle
   global news brief 18 Nov 2026, Medium/All Voices strategic brief.
3. **Nvidia Board Rules Out Huang's Return** (Technology) — board chair
   Harvey Jones said on the Q3 FY27 earnings call that the board
   unanimously accepted Jensen Huang's resignation and does not intend to
   reinstate him as CEO; CFO Colette Kress serves as interim CEO while
   the board searches for a permanent chief. Q3 revenue $115.84bn.
   Sources: The Motley Fool (18 Nov 2026), The Hindu BusinessLine
   (18 Nov 2026), YourStory (18 Nov 2026).
4. **EU Proposes €45bn Ukraine Loan for 2027** (Europe, Ukraine) — the
   European Commission proposed a new €45bn loan for 2027: €20bn budget
   support and €25bn military assistance, covering two-thirds of
   Ukraine's €70bn financing gap, repaid only once Russia pays
   reparations. Sources: Reuters explainer (18 Nov 2026), Agence Europe
   (18 Nov 2026), EUobserver via 7788news.com (18 Nov 2026).
5. **Fed Minutes Point to More Hikes** (Economy, US) — minutes of the
   27–28 Oct FOMC meeting, released 18 Nov at 2:00 p.m. ET: almost all
   participants judged further rate rises would likely be appropriate;
   the October hold at 3.75–4% was 10–2 (Cook and Hammack dissenting,
   preferring a hike). Sources: TradingView/dpa-AFX (18 Nov 2026),
   trendandticker.com (18 Nov 2026), blockchainreporter.net.
6. **GTA VI Unlocks First in New Zealand** (Culture, games) — Grand
   Theft Auto VI unlocked first in New Zealand at 11:00 UTC on
   Wednesday, with early reviews arriving ahead of the wider
   midnight-local rollout; launch-eve network traffic surged (DE-CIX
   Frankfurt 22.15 Tbps on 18 Nov). Sources: gtaviunderground.com
   (18 Nov 2026), leonida-intel.com pre-load guide, Computer Weekly
   (19 Nov 2026, reporting 18 Nov traffic).

Also verified but left out for space/legibility: Mary Peltola wins
Alaska, giving Democrats a projected 56–44 Senate majority; Quad meets
in Manila at leader level for the first time in over two years; Board of
Peace warns the Gaza ceasefire could collapse; Cyclone Akvan triggers
large-scale evacuations in Odisha; COP31 climate talks enter their
decisive phase with 144 disputed items. The ICJ Myanmar/Rohingya
genocide ruling was 19 Nov, NOT 18 Nov, and was excluded. Nothing in
the image is invented — no made-up quotes, numbers, or casualty figures.

## Design
- Newspaper front page: masthead "THE WORLD IN ONE DAY", date line
  "Wednesday, 18 November 2026" in large bold type, lead story full
  width, 4 stories in a 2×2 grid, one full-width culture story, footer.
- Warm paper background (#fbf9f4), near-black ink, one accent colour
  per story's kicker. Icons are drawn shapes only (burst, flag circles,
  chip, euro coin, rising chart, skyline) — no photos, no external images.
- Smallest body text 22 px at full size, headlines 29–47 px, so the
  page stays readable scaled to ~300 px wide.

## Revision pass (v1 → v2)
- v1 rendered cleanly except the bottom GTA VI summary wrapped to two
  lines and its second line ("networks surge on launch eve.") overlapped
  the footer line.
- v2: bottom summary shortened to one line ("The game goes live region
  by region from midnight local time; early reviews arrive."); the
  launch-eve network surge detail is kept in this report instead.
  Re-rendered and visually inspected — no overlap, no cut-off text, no
  spelling errors.

## Verification
- `mkdir -p out out2 && MAKEFUN_OUTPUT_DIR=out node main.ts` and
  `MAKEFUN_OUTPUT_DIR=out2 node main.ts`:
  - out/entry.png sha256:
    `fafb85b4296595ab457ea3b304f0edce7164aa15a43d8ab283766779b1d7e054`
  - out2/entry.png sha256: identical
  - repo entry.png sha256: identical — **BYTE-IDENTICAL across runs**
  - Dimensions 1024×1024, mode RGB, 151,202 bytes ≤ 1,048,576
- Visual check (image read back): date line present and correct, all
  six headlines legible, no cut-off or overlapping text, no spelling
  errors.
- `main.ts` is stdlib-only (`node:fs`, `node:path`), does no network,
  reads only `./entry.png`.
