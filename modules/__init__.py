from openpyxl import load_workbook

def _init_(self, file_path):
    self.workbook_path = file_path
    self.workbook = load_workbook(file_path)
    self.sheet = self.workbook["Interns"]