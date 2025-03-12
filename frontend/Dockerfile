# Sử dụng Nginx làm base image
FROM nginx:latest

# Sao chép file cấu hình Nginx vào container
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Sao chép file HTML vào thư mục mặc định của Nginx
COPY html /usr/share/nginx/html

# Mở cổng 80
EXPOSE 80

# Chạy Nginx
CMD ["nginx", "-g", "daemon off;"]
