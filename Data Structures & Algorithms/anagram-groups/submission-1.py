class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        output = []
        for word in strs:
            base_key = [0] * 26
            for char in word: base_key[ord(char) - ord('a')] += 1
            base_key_tuple = tuple(base_key)
            if base_key_tuple in my_map.keys(): output[my_map[base_key_tuple]].append(word)
            else:
                output.append([word])     
                my_map[base_key_tuple] = len(output) - 1
            print(f"My current output {output}")
        return output
        