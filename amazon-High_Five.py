"""
There are two properties in the node student id and scores, 
to ensure that each student will have at least 5 points, 
find the average of 5 highest scores for each person.
"""

'''
Definition for a Record (for the exact problem online)

class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''

def highFive(ratings):
    
    import heapq

    dic, res = {}, {}
    LIMIT = 5

    for rating in ratings:
        if rating[0] not in dic:
            heap = []
            heapq.heappush(heap, rating[1])
            dic[rating[0]] = heap
        else:
            heap = dic[rating[0]]
            heapq.heappush(heap,rating[1])
        
    for item in dic:
        total = 0
        for _ in range(min(len(item[1]), LIMIT)):
            total += heapq.heappop(item[1])
        res[item[0]] = (total + 0.0) / LIMIT
    
    return res

scores = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
print(highFive(scores))       
        