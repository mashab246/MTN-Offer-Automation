"""from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class Browser:

    def __init__(self):

        options = webdriver.EdgeOptions()

        options.add_argument("--start-maximized")

        self.driver = webdriver.Edge(
            service=Service(EdgeChromiumDriverManager().install()),
            options=options
        )

    def open(self, url):

        self.driver.get(url)

    def close(self):

        self.driver.quit()"""

import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class Browser:

    def _init_(self):

        # Downloads folder inside the project
        download_path = os.path.join(
            os.getcwd(),
            "downloads"
        )

        os.makedirs(download_path, exist_ok=True)

        options = webdriver.EdgeOptions()

        options.add_argument("--start-maximized")

        # Automatic downloads
        options.add_experimental_option(
            "prefs",
            {
                "download.default_directory": download_path,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            }
        )

        self.driver = webdriver.Edge(
            service=Service(
                EdgeChromiumDriverManager().install()
            ),
            options=options
        )

        self.download_path = download_path

    def open(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()