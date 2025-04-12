""" 用 socket 傳遞數據 """

import os
import socket
import json
import logging
from utils.load_json import get_config

log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.log")
print(f"Log will write to: {log_path}")

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    encoding="utf-8"
)


class SocketDataManager:
    """負責處理數據傳遞"""

    def __init__(self, host="localhost"):
        self.host = host
        self.port = int(get_config("SOCKET_PORT"))
        self.data_store = {}

    def set_data(self, tag, data):
        """Client端-發送 data 跟相對應的 tag"""
        command = {"action": "SET_DATA", "tag": tag, "data": data}
        command_str = json.dumps(command, ensure_ascii=False)  # 確保不轉義非 ASCII 字符
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.settimeout(5)
                client_socket.connect((self.host, self.port))
                client_socket.sendall(command_str.encode("utf-8"))
                logging.info(f"儲存 [{tag}]:{data}")
        except ConnectionRefusedError as e:
            logging.error(f"無法連接到伺服器 {self.host}:{self.port}: {e}")
            raise RuntimeError(f"無法連接到伺服器 {self.host}:{self.port}: {e}") from e
        except socket.timeout as e:
            logging.error(f"連接超時: {e}")
            raise RuntimeError(f"連接超時: {e}") from e
        except socket.error as e:
            logging.error(f"Socket 錯誤: {e}")
            raise RuntimeError(f"Socket 錯誤: {e}") from e

    def get_data(self, tag):
        """Client端-獲取對應 tag 的 data"""
        command = {"action": "GET_DATA", "tag": tag}
        command_str = json.dumps(command, ensure_ascii=False)
        logging.info(f"送出指令: {command_str}")

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.settimeout(5)
                client_socket.connect((self.host, self.port))
                client_socket.sendall(command_str.encode("utf-8"))
                response = client_socket.recv(1024).decode("utf-8")
                logging.info(f"獲取 [{tag}] => {response}")
                if response == "None":
                    return None
                return response
        except ConnectionRefusedError as e:
            logging.error(f"無法連接到伺服器 {self.host}:{self.port}: {e}")
            raise RuntimeError(f"無法連接到伺服器 {self.host}:{self.port}: {e}") from e
        except socket.timeout as e:
            logging.error(f"連接超時: {e}")
            raise RuntimeError(f"連接超時: {e}") from e
        except socket.error as e:
            logging.error(f"Socket 錯誤: {e}")
            raise RuntimeError(f"Socket 錯誤: {e}") from e

    def handle_set_data(self, data_store, tag, data):
        """伺服器端-處理 SET_DATA 請求"""
        data_store[tag] = data
        logging.info(f"[SET] : {tag} => {data}")
        return f"{data}"

    def handle_get_data(self, data_store, tag):
        """伺服器端-處理 GET_DATA 請求"""
        data = data_store.get(tag)
        logging.info(f"[GET] : {tag}")
        return f"{data}"

    def parse_command(self, command):
        """伺服器端-解析接收到的命令"""
        try:
            cmd = json.loads(command)
            action = cmd.get("action")
            tag = cmd.get("tag")
            data = cmd.get("data")
            return action, tag, data
        except json.JSONDecodeError:
            logging.error("解析命令失敗: 無效的 JSON 格式")
            return "ERROR", None, None
