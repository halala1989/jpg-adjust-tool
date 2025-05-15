import json
import os

DEFAULT_CONFIG = {
    "quality": 85,          # 默认JPEG质量 (1-100)
    "max_size_kb": 100,     # 默认最大文件大小(KB)
    "output_format": "jpg", # 默认输出格式
    "backup_original": True # 是否备份原始文件
}

def load_config(config_path="config.json"):
    """
    加载配置文件
    :param config_path: 配置文件路径
    :return: 配置字典
    """
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
                # 合并默认配置和用户配置
                return {**DEFAULT_CONFIG, **config}
        except json.JSONDecodeError:
            print(f"警告: 配置文件 {config_path} 格式错误，使用默认配置")
    return DEFAULT_CONFIG

def save_config(config, config_path="config.json"):
    """
    保存配置文件
    :param config: 配置字典
    :param config_path: 配置文件路径
    """
    try:
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"无法保存配置文件: {str(e)}")