        dt = datetime.fromisoformat(date.replace("Z", "+00:00")0
        unix_timestamp = int(dt.timestamp())
# TipToi-dl

[![Generate TipToi catalog](https://github.com/Bouni/tiptoi-dl/actions/workflows/catalog.yaml/badge.svg)](https://github.com/Bouni/tiptoi-dl/actions/workflows/catalog.yaml)

A linux CLI TipToi audiofile downloader.

## Motivation

[Ravensburger](https://www.ravensburger.de/), the manufacturer of the famous [TipToi](https://www.ravensburger.de/de-DE/entdecken/tiptoi) offers a Windows and a Mac Program for downloading new audiofiles.
As a Linux user you have to do that [manually via their website](https://service.ravensburger.de/tiptoi%C2%AE/tiptoi%C2%AE_Audiodateien) which is not the best experience.

So I decided to build this little CLI that allows me to download and copy the audiofile for a new book onto my kids TipToi within seconds.

## Setup

### With installation

1. Install uv if you have not already (see https://docs.astral.sh/uv/getting-started/installation/)
2. Run `uv tool install git+https://github.com/Bouni/tiptoi-dl.git`
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
