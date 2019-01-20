"""
Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that has exactly k distinct characters.
Examples:

Input: abc, k = 2
Output: 2
Possible substrings are {"ab", "bc"}

Input: aba, k = 2
Output: 3
Possible substrings are {"ab", "ba", "aba"}

Input: aa, k = 1
Output: 3
Possible substrings are {"a", "a", "aa"}
"""
def countSubstringsWithKDistinctCharacters(s, k):

    total = 0

    for i in range(len(s)):
        distinct_count, dic = 0, {}
        for j in range(i, len(s)):
            if s[j] not in dic and distinct_count < k:
                dic[s[j]] = 1
                distinct_count += 1
                if distinct_count == k:
                    total += 1
            elif s[j] in dic and distinct_count == k:
                total += 1
            else:
                break
                    
    return total

    
text = "aa"
print(countSubstringsWithKDistinctCharacters(text, 1))
