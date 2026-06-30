import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SharePoint:

    def __init__(self, driver):
        self.driver = driver

    def open_workbook(self, url):
        self.driver.get(url)

    def download_copy(self):

        wait = WebDriverWait(self.driver, 30)

        # File
        wait.until(
            EC.element_to_be_clickable(
                #(By.XPATH, "//span[text()='File']")
                (By.XPATH, "//*[normalize-space()='File']")
            )
        ).click()

        time.sleep(2)

        # Create a Copy
        """wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Create a Copy')]")
            )
        ).click()"""

        create_copy = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[@data-unique-id='FileMenuCreateCopySection']"
            ))
        )

        create_copy.click()

        time.sleep(2)

        # Download a Copy
        """wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Download a Copy')]")
            )
        ).click()"""

        download_copy = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//span[normalize-space()='Download a Copy']"
            ))
        )

        download_copy.click()

        print("Downloading workbook...")

    def wait_for_download(self, folder):

        while True:

            files = os.listdir(folder)

            downloading = [
                f for f in files
                if f.endswith(".crdownload")
                or f.endswith(".tmp")
            ]

            if downloading:
                time.sleep(1)
                continue

            excel = [
                f for f in files
                if f.endswith(".xlsx")
            ]

            if excel:
                latest = max(
                    [os.path.join(folder, f) for f in excel],
                    key=os.path.getmtime
                )

                print("Downloaded:", latest)

                return latest