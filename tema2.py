# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor
# care reprezintă numere întregi sau reale.

def your_function(*args, **kargs):
    sum = 0;
    try:
        for i in args:
            sum += i
    except BaseException as e:
        i = 0;
    return sum


print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(your_function())
print(your_function(2, 4, 'abc', param_1=2))


# Să se scrie o funcție recursivă care primește ca
# parametru un număr întreg și returnează:

# - suma tuturor numerelor de la [0,n]

def sum_all(n):
    if n == 0:
        return 0
    return n + sum_all(n - 1)


print(sum_all(10))


# - suma numerelor pare de la [0,n]

def sum_pare(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return n + sum_pare(n - 2)
    return sum_pare(n - 1)


print(sum_pare(6))


# - suma numerelor impare de la [0,n]

def sum_impare(n):
    if n==0:
        return 0
    elif n%2!=0:
        return n+sum_impare(n-1)
    return sum_impare(n-1)

print(sum_impare(7))


# Să se scrie o funcție care citește de la tastatură și returnează
# valoarea dacă aceasta este un număr întreg, altfel returnează
# valoarea 0.

my_var=input("Enter an integer value: ")
try:
    my_number=int((my_var))
except ValueError as e:
    print("You entered a str, not an int ")
    my_number=0
print(my_number)