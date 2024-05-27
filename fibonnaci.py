def multiply(A,B):
      C = [[0,0],[0,0]]
      for _ in range(2):
            for __ in range(2):
                  for ___ in range(2):
                        C[_][___] += A[_][__] * B[__][___]
      return C
def mat_power(A,b):
      # return A^b
      Res = [[1,0][0,1]]
      while(b):
            if(b % 2 == 1):
                  Res = multiply(Res,A)
            A = multiply(A,A)
            b //= 2
      return Res
def fibonacci(n):
      f0 = 0
      f1 = 1
      # (f2 f1) = ((1 1)(1 0)) (f1 f0)
      # A = ((1 1)(1 0))
      # (fn fn-1) = A^(n-1) (f1 f0)
      # We need B = A^(n - 1)
      A = [[1,1],
           [1,0]]
      B = mat_power(A,n - 1)
      return B[0][0]
      
print(fibonacci(9))  
