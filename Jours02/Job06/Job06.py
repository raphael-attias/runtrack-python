def est_premier(n):
 #Renvoie True si n est un nombre premier.
 if n <= 1:
   return False
 for i in range(2, int(n ** 0.5) + 1):
   if n % i == 0:
     return False
 return True

def main():
 #Affiche les nombres premiers jusqu'à 1000.
 for i in range(1, 1001):
   if est_premier(i):
     print(i)

if __name__ == "__main__":
 main()
