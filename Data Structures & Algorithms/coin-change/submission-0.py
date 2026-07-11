class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Inizializziamo l'array con un valore superiore a qualsiasi risultato possibile
        # (amount + 1 è perfetto perché al massimo useremmo tutte monete da 1)
        dp = [amount + 1] * (amount + 1)
        
        # Caso base
        dp[0] = 0
        
        # Ciclo esterno: calcoliamo i min-coins per ogni target intermedio
        for i in range(1, amount + 1):
            # Ciclo interno: proviamo OGNI moneta del nostro set
            for coin in coins:
                # Possiamo usare la moneta solo se non supera l'importo corrente
                if i - coin >= 0:
                    # La formula magica: prendo il minimo tra il valore attuale 
                    # e l'opzione di usare questa moneta (1 + il costo del resto)
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        # Se l'ultima cella è rimasta al valore iniziale (amount + 1), 
        # significa che non è stato possibile combinare le monete per raggiungere il target
        return dp[amount] if dp[amount] != amount + 1 else -1