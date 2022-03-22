"""
non-ASCII delimiter
- O(n), O(1)
"""
class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return None # easy to miss: distinguish from [""] -> ""
        
        return chr(9999).join(s for s in strs)
        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if s == None:
            return []
        if not s:
            return [""]
        return  s.split(chr(9999))


"""
- Chunked transfer encoding (length + string)
- O(n), O(1)
"""
class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return ""
        encoded = []
        for s in strs:
            length = self.getLengthInThreeBytes(len(s))
            encoded.append(length)
            encoded.append(s)
            
        return "".join(encoded)
    
    def getLengthInThreeBytes(self, n):
        res = str(n)
        if len(res) < 3:
            res = "0" * (3 - len(res)) + res
        return res
        res = []

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if s == "":
            return []
        decoded = []
        idx = 0
        while idx < len(s):
            length = int(s[idx:idx+3])
            idx += 3
            decoded.append(s[idx:idx+length])
            idx += length
        return decoded
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))