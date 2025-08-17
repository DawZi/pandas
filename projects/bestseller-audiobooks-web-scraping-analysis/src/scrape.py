from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

website = "https://www.audible.com/charts/best?srsltid=AfmBOopwLQt-A_jONbLpXdKmFck4iC2bliAfFzFaVj2Q7PR7T4RP0Tn1"
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(website)


titles, authors, runtimes, languages, rating = [], [], [], [], []

i = 2
while i != 6:
    next_page = driver.find_element(
        By.XPATH, f"//a[contains(@class, 'pageNumberElement') and text()='{i}']"
    )
    titles = titles + [
        t.text
        for t in driver.find_elements(
            By.XPATH, "//*/div/div[1]/div/div[2]/div/div/span/ul/li[1]/h3/a"
        )
    ]
    authors = authors + [
        a.text
        for a in driver.find_elements(
            By.XPATH,
            "//li[contains(@class, 'authorLabel')]//a[contains(@href, '/author/')]",
        )
    ]
    runtimes = runtimes + [
        r.text
        for r in driver.find_elements(
            By.XPATH, "//li[contains(@class, 'runtimeLabel')]"
        )
    ]
    languages = languages + [
        l.text
        for l in driver.find_elements(
            By.XPATH, "//li[contains(@class, 'languageLabel')]"
        )
    ]
    rating = rating + [
        rt.text
        for rt in driver.find_elements(
            By.XPATH,
            "//li[contains(@class, 'ratingsLabel')]//span[contains(text(), 'stars')]",
        )
    ]

    next_page.click()
    i += 1


d = {
    "title": titles,
    "author": authors,
    "runtime": runtimes,
    "language": languages,
    "rating": rating,
}

df = pd.DataFrame(data=d)
df
df.to_csv("../data/scraped/bastsellers_scrape.csv", index=False)

driver.quit()
