""" 另開一個命令視窗 """

# pylint: disable=W0718
import os
import signal
import sys
import subprocess
import psutil


class ProcessManager:
    """開啟/關閉命令提示視窗，並執行命令"""
    def __init__(self):
        """初始化進程 PID"""
        self.pid = None  # 存儲啟動的終端進程 PID

    def open_console(self):
        """另開 `cmd.exe` 視窗運行 start_server.py, return PID"""
        if hasattr(sys, '_MEIPASS'):
            # 打包執行時：PyInstaller 會將所有檔案解壓到 sys._MEIPASS
            base_path = sys._MEIPASS
        else:
            # 開發環境：直接用當前檔案目錄往上一層找
            base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        script_path = os.path.join(base_path, 'start_server.py')
        cmd = f'python {script_path}'
        # cmd = ["python", "start_server.py"]

        if sys.platform == "win32":
            # process = subprocess.Popen(cmd)
            process = subprocess.Popen(
                ["cmd.exe", "/K", cmd],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            process = subprocess.Popen(["bash", "-c", cmd], shell=False)
        self.pid = process.pid
        print(f"啟動 socket server (PID: {self.pid})")
        return self.pid


    def close_console(self):
        """關閉該終端所有子進程"""
        if not self.pid:
            print("尚未啟動任何進程，無法關閉")
            return
        # 檢查 `PID` 是否仍然存在
        if not psutil.pid_exists(self.pid):
            print("進程已經結束，無需關閉 (PID: %s)", self.pid)
            return
        try:
            self._extracted_from_close_console()
        except Exception as e:
            print("關閉 console 時發生錯誤: %s", e)

    # 關閉主進程的邏輯 pylint: disable=no-member
    def _extracted_from_close_console(self):
        system = sys.platform  # 取得當前系統
        parent = psutil.Process(self.pid)
        # 取得所有子進程
        try:
            children = parent.children(recursive=True)
        except psutil.NoSuchProcess:
            print(f"主進程 (PID: {self.pid}) 已結束，無法獲取子進程")
            return
        # 先關閉子進程
        for child in children:
            try:
                if psutil.pid_exists(child.pid):
                    if system == "win32":
                        subprocess.run(f"taskkill /PID {child.pid} /F", shell=True, check=False)
                    else:
                        os.kill(child.pid, signal.SIGKILL)  # Linux 內改用 kill 指令
                print(f"已停止子進程 (PID: {child.pid})")
            except psutil.NoSuchProcess:
                print("子進程已經結束")
        # 再關閉主進程
        if psutil.pid_exists(self.pid):
            if system == "win32":
                subprocess.run(f"taskkill /PID {self.pid} /F", shell=True, check=False)
            else:
                os.kill(self.pid, signal.SIGKILL)  # Linux 內改用 kill 指令
            print(f"關閉 console (PID: {self.pid})")
        else:
            print("主進程已經結束")


if __name__ == "__main__":
    # 創建 ProcessManager
    import time
    process_manager = ProcessManager()
    process_manager.open_console()
    time.sleep(2)
    # process_manager.close_console()  # 結束該 console 及其子進程
