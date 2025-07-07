from Clases import Analizador_de_texto

texto1 = "Espero que este ejercicio funcione dios mio me faltaron varias cosas pero buee dios buee"
texto2 = "Que no se caiga produccion dios mio o no podre volver a estar en esta oficina"

analisis1 = Analizador_de_texto(texto1, "Análisis de ejercicio")
analisis2 = Analizador_de_texto(texto2, "Análisis de produccion")

print(f"\nTexto limpio 1: {analisis1.texto_limpio()}")
print(f"Texto limpio 2: {analisis2.texto_limpio()}")

print(f"\nEstadísticas texto 1: {analisis1.estadisticas_basicas()}")
print(f"Estadísticas texto 2: {analisis2.estadisticas_basicas()}")


print(f"\nFrecuencia palabras 1: {analisis1.frecuencia_palabras()}")
print(f"Frecuencia palabras 2: {analisis2.frecuencia_palabras()}")

print(f"\nPalabras relevantes 1 (umbral=2): {analisis1.palabras_relevantes(2)}")
print(f"Palabras relevantes 2 (umbral=2): {analisis2.palabras_relevantes(2)}")

print(f"\nTotal de análisis realizados: {Analizador_de_texto.contador_analisis}")
