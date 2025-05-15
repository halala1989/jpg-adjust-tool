from PIL import Image
import io
import os

class ImageProcessor:
    def __init__(self, quality=85, max_size_kb=100):
        """
        初始化图像处理器
        :param quality: 输出质量 (1-100)
        :param max_size_kb: 最大文件大小(KB)
        """
        self.quality = quality
        self.max_size = max_size_kb * 1024  # 转换为字节

    def process_image(self, input_path, output_path):
        """
        处理单张图片
        :param input_path: 输入文件路径
        :param output_path: 输出文件路径
        :return: 处理结果 (成功/失败)
        """
        try:
            # 加载图像
            img = self._load_image(input_path)
            if img is None:
                return False

            # 转换格式为JPEG
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # 调整图像质量以满足大小限制
            img = self._adjust_image_size(img)

            # 保存图像
            img.save(output_path, 'JPEG', quality=self.quality)
            return True

        except Exception as e:
            print(f"处理图像时出错: {str(e)}")
            return False

    def _load_image(self, path):
        """加载图像文件"""
        try:
            return Image.open(path)
        except IOError:
            print(f"无法加载图像文件: {path}")
            return None

    def _adjust_image_size(self, img):
        """调整图像大小以满足文件大小限制"""
        output = io.BytesIO()
        img.save(output, format='JPEG', quality=self.quality)
        
        while output.getbuffer().nbytes > self.max_size and self.quality > 10:
            self.quality -= 5
            output = io.BytesIO()
            img.save(output, format='JPEG', quality=self.quality)
        
        output.seek(0)
        return Image.open(output)