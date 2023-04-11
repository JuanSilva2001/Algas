import matplotlib.pyplot as plt
import conectDB

for contadorN in range(10):
    vetor = conectDB.selecionarDados(f"sensor_{str(contadorN+1).zfill(2)}")
    plt.plot(vetor[4], vetor[0], label="PH")
    plt.plot(vetor[4], vetor[1], label="Temperatura")
    plt.plot(vetor[4], vetor[2], label="Turbidez")
    plt.plot(vetor[4], vetor[3], label="Oxigenio")
    plt.legend(loc='upper left')
    plt.show()