while True:

    try:

        N = float(input("Четное значение входной границы, не включая '2':"))

        

         



        n = float(N)

        if n - int(n) == 0:

            n = int(n)

            if n % 2 != 0:

                print("Введите четное число")

                continue

            elif n < 0:

                print("Только положительные числа")

                continue

            elif n == 2:

                print("ВВедите другое число")

                continue

            elif n == 0:

                print("Please, input another even number")

                continue

            break

        else:

            continue

        

    except ValueError:

        print("Неверное значение!")



def prime_check(n):

    print("Номер для проверки", n, '\n')

    numbers = list(range(2, n + 1))

    for i in numbers:

        if i != 0:

            for k in range(2 * i, n + 1, i):

                numbers[k - 2] = 0



    primes = [x for x in numbers if x != 0]

    print("Список простыч чисел:", primes, '\n')



    def task():

        for position in range(len(primes)):

            z = n - primes[position]

            if z in primes:

                print("Общее количество этих элементов из списка простых чисел дает наше значение:", 2, "+",

                      primes[position])

            position += 1



    task()



if __name__ == '__main__':

    prime_check(n)
