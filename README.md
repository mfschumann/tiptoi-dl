[project0
name = "tiptoi-dl"
version = "0.1.0"
description = "A TipToi Download helper"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "beautifulsoup4>=4.14.2",
    "coloredlogs>=15.0.1",
    "psutil>=7.1.0",
    "requests>=2.32.5",
    "tqdm>=4.67.1",
]

[project.scripts]
tiptoi-dl = "tiptoidl:main"
# TipToi-dl

[![Generate TipToi catalog](https://github.com/Bouni/tiptoi-dl/actions/workflows/catalog.yaml/badge.svg)](https://github.com/Bouni/tiptoi-dl/actions/workflows/catalog.yaml)

A linux CLI TipToi audiofile downloader.

## Motivation

[Ravensburger](https://www.ravensburger.de/), the manufacturer of the famous [TipToi](https://www.ravensburger.de/de-DE/entdecken/tiptoi) offers a Windows and a Mac Program for downloading new audiofiles.
As a Linux user you have to do that [manually via their website](https://service.ravensburger.de/tiptoi%C2%AE/tiptoi%C2%AE_Audiodateien) which is not the best experience.

So I decided to build this little CLI that allows me to download and copy the audiofile for a new book onto my kids TipToi within seconds.

## Setup

1. Install uv if you have not already (see https://docs.astral.sh/uv/getting-started/installation/)
2. Run `uv tool install tiptoi-dl` (or `uv tool install git+https://github.com/Bouni/tiptoi-dl.git` for the main branch)
3. Run the script: `tiptoi-dl`

> [!NOTE]
> If the command is not found, the path is most likely not in your PATH. 
> run `uv tool update-shell` to fix that

## Usage

You can enter any word thats in the title of a book, afterwards you get a list of possible matches.
The script guides you through the rest of the steps and will download the .gme file automatically if the TipToi pen is connected via USB and mounted.
Otherwise the .gme file is downloaded into your Downloads folder.

![](https://github.com/Bouni/tiptoi-dl/blob/d73cdd2e0c5f3f5bb59584a734ea6f9805bd51bb/demo.gif)

## Disclaimer

tiptoi-dl is neither offered nor supported by Ravensburger.
The authors do not take any liability for possible damages.
