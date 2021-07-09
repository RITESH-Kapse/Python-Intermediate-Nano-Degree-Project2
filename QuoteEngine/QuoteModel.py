"""Base class with constructor and representation definition."""


class QuoteModel():
    """Class to get body and auther of message in files."""

    def __init__(self, body, author):
        """Create instances of variables."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Represent the class returning variables of constructor."""
        return f'<{self.body}, {self.author}>'
