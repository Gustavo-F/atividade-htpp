import socket 
import threading 
   
USERNAME = 'ifsc'
PASSWORD = 'aluno'

def workerThread(s):
    while True: 
        msg = s.recv(1024)
        if not msg: break
        msg_split = msg.decode().split('=')
        password = msg_split[-1].strip()
        username = msg_split[-2].strip().split('&')[0]

        try:
            if password == PASSWORD and username == USERNAME:
                try:
                    with open('success.html', 'r') as file:
                        html_content = file.read().replace('\n', '')
                except:
                    html_content = '<h1>Could not load HTML page.</h1>'
                
                response = f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n{html_content}\n"

            else:
                try:
                    with open('index.html', 'r') as file:
                        html_content = file.read().replace('\n', '')
                except:
                    html_content = '<h1>Could not load HTML page.</h1>'

                response = f"HTTP/1.1 401 Unauthorized\nContent-Type: text/html\n\n{html_content}\n"
                
            s.send(response.encode())  
        except:
            print('Erro ao responder.')
        
        s.shutdown(socket.SHUT_RDWR)
        print('Conexão encarrada')
  
def Main(): 
    host = "127.0.0.1" 
    port = 2550

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