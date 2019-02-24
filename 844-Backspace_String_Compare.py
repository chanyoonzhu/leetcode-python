class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        """
        - O(m+n), O(m+n)
        - build string

        s1 = t1 = ""
        
        for c in S:
            if c == '#':
                if s1: # df: dont and this with c=='#'
                    s1 = s1[:-1]
            else:
                s1 += c
        
        for c in T:
            if c == '#':
                if t1:
                    t1 = t1[:-1]
            else:
                t1 += c
        
        return s1 == t1
        """
        
        

        """
        - O(m+n), O(1)
        - two pointers, reverse string - smart idea!
        """
        
        sp, tp = len(S) - 1, len(T) - 1
        sskip = tskip = 0
        
        while sp >= 0 or tp >= 0:
            # sp stops at first non-deleted character in S or -1
            while sp >= 0:
                if S[sp] == '#':
                    sskip += 1
                    sp -= 1
                elif sskip:
                    sskip -= 1
                    sp -= 1
                else:
                    break
            # tp stops at first non-deleted character in T or -1        
            while tp >= 0:
                if T[tp] == '#':
                    tskip += 1
                    tp -= 1
                elif tskip:
                    tskip -= 1
                    tp -= 1
                else:
                    break
            
            if sp < 0 and tp >= 0 or tp < 0 and sp >= 0 or S[sp] != T[tp]:
                return False

            sp -= 1
            tp -= 1
        
        return True


print(Solution().backspaceCompare("ab#c",
"ad#c"))