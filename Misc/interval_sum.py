''' prefix_sum '''
# O(N + M)
# P[R] - P[L - 1]

def get_interval_sum(data, left, right):
  summary = 0
  prefix_sum = [0]
  
  for i in data:
    summary += i
    prefix_sum.append(summary)
    
  return prefix_sum[right] - prefix_sum[left - 1]