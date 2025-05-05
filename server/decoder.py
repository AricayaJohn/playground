import requests
from collections import defaultdict
from html.parser import HTMLParser

class TableHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False       
        self.in_tr = False          
        self.in_td = False          
        self.current_row = []     
        self.table_data = []       

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == 'table':
            self.in_table = True
        if self.in_table and tag == 'tr':
            self.in_tr = True
            self.current_row = []
        if self.in_tr and tag == 'td':
            self.in_td = True

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == 'table':
            self.in_table = False
        if tag == 'tr' and self.in_tr:
            self.table_data.append(self.current_row)
            self.in_tr = False
        if tag == 'td' and self.in_td:
            self.in_td = False

    def handle_data(self, data):
        if self.in_td:
            self.current_row.append(data.strip())

def decode_secret_message(doc_url):
    try:
        response = requests.get(doc_url)
        response.raise_for_status()
        html_text = response.text

        parser = TableHTMLParser()
        parser.feed(html_text)
        table = parser.table_data

        if not table:
            print("No table found in the document")
            return

        header = table[0] if len(table[0]) > 0 else []
        if header and header[0].lower().startswith('x'):
            rows = table[1:]
        else:
            rows = table

        raw_data = []
        for row in rows:
            if len(row) >= 3:
                raw_data.append("\t".join(row[:3]))

        grid_data = defaultdict(dict)
        max_x = 0
        max_y = 0

        for line in raw_data:
            parts = line.split('\t')
            if len(parts) >= 3:
                try:
                    x = int(parts[0].strip())
                    char = parts[1].strip()
                    y = int(parts[2].strip())
                    grid_data[y][x] = char
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)
                except (ValueError, IndexError):
                    continue

        for y in range(max_y + 1):
            row_output = []
            for x in range(max_x + 1):
                row_output.append(grid_data.get(y, {}).get(x, ' '))
            print(''.join(row_output))

    except requests.RequestException as e:
        print(f"Error fetching document: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

DOC_URL = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
decode_secret_message(DOC_URL)
