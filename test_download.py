from modules.browser import Browser
from modules.sharepoint import SharePoint

URL = "https://airtelaf-my.sharepoint.com/:x:/g/personal/13400403_airtel_africa/IQAnROVW_apXSJ2A0axNmhZiAcmSDh1qT8AUatkIzirW66Y?e=eJOza1&isSPOFile=1&ovuser=16c73727-979c-4d82-b3a7-eb6a2fddfe57%2C23245518%40airtel.africa&wdExp=TEAMS-TREATMENT&web=1&TeamsCID=2c21f2f2-9c46-49d3-b7a8-f0af79d561a1&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI0OS8yNjA1MjkwNjEyMSJ9&linkOpenTime=1782796862307"
browser = Browser()

sharepoint = SharePoint(browser.driver)

sharepoint.open_workbook(URL)

input("Login if necessary, then press Enter...")

sharepoint.download_copy()

path = sharepoint.wait_for_download(browser.download_path)

print(path)

input("Done")

