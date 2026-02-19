morning = float(input())
afternoon = float(input())
evening = float(input())

cartej = (morning, afternoon, evening)

tem = sum(cartej) / len(cartej)

print(f"{tem:.2f}")
