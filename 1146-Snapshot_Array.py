class SnapshotArray:

    """
    - array with linear search
    -   SnapshotArray(int length): O(n), O(n)
        set(int index, int val): O(1), O(1)
        snap(): O(1), O(1)
        get(int index, int snap_id): O(Set), O(1)
    """
    def __init__(self, length: int):
        self.history = [[[0, 0]] for _ in range(length)]
        self.snapshot_id = -1
        
    def set(self, index: int, val: int) -> None:
        current_snapshot_id = self.history[index][-1][1]
        if current_snapshot_id == self.snapshot_id + 1:
            self.history[index][-1] = [val, current_snapshot_id]
        else:
            self.history[index].append([val, self.snapshot_id + 1])

    def snap(self) -> int:
        self.snapshot_id += 1
        return self.snapshot_id

    def get(self, index: int, snap_id: int) -> int:
        i = 0
        history = self.history[index]                       
        while i < len(history) and history[i][1] <= snap_id:
            i += 1
        return history[i - 1][0]
    
    """
    - array with binary search - my solution
    -   SnapshotArray(int length): O(n), O(n)
        set(int index, int val): O(1), O(1)
        snap(): O(1), O(1)
        get(int index, int snap_id): O(log(Set)), O(1)
    """
class SnapshotArray:
    def __init__(self, length: int):
        self.history = [[[0, 0]] for _ in range(length)]
        self.snapshot_id = -1
        
    def set(self, index: int, val: int) -> None:
        current_snapshot_id = self.history[index][-1][1]
        if current_snapshot_id == self.snapshot_id + 1:
            self.history[index][-1] = [val, current_snapshot_id]
        else:
            self.history[index].append([val, self.snapshot_id + 1])

    def snap(self) -> int:
        self.snapshot_id += 1
        return self.snapshot_id

    def get(self, index: int, snap_id: int) -> int:
        history = self.history[index]  
        return self.binary_search(snap_id, history, 0, len(history) - 1)
    
    def binary_search(self, target, history, i, j):
        while i < j:
            mid = i + (j - i + 1) // 2
            snapshot_id = history[mid][1]
            if snapshot_id == target:
                return history[mid][0]
            elif snapshot_id > target:
                j = mid - 1
            else:
                i = mid
        return history[i][0]

    """
    - array with binary search - cleaner solution
    -   SnapshotArray(int length): O(n), O(n)
        set(int index, int val): O(1), O(1)
        snap(): O(1), O(1)
        get(int index, int snap_id): O(log(Set)), O(1)
    """
class SnapshotArray:
    def __init__(self, length: int):
        self.history = [[[-1, 0]] for _ in range(length)]
        self.snapshot_id = -1
        
    def set(self, index: int, val: int) -> None:
        self.history[index].append([self.snapshot_id + 1, val]) # update regardless

    def snap(self) -> int:
        self.snapshot_id += 1
        return self.snapshot_id

    def get(self, index: int, snap_id: int) -> int:
        history = self.history[index]  
        return self.binary_search(snap_id, history, 0, len(history) - 1)
    
    def binary_search(self, target, history, i, j):
        while i < j:
            mid = i + (j - i + 1) // 2
            snapshot_id = history[mid][0]
            if snapshot_id <= target:
                i = mid
            else:
                j = mid - 1
        return history[i][1]
    
"""
- array and binary search with bisect
- java can use Treemap
-   SnapshotArray(int length): O(n), O(n)
    set(int index, int val): O(1), O(1)
    snap(): O(1), O(1)
    get(int index, int snap_id): O(log(Set)), O(1)
"""
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = -1
        self.num_snaps = [[(-1, 0)] for _ in range(length)] # list of (snap_id, value)
        

    def set(self, index: int, val: int) -> None:
        prev_snap_id, prev_val = self.num_snaps[index][-1]
        if prev_snap_id == self.snap_id:
            self.num_snaps[index][-1] = (self.snap_id, val)
        else:
            self.num_snaps[index].append((self.snap_id, val))      

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id
        
    def get(self, index: int, snap_id: int) -> int:
        snaps = self.num_snaps[index] # snap_id, val
        idx = bisect.bisect_left(snaps, (snap_id, -1)) - 1 # have to make snap_id + 1 a list to be searchable with bisect
        return snaps[idx][1]
                
                                      
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)