"""Extracting the data from TXT files."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Class to parse txt files and return a list of QuoteModel class."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse data from lines using split functions."""
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        file = open(path, "r")
        quotes = []

        for line in file.readlines():
            line = line.strip('\n\r').strip()
            line_length = len(line)
            if line_length > 0:
                parsed_line = line.split(' - ')
                new_quote = QuoteModel(parsed_line[0], parsed_line[1])
                quotes.append(new_quote)

        file.close()
        return quotes
