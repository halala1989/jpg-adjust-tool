import os
import imghdr

def validate_image_file(file_path):
    """
    验证文件是否为支持的图像格式
    :param file_path: 文件路径
    :return: 是否是有效图像文件
    """
    if not os.path.isfile(file_path):
        return False
    
    # 检查文件扩展名
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in ('.jpg', '.jpeg', '.png', '.bmp'):
        return False
    
    # 检查实际文件类型
    try:
        return imghdr.what(file_path) in ('jpeg', 'png', 'bmp')
    except:
        return False

def ensure_directory(path):
    """
    确保目录存在，不存在则创建
    :param path: 目录路径
    """
    os.makedirs(path, exist_ok=True)

def get_output_filename(input_path, output_dir, suffix='_adjusted'):
    """
    生成输出文件名
    :param input_path: 输入文件路径
    :param output_dir: 输出目录
    :param suffix: 文件名后缀
    :return: 完整输出路径
    """
    basename = os.path.basename(input_path)
    name, ext = os.path.splitext(basename)
    output_name = f"{name}{suffix}.jpg"  # 统一输出为jpg格式
    return os.path.join(output_dir, output_name)

def backup_file(original_path, backup_dir='backup'):
    """
    备份原始文件
    :param original_path: 原始文件路径
    :param backup_dir: 备份目录
    :return: 备份文件路径
    """
    ensure_directory(backup_dir)
    filename = os.path.basename(original_path)
    backup_path = os.path.join(backup_dir, filename)
    
    try:
        if os.path.exists(backup_path):
            os.remove(backup_path)
        os.rename(original_path, backup_path)
        return backup_path
    except Exception as e:
        print(f"备份文件失败: {str(e)}")
        return None