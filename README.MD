# 🏭 Manufacturing Text & Image Generator  
> 自动生成制造业测试用文字和图片的 Python 工具  

本程序用于快速生成包含制造业常用词汇的测试数据集，包括：  
- 一份随机 **2000 字** 的制造业文本文件（自动每 80 个字符换行）  
- **5 张随机图片**（包含制造业术语和简单图形）  

可用于 **OCR 训练、算法测试、文字识别、界面样式调试** 等场景。  

---

## 📁 项目结构
manufacturing_data_generator/
├─ generator.py # 主程序
├─ README.md # 使用说明
└─ output/ # 自动生成的输出文件夹
├─ test_image_01.png
├─ test_image_02.png
├─ test_image_03.png
├─ test_image_04.png
├─ test_image_05.png
└─ manufacturing_2000.txt


---

## ⚙️ 功能说明

| 功能 | 描述 |
|------|------|
| 🧾 文本生成 | 随机生成 2000 字制造业主题文字，每 80 字自动换行 |
| 🖼️ 图片生成 | 一次生成 5 张 1000×800 的测试图片 |
| 🔤 字体 | 默认使用 `simhei.ttf` 黑体，可在代码中修改字体路径 |
| 🎨 图形元素 | 随机生成矩形、椭圆、直线等图形背景 |
| 🏗️ 行业语料 | 内置 120+ 条制造业常用词汇（涵盖工艺、设备、信息化、质量等领域） |

---

##  🚀 安装依赖
pip install -r requirements.txt

##  📘 打包成exe
pyinstaller --onefile --noconsole testDataGenerate.py

##  🧠 许可声明

本项目可自由使用、修改、分发，用于科研、教学、开发测试等场景。
如用于商业或公开项目，请注明来源。