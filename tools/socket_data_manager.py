""" 用 socket 傳遞數據 """

import socket
from multiprocessing import Manager  # 多進程共享數據
from utils.load_json import get_config

class SocketDataManager:
    """負責處理數據傳遞"""

    def __init__(self):
        self.host = "localhost"
        self.port = int(get_config("SOCKET_PORT"))
        self.manager = Manager()
        self.data_store = self.manager.dict()  # 用字典管理

    def set_data(self, tag, data):
        """Client端-發送 data 跟相對應的 tag"""
        command = f"SET_DATA {tag} {data}"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.sendall(command.encode("utf-8"))
        print(f"儲存 [{tag}]:{data}")

    def get_data(self, tag):
        """Client端-獲取對應 tag 的 data"""
        command = f"GET_DATA {tag}"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.sendall(command.encode("utf-8"))
            response = client_socket.recv(1024).decode("utf-8")
            print(f"獲取 [{tag}] => {response}")
            return response

    def handle_set_data(self, data_store, tag, data):
        """伺服器端-處理 SET_DATA 請求"""
        data_store[tag] = data
        print(f"[SET] : {tag} => {data}")
        return f"{data}"

    def handle_get_data(self, data_store, tag):
        """伺服器端-處理 GET_DATA 請求"""
        data = data_store.get(tag)
        print(f"[GET] : {tag}")
        return f"{data}"

    def parse_command(self, command):
        """伺服器端-解析接收到的命令"""
        parts = command.split(" ", 2)  # 最多分為 3 部分
        if len(parts) < 2:
            return "ERROR", None, None
        action = parts[0]
        tag = parts[1]
        data = parts[2] if len(parts) == 3 else None
        return action, tag, data
