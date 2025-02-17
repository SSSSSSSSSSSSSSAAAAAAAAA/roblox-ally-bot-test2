from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuration
ROBLOX_LOGIN_URL = "https://www.roblox.com/login"
GROUP_URL = "https://www.roblox.com/communities/34946748/7-S-I-N-S#!/about"  # Your group URL
ROBLOX_USERNAME = "proallybot"  # Your Roblox username
ROBLOX_PASSWORD = "223344448"  # Your Roblox password

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Log in to Roblox
def login(username, password):
    driver.get(ROBLOX_LOGIN_URL)
    time.sleep(2)

    # Enter username and password
    driver.find_element(By.ID, "login-username").send_keys(username)
    driver.find_element(By.ID, "login-password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    time.sleep(5)  # Wait for login to complete

# Send ally request to a group
def send_ally_request(group_id):
    driver.get(f"https://www.roblox.com/groups/{group_id}")
    time.sleep(3)

    try:
        # Click the "More" button
        more_button = driver.find_element(By.CSS_SELECTOR, ".btn-more")
        more_button.click()
        time.sleep(1)

        # Click the "Ally" option
        ally_button = driver.find_element(By.CSS_SELECTOR, ".dropdown-menu .rbx-menu-item[data-group-ally]")
        ally_button.click()
        time.sleep(1)

        # Confirm the ally request
        confirm_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer .btn-primary")
        confirm_button.click()
        time.sleep(2)

        print(f"Ally request sent to group {group_id}")
    except Exception as e:
        print(f"Failed to send ally request to group {group_id}: {e}")

# Main script
if __name__ == "__main__":
    # Log in to Roblox
    login(ROBLOX_USERNAME, ROBLOX_PASSWORD)

    # Send ally requests to group IDs from 1 to 100000
    for group_id in range(1, 100001):  # Looping from 1 to 100,000
        send_ally_request(group_id)

    # Close the browser
    driver.quit()
