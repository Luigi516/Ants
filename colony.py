import random
import matplotlib.pyplot as plt

class Formica:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muovi(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

class Ambiente:
    def __init__(self, dimensione):
        self.dimensione = dimensione
        self.cibo_x = random.randint(0, dimensione-1)
        self.cibo_y = random.randint(0, dimensione-1)
        self.formiche = [Formica(random.randint(0, dimensione-1), random.randint(0, dimensione-1)) for _ in range(10)]

    def aggiorna(self):
        for formica in self.formiche:
            formica.muovi()

    def visualizza(self):
        plt.scatter(self.cibo_x, self.cibo_y, color='green', marker='X', s=200, label='Cibo')
        for formica in self.formiche:
            plt.scatter(formica.x, formica.y, color='black', marker='o')
        plt.xlim(0, self.dimensione)
        plt.ylim(0, self.dimensione)
        plt.legend()
        plt.show()

def main():
    dimensione_ambiente = 20
    ambiente = Ambiente(dimensione_ambiente)

    for _ in range(100):
        ambiente.aggiorna()
        ambiente.visualizza()

if __name__ == "__main__":
    main()