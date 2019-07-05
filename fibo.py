def get(n):
        n = n + 1
        a = 0
        b = 1
        if n == 0: 
                return a 
        elif n == 1: 
                return b 
        else: 
                for i in range(2,n): 
                    c = a + b 
                    a = b 
                    b = c 
                return b


def main():
	print(get(7))	

if __name__ == '__main__':
	main()

