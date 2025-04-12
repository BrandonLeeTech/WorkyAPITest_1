"""清除啟動後殘存的 edge 進程"""

import psutil

def cleanup_edge_processes():
    """檢查並終止所有與 Edge 和 WebDriver 相關的進程"""
    processes_to_kill = ['msedge.exe', 'msedgedriver.exe']  # 需要終止的進程名稱
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] in processes_to_kill:
            print(f"找到正在運行的進程 {proc.info['name']} (PID: {proc.pid})，正在終止...")
            try:
                proc.terminate()
                proc.wait(timeout=5)  # 等待進程結束
                print(f"進程 {proc.info['name']} (PID: {proc.pid}) 已終止。")
            except psutil.Error as e:
                print(f"無法終止進程 {proc.info['name']} (PID: {proc.pid}): {e}")
