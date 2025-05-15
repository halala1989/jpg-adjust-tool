# 广东医学高级职称报名图片处理工具

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 项目简介

本工具是为广东省医学高级职称报名系统开发的专用图片处理工具，能够将报名所需的图片文件压缩至100KB以下，同时保持良好的视觉质量。

**主要功能**:
- 智能图片压缩，确保文件大小≤100KB
- 支持JPG/JPEG格式输出
- 批量处理模式
- 简单易用的命令行界面

## 安装说明

### 通过pip安装

```bash
pip install git+https://github.com/halala1989/jpg-adjust-tool.git
```

### 从源码安装

1. 克隆仓库:
```bash
git clone https://github.com/halala1989/jpg-adjust-tool.git
cd jpg-adjust-tool
```

2. 安装依赖:
```bash
pip install -r requirements.txt
```

3. 安装工具:
```bash
python setup.py install
```

## 使用方法

### 处理单张图片

```bash
jpg-adjust input.jpg output.jpg
```

### 批量处理图片

```bash
jpg-adjust input_dir output_dir --batch
```

### 可选参数

| 参数 | 描述 | 默认值 |
|------|------|--------|
| `--quality` | 初始JPEG质量 (1-100) | 85 |
| `--max-size` | 最大文件大小(KB) | 100 |
| `--batch` | 启用批量处理模式 | False |

## 开发指南

### 项目结构

```
jpg-adjust-tool/
├── image_processor.py  # 核心图像处理逻辑
├── main.py             # 命令行入口
├── config.py           # 配置管理
├── utils.py            # 工具函数
└── tests/              # 测试代码
```

### 运行测试

```bash
pytest tests/
```

## 贡献指南

欢迎提交Issue和Pull Request。提交代码前请确保:

1. 通过所有单元测试
2. 符合PEP8代码规范
3. 更新相关文档

## 许可证

本项目采用MIT许可证 - 详情请见[LICENSE](LICENSE)文件。