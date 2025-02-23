import logging # Logs
import os # Variables de entorno
#import sys # Leer argumentos de la terminal
import argparse # Leer argumentos de la terminal (más avanzado)
from executor import Executor

logging.basicConfig(
    filename='dev.log',
    level=logging.INFO)
logging.info('Inicio de la ejecución')


#print(os.getenv('HOST'))
#print(f"Parametros: {sys.argv}")

# Leer esta llamada python3 deployment.py --script_name create_file --args "file_name=deploy.txt"
# Leer esta llamada python3 deployment.py --script_name install --args "file_name=SnakE version=2 pin=TR3S"

# Argumentos de la terminal
parse = argparse.ArgumentParser()

parse.add_argument('--script_name', type=str, help='Nombre del script a ejecutar')
parse.add_argument('--args', type=str, help='Argumento para el script');
args = parse.parse_args()

argumentos = []

#for x in args.args.split(' '):
#    argumentos.append(x.split('='))

argumentos = dict(item.split('=') for item in args.args.split(' '))
logging.info(f"Argumentos: {argumentos}")
print(argumentos)

#print(args)
#print(args.script_name)
#print(args.args)

# Ejecutar un script
#subprocess.run(f"bash ./scripts/{args.script_name}.sh", shell=True)
#subprocess.run(f"bash ./scripts/{args.script_name}.sh {args.args}", shell=True)

"""
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print(os.getenv('HOST'))
print(os.getenv('REMOTE_USER'))
print(os.getenv('PORT'))

try:
    client.connect(
        hostname=os.getenv('HOST'),
        username=os.getenv('REMOTE_USER'),
        port=os.getenv('PORT')
    )

    # Templates

    env = Environment(loader=FileSystemLoader('scripts'))
    template = env.get_template(f"{args.script_name}.sh")
    template_output = template.render(args.args)

    print(template_output)

    client.exec_command(template_output)

except Exception as e:
    print(f"Error: {e}")
finally:
    # Cerrar la conexión
    client.close()
"""
    
"""
logging.basicConfig(
    filename='dev.log',
    level=logging.INFO)
logging.info('This is an info message')
logging.error('This is an error message')
"""

executor = Executor(args.script_name, argumentos)
executor.execute()
logging.info('Fin de la ejecución')