a = 0
b = 1

print("Els 10 primers termes de Fibonacci són:")

# Com que sabem exactament que volem 10 números, fem un bucle for
for i in range(10):
    print(a)  # Mostrem el número actual per pantalla
    
    # Fem el "baile" de variables: actualitzem 'a' i 'b' alhora
    a, b = b, a + b
