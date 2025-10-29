import os
import pandas as pd
from fpdf import FPDF
from fpdf.enums import XPos, YPos

DATA_FILE = "banking-dataset.csv"

# -- Đọc dữ liệu từ file CSV --

# Đọc dữ liệu từ file CSV trong thư mục "data"
df = pd.read_csv(f"./data/{DATA_FILE}", encoding="utf-8")
# Xóa các dòng (row) có giá trị bị thiếu (NaN / trống), lỗi format
df = df.dropna(subset=["Date", "Category", "Debit Amount", "Credit Amount", "Closing Balance"])

# CHuyển đổi dữ liệu trong các cột này sang dạng "float"
df["Debit Amount"] = df["Debit Amount"].astype(float)
df["Credit Amount"] = df["Credit Amount"].astype(float)
df["Closing Balance"] = df["Closing Balance"].astype(float)

# Tính 
# tổng chi tiêu và thu nhập
total_debit = df["Debit Amount"].sum()
total_credit = df["Credit Amount"].sum()
closing_balance = df["Closing Balance"].iloc[-1]

# giao dịch hằng ngày
daily_summary = (
    df.groupby("Date")[["Debit Amount", "Credit Amount"]].sum().reset_index()
)

# chi tiêu theo doanh mục
category_summary = (
    df.groupby("Category")["Debit Amount"]
    .sum()
    .reset_index()
    .sort_values(by="Debit Amount", ascending=False)
)

# -- Tạo PDF --

# Khởi tạo PDF & Thêm 1 trang A4 trắng
pdf = FPDF()
pdf.add_page()

# Dùng font "Helvetica", kiểu đậm (Bold), cỡ 16pt
pdf.set_font("Helvetica", "B", 16)

# Tạo tiêu đề của cả PDF với tên "Banking Statement Summary"
pdf.cell(0, 10, "Banking Statement Summary", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

# In ra các giá trị tổng kết
pdf.set_font("Helvetica", size=12)
pdf.cell(0, 10, f"Total Debit: {total_debit:.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(0, 10, f"Total Credit: {total_credit:.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(0, 10, f"Total Closing Balance: {closing_balance:.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.ln(10)  # Xuống dòng

# Tiêu đề "Spending by Category"
pdf.set_font("Helvetica", "B", 14)
pdf.cell(0, 10, "Spending by Category", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

# In từng dòng danh mục chi tiêu
pdf.set_font("Helvetica", size=12)
for _, row in category_summary.iterrows():
    pdf.cell(0, 10, f"{row['Category']}: {row['Debit Amount']:.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Lưu file vào trong thư mục "output"
output_dir = "./output"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "banking_report.pdf")
pdf.output(output_path)

print(f"✅ Report generated: {output_path}")
