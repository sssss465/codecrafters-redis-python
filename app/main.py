# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    (conn, address) = server_socket.accept() # wait for client
    while True: 
        try:
            data = conn.recv(1024) # read the first line
            cmd = data.decode('unicode_escape').split('\r\n')
            cur = 0
            ans = b"+"
            ans += respond("ping")
            if len(ans) > 1:
                ans += b"\r\n"
                conn.send(ans)
            RESPTYPE_FIRSTBYTE = {
                'simple': b'+',
                'error': b'-',
                'integer': b':',
                'bulk': b'$',
                'array': b'*',

            }
            
        except:
            conn.close()

def respond(cmd):
    if "ping" in cmd:
        return (b"PONG")
    else:
        return -1


if __name__ == "__main__":
    main()
