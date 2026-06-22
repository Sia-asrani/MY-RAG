from parser.pdf_parser import extract_pages
from parser.hierarchy_detector import get_heading

pages = extract_pages("data/muj_handbook.pdf")

for page in pages[14:18]:

    print("\nPAGE", page["page"])

    for line in page["text"].split("\n"):

        result = get_heading(line)

        if result:

            print(result)