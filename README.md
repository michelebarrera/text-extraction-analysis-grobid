# Text Extraction and Analysis with Grobid

## Project Description
This project performs text extraction and analysis on 10 open-access scientific articles using Grobid.

## Dataset
Description of selected papers (source, topic, why chosen).

## Methodology
1. PDF extraction using Grobid
2. Parsing TEI XML output
3. Keyword extraction from abstracts
4. Figure counting
5. Link extraction

## Results
- Keyword cloud
- Figures per article visualization
- List of links per paper

## Validation

### Keyword cloud
We manually checked that the most frequent words correspond to domain-specific terminology.

### Figures per article
We manually opened 2–3 PDFs and counted figures visually to compare with XML results.

### Links extraction
We verified extracted URLs against the PDF text using Ctrl+F.
