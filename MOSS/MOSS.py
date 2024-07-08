import mosspy
import os

# Reemplaza esto con tu ID de usuario MOSS
userid = "908437891"

# Crear una instancia de Moss con tu ID de usuario y el lenguaje C#
m = mosspy.Moss(userid, "csharp")

# Función para agregar archivos de una carpeta a MOSS
def add_files_from_directory(moss, directory, as_base=False):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".cs"):
                file_path = os.path.join(root, file)
                if as_base:
                    moss.addBaseFile(file_path)
                else:
                    moss.addFile(file_path)


# Agregar archivos del proyecto1 con una etiqueta
add_files_from_directory(m, "Projects/domino/Domino-main", as_base=True)

# Agregar archivos del proyecto2 con una etiqueta diferente
add_files_from_directory(m, "Projects/domino/Proyecto-Domino--master", as_base=False)

# Enviar los archivos a MOSS
url = m.send()

# Imprimir la URL del reporte generado por MOSS
print("Report URL: " + url)

# Opcional: descargar el reporte
# m.saveWebPage(url, "report.html")

# # Opcional: descargar los archivos de coincidencias del reporte
# mosspy.download_report(url, "report/", connections=8)
 
# Ejemplo de lectura y análisis básico de un archivo de coincidencias de MOSS

def read_moss_report(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def parse_moss_report(lines):
    results = []
    current_match = None
    for line in lines:
        line = line.strip()
        if line.startswith("==="):
            if current_match:
                results.append(current_match)
            current_match = {'file1_lines': [], 'file2_lines': []}
        elif line.startswith("File 1"):
            current_match['file1'] = line.split(":")[1].strip()
        elif line.startswith("File 2"):
            current_match['file2'] = line.split(":")[1].strip()
        elif line.startswith("Lines"):
            parts = line.split(":")
            current_match['file1_lines'].append(int(parts[1].strip()))
            current_match['file2_lines'].append(int(parts[2].strip()))
    if current_match:
        results.append(current_match)
    return results

def visualize_moss_results(results):
    for idx, match in enumerate(results, start=1):
        print(f"Match {idx}:")
        print(f"  File 1: {match['file1']}")
        print(f"  File 2: {match['file2']}")
        print("  Matched Lines:")
        for i in range(len(match['file1_lines'])):
            print(f"    File 1 Line {match['file1_lines'][i]} <-> File 2 Line {match['file2_lines'][i]}")

if __name__ == "__main__":
    # Ruta al archivo de coincidencias descargado de MOSS
    moss_report_file = 'report.txt'

    # Leer y parsear el archivo de coincidencias
    moss_lines = read_moss_report(moss_report_file)
    moss_results = parse_moss_report(moss_lines)

    # Visualizar los resultados
    visualize_moss_results(moss_results)
