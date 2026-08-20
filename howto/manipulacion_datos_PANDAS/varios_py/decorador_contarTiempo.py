import time


def contarTiempo(funcion):
    def medir_duracion(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        duracion = time.time() - inicio
        print(f"⏱️ Tiempo de ejecución: {duracion:.4f} segundos")
        return resultado
    return medir_duracion