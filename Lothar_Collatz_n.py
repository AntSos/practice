#Asimple program that count the steps to reach number using Collatz teory

def l_c_steps (number):
    count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2 # Sameas number = number // 2
        else:
            number = (number * 3) + 1

        count += 1
    print (f"Steps to Lothar Collatz conjeture = {count}")

def main ():
    number = int (input ("Enter a number: "))
    l_c_steps (number)

if __name__ == "__main__":
    main ()