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

        wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.ID, "WacFrame_Excel_0")
            )
        )

        print("switched to excel frame")
        print("step 1: looking for file")

        """print("Current URL:", self.driver.current_url)

        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        print(f"found {len(iframes)} iframes")

        for i, frame in enumerate(iframes):
            print(i, frame.get_attribute("id"), frame.get_attribute("name"))"""
        # File
        file_btn = wait.until(
            EC.element_to_be_clickable(
                #(By.XPATH, "//span[text()='File']")
                (By.XPATH, "//*[normalize-space()='File']")
            )
        )

        print("step 2: file found")

        file_btn.click()

        print("step 3: file clicked")

        time.sleep(2)

        print("Step 4: Looking for Create a Copy")

        create_copy = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[normalize-space()='Create a Copy']")
            )
        )

        # Scroll into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            create_copy
        )

        time.sleep(1)

        # JavaScript click
        self.driver.execute_script(
            "arguments[0].click();",
            create_copy
        )

        print("Create a Copy clicked")

        # Give the side panel time to open
        time.sleep(3)


        downloads = self.driver.find_elements(
            By.XPATH,
            "//*[contains(., 'Download a Copy')]"
        )

        print(f"Found {len(downloads)} Download a Copy elements")

        for i, d in enumerate(downloads):
            print(i, repr(d.text))


        # Create a Copy
        """create_copy = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[normalize-space()='Create a Copy')]")
            )
        )

        self.driver.excute_script("arguments[0].click();", create_copy)

        print("Create a copy clicked")"""

        """create_copy = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[@data-unique-id='FileMenuCreateCopySection']"
            ))
        )

        create_copy.click()"""

        time.sleep(2)

        # Download a Copy
        """wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Download a Copy')]")
            )
        ).click()"""

        print("Workbook download initiated...")

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