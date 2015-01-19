def memoize(proc):
  memo = {}
  def helper(x):
        if x in memo:
          return memo[x]
        else:
          memo[x] = proc(x, helper)
          return memo[x]
  return helper
