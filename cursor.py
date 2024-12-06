import pyautogui
import time

# Continuously display the current cursor position in real-time
try:
    while True:
        x, y = pyautogui.position()  # Get the current position of the mouse cursor
        print(f"Cursor position: ({x}, {y})")  # Print the coordinates
        time.sleep(0.1)  # Delay to avoid excessive CPU usage, adjustable as needed
except KeyboardInterrupt:
    print("\nProgram exited.")  # Exit on keyboard interrupt
