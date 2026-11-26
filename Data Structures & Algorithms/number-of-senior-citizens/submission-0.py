class Solution:
    def countSeniors(self, details: List[str]) -> int:
        over_60_count = 0

        for detail in details:
            if int(detail[11:13]) > 60:
                over_60_count += 1
        
        return over_60_count