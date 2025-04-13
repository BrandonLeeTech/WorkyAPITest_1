"""清除啟動後殘存的 edge 進程"""
import psutil
import time

def cleanup_edge_processes():
    """清除所有 Edge 及其 WebDriver 的殘留進程"""
    processes_to_kill = ['msedge.exe', 'msedgedriver.exe']
    killed_any = False

    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            name = proc.info['name'] or ''
            if name.lower() in processes_to_kill:
                print(f"🧹 發現 Edge 相關進程：{name} (PID: {proc.pid})，嘗試終止中...")
                proc.terminate()
                try:
                    proc.wait(timeout=3)
                    print(f"✅ 已終止 {name} (PID: {proc.pid})")
                    killed_any = True
                except psutil.TimeoutExpired:
                    print(f"⚠️ 無法在預期時間內終止 {name}，強制殺掉")
                    proc.kill()
                    killed_any = True
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            print(f"⚠️ 無法終止進程：{e}")

    if not killed_any:
        print("✅ 沒有殘留的 Edge 或 WebDriver 進程")

    time.sleep(1)  # 等待一下，確保資源釋放乾淨
