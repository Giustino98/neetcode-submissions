class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = "".join([char.lower() if char.isalnum() else "" for char in s])

        l = 0
        r = len(stripped) - 1
        while l <= r:
            if stripped[l] == stripped[r]:
                l += 1
                r -= 1
            else: return False
        return True