
# Zen Quotes

**Zen Quotes** is a lightweight, fullscreen quote display application designed to run on a Raspberry Pi Zero W paired with a UCTRONICS touchscreen display.  The app presents calming, meditative, and spiritually inspired quotes at fixed intervals, creating a peaceful ambient display suitable for a home, meditation space, or bedside environment.

The project was originally created as a personal gift, with a focus on simplicity, readability, and a tranquil visual experience.

Quotes are sourced from a variety of spiritual and philosophical teachers, focusing on mindfulness, calm, presence, and inner peace.

---

## Features

- Fullscreen display (1024×600)
- Calming background image optimized for the UCTRONICS screen
- Quotes rotate automatically every 5 minutes
- Randomized selection from a curated quote list
- Designed for continuous, unattended operation
- Minimal resource usage — ideal for Raspberry Pi Zero W

---

## How It Works

The application is built with CustomTkinter and runs in fullscreen mode. On startup, it loads a background image and reads a list of quotes from a text file. Every five minutes, a new quote is randomly selected and displayed, allowing the screen to function as a quiet, ever-changing source of reflection without user interaction.

The application is configured to start automatically on boot using a custom systemd service, allowing the Raspberry Pi to function as a standalone, unattended display without manual intervention Below is a sample systemd configuration, edit as needed:

``` bash
[Unit]
Description=Zen Quotes Display
After=graphical.target

[Service]
Type=simple
User=pi
Environment=DISPLAY=:0
WorkingDirectory=/home/pi/zen_quotes
ExecStart=/usr/bin/python3 /home/pi/zen_quotes/zen_quotes.py
Restart=always
RestartSec=5

[Install]
WantedBy=graphical.target

```



---

## Hardware & Software

**Hardware**

- Raspberry Pi Zero W
- UCTRONICS 7" touchscreen (1024×600)


**Software**

- Python 3
- CustomTkinter
- Pillow (PIL)

---

## Use Case

This project is intended as a passive display rather than an interactive application. Once launched, it can run indefinitely, making it well-suited for personal spaces where a gentle, meditative atmosphere is desired 


---

## Screenshots

<p align="center"> <img src="https://i.imgur.com/p8FTowS.png" width="75%" alt="image1"/></p>

<p align="center"> <img src="https://i.imgur.com/4YHXOAS.png" width="75%" alt="image1"/></p>

<p align="center"> <img src="https://i.imgur.com/oNniiwS.png" width="75%" alt="image1"/></p>

<p align="center"> <img src="https://i.imgur.com/lcxyuET.png" width="75%" alt="image1"/></p>
