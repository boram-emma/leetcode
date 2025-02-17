class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # 인용 횟수를 내림차순 정렬
        h = 0
        
        for i, c in enumerate(citations):  # i는 논문 개수 (0부터 시작), c는 인용 횟수
            if c >= i + 1:
                h = i + 1  # 최대 h-index를 갱신
            else:
                break  # h-index 조건을 만족하지 않으면 종료
        
        return h



# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         check = []
#         for i in range(0,len(citations)):
#             if len([x for x in citations if x >= i+1]) >= i+1:
#                     check.append(i+1)

#         return max(check)
