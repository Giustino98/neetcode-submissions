"""
h = 9
1 < k < 4 (max banana)
1 - |
2 - | | | |
3 - | | |
4 - | |

supponiamo k = 2 -> quante ore ci metto? in base a se < o > 9 decido come spostare k

for pile in piles -> len(pile) / k approssimato all'intero superiore
sommo tutti i len(pile) / k e ottengo h

se h < 9 -> provo a diminuire k perchè ho ancora spazio per ottimizzare
se h > 9 -> devo aumentare k
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            hours = 0
            k = (r+l) // 2

            for pile in piles:
                hours += (pile + k - 1) // k   #greater integer rounded
            if hours <= h:
                min_k = k
                r = k - 1
            elif hours > h:
                l = k + 1
        return min_k
        
            
