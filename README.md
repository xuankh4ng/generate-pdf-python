# Cách dùng
***Clone dự án về***

## Cài đặt các thư viện cần thiết
1. Tạo và kích hoạt môi trường ảo Python:
- Khởi tạo:
```shell
python -m venv .venv
```
- Kích hoạt:
  - Powershell:
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
## Chạy chương trình
```shell
python main.py
```

> [!important]
> Chỉ chạy chương trình khi đã kích hoạt môi trường ảo và cài đặt thư viện trong môi trường ảo đó.

# Phát triển tính năng
- Chuyển sang nhánh **feature** và làm trên đó.
```shell
git checkout feature
```
- Khi xong thì cứ push lên repo này, còn lại để tui kiểm tra rồi **merge** vào nhánh main.
