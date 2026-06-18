class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for word in strs:
            appended = False
            for group in output:
                if Counter(word) == Counter(group[0]): 
                    group.append(word)
                    appended = True
                    print(f"Appended word {word} in group {group}")
                    break
                    
            if appended == False: output.append([word])
            print(f"Output attuale: {output} \n")
        return output
        