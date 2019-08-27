class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        front = 0
        end = len(s) - 1
        sl = list(s)
        while front < end:
            while not sl[front] in vowels and front < end:
                front += 1
            while not sl[end] in vowels and end > front:
                end -= 1
            if front < end and sl[front] in vowels and sl[end] in vowels:
                sl[front], sl[end] = sl[end], sl[front]
                front += 1
                end -= 1
        return ''.join(sl)
