import numpy as np
import matplotlib.pyplot as plt

def solucion_analitica(t, g, m, c):
    return (g * m / c) * (1 - np.exp(- (c / m) * t))

def solucion_numerica(dt, t_max, g, m, c):
    t_values = np.arange(0, t_max + dt, dt)
    v_values = np.zeros_like(t_values, dtype=float)
    
    for i in range(1, len(t_values)):
        v_values[i] = v_values[i-1] + (g - (c/m) * v_values[i-1]) * dt
    
    return t_values, v_values

def main():
    # Parámetros
    g = 9.8      # Gravedad (m/s²)
    m = 62       # Masa del paracaidista (kg)
    c = 12.5     # Coeficiente de resistencia del aire (kg/s)
    dt = 0.1     # Paso de tiempo (s)
    t_max = 100  # Tiempo máximo de simulación (s)
    
    print("Solución Analítica")
    t_vals = np.arange(0, t_max + dt, dt)
    v_analitica = [solucion_analitica(t, g, m, c) for t in t_vals]
    
    print("\nSolución Numérica (Método de Euler)")
    t_numerico, v_numerico = solucion_numerica(dt, t_max, g, m, c)
    
    print("\nError en cada tiempo")
    errores = [abs(va - vn) for va, vn in zip(v_analitica, v_numerico)]
    
    for t, v_a, v_n, error in zip(t_vals, v_analitica, v_numerico, errores):
        print(f"t = {t:.1f}s -> v_analítica = {v_a:.16f} m/s, v_numérica = {v_n:.16f} m/s, Error = {error:.16f} m/s")
    
    # Graficar ambas soluciones y el error
    plt.figure(figsize=(8, 6))
    plt.plot(t_vals, v_analitica, label='Solución Analítica', linestyle='-', linewidth=2)
    plt.plot(t_numerico, v_numerico, label='Solución Numérica (Euler)', linestyle='--', linewidth=2)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.title('Comparación de Soluciones: Caída de un Paracaidista')
    plt.legend()
    plt.grid()
    plt.show()
    
    plt.figure(figsize=(8, 6))
    plt.plot(t_vals, errores, label='Error Absoluto', linestyle='-', color='red', linewidth=2)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Error (m/s)')
    plt.title('Error entre Solución Analítica y Numérica')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
