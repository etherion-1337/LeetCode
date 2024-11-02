class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        word_list = sentence.split(" ")
        # handle from 2nd word to the last word
        for i in range(1, len(word_list)):
            if word_list[i][0] != word_list[i-1][-1]:
                return False
            if i < len(word_list)-1: # skip last word to avoid index out of range
                if word_list[i][-1] != word_list[i+1][0]:
                    return False
        # handle the last word here
        if word_list[0][0] != word_list[-1][-1]:
            return False
                
        return True
    
class Solution:
    """
    time complexity: O(n) where n is the total number of characters in the sentence
    space complexity: O(n) where n is the total number of characters in the sentence
    """
    def isCircularSentence(self, sentence: str) -> bool:
        # Use the split function to store the words in a list.
        words = sentence.split(" ")
        n = len(words)

        # Start comparing from the last character of the last word.
        last = words[n - 1][-1]

        for i in range(n):
            # If this character is not equal to the first character of current word, return false.
            if words[i][0] != last:
                return False
            last = words[i][-1]

        return True
    
class Solution:
    """
    time complexity: O(n) where n is the total number of characters in the sentence
    space complexity: O(1)
    """
    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i - 1] != sentence[i + 1]:
                return False
        return sentence[0] == sentence[len(sentence) - 1]