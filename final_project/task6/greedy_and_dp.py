def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if budget >= info['cost']:
            selected_items.append(item)
            total_calories += info['calories']
            budget -= info['cost']

    return selected_items, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]

    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1]
                               [w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(names[i - 1])
            w -= costs[i - 1]

    total_calories = dp[n][budget]
    return selected_items, total_calories


if __name__ == "__main__":

    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    while True:
        try:
            budget = int(
                input("Enter your budget (for stop enter <-1> or NaN): "))
            if budget < 0:
                print("While stoped.")
                break
        except ValueError:
            print("Invalid input. Please enter a intenger number.")
            break

        greedy_result = greedy_algorithm(items, budget)
        print("\nGreedy Algorithm:")
        print("Selected items:", greedy_result[0])
        print("Total calories:", greedy_result[1])

        dp_result = dynamic_programming(items, budget)
        print("\nDynamic Programming:")
        print("Selected items:", dp_result[0])
        print("Total calories:", f"{dp_result[1]}\n")
