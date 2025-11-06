#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
制造业测试数据生成器：
- 生成5张随机制造业风格图片 (output/test_image_01.png ~ test_image_05.png)
- 生成一个随机2000字制造业测试文本，80字换行 (output/manufacturing_2000.txt)
"""

import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap

# ====================================
# 配置
# ====================================
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

IMG_COUNT = 5
IMG_WIDTH, IMG_HEIGHT = 1000, 800
TXT_LENGTH = 2000
LINE_WIDTH = 80  # 每行字符数

FONT_PATH = "C:/Windows/Fonts/simhei.ttf"  # 黑体
DEFAULT_FONT_SIZE = 60

manufacturing_terms = [
    "零件", "装配", "工艺卡", "BOM", "刀具", "夹具", "基准", "公差",
    "尺寸链", "工序", "毛坯", "热处理", "机加工", "焊接", "三坐标", "PDM",
    "MES", "工装", "检验", "试制", "批量生产", "数控", "图纸", "CAD",
    "CAPP", "加工中心", "材料牌号", "粗糙度", "表面处理", "库存", "流程卡",
    "工艺路线", "标准件", "外购件", "刀具编号", "工序时间", "编程", "设备",
    "质检", "条码", "批次", "计划", "发料", "领料", "返工", "合格", "不合格",
    "物料编码", "装夹", "定位", "夹具设计", "程序", "刀轨", "切削", "进给",
    "主轴", "夹紧", "验收", "试验", "参数", "调整", "优化", "上线", "下线",
    "ERP", "PLM", "MRP", "工时", "刀具寿命", "换刀", "刀补", "测量",
    "量具", "模具", "冲压", "折弯", "激光切割", "数控铣", "车削", "钻孔",
    "攻丝", "抛光", "去毛刺", "工艺参数", "制造资源", "产能分析", "工艺仿真",
    "夹具定位", "夹紧力", "基准孔", "装配公差", "焊缝", "热变形", "冷却液", "主程序",
    "子程序", "G代码", "M代码", "刀补表", "工序卡片", "检验报告", "质量追溯",
    "条码系统", "RFID", "生产计划", "调度", "在制品", "入库", "出库", "台账",
    "工单", "派工单", "物料清单", "BOP", "ERP接口", "数据采集", "设备状态",
    "维护保养", "故障报警", "工艺标准", "作业指导书", "产品结构", "BOM展开",
    "三维模型", "模型转换", "CAM编程", "刀轨仿真", "碰撞检测", "夹具校核",
    "制造偏差", "工艺模板", "工艺基准", "尺寸公差", "几何公差", "形位公差",
    "统计过程控制", "SPC", "质量体系", "ISO9001", "计量器具", "生产节拍",
    "节拍时间", "换线", "首件检验", "过程检验", "终检", "FMEA", "PPAP",
    "工艺改进", "降本增效", "制造执行", "生产可视化", "数据采集终端", "电子看板",
    "设备联网", "智能制造", "数字化工厂", "数字孪生", "虚拟仿真", "物联网",
    "MES集成", "生产追踪", "质量分析", "报工系统", "能耗监控", "设备稼动率"
]


# ====================================
# 工具函数
# ====================================
def random_color(low=100, high=255):
    return tuple(random.randint(low, high) for _ in range(3))


def draw_random_shapes(draw, width, height):
    for _ in range(random.randint(5, 10)):
        shape_type = random.choice(["rectangle", "ellipse", "line"])
        x1, y1 = random.randint(0, width//2), random.randint(0, height//2)
        x2, y2 = random.randint(width//2, width), random.randint(height//2, height)
        color = random_color(120, 220)
        line_width = random.randint(2, 5)
        if shape_type == "rectangle":
            draw.rectangle([x1, y1, x2, y2], outline=color, width=line_width)
        elif shape_type == "ellipse":
            draw.ellipse([x1, y1, x2, y2], outline=color, width=line_width)
        elif shape_type == "line":
            draw.line([x1, y1, x2, y2], fill=color, width=line_width)


def draw_random_texts(draw, font_path, width, height):
    used_words = random.sample(manufacturing_terms, random.randint(8, 15))
    for text in used_words:
        size = random.randint(40, 80)
        font = ImageFont.truetype(font_path, size)
        x = random.randint(0, width - 200)
        y = random.randint(0, height - 100)
        color = random_color(0, 100)
        draw.text((x, y), text, font=font, fill=color)
    return used_words


def generate_image(img_index):
    """生成一张制造业测试图片"""
    bg_color = random_color(200, 240)
    img = Image.new("RGB", (IMG_WIDTH, IMG_HEIGHT), color=bg_color)
    draw = ImageDraw.Draw(img)
    draw_random_shapes(draw, IMG_WIDTH, IMG_HEIGHT)
    draw_random_texts(draw, FONT_PATH, IMG_WIDTH, IMG_HEIGHT)
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img_path = os.path.join(OUTPUT_DIR, f"test_image_{img_index:02d}.png")
    img.save(img_path)
    print(f"✅ 图片已生成：{img_path}")


def generate_text():
    """生成2000字制造业测试文本，80字换行"""
    connectors = ["，", "。", "；", "：", "并且", "同时", "因此", "例如", "包括", "与", "或", "并"]
    single_chars = list("制造业测试工序刀具夹具工装材料表面加工质量")
    text = ""
    while len(text) < TXT_LENGTH:
        if random.random() < 0.85:
            term = random.choice(manufacturing_terms)
        else:
            term = random.choice(single_chars)
        if random.random() < 0.4:
            term += random.choice(connectors)
        remain = TXT_LENGTH - len(text)
        if len(term) <= remain:
            text += term
        else:
            text += term[:remain]
            break
    # 自动换行
    lines = textwrap.wrap(text, LINE_WIDTH)
    text_with_lines = "\n".join(lines)
    txt_path = os.path.join(OUTPUT_DIR, "manufacturing_2000.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text_with_lines)
    print(f"✅ 文本已生成：{txt_path}（总长度 {len(text)} 字，80字换行）")


# ====================================
# 主执行
# ====================================
if __name__ == "__main__":
    # 生成5张图片
    for i in range(1, IMG_COUNT + 1):
        generate_image(i)
    # 生成2000字文本
    generate_text()
    print("\n🎉 图片与文本生成完成！")
