import argparse
import os
from image_processor import ImageProcessor

def main():
    # 设置命令行参数
    parser = argparse.ArgumentParser(
        description='广东医学高级职称报名图片处理工具 - 调整图片大小至100KB以下')
    
    parser.add_argument('input', help='输入文件或目录路径')
    parser.add_argument('output', help='输出文件或目录路径')
    parser.add_argument('--quality', type=int, default=85,
                      help='初始JPEG质量 (1-100), 默认85')
    parser.add_argument('--max-size', type=int, default=100,
                      help='最大文件大小(KB), 默认100')
    parser.add_argument('--batch', action='store_true',
                      help='批量处理模式')
    
    args = parser.parse_args()

    # 创建处理器实例
    processor = ImageProcessor(quality=args.quality, 
                             max_size_kb=args.max_size)

    # 处理单个文件或批量处理
    if not args.batch:
        # 单文件处理
        if not os.path.isfile(args.input):
            print(f"错误: 输入路径不是文件: {args.input}")
            return
        
        print(f"正在处理: {args.input}")
        success = processor.process_image(args.input, args.output)
        if success:
            print(f"处理完成, 输出到: {args.output}")
        else:
            print("处理失败")
    else:
        # 批量处理
        if not os.path.isdir(args.input):
            print(f"错误: 输入路径不是目录: {args.input}")
            return
        
        if not os.path.exists(args.output):
            os.makedirs(args.output)
        
        processed = 0
        for filename in os.listdir(args.input):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                input_path = os.path.join(args.input, filename)
                output_path = os.path.join(args.output, filename)
                
                print(f"正在处理: {input_path}")
                if processor.process_image(input_path, output_path):
                    processed += 1
                    print(f"已完成: {output_path}")
                else:
                    print(f"处理失败: {input_path}")
        
        print(f"\n批量处理完成, 共处理 {processed} 个文件")

if __name__ == '__main__':
    main()