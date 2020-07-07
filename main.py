#   Bibliotecas construídas
#from menus.login        import *

#   Bibliotecas nativas
import  time;
import  os;

#   Limpa
os.system('cls');

#   Cria efeito de sistema inicialindo
print("\nIniciando sistema...\n");
for i in range(10, 0, -1):
    time.sleep(0.5);
    print(f"{i}...");

#   Requisita Login do usuário
login = str(input("Digite seu login:     "));
senha = str(input("Digite sua senha:     "));

#   Finalizando rotina
print("\nFinalizando sistema...\n");