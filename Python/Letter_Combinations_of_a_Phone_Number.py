# Problem: Letter Combinations of a Phone Number
# LeetCode URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Description: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# Medium level


class Solution:
    def get_chars(self, digit: str) -> List[str]:
        match digit:
            case 2:
                return ["a", "b", "c"]
            case 3:
                return ["d", "e", "f"]
            case 4:
                return ["g", "h", "i"]
            case 5:
                return ["j", "k", "l"]
            case 6:
                return ["m", "n", "o"]
            case 7:
                return ["p", "q", "r", "s"]
            case 8:
                return ["t", "u", "v"]
            case 9:
                return ["w", "x", "y", "z"]

    def letterCombinations(self, digits: str) -> List[str]:
        if digits =="":
            return []
        result = self.get_chars(int(digits[0]))
        for ch in digits[1:]:
            new_lst = []
            get_chars = self.get_chars(int(ch))
            for k in result:
                for m in get_chars:
                    new_lst.append(k+m)
            result = new_lst
        return result
