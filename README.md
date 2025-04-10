# Billboard-Retro-Top-100-to-Spotify
Billboard Retro Top 100 to Spotify is a Python-based tool that takes a Billboard Top 100 list from a given year and automatically builds a matching Spotify playlist. It's perfect for reliving music from your favorite decade — whether you're into 80s synths, 90s bangers, or early 2000s throwbacks.

# 🎶 Billboard Retro Top 100 to Spotify

Bring back the hits! This tool lets you convert the Billboard Top 100 songs from any retro year (e.g., 1984, 1995, 2003) into a ready-to-play Spotify playlist.

## 🧰 Features

- 🔄 Automatically fetches Billboard Top 100 songs by year
- 🔎 Searches and matches each track on Spotify
- 🎧 Creates or updates a Spotify playlist with the full list
- ✅ Handles duplicates and missing tracks gracefully

## 🚀 How It Works

1. Choose a year (e.g. `1984`)
2. The script scrapes Billboard's Top 100 for that year
3. It finds the closest matches on Spotify
4. Then it builds a playlist with those tracks in your Spotify account

## 📦 Requirements

- Python 3.7+
- Spotify Developer account & credentials (Client ID + Secret)
- BeautifulSoup / Requests / Spotipy

Install dependencies:

```bash
pip install spotipy requests beautifulsoup4
