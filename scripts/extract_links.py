import os
from lxml import etree

DATA_PATH = "../data"
OUTPUT_FILE = "../outputs/links_per_paper.txt"

NS = {"tei": "http://www.tei-c.org/ns/1.0"}

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:

    for file in os.listdir(DATA_PATH):
        if file.endswith(".tei.xml"):
            file_path = os.path.join(DATA_PATH, file)
            tree = etree.parse(file_path)

            refs = tree.findall(".//tei:ref", namespaces=NS)

            out.write(f"\n{file}\n")

            for ref in refs:
                link = ref.get("target")
                if link and link.startswith("http"):
                    out.write(link + "\n")

print("Links extraídos correctamente.")
