class Codec:
    def __init__(self):
        self.codemap = {}  
    def encode(self, longUrl):
        code=str(hash(longUrl)%10000)
        self.codemap[code]=longUrl
        return ("http://tinyurl.com/"+code)

    def decode(self, shortUrl):
        code=shortUrl.replace("http://tinyurl.com/",'')
        return self.codemap[code]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))