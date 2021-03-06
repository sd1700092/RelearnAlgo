from typing import List
def letterCombinations(digits: str) -> List[str]:
    m = {
        '2': list('abc'),
        '3': list('def'),
        '4': list('ghi'),
        '5': list('jkl'),
        '6': list('mno'),
        '7': list('pqrs'),
        '8': list('tuv'),
        '9': list('wxyz'),
    }
    if not digits: return []
    ls1 = ['']
    for i in digits:
        ls1 = [x + y for x in ls1 for y in m[i]]
    return ls1

if __name__ == '__main__':
    lst = letterCombinations("23")
    print(lst)