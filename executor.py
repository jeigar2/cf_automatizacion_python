import logging # Logs
import os # Variables de entorno
import argparse # Leer argumentos de la terminal (más avanzado)
import subprocess # Ejecutar comandos en la terminal
import paramiko # Conexión SSH
from dotenv import load_dotenv # Cargar variables de entorno desde un archivo .env
from jinja2 import Environment, FileSystemLoader # Templates

class Executor:
    def __init__(self, script_name, script_args):
        self.script_name = script_name
        self.script_args = script_args
        logging.basicConfig(
            filename='dev.log',
            level=logging.INFO, append=True)        

    def execute(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        logging.info('Conexion SSH')
        logging.info('cargando variables de entorno fichero .env')
        load_dotenv()

        try:
            client.connect(
                hostname=os.getenv('HOST'),
                username=os.getenv('REMOTE_USER'),
                port=os.getenv('PORT')
            )
            logging.info('Conexion establecida')
            template_output = self.get_template()
            logging.info(f"Template: {template_output}")
            client.exec_command(template_output)
            logging.info('Comando ejecutado')

        except Exception as e:
            print(f"Error: {e}")
            logging.error(f"Error: {e}")
        finally:
            # Cerrar la conexión
            client.close
            logging.info('Conexion cerrada')

    def get_template(self):
        env = Environment(loader=FileSystemLoader('scripts'))
        template = env.get_template(f"{self.script_name}.sh")
        template_output = template.render(self.script_args)

        return template_output