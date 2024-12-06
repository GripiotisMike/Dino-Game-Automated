# Dino Game Automated

## Description
A Python-based automation script for the Chrome Dino game. The project utilizes Selenium for browser automation and PyAutoGUI for keyboard input. It also includes a utility to track the cursor's position, which can help determine screen coordinates for precise gameplay automation.

---

## Features
- **Cursor Position Tracker:** Displays the cursor's real-time coordinates to aid in setting up the game area.
- **Obstacle Detection:** Detects obstacles in the game using screen capture and image processing.
- **Automated Gameplay:** Automatically makes the dino jump to avoid obstacles.
- **Selenium WebDriver:** Opens and controls the Chrome Dino game.

---

## Installation

### Prerequisites
- Python 3.8+
- Google Chrome browser
- ChromeDriver (automatically managed by `webdriver-manager`)

### Dependencies
Install the required libraries:
- pyautogui
- PIL
- numpy
- selenium
- webdriver_manager

### Setup
1. Clone the repository

2. Run the cursor position tracker (optional)
   Use this to identify the region of the screen where obstacles appear.

3. Run the main script

---

## How It Works
1. **Cursor Position Tracker:**
   - Run `cursor.py` to display the cursor's coordinates in real-time.
   - Use these coordinates to adjust the obstacle detection box in the `detect_obstacle` function.

2. **Game Automation:**
   - The script uses Selenium to launch the Chrome Dino game in a browser.
   - PyAutoGUI is used to simulate spacebar presses, making the dino jump.
   - Obstacles are detected by analyzing a specific screen region for changes in pixel intensity.

---

## Customization
- **Obstacle Detection Box:** Adjust the `box` variable in the `detect_obstacle` function to match your screen resolution and game position.
- **Delay Timing:** Modify the `time.sleep` values for optimal performance.

---

## Limitations
- The script is designed for a specific screen setup. Ensure the Chrome Dino game is displayed in full screen.
- Performance may vary based on system speed and display resolution.
