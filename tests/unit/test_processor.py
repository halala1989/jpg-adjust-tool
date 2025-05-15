import pytest
import os
import tempfile
from PIL import Image
from image_processor import ImageProcessor

@pytest.fixture
def sample_image():
    """创建一个测试用的临时图像文件"""
    img = Image.new('RGB', (800, 600), color='red')
    tmp = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
    img.save(tmp.name, 'JPEG', quality=95)
    yield tmp.name
    os.unlink(tmp.name)

@pytest.fixture
def processor():
    """创建一个图像处理器实例"""
    return ImageProcessor(quality=85, max_size_kb=100)

def test_process_image_success(processor, sample_image):
    """测试图像处理成功"""
    output = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False).name
    try:
        result = processor.process_image(sample_image, output)
        assert result is True
        assert os.path.exists(output)
        assert os.path.getsize(output) <= 100 * 1024  # 检查文件大小
    finally:
        if os.path.exists(output):
            os.unlink(output)

def test_process_image_invalid_input(processor):
    """测试无效输入文件"""
    output = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False).name
    try:
        result = processor.process_image('nonexistent.jpg', output)
        assert result is False
    finally:
        if os.path.exists(output):
            os.unlink(output)

def test_adjust_image_size(processor, sample_image):
    """测试图像大小调整"""
    img = Image.open(sample_image)
    adjusted = processor._adjust_image_size(img)
    assert adjusted is not None
    assert adjusted.size == img.size  # 尺寸应保持不变