class Codec:
    
    """
    - O(1), O(n)
    - counter: simple, but prone to security issues - can view all pages by increasing the counter; same url encoded again the next time; length increase out of control
    def __init__(self):
        self.urls = []
        self.shortPrefix = "http://tinyurl.com/"

    def encode(self, longUrl):
        
        counter = len(self.urls)
        self.urls.append(longUrl)
        return self.shortPrefix + str(counter)
        

    def decode(self, shortUrl):
        
        counter = int(shortUrl[len(self.shortPrefix):])
        return self.urls[counter]
    """
    
    """
    - generate random six alphabets and store in hash map for fast retrieval and collsion checking
    
    import random
    
    def __init__(self):
        self.urls = {}
        self.shortPrefix = "http://tinyurl.com/"
        self.alphabetics = self.genAlphabetics()

    def encode(self, longUrl):
        
        short = self.genRandomStr(6)
        while short in self.urls:
            short = self.genRandomStr(6)
        self.urls[short] = longUrl
        return self.shortPrefix + short
        

    def decode(self, shortUrl):

        key = shortUrl[len(self.shortPrefix):]
        return self.urls[key]
    
    def genAlphabetics(self):  
        alphabetics = map(chr, range(ord('a'), ord('a') + 26))
        alphabetics += map(chr, range(ord('A'), ord('A') + 26))
        alphabetics += map(chr, range(ord('0'), ord('0') + 10))
        return alphabetics
    
    def genRandomStr(self, n):
        str = ""
        for i in range(n):
            index = random.randint(0,len(self.alphabetics)-1)
        str += self.alphabetics[index]
        return str
    """
    
    """
    - md5 hash
    def __init__(self):
        self.urls = {}
        self.shortPrefix = "http://tinyurl.com/"

    def encode(self, longUrl):
        import md5
        
        md = md5.new()
        md.update(longUrl)
        short = md.digest()
        self.urls[short] = longUrl
        return self.shortPrefix + short
        

    def decode(self, shortUrl):
        key = shortUrl[len(self.shortPrefix):]
        return self.urls[key]
    """
    
    def __init__(self):
        self.urls = {}
        self.shortPrefix = "http://tinyurl.com/"

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        import md5
        
        md = md5.new()
        md.update(longUrl)
        short = md.digest()
        self.urls[short] = longUrl
        return self.shortPrefix + short
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl[len(self.shortPrefix):]
        return self.urls[key]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))