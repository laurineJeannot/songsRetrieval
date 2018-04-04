class Song:
    """
    Song data structure with
        - Int       id 
        - String    title 
        - String    artist 
        - list of most used words
        - list of lexical fields
    """

    def __init__(self, tid, mxm_tid):
        self.tid = tid
        self.mxm_tid = mxm_tid
        self.title = ""
        self.artist = ""
        self.words = []
        self.lexicalFields = []
        
    def  __str__(self):
        """
        write song data in a line
        """
        return self.tid+","+self.mxm_tid+","+self.title+","+self.artist+",w:"+self.wordlist()+",lf:"+self.lexicalFieldsList()

    def wordlist(self):
        string=""
        for i,w in enumerate(self.words):
            if i < len(self.words) - 1 :
                string += str(w) + ","
            else :
                string += str(w)                
        return string
            

    def lexicalFieldsList(self):
        string=""
        for i,lf in enumerate(self.lexicalFields):
            if i < len(self.lexicalFields) - 1 :
                string += str(lf) + ","
            else :
                string += str(lf)   
        return string
