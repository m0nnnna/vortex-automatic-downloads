import pyautogui
import time

# Use snipping tool to get the buttons and put them in the script folder
download_button = 'button1_image.png'
slow_download_button = 'button2_image.png'
browser_close_button = 'button3_image.png'

def click_button(image_path):
    try:
        # Find the button on the screen. Confidence 0.8 sometimes clicks other stuff, 0.99 sometimes misses button
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.95)
        # If the button is found, click it
        if button_location is not None:
            time.sleep(1)
            pyautogui.click(button_location)
            print(f"Clicked on {image_path}")
            return True
    except pyautogui.ImageNotFoundException:
        # If the button is not found, print a message. Uncomment for debug.
        # print(f"Button from {image_path} not found on the screen.")
        pass
    return False

num_of_browser_windows = 0

try:
    while True:
        if click_button(download_button):
            time.sleep(2) # Optionally give some time for browser to load
            continue
        if click_button(slow_download_button):
            num_of_browser_windows += 1
            time.sleep(6) # Slow download delay
            # This is to prevent opening too many browser windows
            if num_of_browser_windows > 10:
                if click_button(browser_close_button):
                    num_of_browser_windows = 0
                    time.sleep(1)

        # If no buttons were clicked, wait before checking again. Uncomment for debug.
        # print("No buttons were clicked. Waiting before rechecking.")
        time.sleep(1)

except KeyboardInterrupt:
    print('\nExited the program.')
