
def limpiar_palabra(palabra: str) -> str:
    try:
        signos = "¡!¿?.,:;()[]{}\"'<>-_/\\|@#$%^&*~`+="
        palabra = palabra.lower()
        palabra = palabra.strip(signos)
        return palabra
    except AttributeError:
        return ""
    
class Analizador_de_texto:
  contador_analisis=0

  def __init__(self,texto,nombre_analisis="General"):
    self.texto = texto
    self.nombre_analisis = nombre_analisis
    Analizador_de_texto.contador_analisis +=1

  def texto_limpio(self) -> str:
    texto = self.texto.lower()  
    signos_de_puntuacion = "¡!¿?.,:;()[]{}\"'<>-_/\\|@#$%^&*~`+=" 
    for s in signos_de_puntuacion:
      texto = texto.replace(s, "")
    return texto
  
  def estadisticas_basicas(self) -> tuple:
    texto = self.texto_limpio()
    palabras = texto.split()
    if len(palabras) == 0:
      return (0,"")
    numero_palabras =len(palabras)
    palabra_mas_larga = max(palabras, key=len)
    return(numero_palabras,palabra_mas_larga)
  
  def frecuencia_palabras(self) -> dict:
    texto = self.texto_limpio()
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia
  
  def palabras_relevantes(self, umbral=3) -> list:
    lector = self.frecuencia_palabras()  
    relevantes = []
    for titulo_dic, valor_dic in lector.items():
        if valor_dic >= umbral:
            relevantes.append(titulo_dic) 
    return relevantes
