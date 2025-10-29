# Cách dùng
***Clone dự án về***

## Cài đặt các thư viện cần thiết
1. Tạo và kích hoạt môi trường ảo Python:
- Khởi tạo:
```shell
python -m venv .venv
```
- Kích hoạt:
  - PowerShell:
  ```shell
  .venv\Scripts\activate
  ```
  - Bash:
  ```shell
  source .venv/Scripts/activate
  ```
  
2. Cài tất cả thư viện:
```shell
pip install -r requirement.txt
```
> [!important]
> Chỉ nên bắt đầu cài thư viện sau khi đã kích hoạt môi trường ảo Python.

## Chạy chương trình
```shell
python main.py
```

# Phát triển tính năng
- Chuyển sang ***nhánh feature*** và làm trên đó.
```shell
git checkout feature
```
- Khi xong thì cứ push nhánh ***feature*** này lên repo, còn lại để tui kiểm tra rồi ***merge vào nhánh main***.
