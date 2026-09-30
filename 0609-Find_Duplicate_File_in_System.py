"""
- hashmap
- O(n*x), O(n*x) x: average string length
- follow up questions:
Imagine you are given a real file system, how will you search files? DFS or BFS?
DFS. In this case the directory path could be large. DFS can reuse the shared the parent directory before leaving that directory. But BFS cannot.

If the file content is very large (GB level), how will you modify your solution?
In this case, not realistic to match the whole string of the content. So we use file signitures to judge if two files are identical. Signitures can include file size, as well as sampled contents on the same positions. They could have different file names and time stamps though.
Hashmaps are necessary to store the previous scanned file info. S = O(|keys| + |list(directory)|). The key and the directory strings are the main space consumption.

a. Sample to obtain the sliced indices in the strings stored in the RAM only once and used for all the scanned files. Accessing the strings is on-the-fly. But transforming them to hashcode used to look up in hashmap and storing the keys and the directories in the hashmap can be time consuming. The directory string can be compressed to directory id. The keys are hard to compress.
b. Use fast hashing algorithm e.g. MD5 or use SHA256 (no collisions found yet). If no worry about the collision, meaning the hashcode is 1-1. Thus in the hashmap, the storage consumption on key string can be replaced by key_hashcode, space usage compressed.

If you can only read the file by 1kb each time, how will you modify your solution?
?

What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
T = O(|num_files||sample||directory_depth|) + O(|hashmap.keys()|)

How to make sure the duplicated files you find are not false positive?
Add a round of final check which checks the whole string of the content. T = O(|num_output_list||max_list_size||file_size|).
"""
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = collections.defaultdict(list)
        for path_files in paths:
            path_files = path_files.split()
            dir_ = path_files[0]
            for file_content in path_files[1:]:
                split_idx = file_content.index("(")
                file_name = file_content[:split_idx]
                content = file_content[split_idx+1:-1]
                content_to_paths[content].append(f"{dir_}/{file_name}")
                
        res = []
        for paths in content_to_paths.values():
            if len(paths) > 1:
                res.append(paths)
        return res