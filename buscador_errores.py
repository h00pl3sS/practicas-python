import os

def analizar_log(archivo_entrada, palabra_clave):
    archivo_salida = "reporte_errores.txt"
    
    try:
        # Abrimos el log original en modo lectura ('r')
        with open(archivo_entrada, 'r') as log:
            # Creamos (o sobreescribimos) el reporte en modo escritura ('w')
            with open(archivo_salida, 'w') as reporte:
                lineas_encontradas = 0
                
                for linea in log:
                    if palabra_clave.upper() in linea.upper():
                        reporte.write(linea)
                        lineas_encontradas += 1
                
                print(f"✅ Análisis completado. Se encontraron {lineas_encontradas} eventos.")
                print(f"📄 Resultados guardados en: {os.path.abspath(archivo_salida)}")

    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{archivo_entrada}'.")
    except Exception as e:
        print(f"⚠️ Ocurrió un error inesperado: {e}")

# --- Ejecución del script ---
# Cambia 'servidor.log' por el nombre de un archivo que tengas o crea uno de prueba
analizar_log("log.txt", "ERROR")
