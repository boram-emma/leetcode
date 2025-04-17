class Solution:
    def isValid(self, s: str) -> bool:
        ch_dict = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        if s[0] in ch_dict.values():
            return False

        basket = []

        for sc in s:
            if sc in ch_dict.values():
                if ch_dict[basket[-1]] == sc:
                    basket.pop()
                else:
                    basket.append(sc)
            else:
                basket.append(sc)

        if len(basket) == 0:
            return True
        else:
            return False

