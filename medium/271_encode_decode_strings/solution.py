class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        if strs == [""]:
            return "<special_empty>"
        elif strs:
            return "<special_token>".join(strs)
        else:
            return []
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        if s == "<special_empty>":
            return [""]
        if s:
            return s.split("<special_token>")
        else:
            return []
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))