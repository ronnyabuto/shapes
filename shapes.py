def draw_triangle(height):
    print("n--- 0. Triangle ---")
    for i in range(1, height + 1):
        print("*" *i)
    
draw_triangle(5)

def draw_heart():
    print("\n--- 1. Heart (for loop) ---")
    for i in range(6):
        for j in range(7):
            if (
                (i == 0 and j % 3 != 0)
                or (i == 1 and j % 3 == 0)
                or (i - j == 2)
                or (i + j == 8)
            ):
                print("*", end="")
            else:
                print(" ", end="")
        print()

draw_heart()

def draw_inverted_triangle(height):
    print("\n--- 2. Inverted Triangle (while loop) ---")
    i = height
    while i > 0:
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        
        print(spaces + stars)
        i -= 1
draw_inverted_triangle(5)


def draw_hollow_square(size):
    print("\n--- 3. Hollow Square (while loop) ---")
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            if i == 1 or i == size or j == 1 or j == size:
                print("*", end=" ")
            else:
                print(" ", end=" ")
            j += 1
        print()
        i += 1

draw_hollow_square(5)


def draw_xmas_tree(height):
    print("\n--- 4. Christmas tree (for loop) ---")
    for i in range(height):
        print(" " * (height - i - 1) + "* " * (i + 1))

    print(" " * (height - 1) + "*")

draw_xmas_tree(5)


def draw_diamond(rows):
    print("\n--- 5. Diamond (for loop) ---")
    for i in range(rows):
        print(" " * (rows - i - 1) + "* " * (i + 1))

    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "* " * i)

draw_diamond(5)