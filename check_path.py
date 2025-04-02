"""檢查導入路徑"""
import os
import sys

print(f"✅ PYTHONPATH 環境變數：{os.environ.get("PYTHONPATH")}")

# 印出目前 sys.path（用來確認路徑優先順序）
print("\n✅ sys.path 路徑優先順序：")
for p in sys.path:
    print("   -", p)
