class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not (s and words):
            return []
        
        slen = len(s)
        strlen = len(words)
        wordlen = len(words[0])
        
        #count word frequencies in words
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        def is_concatenation(start_index):
            word_freq_copy = word_freq.copy()
            end_index = start_index + strlen * wordlen
            while start_index < end_index:
                if not s[start_index : start_index + wordlen] in word_freq_copy:
                    return False
                word_freq_copy[s[start_index : start_index + wordlen]] -= 1
                if word_freq_copy[s[start_index : start_index + wordlen]] == 0:
                    del word_freq_copy[s[start_index : start_index + wordlen]]
                start_index += wordlen
            return True
        
        return [i for i in range(slen - strlen * wordlen + 1) if is_concatenation(i)]
