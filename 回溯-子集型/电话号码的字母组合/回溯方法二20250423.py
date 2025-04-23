class Solution:
    def __init__(self):
        # self.letter_map=[
        #     '',
        #     '',
        #     'abc', 
        #     'def',
        #     'ghi',
        #     'jkl',
        #     'mno',
        #     'pqrs',
        #     'tuv',
        #     'wxyz'
        # ]
        self.letter_map={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        result=[]
        if len(digits)==0:
            return []
        self.traversal(result, digits, [], 0, self.letter_map)
        return result
    
    def traversal(self, result, digits, path, startIndex, letter_map):
        if len(path)==len(digits):
            result.append(''.join(path[:]))
            return 
        index=digits[startIndex]
        letters=letter_map[index]
        for letter in letters:
            path.append(letter)
            self.traversal(result, digits, path, startIndex+1, letter_map)
            path.pop()



        