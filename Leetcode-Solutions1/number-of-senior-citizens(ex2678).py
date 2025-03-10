class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for detail in details:
            piece = detail[11:13]
            if int(piece) > 60:
                counter += 1
        return counter