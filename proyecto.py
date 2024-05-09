DECIMALES = 3

def imprimirMatriz(A: list[list[float]]) -> None:
    """
    Imprime una matriz
    Args:
        A (list[list[float]]): matriz a imprimir.

    Returns:
        None
    """
    n = len(A)
    for i in range(n):
        for j in range(n):
             print(A[i][j], end="  ")
        print()


def descomposicionLU( A:list[list[float]], b:list[float] ) -> list[float]:
    """
    Esta función resuelve un sistema de ecuaciones, retornando un 
    vector con la solucion.

    Args:
        A (list[list[float]]): matriz cuadrada de coeficientes.
        b (list[float]): vector de terminos independientes.

    Returns:
        list[float]: vector con las soluciones.
    """
    
    # crear matrices iniciales LU
    n = len(A)

    # matriz L
    L = []
    for i in range(n):
        L.append([])
        for j in range(n):
                if i == j: 
                    L[i].append(1.0)
                else:
                     L[i].append(0.0)
    
    # matriz U
    U = []
    for i in range(n):
        U.append([])
        for j in range(n):
                U[i].append(0.0)
    
    """
    Renglon 1 de U:
        u{1}{j} = a{1}{j}
    """
    for j in range(n):
        U[0][j] = A[0][j]
    
    """
    Columna 1 de L:
        l{i}{1} = a{i}{1}/u {1}{1}
    """
    for i in range(1, n):
        # redonde de 3 cifras
        L[i][0] = round(A[i][0]/U[0][0], DECIMALES)
    
    """
    Renglon 2 <= i <= n - 2 de U
        i{i}{j} = a{i}{j} - suma( desde k = 1 hasta i - 1){
            l{i}{k}*u{k}{j}
        }
    """
    for i in range(1, n-2):
        for j in range(i, n):
            suma = 0
            for k in range(0, i):
                suma += L[i][k] * U[k][j]

            U[i][j] = A[i][j] - suma

    """
    Columna 2 de L:
    """
    for i in range(2, 4):
        # redonde de 3 cifras
        L[i][1] = round( (A[i][1]-(L[i][0]*U[0][1])) / U[1][1], DECIMALES)

    """
    Renglon 3 de U
    """
    for i in range(2, n-1):
        for j in range(i, n):
            suma = 0
            for k in range(0, i):
                suma += L[i][k] * U[k][j]

            U[i][j] = A[i][j] - suma

    """
    Columna 3 de L
    """
    suma = 0.0
    for k in range(2):
        suma += L[3][k] * U[k][2]

    L[3][2] = round( (A[3][2] - suma)/U[2][2], DECIMALES )

    """
    Ultimo renglon de U
    """
    for i in range(3,n):
        suma = 0
        for k in range(n-1):
            suma += L[n-1][k] * U[k][n-1]

        U[n-1][n-1] = round( A[n-1][n-1] - suma, DECIMALES )

    """
    Calculo de d con sustitucion hacia delante
    i = 1,2,3,...,n
    d{i} = b{i} - sum( desde k = 1 hasta i - 1){
        l{i}{k} * d{k}
    }
    """
    d = [0.0 for _ in range(n)]
    for i in range(n):
        suma = 0
        for k in range(i):
            suma += L[i][k] * d[k]
        d[i] = round( b[i] - suma, 3 )

    """
    Calculo de x con sustitucion hacia atras
    i = n, n-1,...,1
    x{i} = d{i} - sum( desde k = i + 1 hasta n){
        u{i}{k} * x{k}
    } / u{i}{i}
    """
    x = [0.0 for _ in range(n)]
    for i in range(n-1 , -1, -1):
        suma = 0
        for k in range(i+1, n):
            suma += U[i][k] * x[k]

        x[i] = round( (d[i] - suma)/U[i][i], DECIMALES )

    return x

            
print("== Mejora ergonómica en Área de urgencias del hospital gea gonzalez ==")

print("\nPara un día se realizaran 4 operaciones usando este equipo:")
print("Transfer estriado")
print("Discos giratorios")
print("Sillas de ducha")
print("Cinturón para cargar paciente")

b = [0.0 for _ in range(4)]
print("\nIngresa el tiempo (paciente\día) para las 4 operaciones:")
for i in range(4):
    b[i] = float(input(f"Operación {i+1}: "))
print("Tiempo de operaciones:")
for i in range(4):
    print(f"Operación {i+1}: {b[i]} (pacientes/dia)")

A = [[0.0] * 4 for _ in range(4)]
equipo = ["Transfer estriado", "Discos giratorios", "Sillas de ducha", "Cinturón para cargar paciente"]
print("\nIngresa el tiempo de uso al día de cada equipo ergonómico para cada operación:")
for i in range(4):
    for j in range(4):
        A[i][j] = float(input(f"Para la opeación {i+1} el equipo '{equipo[j]}' se ocupa: "))
    print()
print("Tiempo de uso de cada equipo para cada operacion:")
for i in range(4):
    for j in range(4):
        print(f"Para la operacion {i+1} el equipo '{equipo[j]}' se usara: {A[i][j]}")
    print()

imprimirMatriz(A)
print(b)

