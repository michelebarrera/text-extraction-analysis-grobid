def extract_links(folder_path):
    results = {}
    for file in os.listdir(folder_path):
        if file.endswith(".xml"):
            with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'lxml-xml')
                # Buscamos etiquetas ptr o ref que tengan un atributo target (la URL)
                links = [tag['target'] for tag in soup.find_all(['ptr', 'ref']) if tag.has_attr('target') and tag['target'].startswith('http')]
                results[file] = list(set(links)) # Usamos set para evitar duplicados
    return results

# Imprimir resultados
links_found = extract_links('./mis_xmls/')
for paper, links in links_found.items():
    print(f"\n--- {paper} ---")
    for l in links: print(l)
