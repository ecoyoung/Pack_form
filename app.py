#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
剂型打标Web工具 (Streamlit)
开发维护：IDC团队
"""

import streamlit as st
import pandas as pd
from io import BytesIO
from pack_form_labeler import PackFormLabeler
import base64

# 页面配置
st.set_page_config(
    page_title="剂型智能打标工具",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义CSS样式
def get_custom_css():
    return """
    <style>
    .stApp {
        background: rgba(255, 255, 255, 0.95);
    }
    
    .main-header {
        background: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .content-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .footer {
        background: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-top: 30px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .logo-container {
        text-align: center;
        margin-bottom: 20px;
    }
    
    .logo-image {
        max-width: 200px;
        height: auto;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    </style>
    """

# 主应用
def main():
    # 应用自定义CSS样式
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    # 显示logo图片
    try:
        st.markdown('<div class="logo-container">', unsafe_allow_html=True)
        st.image("aaa.jpeg", width=1500, caption="Anker Oceanwing Inc.")
        st.markdown('</div>', unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"无法加载logo图片: {str(e)}")
    
    # 主标题区域
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title("剂型打标工具")
    st.markdown("通过匹配产品标题，自动识别剂型并填充到空的Pack form列中")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 功能介绍
    with st.container():
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("功能说明")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**支持的剂型分类：**")
            st.markdown("• Capsule - 胶囊类")
            st.markdown("• Tablet - 片剂类")
            st.markdown("• Powder - 粉剂类")
            st.markdown("• Gummy - 软糖类")
            st.markdown("• Drop - 滴剂类")
            st.markdown("• Softgel - 软胶囊类")
            st.markdown("• Liquid - 液体类")
            st.markdown("• Oil - 油类")
            st.markdown("• Cream - 乳霜软膏类")
            st.markdown("• Spray - 喷雾类")
            st.markdown("• Lotion - 乳液类")
            st.markdown("• Patch - 贴剂/贴片类")
            st.markdown("• Suppository - 栓剂类")
            st.markdown("• Bundle - 多种剂型组合")
            st.markdown("• Others - 其他剂型")
        
        st.markdown("**输入要求：** Excel文件必须包含 `Pack form` 和 `Product` 列")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # 文件上传区域
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("文件上传")
    
    uploaded_file = st.file_uploader(
        "请选择您的Excel文件 (.xlsx格式)",
        type=["xlsx"]
    )
    st.markdown("</div>", unsafe_allow_html=True)
    
    if uploaded_file is not None:
        try:
            # 读取文件
            df_input = pd.read_excel(uploaded_file)
            
            # 显示文件信息
            st.markdown('<div class="content-box">', unsafe_allow_html=True)
            st.subheader("文件信息")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("总行数", len(df_input))
            with col2:
                st.metric("总列数", len(df_input.columns))
            with col3:
                empty_count = df_input['Pack form'].isna().sum() if 'Pack form' in df_input.columns else 0
                st.metric("Pack form空值", empty_count)
            
            # 检查必要的列
            required_columns = ['Pack form', 'Product']
            missing_columns = [col for col in required_columns if col not in df_input.columns]
            
            if missing_columns:
                st.error(f"文件缺少必要的列: {missing_columns}")
            else:
                st.success("文件格式正确，包含所有必要的列")
                
                # 显示数据预览
                st.subheader("数据预览 (前5行)")
                st.dataframe(df_input.head(), use_container_width=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # 处理按钮
                st.markdown('<div class="content-box">', unsafe_allow_html=True)
                st.subheader("开始处理")
                
                if st.button("开始剂型打标", type="primary", use_container_width=True):
                    with st.spinner("正在进行剂型智能打标，请稍候..."):
                        try:
                            # 创建标签器实例
                            labeler = PackFormLabeler()
                            
                            # 处理数据
                            df_processed, processed_count, standardization_count = labeler.process_dataframe(df_input)
                            
                            # 显示处理结果
                            st.success("剂型打标完成！")
                            
                            # 统计结果
                            original_empty_count = (df_input['Pack form'].isna() | (df_input['Pack form'] == '')).sum()
                            final_empty_count = (df_processed['Pack form'].isna() | (df_processed['Pack form'] == '')).sum()
                            successfully_filled_count = original_empty_count - final_empty_count
                            # standardization_count 已经从 process_dataframe 返回
                            
                            # 显示统计信息
                            col1, col2, col3, col4, col5 = st.columns(5)
                            with col1:
                                st.metric("原始空值", original_empty_count)
                            with col2:
                                st.metric("成功填充", successfully_filled_count)
                            with col3:
                                st.metric("标准化处理", standardization_count)
                            with col4:
                                st.metric("处理后空值", final_empty_count)
                            with col5:
                                if original_empty_count > 0:
                                    success_rate = successfully_filled_count / original_empty_count * 100
                                    st.metric("成功率", f"{success_rate:.1f}%")
                                else:
                                    st.metric("成功率", "N/A")
                            
                            # 显示标准化处理详情
                            if standardization_count > 0:
                                st.subheader("标准化处理详情")
                                st.info(f"对 {standardization_count} 行已有剂型进行了标准化处理")
                                
                                # 显示标准化前后的对比
                                standardization_examples = df_processed[df_processed['Standardization_Applied'] == True].head(5)
                                if len(standardization_examples) > 0:
                                    st.markdown("**标准化示例：**")
                                    for idx, row in standardization_examples.iterrows():
                                        st.markdown(f"• 行 {idx+1}: 标准化处理")
                            
                            # 显示剂型分布
                            st.subheader("剂型分布")
                            pack_form_counts = df_processed['Pack form'].value_counts()
                            st.bar_chart(pack_form_counts)
                            
                            # 显示处理后的数据预览
                            st.subheader("处理结果预览 (前5行)")
                            st.dataframe(df_processed.head(), use_container_width=True)
                            
                            # 下载结果
                            st.subheader("下载结果")
                            output = BytesIO()
                            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                                df_processed.to_excel(writer, index=False, sheet_name='Labeled Data')
                            output.seek(0)
                            
                            st.download_button(
                                label="下载打标后的Excel文件",
                                data=output,
                                file_name="labeled_pack_forms.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                use_container_width=True
                            )
                            
                            st.info("下载的文件包含：原始数据、填充和标准化后的Pack form列，以及新增的匹配信息列")
                            
                        except Exception as e:
                            st.error(f"处理过程中发生错误: {str(e)}")
                
                st.markdown("</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"读取文件时发生错误: {str(e)}")
    
    # 页脚
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("**开发维护：海翼 IDC团队**")
    st.markdown("© 2025 剂型打标工具. All rights reserved.")
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
