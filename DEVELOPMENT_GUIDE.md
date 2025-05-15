# 广东医学高级职称报名图片处理工具开发文档

## 1. 技术架构

### 1.1 系统架构图
```
[用户界面层] -> [业务逻辑层] -> [图像处理层] -> [文件IO层]
```

### 1.2 技术栈
- 编程语言: Python 3.9+
- 核心库: 
  - Pillow 9.0+ (图像处理)
  - OpenCV 4.5+ (可选，高级图像处理)
- 用户界面:
  - 命令行界面: argparse
  - GUI界面: Tkinter/PyQt (可选)
- 测试框架: pytest
- 打包工具: PyInstaller

## 2. 模块设计

### 2.1 核心模块
```python
.
├── main.py              # 程序入口
├── image_processor.py   # 图像处理核心逻辑
├── config.py            # 配置管理
└── utils.py             # 工具函数
```

### 2.2 图像处理模块(详细)
```python
class ImageProcessor:
    def __init__(self, config):
        self.config = config
    
    def load_image(self, path):
        """加载图像文件"""
    
    def convert_format(self, image, target_format='JPEG'):
        """转换图像格式"""
    
    def resize_image(self, image, max_size_kb=100):
        """调整图像大小"""
    
    def save_image(self, image, output_path):
        """保存图像文件"""
```

## 3. API说明

### 3.1 命令行接口
```bash
python main.py [input_path] [output_path] [options]

Options:
  --quality QUALITY    输出质量 (1-100)
  --max-size MAX_SIZE  最大文件大小(KB)
  --batch              批量处理模式
```

### 3.2 函数API
```python
def process_image(input_path, output_path, max_size=100, quality=85):
    """
    处理单张图片
    参数:
        input_path: 输入文件路径
        output_path: 输出文件路径
        max_size: 最大文件大小(KB)
        quality: 输出质量(1-100)
    """
```

## 4. 开发环境配置

### 4.1 安装依赖
```bash
pip install -r requirements.txt
```

### 4.2 requirements.txt
```
pillow>=9.0.0
opencv-python>=4.5.0  # 可选
pytest>=7.0.0
```

## 5. 测试方案

### 5.1 单元测试
```python
def test_image_compression():
    # 测试压缩功能
    test_image = create_test_image()
    processed = compress_image(test_image)
    assert processed.size <= 100 * 1024  # 100KB
```

### 5.2 测试目录结构
```
tests/
├── unit/
│   ├── test_processor.py
│   └── test_utils.py
└── integration/
    └── test_cli.py
```

## 6. 部署方案

### 6.1 打包为可执行文件
```bash
pyinstaller --onefile main.py
```

### 6.2 打包配置文件
```python
# setup.py
from setuptools import setup

setup(
    name='jpg-adjust-tool',
    version='1.0.0',
    install_requires=['pillow>=9.0.0'],
    entry_points={
        'console_scripts': [
            'jpg-adjust=jpg_adjust_tool.main:main'
        ]
    }
)
```

## 7. 开发规范

1. 代码风格: 遵循PEP8规范
2. 提交信息: 使用约定式提交(Conventional Commits)
3. 文档要求: 所有公共API必须包含docstring
4. 测试覆盖率: 保持≥80%的测试覆盖率

## 8. 路线图

- v1.0: 基础图片压缩功能
- v1.1: 增加批量处理功能
- v1.2: 添加GUI界面
- v2.0: 支持智能裁剪和优化