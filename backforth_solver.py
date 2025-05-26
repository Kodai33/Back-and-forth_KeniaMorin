# -*- coding: utf-8 -*-
"""
@Author: Kenia Moein Suchel 2047938
"""

def solve():
    # Leer los datos desde el archivo de entrada
    with open('backforth.in', 'r') as f:
        barn1 = list(map(int, f.readline().split()))
        barn2 = list(map(int, f.readline().split()))

    unique_totals = set()

    # Función recursiva para realizar la búsqueda completa
    def dfs(day, total1, total2, b1, b2):
        if day == 4:
            unique_totals.add(total1)
            return

        if day % 2 == 0:
            # Día par: mover de barn1 a barn2
            for i in range(len(b1)):
                new_b1 = b1[:i] + b1[i+1:]
                new_b2 = b2 + [b1[i]]
                dfs(day + 1, total1 - b1[i], total2 + b1[i], new_b1, new_b2)
        else:
            # Día impar: mover de barn2 a barn1
            for i in range(len(b2)):
                new_b2 = b2[:i] + b2[i+1:]
                new_b1 = b1 + [b2[i]]
                dfs(day + 1, total1 + b2[i], total2 - b2[i], new_b1, new_b2)

    # Iniciar DFS desde el día 0 con los valores iniciales
    dfs(0, 1000, 1000, barn1, barn2)

    # Escribir el resultado en el archivo de salida
    with open('backforth.out', 'w') as f:
        f.write(f"{len(unique_totals)}\n")

# Ejecutar la función
solve()
