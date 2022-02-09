"""
- brute force with heap
- O(mn + mlogmn), O(mn)
- TLE
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        visited_worker, visited_bike = set(), set()
        res = [-1] * len(workers)
        heap = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                heap.append((self.manhanttan_dist(workers[i], bikes[j]), i, j))
        heapq.heapify(heap)
        while len(visited_worker) < len(workers):
            _, worker_i, bike_i = heapq.heappop(heap)
            if worker_i not in visited_worker and bike_i not in visited_bike:
                visited_worker.add(worker_i)
                visited_bike.add(bike_i)
                res[worker_i] = bike_i
        return res
        
        
    def manhanttan_dist(self, worker, bike):
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

"""
- greedy with heap
- intuition: instead of pushing all possible combinations to heap, only push shortest manhatten for each worker
- TLE
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        N, M = len(workers), len(bikes)
        workers_dists = [list() for _ in range(N)] # element at i is the list of tuple(dist, worker, bike) in sorted order
        
        visited_worker, visited_bike = set(), set()
        res = [-1] * len(workers)
        heap = []
        for i in range(N):
            for j in range(M):
                workers_dists[i].append((self.manhanttan_dist(workers[i], bikes[j]), i, j))
            workers_dists[i] = sorted(workers_dists[i])
        
        for i in range(N):
            heapq.heappush(heap, workers_dists[i].pop(0)) # heap only contains the shortest manhattan dist for each i
        
        while len(visited_worker) < len(workers):
            _, worker, bike = heapq.heappop(heap)
            if worker not in visited_worker and bike not in visited_bike:
                res[worker] = bike
                visited_worker.add(worker)
                visited_bike.add(bike)
            else: # if bike already used, push next in the list for worker to the heap
                heapq.heappush(heap, workers_dists[worker].pop(0))
        return res
