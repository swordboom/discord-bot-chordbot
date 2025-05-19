# 🎵 ChordBot

**ChordBot** is a modular Discord bot built around slash commands. It delivers smooth music playback with per-server queues, voice channel controls, plus handy utilities like time, ping, and text echoing. Designed to keep your server interactive, fun, and clutter-free.

---

## 🧭 Table of Contents

* [✨ Features](#-features)
* [📁 Project Structure](#-project-structure)
* [⚙️ Prerequisites](#-prerequisites)
* [🚀 Setup & Installation](#-setup--installation)
* [🔐 Bot Token Configuration](#-bot-token-configuration)
* [🛠️ Running the Bot](#-running-the-bot)
* [🧾 Commands Overview](#-commands-overview)
* [🤝 Contributing](#-contributing)
* [📝 License](#-license)

---

## ✨ Features

* Fully **slash command based** (no prefix commands) for clean, modern Discord UX
* **Music playback** with per-guild (server) song queues and repeat toggling
* 🎤 Voice channel control: join, leave, play, pause, resume, skip
* 🛠️ Utility commands: current time/date, ping, copy text, speak in voice
* 📦 Modular codebase with separate cogs for easy maintenance and expansion
* 💬 Ephemeral command responses where appropriate, to reduce channel clutter

---

## 📁 Project Structure

```
chordbot/
│
├── bot.py                  # Entry point
├── config.json             # Contains the bot token (excluded from git)
├── requirements.txt        # Python dependencies
│
├── song-lib/               # All mp3 songs stored here
│
├── cogs/
│   ├── music.py            # Music-related commands
│   ├── misc.py             # Fun and utility commands (ping, hello, etc.)
│   ├── system.py           # Commands like close_bot, refresh
│   └── __init__.py
│
└── README.md               # You're reading it
```

---

## ⚙️ Prerequisites

* Python 3.10 or above
* `ffmpeg` installed and accessible via your system PATH (required for audio streaming)
* A Discord bot application with token and **application commands (slash commands)** enabled
* Basic knowledge of Python and Discord bots

---

## 🚀 Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/discord-modular-slash-bot.git
   cd discord-modular-slash-bot
   ```

2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install ffmpeg**

   * Windows: Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html), add to PATH
   * Linux: `sudo apt install ffmpeg` or your distro’s equivalent
   * macOS: `brew install ffmpeg` (if Homebrew installed)

---

## 🔐 Bot Token Configuration

Open the existing `config.json` file in the root directory and add your Discord bot token and application ID like this:

```json
{
  "token": "YOUR_DISCORD_BOT_TOKEN",
  "application_id": 123456789012345678
}
```

* Replace `"YOUR_DISCORD_BOT_TOKEN"` with your actual bot token.
* Replace `123456789012345678` with your bot's **Application ID** (found in the [Discord Developer Portal](https://discord.com/developers/applications)).

> 🔒 Never commit this file to public repositories.
> Make sure it's listed in your `.gitignore`:

```
config.json
```

---

## 🛠️ Running the Bot

Make sure you have Python 3.10+ installed.

Install required packages:

```bash
pip install -r requirements.txt
```

Then start the bot with:

```bash
python bot.py
```

* On startup, the bot will automatically sync all slash commands with Discord. This may take a few seconds.
* Ensure your bot has appropriate permissions in the Discord server, including:

  * Send Messages
  * Connect and Speak in Voice Channels
  * Use Application Commands (slash commands)

---

## 🧾 Commands Overview

| Command         | Description                                     |
| --------------- | ----------------------------------------------- |
| `/join`         | Join your current voice channel                 |
| `/play [song]`  | Play a song from the `song-lib/` directory      |
| `/skip`         | Skip the current track                          |
| `/pause`        | Pause the current track                         |
| `/resume`       | Resume the paused track                         |
| `/stop`         | Stop playback and clear the queue               |
| `/repeat`       | Toggle repeating the current track              |
| `/queue`        | Show the current queue                          |
| `/leave`        | Leave the voice channel                         |
| `/hello`        | Say hello to the bot                            |
| `/help`         | Display this command list                       |
| `/ping`         | Show the bot's latency                          |
| `/curtime`      | Display the current system time                 |
| `/curdate`      | Display the current system date                 |
| `/copy [text]`  | Bot repeats the provided text                   |
| `/refresh`      | Refresh internal states (stub for custom logic) |
| `/speak [text]` | Bot speaks your text in the voice channel       |
| `/close_bot`    | Gracefully shuts down the bot (admin only)      |

---

## 🎶 Song Library

All music files should be stored in the `song-lib/` folder.

* Format: `.mp3`
* Filenames should match the names used in `/play` without the extension.

Example:

```
song-lib/
  ├── lovely.mp3
  ├── thunderstruck.mp3
  └── chill-vibes.mp3
```

To play `lovely.mp3`, use:

```bash
/play lovely
```

---

## 🤝 Contributing

Pull requests and ideas are welcome! If you’d like to contribute:

1. Fork the repo
2. Create a new branch
3. Submit a PR with clear explanation

Please keep slash commands modular and follow the project structure.

---

## 📝 License

MIT License

Copyright (c) 2025 Soham Chakraborty

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 📬 Contact

* GitHub: [swordboom](https://github.com/swordboom)
* Email: [isitsohamc@gmail.com](mailto:isitsohamc@gmail.com)

---

Enjoy using **ChordBot**! 🎧
