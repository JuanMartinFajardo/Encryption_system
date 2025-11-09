def break_cipher(msn):
    """
    Intenta romper el cifrado V2, buscando el patrón de "marcador-ancla".
    No usa la key, solo el criptograma 'msn'.
    """
    
    # 1. Crear el mapa de frecuencias para búsquedas rápidas
    mapa_frecuencias = dict(zip(msn[0], msn[1]))
    
    # 2. Obtener una lista ordenada de todos los números
    numeros_ordenados = sorted(mapa_frecuencias.keys())
    
    letras_encontradas = {}
    
    # 3. El atacante tiene que adivinar dónde empieza el primer rango.
    #    La suposición más lógica es 0 o 1.
    lim_1 = 0 

    print("--- Iniciando Criptoanálisis V2 (Patrón de Frecuencias) ---")

    # 4. Iteramos por cada número 'k' y suponemos que ES un marcador
    for k in numeros_ordenados:
        
        if k not in mapa_frecuencias: continue
            
        frec_marcador = mapa_frecuencias[k]
        if frec_marcador == 0: continue

        # 5. Definimos el rango que este marcador 'k' estaría cubriendo
        intervalo = [t for t in range(lim_1, k) if t in mapa_frecuencias]
        
        if not intervalo:
            # Este rango estaba vacío, 'k' no es un marcador de este rango.
            continue 
            
        # 6. EL ATAQUE: Buscar el patrón "ancla"
        #    ¿Existe algún número 't' en el intervalo que tenga
        #    la MISMA frecuencia que nuestro supuesto marcador 'k'?
        tiene_ancla = False
        for t in intervalo:
            if mapa_frecuencias[t] == frec_marcador:
                tiene_ancla = True
                break # ¡Patrón encontrado!

        # 7. Si encontramos el patrón, 'k' es un marcador.
        if tiene_ancla:
            print(f"¡Patrón detectado! Marcador: {k} (Frec: {frec_marcador}), Rango: {lim_1}-{k}")
            
            posiciones = []
            
            # 8. APLICAMOS TU PROPIA LÓGICA DE DECODE
            for f_check in range(1, frec_marcador + 1):
                M = []
                for t in intervalo:
                    if mapa_frecuencias[t] >= f_check:
                        M.append(t)
                
                pos = len(M)
                if pos > 0 and pos not in posiciones:
                    posiciones.append(pos)
            
            if posiciones:
                posiciones.sort()
                nombre_char = f"Char_Marcador_{k}"
                letras_encontradas[nombre_char] = {
                    "posiciones": posiciones, 
                    "veces": frec_marcador
                }
            
            # 9. El siguiente rango empieza después de este marcador
            lim_1 = k + 1

    print(f"--- Análisis Completo ---")
    return letras_encontradas

# --- Ejemplo de uso (simulado) ---
#
# Si el mensaje fue "banana" y la key dio:
# 'a' (marcador 15): [1, 3, 5]
# 'b' (marcador 30): [4]
# 'n' (marcador 23): [0, 2]
#
# Y 'msn' es el resultado de tu encriptador (sin ruido)...
#
# resultado_del_ataque = break_cipher_v2(msn_de_banana)
# print(resultado_del_ataque)
#
# SALIDA ESPERADA:
# --- Iniciando Criptoanálisis V2 (Patrón de Frecuencias) ---
# ¡Patrón detectado! Marcador: 15 (Frec: 3), Rango: 0-15
# ¡Patrón detectado! Marcador: 23 (Frec: 2), Rango: 16-23
# ¡Patrón detectado! Marcador: 30 (Frec: 1), Rango: 24-30
# --- Análisis Completo ---
# {
#   'Char_Marcador_15': {'posiciones': [1, 3, 5], 'veces': 3}, # (La 'a')
#   'Char_Marcador_23': {'posiciones': [0, 2], 'veces': 2},    # (La 'n')
#   'Char_Marcador_30': {'posiciones': [4], 'veces': 1}       # (La 'b')
# }

msn1 = [[4, 11, 21, 32, 33, 47, 67, 73, 75, 83, 86, 87, 395, 399, 400, 411, 469, 490, 501, 504, 505, 844, 1038, 1042, 1051, 1057, 1059, 1061, 1069, 1075, 1076, 1078, 1081, 1083, 1087, 1458, 1497, 1596, 1597, 1634, 1645, 1700, 1783, 1792, 1916, 1919, 1921, 1942, 1944, 1954, 1956, 1957, 1960, 1965, 1970, 1984, 1993, 2010, 2011, 2013, 2014, 2025, 2042, 2625, 2639, 2651, 2668, 2703, 2719, 2725, 2736, 2740, 2748, 5370, 5383, 5413, 5420, 5421, 7571, 7573, 7582, 7585, 7599, 7616, 7626, 7628, 7630, 7633, 7639, 7654, 7659, 7662, 7663, 14030, 14064, 14091, 14104, 14108, 14119, 14125, 14128], [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 9, 14, 14, 3, 5, 22, 6]]

msn = [[4, 6, 8, 14, 16, 17, 19, 20, 21, 23, 24, 30, 31, 39, 40, 42, 43, 44, 51, 60, 61, 62, 65, 66, 67, 69, 71, 76, 81, 87, 90, 93, 97, 100, 109, 112, 113, 114, 124, 126, 130, 136, 140, 143, 145, 156, 174, 186, 189, 192, 196, 208, 214, 217, 219, 220, 222, 223, 224, 228, 230, 240, 247, 248, 249, 252, 257, 258, 263, 267, 269, 272, 274, 278, 280, 283, 285, 287, 291, 307, 318, 320, 323, 325, 337, 343, 349, 353, 358, 363, 366, 368, 373, 374, 376, 384, 385, 386, 392, 397, 401, 405, 410, 426, 430, 438, 445, 448, 453, 455, 460, 461, 466, 477, 484, 489, 495, 496, 499, 504, 505, 845, 852, 855, 857, 860, 863, 866, 867, 869, 870, 875, 878, 879, 881, 882, 885, 888, 890, 891, 892, 895, 896, 897, 900, 902, 903, 905, 907, 908, 909, 910, 912, 1192, 1195, 1197, 1201, 1203, 1211, 1217, 1224, 1227, 1229, 1230, 1237, 1245, 1246, 1248, 1250, 1251, 1254, 1255, 1257, 1259, 1262, 1271, 1272, 1275, 1280, 1281, 1292, 1302, 1304, 1307, 1313, 1314, 1316, 1403, 1407, 1408, 1409, 1412, 1413, 1418, 1419, 1421, 1427, 1428, 1434, 1436, 1440, 1441, 1445, 1446, 1459, 1466, 1468, 1469, 1470, 1471, 1473, 1476, 1481, 1484, 1485, 1488, 1490, 1493, 1494, 1497, 1499, 1501, 1502, 1503, 1505, 1509, 1512, 1517, 1518, 1520, 1521, 1526, 1527, 1530, 1533, 1535, 1537, 1539, 1544, 1545, 1547, 1548, 1550, 1551, 1554, 1555, 1556, 1557, 1795, 1796, 1799, 1804, 1805, 1807, 1810, 1817, 1820, 1821, 1823, 1824, 1825, 1827, 1828, 1829, 1830, 1831, 1832, 1834, 1836, 1840, 1842, 1843, 1846, 1848, 1849, 1862, 1871, 1875, 1891, 1910, 1914, 1915, 1916, 1920, 1921, 1924, 1926, 1927, 1931, 1932, 1934, 1937, 1938, 1939, 1940, 1946, 1947, 1949, 1950, 1954, 1955, 1957, 1958, 1961, 1962, 1963, 1965, 1967, 1968, 1970, 1971, 1972, 1975, 1978, 1983, 1986, 1988, 2001, 2003, 2006, 2007, 2029, 2032, 2037, 2042, 2634, 2635, 2637, 2643, 2645, 2662, 2663, 2668, 2669, 2674, 2676, 2681, 2696, 2699, 2701, 2705, 2714, 2730, 2738, 2739, 2742, 2748, 3163], [3, 2, 1, 2, 1, 1, 2, 3, 3, 3, 3, 3, 1, 2, 1, 3, 1, 1, 1, 1, 2, 2, 3, 3, 3, 2, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 3, 4, 4, 3, 1, 2, 4, 3, 3, 2, 4, 3, 3, 2, 3, 2, 3, 3, 4, 4, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 3, 2, 1, 1, 3, 1, 2, 1, 2, 3, 1, 2, 2, 3, 2, 2, 3, 2, 2, 3, 2, 1, 3, 2, 1, 3, 3, 2, 2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 3, 2, 4, 4, 5, 2, 3, 2, 5, 2, 1, 1, 3, 2, 2, 2, 1, 5, 3, 5, 4, 5, 1]]
Dec = break_cipher(msn1)
print(Dec)