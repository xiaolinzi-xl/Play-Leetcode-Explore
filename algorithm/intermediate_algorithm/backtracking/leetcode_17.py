class Solution:
    digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    ans = []

    def search(self, digit, idx, string):
        if idx >= len(digit):
            self.ans.append(string)
            return
        for ele in self.digit_map[digit[idx]]:
            self.search(digit, idx + 1, string + ele)

    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        self.ans.clear()
        self.search(digits, 0, '')
        return self.ans
