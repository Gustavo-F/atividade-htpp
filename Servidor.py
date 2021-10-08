import socket 
import threading 
   
USERNAME = 'gustavo'
PASSWORD = 'senhaforte'

def workerThread(s):
    while True: 
        msg = s.recv(1024)
        if not msg: break
        print('O cliente enviou: ', msg.decode().split('username'))
        msg = msg[::-1] #Inverte a String
        try:
           s.send(msg)
        except:
            print('Erro ao responder.')
    s.close() 
  
def Main(): 
    host = "" 
    port = 2803

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