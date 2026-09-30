class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        out = []
        multi = 0
        
        outline = ''
        for line in source:
            idx = 0
            while idx < len(line):
                if not multi:
                    if line[idx:idx+2] == '//':
                        break
                    elif line[idx:idx+2] == '/*':
                        multi = 1
                        idx += 2
                    else:
                        outline += line[idx]
                        idx += 1
                else:
                    if line[idx:idx+2] == '*/':
                        multi = 0
                        idx += 2
                    else:
                        idx += 1
                        
            if not multi and outline:
                out.append(outline)
                outline = ''
                
        return out

s = Solution()
source = ["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]
s.removeComments(source)