import pytest
import os
import subprocess
import tempfile
from PIL import Image

@pytest.fixture
def sample_image():
    """创建一个测试用的临时图像文件"""
    img = Image.new('RGB', (800, 600), color='blue')
    tmp = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
    img.save(tmp.name, 'JPEG', quality=95)
    yield tmp.name
    os.unlink(tmp.name)

@pytest.fixture
def output_file():
    """创建一个临时输出文件路径"""
    tmp = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
    path = tmp.name
    tmp.close()  # 立即关闭，让测试函数使用
    yield path
    if os.path.exists(path):
        os.unlink(path)

def test_cli_single_file(sample_image, output_file):
    """测试命令行单文件处理"""
    # 删除可能存在的输出文件
    if os.path.exists(output_file):
        os.unlink(output_file)
    
    # 运行命令行程序
    cmd = f"python main.py {sample_image} {output_file}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    # 验证结果
    assert result.returncode == 0
    assert os.path.exists(output_file)
    assert "处理完成" in result.stdout
    assert os.path.getsize(output_file) <= 100 * 1024  # 检查文件大小

def test_cli_batch_mode(tmp_path, sample_image):
    """测试命令行批量处理模式"""
    # 准备测试目录和文件
    input_dir = tmp_path / "input"
    input_dir.mkdir()
    output_dir = tmp_path / "output"
    
    # 创建多个测试文件
    test_files = []
    for i in range(3):
        file_path = input_dir / f"test_{i}.jpg"
        img = Image.new('RGB', (800, 600), color=(i*50, i*50, i*50))
        img.save(file_path, 'JPEG', quality=95)
        test_files.append(file_path)
    
    # 运行命令行程序
    cmd = f"python main.py {input_dir} {output_dir} --batch"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    # 验证结果
    assert result.returncode == 0
    assert "批量处理完成" in result.stdout
    assert os.path.exists(output_dir)
    
    # 检查输出文件
    output_files = list(os.listdir(output_dir))
    assert len(output_files) == 3
    for file in output_files:
        assert os.path.getsize(os.path.join(output_dir, file)) <= 100 * 1024