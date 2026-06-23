<p align="center">
  <img src="https://raw.githubusercontent.com/Noxxi-hub/Noxxis-Discord-Musik-Bot/main/assets/nowplaying_bg.jpeg" alt="Playify Banner" width="900">
</p>

<h1 align="center">🎵 Noxxis Musik Bot</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Discord-Bot-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status">
</p>

<p align="center">
  <strong>Selbst-gehosteter Discord Musik-Bot für Noxxi's Cyber-Network. Keine Werbung, keine Limits — einfach Musik.</strong>
</p>

---

## 📋 Was ist das?

Ein Discord Musik-Bot basierend auf [Playify](https://github.com/alan7383/playify), angepasst und selbs-gehostet auf Noxxi's Server. Unterstützt YouTube, SoundCloud, Twitch, Spotify, Deezer und mehr.

---

## ⚙️ Tech Stack

| Komponente | Details |
|------------|---------|
| **Sprache** | Python 3.9+ |
| **Discord** | discord.py |
| **Audio** | FFmpeg 6.1.1+ |
| **Streaming** | yt-dlp |
| **Hosting** | Linux (systemd) |

---

## 🎧 Unterstützte Quellen

- YouTube & YouTube Music
- SoundCloud
- Twitch
- Spotify (Tracks, Playlists)
- Deezer
- Bandcamp
- Apple Music
- Tidal
- Amazon Music
- Direkte Audio-Links (MP3, FLAC, WAV)
- Lokale Dateien

---

## 💬 Befehle

| Befehl | Beschreibung |
|--------|-------------|
| `/play <url/suche>` | Song oder Playlist abspielen |
| `/search <suche>` | Suchen und aus Ergebnis wählen |
| `/play-files <datei(en)>` | Hochgeladene Audio-/Videodateien abspielen |
| `/playnext <suche/datei>` | Song an Queue-Anfang setzen |
| `/pause` / `/resume` | Pause / Fortsetzen |
| `/skip` | Aktuellen Song überspringen |
| `/stop` | Stoppen, Queue leeren, Disconnect |
| `/nowplaying` | Aktueller Song anzeigen |
| `/seek` | Interaktives Seek-Menü |
| `/queue` | Queue mit interaktiven Seiten |
| `/remove` | Song aus Queue entfernen |
| `/shuffle` | Queue mischen |
| `/clearqueue` | Gesamte Queue leeren |
| `/loop` | Loop für aktuellen Song umschalten |
| `/autoplay` | Autoplay umschalten |
| `/24_7 <modus>` | 24/7-Modus (`normal`, `auto`, `off`) |
| `/filter` | Audio-Filter (slowed, reverb, bass boost, nightcore, etc.) |
| `/lyrics` | Songtext anzeigen |
| `/karaoke` | Karaoke-Modus mit synchronisiertem Text |
| `/reconnect` | Voice-Verbindung erneuern |
| `/status` | Bot-Performance und Ressourcen |
| `/kaomoji` | Kawaii-Modus umschalten `(ADMIN)` |

---

## 📦 Installation

### Methode 1: Docker (empfohlen)

```bash
git clone https://github.com/Noxxi-hub/Noxxis-Discord-Musik-Bot.git
cd Noxxis-Discord-Musik-Bot
cp .env.example .env
```

`.env` mit deinen Tokens füllen:

```ini
DISCORD_TOKEN=dein_discord_bot_token
SPOTIFY_CLIENT_ID=dein_spotify_client_id
SPOTIFY_CLIENT_SECRET=dein_spotify_client_secret
GENIUS_TOKEN=dein_genius_api_token
```

Starten:

```bash
docker compose up -d --build
```

Logs: `docker compose logs -f`

### Methode 2: Manuell

**Voraussetzungen:**
- Python 3.9+
- FFmpeg 6.1.1+ im PATH
- Git

```bash
git clone https://github.com/Noxxi-hub/Noxxis-Discord-Musik-Bot.git
cd Noxxis-Discord-Musik-Bot
pip install -r requirements.txt
playwright install
cp .env.example .env
```

`.env` mit Tokens füllen, dann:

```bash
python playify.py
```

**Windows:** Einfach `start.bat` doppelklicken — installiert alles automatisch.

---

## 🔑 Umgebungsvariablen

| Variable | Erforderlich | Beschreibung |
|----------|-------------|--------------|
| `DISCORD_TOKEN` | ✅ | Bot-Token vom [Discord Developer Portal](https://discord.com/developers/applications) |
| `SPOTIFY_CLIENT_ID` | ❌ | Spotify Client ID |
| `SPOTIFY_CLIENT_SECRET` | ❌ | Spotify Client Secret |
| `GENIUS_TOKEN` | ❌ | Genius API Token (für Lyrics) |

---

## 🚀 Setup als systemd Service

```bash
sudo cp playify.service /etc/systemd/system/discord-music-bot.service
sudo systemctl daemon-reload
sudo systemctl enable discord-music-bot
sudo systemctl start discord-music-bot
```

---

## 🔧 Troubleshooting

- **FFmpeg nicht gefunden** — FFmpeg 6.1.1+ muss installiert und im PATH sein
- **Spotify Fehler** — `SPOTIFY_CLIENT_ID` und `SPOTIFY_CLIENT_SECRET` prüfen
- **Bot offline** — `DISCORD_TOKEN` und Bot-Bereigungen im Developer Portal prüfen
- **Link funktioniert nicht** — Muss ein direkter, öffentlicher Audio-Link sein

---

## 🔒 Datenschutz

- Komplett selbst-gehostet — alle Logs bleiben lokal
- Keine Telemetrie, kein Tracking

---

## 📄 Lizenz

MIT License — mach was du willst mit dem Code.

---

<p align="center">
  ❤️ Gehostet von <strong>Noxxi</strong> ✨🦋
</p>
