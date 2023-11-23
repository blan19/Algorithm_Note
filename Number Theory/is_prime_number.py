import math

# O(x)
# def is_prime_number(x):
#   for i in range(2, x):
#     if x % i == 0:
#       return False
#   return True

def is_prime_number(x):
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % i:
      return False
  return True

def get_prime_number(n):
  result = []

  arr = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
  
  for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인
    if arr[i] == True: # i가 소수인 경우(남은 수인 경우)
      # i를 제외한 i의 모든 배수를 지운다
      j = 2
      while i * j <= n:
        arr[i * j] = False
        j += 1
        
  for i in range(2, n + 1):
    if arr[i]:
      result.append(i)
      
  return result