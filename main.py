import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up headless browser
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-sandbox")

service = Service("/path/to/chromedriver")  # Update this path
driver = webdriver.Chrome(service=service, options=chrome_options)

# Casinos to target
casinos = [
    "https://fafaau.com/FAFA11311129",
    "https://spinfred.com/RF280600937",
    "https://spinsx.net/RF272A71117"
]

# Login function (Replace with actual casino login handling)
def login(casino_url):
    driver.get(casino_url)
    time.sleep(5)  # Allow time for page load
    print(f"Logged into {casino_url}")

# Spin function with bet cycling
def spin_and_monitor():
    for casino in casinos:
        login(casino)
        for _ in range(10):  # Number of spins per session
            try:
                spin_button = driver.find_element(By.CLASS_NAME, "spin-button")
                spin_button.click()
                print(f"Spinning at {casino}...")
                time.sleep(random.uniform(2, 5))  # Random delay between spins
            except Exception as e:
                print(f"Error spinning: {e}")

# Main bot loop
try:
    spin_and_monitor()
except KeyboardInterrupt:
    print("Bot stopped by user.")
finally:
    driver.quit()
