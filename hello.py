from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Set up the webdriver
driver = webdriver.Chrome(executable_path='path_to_your_chromedriver')  # Replace with your ChromeDriver path
driver.get('http://upmsp.edu.in/')

# Wait for the page to load (you may need to adjust the timing)
time.sleep(3)

# Locate the results link (adjust if the element's identifier changes)
result_link = driver.find_element(By.LINK_TEXT, "Results")  # Replace with the actual link text or element selector
result_link.click()

# Wait for the results page to load
time.sleep(3)

# Now, we will automate inputting roll numbers to fetch the results
roll_numbers = ['123456', '789101', '112233']  # List of roll numbers you want to search for
results = []

for roll_number in roll_numbers:
    # Find the input field for the roll number
    roll_input = driver.find_element(By.NAME, 'roll_number_field')  # Replace with actual field name
    roll_input.clear()
    roll_input.send_keys(roll_number)
    roll_input.send_keys(Keys.RETURN)  # Simulate pressing Enter

    # Wait for the results to load (you may need to adjust the timing)
    time.sleep(2)

    # Extract result data (adjust the element identifier to match the result)
    try:
        result = driver.find_element(By.XPATH, '//*[@id="result_xpath"]')  # Replace with actual XPath
        results.append({'Roll Number': roll_number, 'Result': result.text})
    except Exception as e:
        print(f"Failed to get result for roll number {roll_number}: {e}")

# Convert results into a DataFrame for easy export
df = pd.DataFrame(results)

# Save results to a CSV file
df.to_csv('student_results.csv', index=False)

# Close the browser
driver.quit()

print("Results saved successfully.")
