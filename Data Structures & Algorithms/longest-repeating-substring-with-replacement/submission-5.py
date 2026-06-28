class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq_counter = defaultdict(int)
        max_length = 0

        for r in range(len(s)):
            freq_counter[s[r]] +=1 #incremento il counter
            most_freq_value = 0
            for value in freq_counter.values():  # trovo la freq max in sottostringa
                most_freq_value = max(most_freq_value,value)
            while (r-l+1) - most_freq_value > k:
                freq_counter[s[l]] -=1
                l +=1
            max_length = max(max_length,r-l+1)
        return max_length
