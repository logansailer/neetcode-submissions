class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for char in s:
            if (char == "(" or char == "{" or char == "["):
                arr.append(char)
            elif (char == ")"):
                if not arr: return False
                last = arr.pop()
                if (last != "("):
                    return False
            elif (char == "}"):
                if not arr: return False
                last = arr.pop()
                if (last != "{"):
                    return False
            elif (char == "]"):
                if not arr: return False
                last = arr.pop()
                if (last != "["):
                    return False
        return len(arr) == 0