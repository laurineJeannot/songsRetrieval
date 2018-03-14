class Song:
    """
    Song data structure with
        - Int       id 
        - String    title 
        - String    artist 
        - list of most used words
        - list of lexical fields
    """

    def __init__(self, id):
        self.id = id
        self.title = ""
        self.artist = ""
        self.words = []
        self.lexicalFields = []
        
    def toString(self):
        """
        write song data in a line
        """