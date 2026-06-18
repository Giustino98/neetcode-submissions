class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for elem in strs:
            new_str = new_str + str(len(elem)) + "#" + elem
        print(f"Encoded string {new_str}")
        return new_str

    def decode(self, s: str) -> List[str]:
        i = 0
        length = 0
        output_list = []
        while i < len(s) - 1:
            j = i
            while s[j + 1] != "#":
                j += 1
            length = int(s[i:j+1])
            if s[i] == 0:
                output_list.append("")
            output_list.append(s[j+2: j + 2 + length])
            i = j + 2 + length
            print(f"Decoded str {output_list} up to i = {i}")
        return output_list