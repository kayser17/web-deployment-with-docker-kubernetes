import os
import subprocess
import re
import sys

# Paso 1: Establecer la variable de entorno
def set_group_number():
    """Establece la variable de entorno GRUP_NUM a 29"""
    os.environ["GROUP_NUM"] = "29"
    print("Variable de entorno GROUP_NUM establecida a:", os.environ["GROUP_NUM"])

# Paso 2: Modificar el título en productpage.html
def modify_productpage_html():
    """Modifica el archivo productpage.html para cambiar el título con la variable {{group_num}}"""
    filepath = 'bookinfo/src/productpage/templates/productpage.html'
    with open(filepath, 'r') as file:
        content = file.read()
    
    # Cambiar el contenido entre {% block title %} y {% endblock %}
    if "{% block title %}" in content:
        content = content.replace(
            "{% block title %}Simple Bookstore App {% endblock %}",
            "{% block title %}Simple Bookstore App - Group {{group_num}}{% endblock %}"
        )
    else:
        print("Advertencia: No se encontró el bloque de título esperado en productpage.html")
    
    with open(filepath, 'w') as file:
        file.write(content)
    
    print("productpage.html modificado exitosamente.")

# Paso 3: Modificar productpage_monolith.py para añadir la variable de entorno
def modify_productpage_monolith():
    """Modifica productpage_monolith.py para pasar la variable de entorno GROUP_NUM"""
    filepath = 'bookinfo/src/productpage/productpage_monolith.py'
    with open(filepath, 'r') as file:
        content = file.read()
    
    # Buscar el bloque de render_template y añadir grupo_numero
    render_call = """return render_template(
        'productpage.html',
        detailsStatus=detailsStatus,
        reviewsStatus=200,
        product=product,
        details=details,
        reviews={"R1":"OK"},
        user=user)"""
    
    modified_render_call = """return render_template(
        'productpage.html',
        detailsStatus=detailsStatus,
        reviewsStatus=200,
        product=product,
        details=details,
        reviews={"R1":"OK"},
        user=user,
        group_num=os.getenv('GROUP_NUM', 'Unknown Group'))"""

    if render_call in content:
        content = content.replace(render_call, modified_render_call)
    else:
        print("Advertencia: No se encontró el render_template esperado en productpage_monolith.py")
    
    with open(filepath, 'w') as file:
        file.write(content)
    
    print("productpage_monolith.py modificado exitosamente.")

# Paso 4: Modificar requirements.txt
def modify_requirements():
    """Modifica el archivo requirements.txt para actualizar la versión de requests y json2html"""
    filepath = 'bookinfo/src/productpage/requirements.txt'
    with open(filepath, 'r') as file:
        lines = file.readlines()
    
    with open(filepath, 'w') as file:
        for line in lines:
            if line.startswith("requests=="):
                file.write("requests\n")  # Cambiar a la versión deseada
            elif line.startswith("json2html=="):
                file.write("json2html==1.3.0\n")  # Cambiar a la versión 1.3.0
            else:
                file.write(line)
    
    print("requirements.txt modificado exitosamente.")

# Paso 5: Instalar dependencias de Python
def install_requirements():
    """Instala las dependencias desde requirements.txt"""
    print("Instalando dependencias...")
    subprocess.run(["pip", "install", "-r", "bookinfo/src/productpage/requirements.txt"], check=True)

# Paso 6: Obtener la IP pública desde eth0
def get_public_ip():
    """Obtiene la IP pública de la interfaz eth0 usando ifconfig"""
    result = subprocess.run(["ifconfig"], capture_output=True, text=True)
    match = re.search(r"eth0:.*?inet (\d+\.\d+\.\d+\.\d+)", result.stdout, re.DOTALL)
    if match:
        return match.group(1)
    else:
        print("No se pudo encontrar la IP pública.")
        return "127.0.0.1"

# Paso 7: Ejecutar la aplicación con un puerto dinámico
def run_application(port):
    """Ejecuta la aplicación con el número de grupo y el puerto dinámico"""
    os.environ["PORT"] = str(port)  
    print(f"Ejecutando la aplicación en el puerto {port}...")
    process = subprocess.Popen(
        ["python3", "bookinfo/src/productpage/productpage_monolith.py", str(port)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(f"La aplicación se está ejecutando en el puerto {port}.")
    return process

# Paso 8: Imprimir el mensaje de acceso
def print_access_message(port):
    """Imprime la URL para acceder a la aplicación"""
    public_ip = get_public_ip()
    print(f"\nAccede a la aplicación en los siguientes enlaces:")
    print(f"Desde localhost: http://localhost:{port}/productpage")
    print(f"Desde la IP pública: http://{public_ip}:{port}/productpage")

# Ejecutar todo
def setup_application(port=9090):
    set_group_number()
    modify_productpage_html()
    modify_productpage_monolith()
    modify_requirements()
    install_requirements()
    process = run_application(port)
    print_access_message(port)
    try:
        process.communicate()  
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario.")
        process.terminate()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 9090
    setup_application(port)
