import math


@profile
def check_prime(number):
    sqrt_number = math.sqrt(number)
    number_float = float(number)
    numbers = range(2, int(sqrt_number) + 1)
    for i in range(0, len(numbers), 10):
        if any([(number_float / e).is_integer() for e in numbers[i:i+5]]):
            return False
    return True


# x = 12026655772210679470465581609002525329245773732132014742758935511187863487919026457076252932048619706498126046597130520643092209728783224795661331197604583
# check_prime(x)
# for i in range(100):
#     print(f'{i} : {check_prime(i)}')
check_prime(100001651)