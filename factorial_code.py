def factorial(n):
    # a factorial is N!
    count = 0
    n_going_down = n
    answer = 1

    while n > count:
        answer = answer * n_going_down
        count += 1
        n_going_down -= 1

    print(answer)
    return answer


factorial(11)
