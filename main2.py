import time
from modules.browser import Browser
from modules.website import Website
from modules.excel_handler import ExcelHandler
from modules.bundle_mapping import OFFER_MAPPING, EXCEL_COLUMNS
from modules.sharepoint import SharePoint


DATA_URL = "https://www.mtn.co.ug/deal-types/daily-data-bundles/"
VOICE_URL = "https://www.mtn.co.ug/deal-types/daily-voice-bundles/"

downloaded_file = SharePoint.wait_for_download(Browser.download_Path)

excel = ExcelHandler(downloaded_file)

numbers = excel.get_phone_numbers()

print(f"Found {len(numbers)} phone numbers")


browser = Browser()

website = Website(browser.driver)


# Dictionary to hold all results
results = {}


print("\n==============================")
print("PROCESSING DATA BUNDLES")
print("==============================")

browser.open(DATA_URL)

website.accept_cookies()

time.sleep(2)

for row, phone in numbers:

    print(f"\nProcessing DATA for {phone}")

    website.enter_number(phone)

    website.click_proceed()

    time.sleep(3)

    data_offers = website.get_available_offers()

    print(data_offers)

    results[phone] = {

        "row": row,
        "data": data_offers,
        "voice": []

    }

    website.reset_page(DATA_URL)
    time.sleep(2)


print("\n==============================")
print("PROCESSING VOICE BUNDLES")
print("==============================")

browser.open(VOICE_URL)

website.accept_cookies()

time.sleep(2)

for row, phone in numbers:

    print(f"\nProcessing VOICE for {phone}")

    website.enter_number(phone)

    website.click_proceed()

    time.sleep(3)

    voice_offers = website.get_available_offers()

    print(voice_offers)

    results[phone]["voice"] = voice_offers

    website.reset_page(VOICE_URL)

    time.sleep(2)


print("\n==============================")
print("WRITING TO EXCEL")
print("==============================")

for phone, info in results.items():

    row = info["row"]

    all_offers = info["data"] + info["voice"]

    print(f"\nWriting offers for {phone}")

    """for offer in all_offers:

        if offer in OFFER_COLUMNS:

            excel.write_offer(
                row,
                OFFER_COLUMNS[offer],
                1
            )"""
    
    for offer in all_offers:

        if offer in OFFER_MAPPING:

            excel_name = OFFER_MAPPING[offer]

            column = EXCEL_COLUMNS[excel_name]

            excel.write_offer(row, column, 1)


# Save Excel
excel.save()

print("\nExcel Saved Successfully.")


# Close Browser
browser.close()

print("\nAutomation Finished Successfully!")