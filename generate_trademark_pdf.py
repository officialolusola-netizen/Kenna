from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

output_path = "/home/user/Kenna/Trademark_Acceptance_Letter_Class35.pdf"
doc = SimpleDocTemplate(output_path, pagesize=A4, topMargin=20*mm, bottomMargin=20*mm, leftMargin=15*mm, rightMargin=15*mm)

styles = getSampleStyleSheet()
title_style = ParagraphStyle("Title2", parent=styles["Title"], fontSize=18, spaceAfter=2)
subtitle_style = ParagraphStyle("Sub", parent=styles["Normal"], fontSize=12, alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=2)
red_title = ParagraphStyle("Red", parent=styles["Title"], fontSize=14, textColor=colors.darkred, spaceAfter=6)
section_style = ParagraphStyle("Section", parent=styles["Normal"], fontSize=12, fontName="Helvetica-Bold", spaceAfter=0)
cell_label = ParagraphStyle("CL", parent=styles["Normal"], fontSize=9, fontName="Helvetica-Bold")
cell_val = ParagraphStyle("CV", parent=styles["Normal"], fontSize=9)
red_notice = ParagraphStyle("Notice", parent=styles["Normal"], fontSize=10, fontName="Helvetica-Bold", textColor=colors.darkred, alignment=TA_CENTER)

elements = []

# Header
elements.append(Paragraph("FEDERAL REPUBLIC OF NIGERIA", title_style))
elements.append(Paragraph("FEDERAL MINISTRY OF INDUSTRY, TRADE AND INVESTMENT", subtitle_style))
elements.append(Paragraph("COMMERCIAL LAW DEPARTMENT", subtitle_style))
elements.append(Spacer(1, 6))
elements.append(Paragraph("TRADEMARK ACCEPTANCE LETTER", red_title))
elements.append(Spacer(1, 8))

full_width = A4[0] - 30*mm
half = full_width / 2

def make_cell(label, value):
    return [Paragraph(f"<b>{label}</b>", cell_label), Paragraph(value, cell_val)]

def section_row(text):
    t = Table([[Paragraph(text, section_style)]], colWidths=[full_width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.Color(0.9, 0.9, 0.9)),
        ("BOX", (0,0), (-1,-1), 0.5, colors.black),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 4),
    ]))
    return t

def two_col_row(l1, v1, l2, v2):
    data = [[make_cell(l1, v1), make_cell(l2, v2)]]
    # Flatten for table: each cell is a list of flowables
    t = Table(data, colWidths=[half, half])
    t.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 0.5, colors.black),
        ("INNERGRID", (0,0), (-1,-1), 0.5, colors.black),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING", (0,0), (-1,-1), 4),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    return t

def full_row(label, value):
    data = [[Paragraph(f"<b>{label}</b>", cell_label)], [Paragraph(value, cell_val)]]
    t = Table(data, colWidths=[full_width])
    t.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 0.5, colors.black),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING", (0,0), (-1,-1), 4),
    ]))
    return t

# FILE INFORMATION
elements.append(section_row("FILE INFORMATION"))
elements.append(two_col_row("Filing Date:", "08 February, 2026", "File Number:", "NG/TM/O/2026/416642"))
elements.append(two_col_row("Payment Date:", "08 February, 2026", "Payment ID:", "271428596699"))

# APPLICANT INFORMATION
elements.append(section_row("APPLICANT INFORMATION"))
elements.append(two_col_row("Applicant Name:", "Opemipo Zion Oluwanisola", "Email:", "opeifeoluwa242@gmail.com"))
elements.append(two_col_row("Phone Number:", "09029029899", "Nationality:", "Nigeria"))
elements.append(full_row("Applicant Address:", "K7A, Road 14 Victoria Garden City Lekki Lagos"))

# TRADEMARK INFORMATION
elements.append(section_row("TRADEMARK INFORMATION"))
elements.append(two_col_row("Product Title:", "DERMART", "Representation of Trademark:", "DERMMART"))
elements.append(two_col_row("Product class:", "35", "Claims/Disclaimer:", "NONE"))
elements.append(full_row(
    "Description of Goods:",
    "Advertising; business management, organization and administration; office functions; "
    "offering for sale and the sale of goods in the retail and wholesale trade; online retail "
    "store services; marketing and promotional services; import-export agency services; "
    "procurement services for others; commercial information and advice for consumers; "
    "business assistance, management and administrative services; business analysis, research "
    "and information services; provision of an online marketplace for buyers and sellers of "
    "goods and services"
))

# PROCESS INFORMATION
elements.append(section_row("PROCESS INFORMATION"))
elements.append(two_col_row("EXAMINATION DATE:", "09/02/2026", "EXAMINING OFFICER:", "Khasiyat A"))

elements.append(Spacer(1, 30))
elements.append(Paragraph(
    "THIS IS TO NOTIFY YOU THAT YOUR APPLICATION HAS BEEN<br/>"
    "ACCEPTED AND WILL IN DUE COURSE BE ADVERTISED<br/>"
    "IN THE TRADEMARKS JOURNAL",
    red_notice
))

doc.build(elements)
print(f"PDF created: {output_path}")
