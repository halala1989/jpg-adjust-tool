from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jpg-adjust-tool",
    version="1.0.0",
    author="halala1989",
    author_email="cbgtlgc@126.com",
    description="广东医学高级职称报名图片处理工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/halala1989/jpg-adjust-tool",
    packages=find_packages(),
    install_requires=[
        "pillow>=9.0.0",
    ],
    extras_require={
        "opencv": ["opencv-python>=4.5.0"],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "flake8>=4.0.0",
            "black>=22.0.0"
        ],
    },
    entry_points={
        "console_scripts": [
            "jpg-adjust=jpg_adjust_tool.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)