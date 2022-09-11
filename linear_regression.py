from google.colab import drive
drive.mount('/content/drive')

# Kiểm tra CUDA để cài phiên bản MXNet phù hợp với GPU.
!nvcc --version
