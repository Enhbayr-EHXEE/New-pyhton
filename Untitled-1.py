def is_perfect_number(n):
    # Togs too uguig shalgadag function
    divisors_sum = 1  # 1 urgelj yamarch toonii huwaagch
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n and n != 1

def closest_perfect_number(T):
    # T toond hamgiin oit togs toog oldog function
    for i in range(T, 0, -1):
        if is_perfect_number(i):
            return i
    return None  # ene dohioldolt togs too oldoogui gesen ug 

T = int(input("Enter a number T: "))

result = closest_perfect_number(T)

if result:
    print(f"{T} tootoi hamgiin oir togs too bol: {result}")
else:
    print(f"{T} toonoos baga togs too baihgui")
