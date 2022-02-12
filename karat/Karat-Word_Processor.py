"""
lines = [ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant flame" ]

reflowAndJustify(lines, 24) ... "reflow lines and justify to length 24" =>

        [ "The--day--began-as-still",
          "as--the--night--abruptly",
          "lighted--with--brilliant",
          "flame" ] // <--- a single word on a line is not padded with spaces

"""
class Solution:
    def reflowAndJustify(self, lines, max_len) -> list:
        res = []
        line = " ".join(lines)
        sentence = line.split()
        i = 0
        cur_remain_pos = max_len + 1
        cur_words = []
        while i < len(sentence):
            if len(sentence[i]) + 1 <= cur_remain_pos:
                cur_words.append(sentence[i])
                cur_remain_pos -= len(sentence[i]) + 1
                i += 1
            else:
                res.append(self.writeLine(cur_words, max_len))
                cur_words = []
                cur_remain_pos = max_len + 1
        if cur_words: # easy to forget
            res.append(self.writeLine(cur_words, max_len))
        return res
    
    def writeLine(self, words, max_len):
        screen = words[0]
        if len(words) > 1:
            delimiter_groups = len(words) - 1
            total_delimiter = max_len - sum([len(w) for w in words])
            avg, remain = divmod(total_delimiter, delimiter_groups)
            delimiters = [avg] * delimiter_groups
            delimiters[:remain] = [avg + 1] * remain
            for i in range(delimiter_groups):
                screen += ("-" * delimiters[i] + words[i+1])
        return screen

s = Solution()
print(s.reflowAndJustify([ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant flame"], 24))