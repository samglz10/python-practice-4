#gets the max number
from unittest import result


def max_num(a,b,c):
    return max([a,b,c])

print("The Max Number is", max_num(1,2,3))

#multiplies lists
def mult_list(list):
    if len(list) == 0:
        return 0
    new_list = list[0]

    
    if len(list) > 1:
        for i in list[1:]:
            new_list = new_list * i
        return new_list

print(mult_list([1,2,3,4]))

#reverse a string
def rev_string(str):
    return str[::-1]
print(rev_string("Palindromes"))

# Checks whether a number falls in a given range
def num_within(x, num1, num2 ):
    return x in range(num1,num2+1)

# 8 does not fall in the range of 2 & 4 so it will return false      
print(num_within(8,2,4))
print(num_within(3,1,3))

#Pascal triangle https://www.youtube.com/watch?v=MzdzJuvzmS4
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)