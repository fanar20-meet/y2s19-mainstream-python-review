# Part 2 of the Python Review lab.

def is_prime(n):
        if n > 1:
                for i in range(2,n):
                        if n % i == 0:
                                return False
        return True                        


def encode(x, y):
        while not is_prime(x):
                x += 1
        while not is_prime(y):
                y += 1

        if 1 < y < 250 and 500 < x < 1000 :
                return x*y
        else:
                print("invalid input:outside range")
                return(None)



def decode(coded_message):
        for y in range (2,250):
                print(y)
                if not is_prime(y):
                        continue
                # making sure x is also an integer        
                if coded_message % y == 0 :
                        x = coded_message / y
                        if (is_prime(int(x)) and 500 < x < 1000):
                                return(x,y)	





