import socket

sk = socket.socket()
sk.bind(("127.0.0.1",8080))
sk.listen(5)

while True:
    conn, address = sk.accept()
    conn.sendall(bytes("欢迎光临我爱我家", encoding="utf-8"))
    size = conn.recv(1024)
    size_str = str(size, encoding="utf-8")
    file_size = int(size_str)
    conn.sendall(bytes("开始传送", encoding="utf-8"))
    has_size = 0

    f = open("db_new.jpg", "wb")
    while True:
        if file_size == has_size:
            break
        date = conn.recv(1024)
        f.write(date)
        has_size += len(date)
    f.close()

import pickle
pickle.load(encoding='utf-8')