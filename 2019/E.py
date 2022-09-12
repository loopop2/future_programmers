n, q = [int(x) for x in input("Enter N and Q: ").split(" ")]
d_o = [int(x) for in input("Devices and Operations: ").split(" ")]
while n < 1 or n > 5000: n = int(input("Enter valid N: "))
while q < 1 or q > pow(10,6): n = int(input("Enter valid Q: "))

untested = [x for x in range(1,len(d_o),2)]
