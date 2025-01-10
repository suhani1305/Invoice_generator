from fpdf import FPDF
from datetime import datetime

class InvoiceGenerator(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Invoice', border=False, ln=True, align='C')
        self.ln(10)

    def add_company_details(self, company_name, company_address):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'{company_name}', ln=True)
        self.cell(0, 10, f'{company_address}', ln=True)
        self.ln(5)

    def add_client_details(self, client_name, client_address):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Client Details:', ln=True)
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Name: {client_name}', ln=True)
        self.cell(0, 10, f'Address: {client_address}', ln=True)
        self.ln(5)

    def add_invoice_details(self, invoice_number, invoice_date):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Invoice Details:', ln=True)
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Invoice Number: {invoice_number}', ln=True)
        self.cell(0, 10, f'Invoice Date: {invoice_date}', ln=True)
        self.ln(10)

    def add_invoice_table(self, items):
        self.set_font('Arial', 'B', 12)
        self.cell(60, 10, 'Item', 1)
        self.cell(40, 10, 'Quantity', 1)
        self.cell(40, 10, 'Price', 1)
        self.cell(40, 10, 'Total', 1)
        self.ln()

        self.set_font('Arial', '', 12)
        total_amount = 0
        for item_name, quantity, price in items:
            total = quantity * price
            total_amount += total
            self.cell(60, 10, item_name, 1)
            self.cell(40, 10, str(quantity), 1)
            self.cell(40, 10, f"${price:.2f}", 1)
            self.cell(40, 10, f"${total:.2f}", 1)
            self.ln()
        
        return total_amount

    def add_total_amount(self, total_amount):
        self.ln(5)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'Total Amount: ${total_amount:.2f}', ln=True, align='R')

company_name = "Tech Solutions Ltd."
company_address = "654 Tech Park, Silicon Valley, CA"
client_name = "Suhani Parmar"
client_address = "345 Elm Street, Springfield"
invoice_number = "INV-2025-001"
invoice_date = datetime.now().strftime("%Y-%m-%d")
items = [
    ("Laptop", 1, 1200.00),
    ("Monitor", 2, 300.00),
    ("Keyboard", 1, 50.00),
]

invoice = InvoiceGenerator()
invoice.add_page()

invoice.add_company_details(company_name, company_address)
invoice.add_client_details(client_name, client_address)
invoice.add_invoice_details(invoice_number, invoice_date)
total_amount = invoice.add_invoice_table(items)
invoice.add_total_amount(total_amount)

invoice.output("invoice.pdf")
print("Invoice generated and saved as 'invoice.pdf'.")
