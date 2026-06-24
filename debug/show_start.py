from parser.pdf_parser import extract_pages

pages = extract_pages("data/muj_handbook.pdf")

for page in pages[:20]:

    print("\n" + "="*80)
    print("PAGE", page["page"])

    for line in page["text"].split("\n"):

        line = line.strip()

        if line:
            print(line)