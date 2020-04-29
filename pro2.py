def rightShift(numbers):
  #right shifting lsb of a and b into b and c respectively
  a,b,c = numbers

  newA = a[0] + a[0:-1]
  newB = a[-1] + b[0:-1]
  newC = b[-1]

  return [newA,newB,newC]

def addition(numbers):
  #Function to add two binary numbers
  a,b = numbers

  carry = 0
  result = ''
  i = max(len(a),len(b)) -1

  while i >= 0:
    n = int(a[i]) + int(b[i]) + carry
    if n == 0:
      result= '0' + result
      carry = 0
    elif  n == 1:
      result = '1' + result
      carry = 0
    elif n == 2:
      result = '0' + result
      carry = 1
    elif n == 3:
      result = '1' + result
      carry = 1
    i -= 1
  return result

# two's compliment
def two_compliment(num):
	#Function to take 2's compliment of a number.
	l = list(num.strip(""))
	#inverting all the digits
	for i in range(len(l)):
		if(l[i]=="0"):
			l[i] = "1"
		else:
			l[i] = "0"
	#adding 1 to the number.
	carry = "1" 
	l = l[::-1]
	result = ""
	for k in range(len(l)):
		if(l[k]=="0"):
			if(carry == "0"):
				result = "0" + result
			else:
				result = "1" + result
				carry = "0"
		else:
			if(carry == "0"):
				result = "1" + result
			else:
				result = "0" + result
	return result

# binary
def binary(num):
	# if positive gie its binary
	#if the integer n is negative its twos_complement is to be returned
	if(num>=0):
		temp = bin(num)[2:]
		return "0"*(12 - len(temp)) + temp
	else:
		return(two_compliment(binary(-1*num)))

def multiply(num1, num2):
	#Function to multiply two numbers using Booth's Algorithm
	q = binary(num1) #one
	m = binary(num2) #two
	m_comp = two_compliment(m) #two_comp
	ac = "0"*12 #Accumulator content
	sc = 12 #sequence counter
	q_n1 = "0" #Q_n+1 initially 0
	while(sc>0):
		val = q[-1] + q_n1
		if(val=="01"):
			ac = addition([ac, m])
		if(val=="10"):
			ac = addition([ac, m_comp])
		ac, q, q_n1 = rightShift([ac, q, q_n1])
		sc-=1
	ans = ac+q # adds rightshift result to accumulator
	if(ac[0]=="0"):
		final = int(ans, 2) # convert string into int with base as 2
	else:
		final = -1*int(two_compliment(ans), 2)
	return [final, ans]

print("Multiplicand and Multiplyer")
a, b = map(int, input().split())
file=open("output.txt","w+")
temp = multiply(a, b)
file.write("Decimal Answer: "+str(temp[0])+" and "+" Binary: "+str(temp[1]))
file.close()