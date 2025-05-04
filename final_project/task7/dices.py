import random
# import matplotlib.pyplot as plt
from collections import Counter


NUM_SIMULATIONS = 1_000_000

sums = [random.randint(1, 6) + random.randint(1, 6)
        for _ in range(NUM_SIMULATIONS)]
counts = Counter(sums)

analytical_probs = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

monte_carlo_probs = {s: counts[s] / NUM_SIMULATIONS for s in range(2, 13)}

print("| Сума | Monte Carlo | Аналітична |")
print('|------|-------------|------------|')
for s in range(2, 13):
    mcp = f"{monte_carlo_probs[s]:.4f}"
    ap = f"{analytical_probs[s]:.4f}"
    print(f"|{s:^6}|{mcp:^13}|{ap:^12}|")

# # Побудова графіка
# sums_range = list(range(2, 13))
# mc_values = [monte_carlo_probs[s] for s in sums_range]
# analytical_values = [analytical_probs[s] for s in sums_range]

# plt.figure(figsize=(10, 6))
# plt.bar(sums_range, mc_values, width=0.4,
#         label='Monte Carlo', color='skyblue', align='center')
# plt.bar([s + 0.4 for s in sums_range], analytical_values, width=0.4,
#         label='Аналітична', color='orange', align='center')
# plt.xticks(sums_range)
# plt.xlabel("Сума на кубиках")
# plt.ylabel("Ймовірність")
# plt.title("Порівняння ймовірностей сум для двох кубиків")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()
