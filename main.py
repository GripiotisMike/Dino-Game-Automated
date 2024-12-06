import time
import pyautogui
from PIL import ImageGrab, ImageOps
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    """Set up the Selenium WebDriver with Chrome options."""
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--start-fullscreen")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def press_key(key):
    """Simulate pressing a key using pyautogui."""
    pyautogui.press(key)


def detect_obstacle():
    """Detect obstacles in the game by analyzing a specific region of the screen."""
    # Define the bounding box coordinates for obstacle detection (adjust as needed)
    box = (790, 200, 825, 225)
    image = ImageGrab.grab(box)  # Capture the screen region
    gray_image = ImageOps.grayscale(image)  # Convert to grayscale for simplicity
    img_array = np.array(gray_image)  # Convert the image to a NumPy array
    region = img_array[:, :100]  # Focus on a specific region
    threshold = 200  # Define the pixel intensity threshold for detection
    if np.any(region < threshold):  # Check for dark pixels indicating an obstacle
        return True
    return False

# Initialize the Selenium WebDriver and open the Chrome Dino game
print("Setting up WebDriver...")
driver = setup_driver()
driver.get("https://chromedino.com")
time.sleep(2)

# Attempt to dismiss any consent pop-ups
try:
    consent_button = driver.find_element(By.XPATH, '//*[@id="t"]/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
    consent_button.click()
    print("Consent button clicked.")
except Exception as e:
    print("Consent button not found or not needed:", e)

time.sleep(2)

# Start the game
print("Starting the game...")
press_key("space")
time.sleep(2)

# Main loop for obstacle detection and jumping
print("Game automation running...")
try:
    while True:
        if detect_obstacle():
            press_key('space')  # Jump if an obstacle is detected
        time.sleep(0.002)  # Small delay to avoid excessive CPU usage
except KeyboardInterrupt:
    print("Automation stopped by user.")

# Quit the WebDriver session
print("Closing WebDriver...")
driver.quit()
