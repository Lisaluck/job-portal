import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "https://www.ibps.in/career-in-ibps/"
driver.get(URL)

time.sleep(3)   # Wait for JS to load

job_elements = driver.find_elements(By.CSS_SELECTOR, "div.page-content li a")

job_data = []

for job in job_elements:
    title = job.text.strip()
    link = job.get_attribute("href")

    publish_date = "N/A"
    for part in title.split():
        if "-" in part and part.replace("-", "").isdigit():
            publish_date = part
            break

    job_data.append({
        "Job Title": title,
        "Location": "India",
        "Publish Date": publish_date,
        "Job Link": link
    })

driver.quit()

df = pd.DataFrame(job_data)
df.to_csv("ibps_jobs.csv", index=False, encoding="utf-8")

print("✅ Scraping Completed Successfully!")
print(df)
