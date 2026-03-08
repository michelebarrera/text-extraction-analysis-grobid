import unittest
import xml.etree.ElementTree as ET
from io import StringIO


def remove_namespace(tree):
    """
    Eliminar namespace from XML tags 
    """
    for elem in tree.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]


def extract_text(xml_content):
    """
    Extract text from <p> tags in an XML document
    """
    tree = ET.parse(StringIO(xml_content))
    root = tree.getroot()

    # Eliminar TEI namespace used by GROBID
    remove_namespace(tree)
    paragraphs = root.findall(".//p")
    text = " ".join(p.text for p in paragraphs if p.text)
    return text


class TestExtraction(unittest.TestCase):

    def test_extract_simple_xml(self):
        xml_data = """
        <root>
            <p>Hello world</p>
            <p>This is a test</p>
        </root>
        """

        result = extract_text(xml_data)

        self.assertIn("Hello world", result)
        self.assertIn("This is a test", result)

    def test_extract_with_namespace(self):
        xml_data = """
        <TEI xmlns="http://www.tei-c.org/ns/1.0">
            <text>
                <body>
                    <p>Namespace text example</p>
                </body>
            </text>
        </TEI>
        """

        result = extract_text(xml_data)

        self.assertIn("Namespace text example", result)

    def test_returns_string(self):
        xml_data = "<root><p>Test text</p></root>"
        result = extract_text(xml_data)
        self.assertIsInstance(result, str)


if __name__ == "__main__":
    unittest.main()



