from fpdf import FPDF
import json

with open("Resume Details.json") as f:
   data = json.load(f)

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial", size = 15)
text = data

for line in text:
    pdf.cell(200, 10, txt = line, ln = 1, align = "L")
pdf.output("Resume Details.pdf")