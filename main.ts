// news-image-20261118 entry (Node 22, standard library only).
//
// The entry is the image file entry.png beside this program: a newspaper
// front page summing up Wednesday, 18 November 2026, drawn programmatically
// during the build (see build_image.py). This program only copies it to the
// output directory the grader provides — /output, or MAKEFUN_OUTPUT_DIR
// when run locally:
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
//
// No network, no other files read, no randomness: the same bytes go in,
// the same bytes come out, on every run. entry.png must sit beside this
// file; the grader runs it from the repository root.

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outputDir, { recursive: true });
const source = new URL('./entry.png', import.meta.url);
copyFileSync(source, join(outputDir, 'entry.png'));
