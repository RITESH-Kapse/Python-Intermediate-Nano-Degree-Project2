"""Fetch data from QuoteEngine and print on console."""

from QuoteEngine import DocxImporter, CSVImporter, TextIngestor

# print(DocxImporter.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))

# print(CSVImporter.parse('./_data/DogQuotes/DogQuotesCSV.csv'))

from QuoteEngine import Ingestor, PDFImporter

print(DocxImporter.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
print(CSVImporter.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
print(TextIngestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))

# print(Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))

print(PDFImporter.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
