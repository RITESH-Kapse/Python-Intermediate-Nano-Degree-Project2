"""Extracting the data from PDF files."""

from typing import List
import subprocess
import os
import random

from PIL.ImageFont import LAYOUT_BASIC

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFImporter(IngestorInterface):
    """Work with pdf files and split the input data seperated."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse data from pdf using pdftotext subprocess."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        # tmp = f'./tmp/{random.randint(0, 1000)}.txt'
        tmp = f'./tmp_{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', '-layout', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                print(line)
                parsed = line.split(' - ')
                print(parsed)
                new_quote = QuoteModel(parsed[0],
                                       parsed[1]
                                       )
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
