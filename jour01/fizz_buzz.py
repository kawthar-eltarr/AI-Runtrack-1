# Job 19
print("This is job 19 :")
for i in range(0, 100):
    if (i // 3) == 0:
        print("Fizz")
    elif (i // 5) == 0:
        print("Buzz")
    elif (i // 3) == 0 and (i // 5) == 0:
        print("FizzBuzz")
    else:
        print(i)