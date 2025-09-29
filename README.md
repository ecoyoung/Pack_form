# 剂型打标程序

## 功能说明
智能分析Excel表格中的产品描述，自动识别剂型并填充到空的`Pack form`列中。

## 剂型分类
- **Capsule** - 胶囊类（软胶囊、硬胶囊等）
- **Tablet** - 片剂类（普通片、咀嚼片、含片等）
- **Powder** - 粉剂类（粉末、冲剂、散剂等）
- **Gummy** - 软糖类（软糖、咀嚼糖、果冻等）
- **Drop** - 滴剂类（滴剂、滴液、酊剂等）
- **Softgel** - 软胶囊类
- **Liquid** - 液体类（口服液、糖浆、混悬液等）
- **Mixed** - 多种剂型混合（同时检测到多个剂型）
- **Others** - 其他剂型

## 使用方法

### 方法1：命令行工具
```bash
# 安装依赖
pip install -r requirements.txt

# 运行程序
python pack_form_labeler.py
```

### 方法2：Web界面工具（推荐）
```bash
# 安装依赖
pip install -r requirements.txt

# 启动Web应用
streamlit run streamlit_app.py
```

**Windows用户**：双击 `run_app.bat` 文件
**Linux/Mac用户**：运行 `./run_app.sh` 脚本

## 输入要求
Excel文件必须包含：
- `Pack form` - 剂型列（可能包含空值）
- `Product` - 产品描述列

## 输出结果
程序会生成新文件，包含：
- **Pack form** - 已实际填充匹配到的剂型
- **Matched_Pack_Form** - 匹配到的剂型
- **Match_Source** - 匹配的具体文本
- **Is_Originally_Empty** - 标记是否原本为空
- **Confidence_Score** - 匹配置信度分数

## 匹配原理
1. 使用正则表达式匹配中英文剂型关键词
2. 自动处理大小写和单复数形式
3. 检测到多种剂型时标记为Mixed
4. 计算匹配置信度分数

## Web工具特色
- 🖥️ 简洁美观的Web界面
- 📊 实时数据预览和统计
- 📈 可视化剂型分布图表
- 📥 一键下载处理结果
- 🔍 详细的处理过程追踪

## 注意事项
- 确保Excel文件格式正确
- Product列描述越详细，匹配准确率越高
- 建议处理前备份原始文件
- 背景图片需要命名为 `@logo.jpeg` 并放在同一目录

## 开发维护
**IDC团队** - 专业的数据处理解决方案提供商
