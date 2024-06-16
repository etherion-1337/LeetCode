from typing import List

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
        
class Codec:
    """
    Don't use special tokens. Instead, use the length of the string to encode the string.
    O(n) time complexity, where n is the length of the input list of strings.
    """

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        if strs == [""]:
            return strs
        elif not strs:
            return []
        else:
            encoded_str = ""
            for s in strs:
                _s = str(len(s))+"#"+s
                encoded_str += _s
            return encoded_str
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        if s == []:
            return []
        if s == [""]:
            return [""]
        decoded_list = []
        while s:
            count = int(s.split("#")[0])
            first_hash_ind = s.index("#")
            decoded_list.append(s[first_hash_ind+1:first_hash_ind+1+count])
            s = s[first_hash_ind+1+count:]
        return decoded_list
    

class NeetSolution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))