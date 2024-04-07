def fibo_sec (length):
    count= 0
    fibo_list = [0 , 1]
    
    while count <= length-2:
        
        fibo_num = fibo_list[count] + fibo_list[count + 1]
        fibo_list.append (fibo_num)
        count += 1

    return fibo_list


def main ():
    
    number = int (input ("Enter a length for the FibonacciSecuence: "))
    print (f"The fibonacci secuence for the {number} is: ", fibo_sec (number))
   

if __name__ == "__main__":

    main ()
