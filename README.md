#Instrucciones del proceso de automatización

#Introduccion
-El objetivo de este proyecto es de automatizar pruebas en el sitio web "https://www.xtrim.com.ec/" usando python y selenium. 

#Requisitos
-Python
-Navegador de preferencia (Google Chrome)
-ChromeDriver Compatible

#Instalacion
- Crear y activar un entorno virtual para mantener las dependencias aisladas (Usando CMD). Usando python -m venv env, activando el ambiente .\env\Scripts\activate  o usar venv\Scripts\activate y desactivando deactivate
- Instalar dependencias usando pip, instalando selenium y pytest. (requirements.txt)
- Instalar ChromeDriver compatible con la versión del navegador que se esté usando, en este caso Google Chrome.

#Ejecucion de pruebas
- Este pequeño proyecto contiene 3 pruebas automatizadas. Para ejecutarlas utilizar el siguiente comando usando pytest:

-pytest tests/test_login.py -v
-pytest tests/test_formContacto.py -v
-pytest tests/test_pagarServicio.py -v
-pytest tests/test_planZapping.py -v


#Especificaciones de los test:
-test_login: Prueba de Ingreso al sistema de Xtrim.
-test_FormContacto: Formulario de contacto en la sección “Te llamamos”: Contáctanos : Xtrim



