"""to inspect a specific page's contents"""

from parser.pdf_parser import extract_pages

pages = extract_pages("data/muj_handbook.pdf")

page = pages[23]   # page 24

print(page["text"])