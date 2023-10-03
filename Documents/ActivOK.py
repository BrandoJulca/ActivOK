import subprocess
import ctypes

def run_as_admin(command):
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            # El script ya se está ejecutando con privilegios de administrador, ejecuta el comando
            subprocess.run(command, check=True, shell=True)
        else:
            # Si no se están ejecutando como administrador, solicita elevación
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", command, None, 1)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

# Comando para instalar la clave de producto
command_install_key = 'slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX'

# Comando para configurar el servidor KMS
command_configure_kms = 'slmgr /skms kms.digiboy.ir'

# Comando para activar Windows
command_activate = 'slmgr /ato'

# Ejecutar los comandos uno por uno con privilegios de administrador
if __name__ == "__main__":
    run_as_admin(command_install_key)
    run_as_admin(command_configure_kms)
    run_as_admin(command_activate)
    print("Proceso de activación completado con éxito. | De nada, </BranDev>.")

#python -m PyInstaller --onefile --icon="icon.ico" Activ84u.py