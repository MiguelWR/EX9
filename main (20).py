#Exercício 9

def No(n):
  if n == 1:
      return 1
  elif n > 1:
      return n + No(n - 1)

print(No(4))