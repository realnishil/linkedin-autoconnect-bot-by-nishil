from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# 1. Setup the Browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def login_and_setup():
    print("Opening LinkedIn... Please log in manually.")
    driver.get("https://www.linkedin.com")
    
    # Wait for the page to load and user to click "Log In" if needed
    time.sleep(5) 
    print("Logged in. Navigating to Suggestions...")

def get_suggested_connections():
    # Navigate to My Network > Suggested Connections
    driver.get("https://www.linkedin.com/mynetwork/suggestions")
    
    wait = WebDriverWait(driver, 10)
    suggestions = []
    
    # Scroll down to load more suggestions (LinkedIn loads them dynamically)
    for _ in range(5): 
        time.sleep(random.uniform(2, 4))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Find all profile cards (CSS selector might change, this is a common one)
    profiles = driver.find_elements(By.CSS_SELECTOR, "div[class*='profile-card']")
    
    for profile in profiles:
        try:
            name = profile.find_element(By.CLASS_NAME, "text-primary").text # Adjust selector based on current UI
            print(f"Found suggestion: {name}")
            suggestions.append(profile)
        except Exception as e:
            continue
            
    return suggestions

def send_connection_request(profile):
    try:
        # Click the profile to open their page (sometimes needed before connecting)
        profile.click()
        time.sleep(2)
        
        # Find and click "Connect" button
        connect_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Connect')]"))
        )
        connect_btn.click()
        
        print("✅ Connection request sent!")
        time.sleep(random.uniform(3, 6)) # Random delay to avoid detection
        
    except Exception as e:
        print(f"⚠️ Error sending request: {e}")

def main():
    login_and_setup()
    suggestions = get_suggested_connections()
    
    if not suggestions:
        print("No suggestions found.")
        return

    for profile in suggestions:
        send_connection_request(profile)

if __name__ == "__main__":
    main()
