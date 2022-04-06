def fizzbuzz(num_entrada):

    Calc_fizz = num_entrada%3
    Calc_buzz = num_entrada%5


    if Calc_fizz == 0 and Calc_buzz != 0:
        return "Fizz"
    if Calc_fizz !=0 and Calc_buzz ==0:
        return "Buzz"
    if Calc_fizz == 0 and Calc_buzz ==0:
        return "FizzBuzz"
    if Calc_fizz != 0 and Calc_buzz !=0:
        return num_entrada
    

