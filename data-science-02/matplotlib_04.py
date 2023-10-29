from matplotlib import pyplot as plt

clubes = [
    {"nome": "Santos", "libertadores": 3},
    {"nome": "São Paulo", "libertadores": 3},
    {"nome": "Palmeiras", "libertadores": 2},
    {"nome": "Grêmio", "libertadores": 3},
    {"nome": "Internacional", "libertadores": 2},
    {"nome": "Flamengo", "libertadores": 2},
    {"nome": "Cruzeiro", "libertadores": 2},
    {"nome": "Atlético-MG", "libertadores": 1},
    {"nome": "Corinthians", "libertadores": 1},
    {"nome": "Vasco da Gama", "libertadores": 1}
]

nomes_dos_times = [clube["nome"] for clube in clubes]
titulos_dos_times = [clube["libertadores"] for clube in clubes]

plt.bar(nomes_dos_times, titulos_dos_times)
plt.ylabel("# Títulos de Libertadores")
plt.title("Maiores vencedores de Liberta")

plt.show()