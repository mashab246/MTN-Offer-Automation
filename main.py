from modules.browser import Browser
from modules.website import Website
from modules.excel_handler import ExcelHandler
import time


URL = "https://www.mtn.co.ug/deal-types/daily-data-bundles/?gad_source=1&gad_campaignid=23923934047&gbraid=0AAAAADJWrbU4o3K4akuqjQxG_sQW3-Ze8&gclid=CjwKCAjw6f3RBhApEiwAMaCqWQKET5tvtad9tRocoQAllwypSaWsr59NmS7d5gpqlFePlvesO46nDxoCuCgQAvD_BwE"


OFFER_COLUMNS = {

    # DATA
    "1GB @1K": "E",
    "300MB @1K": "F",
    "165MB @1K": "G",

    # These all belong under the 400MB/1GB/5GB column
    "500MB @1K": "H",
    "1GB for 2days @1K": "H",
    "2.6GB for 3days @1K": "H",

    # VOICE
    "80@1000": "J",
    "70@1000": "K",
    "40Allnet@1000": "L",
    "25allnet@1000": "M",
    "40mins@1000": "N",
}


excel = ExcelHandler(
    r"C:\Users\23245518\Desktop\numbers.xlsx"
)


browser = Browser()

browser.open(URL)

website = Website(browser.driver)


website.accept_cookies()

time.sleep(1)


numbers = excel.get_phone_numbers()

print(f"Found {len(numbers)} phone numbers")


for row, phone in numbers:

    try:
        print(f"Processing {row-2}/{len(numbers)} : {phone}")

        website.enter_number(phone)

        website.click_proceed()

        time.sleep(2)

        offers = website.get_available_offers()

        print("Offers found:", offers)

        for offer in offers:

            if offer in OFFER_COLUMNS:

                excel.write_offer(
                    row,
                    OFFER_COLUMNS[offer],
                    1
                )

        excel.save()
        
        browser.driver.get(URL)

        time.sleep(2)

        website.accept_cookies()

        time.sleep(2)

    except Exception as e:
        print(f"Failed for {phone}: {e}")
        
browser.close()

print("Finished Successfully!")

