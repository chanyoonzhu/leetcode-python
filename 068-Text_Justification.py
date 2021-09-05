"""
- Array
- O(n)
"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        word_i = 0
        
        def getSpaceCounts(slots, total_spaces, is_last_line):
            if not is_last_line:
                if not slots: return [total_spaces] # easy to miss
                space_count, additional_count = divmod(total_spaces, slots)
                return [space_count + 1] * additional_count + [space_count] * (slots - additional_count)
            else:
                return [1] * (slots) + [total_spaces - slots]
        
        def printLine(words, space_counts):
            i = 0
            while i < len(space_counts):
                words.insert(i * 2 + 1, ' ' * space_counts[i])
                i += 1
            return ''.join(words)
        
        while word_i < len(words):
            letter_taken, line_words = 0, []
            while word_i < len(words) and letter_taken + len(words[word_i]) + len(line_words) <= maxWidth:
                letter_taken += len(words[word_i])
                line_words.append(words[word_i])
                word_i += 1
            spaceCounts = getSpaceCounts(len(line_words) - 1, maxWidth - letter_taken, word_i == len(words))
            output.append(printLine(line_words, spaceCounts))
        return output