from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=16)
pdf.cell(200, 10, txt="Hello, FPDF is Working!", ln=True, align="C")

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="This is a test PDF generated with Python.", ln=True, align="C"
         
pdf.output("test.pdf")

print("PDF has been generated and saved as 'test.pdf'")
