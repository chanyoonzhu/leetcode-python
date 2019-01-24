import re;

def topKFrequent(s, banned, k):
  s = s.lower()
  words = re.compile(r'[a-z]+').findall(s)
  banned = [w.lower() for w in banned]
  bannedSet = set(banned)
  dic = {}
  for word in words:
    if word in bannedSet:
      continue 
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1 
  frequency = sorted(sorted(dic.items(), key = lambda x: x[0]), key = lambda x: x[1], reverse = True)
  res = [t[0] for t in frequency]
  if k > len(res):
      return res
  else:
      return res[:k]

s = "I love a leetcode's I love s s a coding"
print(topKFrequent(s, ["A"], 2))