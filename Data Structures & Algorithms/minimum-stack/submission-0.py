'''
Io erroneamente ragionavo sul push: volevo che in ogni istante l'ultimo 
elem fosse sempre il minimo. Questo faceva si che ad ogni push, io dovessi
spostare, in caso l'elemento inserito non fosse il min, nella posizione adatta.
Di fatto stavo prevedendo di tenere lo stack linkato e lì mi sono bloccato.
Se invece introduco il concetto di min stack, di fatto questo mi garantisce
ad ogni istante di tempo (aka ad ogni livello dello stack) il minimo fino a quel 
punto. Questo semplifica la get min a ritornare l'ultimo elemento banalmente
(dello stack min), e introduce una minima complessità nel push semplicemente
nel verificare se l'elemento pushato è anche il nuovo minimo della coda fino a
quel punto.
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum_stack: self.minimum_stack.append(val)
        else:
            if val < self.minimum_stack[-1]: self.minimum_stack.append(val)
            else: self.minimum_stack.append(self.minimum_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minimum_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]
