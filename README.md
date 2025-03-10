# TipToi-dl

[![Generate TipToi catalog](https://github.com/Bouni/tiptoi-dl/actions/workflows/catalog.yaml/badge.svg)](https://github.com/Bouni/tiptoi-dl/actions/workflows/catalog.yaml)

A linux CLI TipToi audiofile downloader.

## Motivation

[Ravensburger](https://www.ravensburger.de/), the manufacturer of the famous [TipToi](https://www.ravensburger.de/de-DE/entdecken/tiptoi) offers a Windows and a Mac Program for downloading new audiofiles.
As a Linux user you have to do that [manually via their website](https://service.ravensburger.de/tiptoi%C2%AE/tiptoi%C2%AE_Audiodateien) which is not the best experience.

So I decided to build this little CLI that allows me to download and copy the audiofile for a new book onto my kids TipToi within seconds.

## Setup

### With installation

1. Install with `pip install tiptoi-dl --break-system-packages`
2. Simply run `tiptoi-dl`

[!NOTE]
The `--break-system-packages` is necessary on most systems in order to allow installing packages at system level with pip at all.
If you prefer a `venv`, check out the next section on how to use `uv` and a `venv`.

### Without installation

1. Install uv if you have not already (see https://docs.astral.sh/uv/getting-started/installation/)
2. Sync the project: `uv sync --frozen`
3. Run the script: `uv run src/tiptoi-dl`

## Usage

You can enter any word thats in the title of a book, afterwards you get a list of possible matches.
The script guides you through the rest of the steps and will download the .gme file automatically if the TipToi pen is connected via USB and mounted.
Otherwise the .gme file is downloaded into your Downloads folder.

![](https://github.com/Bouni/tiptoi-dl/blob/d73cdd2e0c5f3f5bb59584a734ea6f9805bd51bb/demo.gif)

## Disclaimer

tiptoi-dl is neither offered nor supported by Ravensburger.
The authors do not take any liability for possible damages.
