
print('yusuf and sons')

principal = float(input('enter initial principal amount:'))


rate = float(input('enter rate:'))


time = float(input('enter time period in years:'))


n = int(input("enter number of times interest is applied per time period:"))


simple_interest = principal * (1 + rate * time)




compound_interest = principal * (1 + rate / n) ** (n * time)


print('yusuf and sons')


print('simple interest:', simple_interest)


print('compound interest:', compound_interest)

