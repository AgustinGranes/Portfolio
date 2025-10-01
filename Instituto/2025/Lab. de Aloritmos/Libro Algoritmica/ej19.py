def f(n):
  if n == 1:
    return 2
  else:
    return n + 1 / f(n - 1)

print(f"f(1) = {f(1)}")
print(f"f(2) = {f(2)}")
print(f"f(3) = {f(3)}")
print(f"f(4) = {f(4)}")
print(f"f(5) = {f(5)}")