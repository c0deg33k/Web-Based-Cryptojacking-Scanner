import socket,sys,_thread,traceback, ssl, requests

 
def main():
    global listen_port, buffer_size, max_conn
    try:
        listen_port = int(input("Enter a listening port: "))
    except KeyboardInterrupt:
        sys.exit (0)
        
    max_conn = 10000
    buffer_size = 10000
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("", listen_port))
        s.listen(max_conn)
        print("[*] Intializing socket. Done.")
        print("[*] Socket binded successfully...")
        print("[*] Server started successfully [{}]".format(listen_port))
    except Exception as e:
        print(e)
        sys.exit(2)

    while True:
        try:
            conn,addr = s.accept()
            print("This is conn", conn)
            data = conn. recv(buffer_size)
            print("This is data", data)
            _thread.start_new_thread(conn_string,(conn, data, addr))
        except KeyboardInterrupt:
            s.close()
            print("\n[*] Shutting down...")
            sys.exit(1)
    s.close()

def conn_string(conn, data, addr):
    try: 
        print("This is the address", addr)
        first_line = data.decode('latin-1').split("\n")[0]
        print("This is the first line",first_line)
        url = first_line.split(" ")[1]
        
        http_pos = url.find("://")
        if http_pos == -1:
            temp = url
        else:
            temp = url[(http_pos + 3):]
            
        port_pos = temp.find(":")
        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos = len(temp)
        webserver = ""
        port = -1
        if port_pos == -1 or webserver_pos < port_pos:
            port = 80
            webserver = temp[:webserver_pos]
        else:
            port = int(temp[(port_pos + 1):][:webserver_pos - port_pos -1])
            webserver = temp[:port_pos]

        print("This is the webserver", webserver)
        proxy_server(webserver,port,conn,data,addr)
    except Exception as e:
        print(e)
        traceback.print_exc()

def blacklist(data):
    def parse(self, response):
        #print()
        keywords = ['_client.start', 'coinhive.min.js', 'CoinHive.Anonymous', 'load.jsecoin.com', 'CRLT.Anonymous(', 'WMP.Anonymous(', 'bmst.pw', 'wp-monero-miner', 'nerohut.com/srv', 'webmr.js', 'cdn.minescripts.info', 'deepMiner.Anonymous', 'monerise_payment_address', 'webmine.cz', 'CoinNebula', 'authedmine.min.js', 'simple-ui.min.js', 'authedmine.eu/lib/1.js']
        
            js_script = str(script)
            for keyword in keywords:
                if keyword in js_script:
                    yield {'site': str(response).split(' ')[-1], 'script_found': script, 'keyword': keyword}
                else:
                    pass
 
def proxy_server(webserver, port, conn, data, addr):
    print("{} {} {} {}".format(webserver, port, conn, addr))
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((webserver, port))
        s.sendall(data)
        while 1:
            reply = s.recv(buffer_size)
            print("This is the reply", reply) #implement requests lib
            
            if len(reply) > 0:
                conn.send(reply)
                print("[*] Request sent: {} > {}".format(addr[0],webserver))
            else:
                #response = requests.get('http://' + webserver)
                #print('this is the content', response)
                #conn.send(response.content)
                print("[*] empty Request sent: {} > {}".format(addr[0],webserver))
                break        
        
        s.close()
        conn.close()
        
    except Exception as e:
        print(e)
        traceback.print_exc()
        s.close()
        conn.close()
        sys.exit(1)

if __name__ == "__main__":
    main()
