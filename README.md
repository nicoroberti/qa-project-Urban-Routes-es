# Proyecto Urban Routes Page

Nicolas Roberti, Grupo 23, Sprint 8

# Descripción del proyecto

En este proyecto se evalúa el funcionamiento de la aplicación Urban Routes y el flujo de trabajo que sigue hasta la solicitud del taxi. Se ha trabajado según la lista de requisitos, eligiendo la tarifa "Comfort" y algunos adicionales incluidos con esta tarifa.
# Tecnologías utilizadas en la automatización de pruebas

- PyCharm Community Edition 2024.3.2 
- Python: 3.13 
- Pytest: 8.3.4
- Librerias de Python: requests 2.32.3
- GitHub

# Instalación
Pasos para instalar y ejecutar el proyecto localmente:

1. Clonar este repositorio:
    ```bash
    git clone git@github.com:nicoroberti/qa-project-Urban-Routes-es.git
    ```

2. Navegar a la carpeta del proyecto:
    ```bash
    cd qa-project-Urban-Routes-es
    ```

3. Trabajar localmente (si usas PyCharm):
    
    Abrir el proyecto "qa-project-Urban-Grocers-app-es" desde la rama "main"


4. Instalar librerias "pytest" y "request":
* Ir a Python Packages
* Digitar el nombre de la librería en "search"
* Seleccionar la versión mas reciente
* Hacer clic en instalar

# Pruebas

Para ejecutar las pruebas realizamos los siguientes pasos:

1. Ir a la terminal 
2. Acceder a la ruta del proyecto con el comando cd
3. Posterior a esto ejecutar 'pytest'
4. Si requiere hacer pruebas especificas 'pytest TestUrbanRoutes.py'

Las pruebas realizadas son las siguientes:

1. def test_set_route: Establecer la ruta
2. def test_click_order_taxi_button: Probar la operatividad del boton "Pedir Taxi"
3. def test_select_comfort_tariff: Seleccionar la tarifa "Comfort"
4. def test_enter_phone_number: Ingresar numero de telefono
5. def test_set_phone_number: Establecer numero de telefono, validando el codigo SMS 
6. def test_set_payment_method: Establecer método de pago "Tarjeta"
7. def test_send_message_to_driver: Enviar un mensaje especifico al conductor
8. def test_order_blanket_and_kerchief: Ordenar Manta y pañuelos
9. def test_order_2_ice_creams: Ordernar 2 helados
10. def test_car_search_modal_appear: Verificar que el Modal solicitando vehiculo esté disponible

# Guardar cambios y actualizar proyecto

1. Efecturar los cambios
2. Realizar un commit de esos cambios
3. Hacer 'push' a la rama