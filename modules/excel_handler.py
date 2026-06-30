from openpyxl import load_workbook


class ExcelHandler:

    def __init__(self, file_path):
        self.file_path = file_path

        self.workbook = load_workbook(file_path)
        self.sheet = self.workbook["Interns"]

    def get_phone_numbers(self):

        numbers = []

        for row in range(3, self.sheet.max_row + 1):

            phone = self.sheet[f"C{row}"].value

            if phone:
                numbers.append((row, str(phone)))

        return numbers

    def write_offer(self, row, column, value):

        self.sheet[f"{column}{row}"] = value

    def save(self):

        self.workbook.save(self.file_path)