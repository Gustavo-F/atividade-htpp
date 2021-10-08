import socket 
import threading 
   
USERNAME = 'gustavo'
PASSWORD = 'senhaforte'

def workerThread(s):
    while True: 
        msg = s.recv(1024)
        if not msg: break
        msg_split = msg.decode().split('=')
        password = msg_split[-1].strip()
        username = msg_split[-2].strip().split('&')[0]

        try:
            if password == PASSWORD and username == USERNAME:
                print('Usuário e Senha corretos')

                response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<html><body>Hello World</body></html>\n"
                print(f'Resposta:\n{response}')
                
                s.send(response.encode())
            else:
                print('Usuário ou Senha incorreto!')
        except:
            print('Erro ao responder.')
    s.close() 
  
def Main(): 
    host = "" 
    port = 2806

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_socket.bind((host, port)) 
    server_socket.listen() 
  
    print("Servidor inicializado na porta " + str(port))

    while True: 
        s, addr = server_socket.accept() 
        print('Cliente Conectado:', addr[0], ':', addr[1])  
        tw = threading.Thread(target=workerThread, args=[s])
        tw.start()

if __name__ == '__main__': 
    Main() 