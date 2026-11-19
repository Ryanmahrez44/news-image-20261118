# Agent prompts — news-image-20261118

The opening prompt for this build, verbatim:

---

Kamu worker entri MakeFun PRIORITAS 1 (PALING URGENT) untuk Ryan (@ryanmahrez44).

KOMPETISI: news-image-20261118 — "Sum up 18 November's world news in one image", $250 (escrow YA), berakhir Jumat 20 Nov 2026 07:00 WIB — tinggal ~2,5 jam dari sekarang (04:25 WIB). GERAK CEPAT. Entri: program menulis SATU gambar berisi ringkasan berita dunia 18 Nov 2026; juri AI membandingkan gambar berpasangan; 50 tempat dibayar (juara 1 $50).

KERJAAN:
1. Work dir: ~/workspace/makefun-news-image-20261118/ dengan pola repo/ + kit/.
2. REUSE generator entri kemarin: copy ~/workspace/makefun-news-image/repo/build_image.py ke repo/ barumu, dan adaptasi isinya ke berita 18 Nov 2026. Copy juga main.ts (program Node 22 stdlib-only yang menyalin entry.png ke output dir), LICENSE, dan pola README dari ~/workspace/makefun-news-image/repo/. Kit CLI: copy ~/workspace/makefun-news-image/news-image-20261119-kit/ ke kit/ di work dir-mu (CLI di kit/cli/makefun.mjs).
3. Pilih 6 berita dunia 18 Nov 2026 yang TERVERIFIKASI — cek tiap berita via browser.search ke sumber berita live, catat sumbernya di BUILD_REPORT.md. JANGAN karang kutipan/angka/korban. Pilih yang berbobot dan beragam wilayah/bidang (seperti entri kemarin: Timur Tengah, diplomasi, teknologi, Eropa/perang, ekonomi, budaya/game). Catatan: GTA VI rilis 19 Nov (kemarin 18 Nov berarti pra-rilis), jadi jangan pakai cerita rilis GTA VI untuk 18 Nov kecuali memang beritanya 18 Nov.
4. Bangun gambar 1024x1024 dengan Python PIL seperti kemarin (programmatic, BUKAN AI-generated — teks harus tajam, tidak ada yang garbled). entry.png, batas 1 MiB. README.md WAJIB berisi 3 baris badge make.fun (salin persis dari README kemarin — baca dulu file itu).
5. Uji lokal: jalankan build_image.py, lalu jalankan main.ts dengan MAKEFUN_OUTPUT_DIR=out dan pastikan entry.png tersalin utuh.
6. Build bundle dengan kit CLI: `node kit/cli/makefun.mjs bundle --no-discover --no-family --session <ID SESI KAMU SENDIRI dari konteks subagent-mu> --parent-session 072effd1-73bc-4705-9f66-c93e9a4bc430` (cek sintaks persisnya dulu dengan `makefun.mjs --help` / `bundle --help`; output bundle ke ~/workspace/makefun-news-image-20261118/news-image-20261118-bundle.tar.gz). PENTING: --parent-session HANYA berisi session koordinator itu — jangan pernah pakai session main agent (terlalu besar, >64 MiB).
7. Jalankan `makefun check` pada bundle; perbaiki sampai LOLOS semua (thinking_reproduces ≥30%, entrypoint ≥1 authored line). Kalau thinking_priced gagal, tulis ~/.makefun/muse-usage-news-image-20261118.jsonl dari baris usage muse.db untuk sesimu (lihat /opt/muse/skills/muse_db/references/schema.md untuk skema), lalu jalankan check ulang. --redact TIDAK diterima pada strict submit — jangan pakai.

JANGAN SUBMIT: repo GitHub ryanmahrez44/news-image-20261118 belum ada dan harus dibuat via browser dulu (kamu tidak bisa pakai browser). Tugasmu berhenti di: gambar + repo + bundle + check LOLOS. Laporkan di pesan akhirmu: path gambar dan bundle (sebagai sandbox link lengkap), hasil check (angka-angkanya), daftar 6 berita + sumbernya, dan konfirmasi entri SIAP untuk repo-init + push + submit. Kalau ada yang gagal/blocked, katakan persis di mana.

Batas submit hari ini: maks 5/hari, 3 sudah terpakai — entri ini adalah #4 dan akan di-submit hari ini begitu repo ada. Kamu sendiri JANGAN submit apa pun.
