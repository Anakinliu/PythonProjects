import math

@profile
def check_prime(number):
    sqer_number = math.sqrt(number)
    number_float = float(number)
    for i in range(2, int(sqer_number) + 1):
        if (number_float / i).is_integer():
            return False
    return True

# x = 12026655772210679470465581609002525329245773732132014742758935511187863487919026457076252932048619706498126046597130520643092209728783224795661331197604583
# check_prime(x)
check_prime(100001651)