# Sử dụng Python image
FROM python:3.10

# Đặt thư mục làm việc
WORKDIR /app

# Copy mã nguồn vào container
COPY route.py /app/
COPY requirements.txt /app/

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Expose cổng 8000
EXPOSE 8000

# Chạy API khi container khởi động
CMD ["uvicorn", "route:app", "--host", "0.0.0.0", "--port", "8000"]
