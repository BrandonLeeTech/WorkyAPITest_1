""" 測試圖片轉 base64 """

import base64
from pathlib import Path

def image_to_base64(file_name) -> str:
    """將圖片轉為 base64 字串"""
    base_dir = Path(__file__).resolve().parents[1]
    image_file = base_dir / 'img' / file_name
    with open(image_file, "rb") as image:
        return base64.b64encode(image.read()).decode("utf-8")

if __name__ == "__main__":
    base64_str = image_to_base64(file_name="worky.png")
    print(base64_str)
