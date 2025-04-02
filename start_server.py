""" 測試前要先啟動 server """

import time
import socket
import threading
from tools.socket_data_manager import SocketDataManager


# pylint: disable=broad-except
class Server:
    """管理測試需要傳遞的數據"""

    def __init__(self):
        self.socket_manager = SocketDataManager()
        self.host = self.socket_manager.host
        self.port = self.socket_manager.port

    def server_task(self):
        """定義子進程"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:  # 創建了一個基於 TCP 的伺服器
            server_socket.bind((self.host, self.port))
            server_socket.listen()  # 監聽模式
            print(f"監聽地址 {self.host}:{self.port}")
            print("--------------------------------------")
            while True:
                try:
                    conn, _ = server_socket.accept()  # 接收 Client 端的連線
                    with conn:
                        data = conn.recv(1024)
                        if not data:
                            continue
                        command = data.decode("utf-8")
                        action, tag, data = self.socket_manager.parse_command(command)
                        # Command 處理
                        if action == "SET_DATA":
                            response = self.socket_manager.handle_set_data(
                                self.socket_manager.data_store, tag, data
                            )
                        elif action == "GET_DATA":
                            response = self.socket_manager.handle_get_data(
                                self.socket_manager.data_store, tag
                            )
                        else:
                            response = "Command 錯誤"
                        conn.sendall(response.encode("utf-8"))
                except Exception as e:
                    print(f"伺服器發生錯誤: {e}")

    def start(self):
        """測試前啟動 server"""
        server_thread = threading.Thread(target=self.server_task, daemon=True)

        server_thread.start()
        return server_thread


if __name__ == "__main__":
    server = Server()
    server.start()

    try:
        print("伺服器已啟動，按 Ctrl+C 結束...")
        while True:
            time.sleep(1)  # 保持運行
    except KeyboardInterrupt:
        print("伺服器關閉")
