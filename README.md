# Tongji AI Final Project - 大语言模型部署与对比分析

本项目为同济大学《人工智能导论》课程期末作业，目标是部署并对比两个中文大语言模型——[ChatGLM3-6B](https://www.modelscope.cn/ZhipuAI/chatglm3-6b.git) 与 [Qwen-7B-Chat](https://www.modelscope.cn/qwen/Qwen-7B-Chat.git)，通过多个中文语义与逻辑测试题目，分析它们在语言理解与生成任务上的表现差异。

---

## 📦 项目内容

- ✅ **ChatGLM3-6B 与 Qwen-7B-Chat 模型部署**
- ✅ **Python 脚本 vs Jupyter Notebook 的部署效率比较**
- ✅ **五组中文歧义/幽默语义测试**
- ✅ **两大模型对比分析报告（含答题内容与评估）**

---

## 🛠️ 安装与环境配置

推荐在 [魔搭 ModelScope 平台](https://www.modelscope.cn/) 上部署，也可本地运行：

### 依赖库

```bash
torch>=2.0.0
transformers>=4.30.0
accelerate
huggingface_hub
sentencepiece
tokenizers

# 克隆模型仓库
git clone https://www.modelscope.cn/ZhipuAI/chatglm3-6b.git
git clone https://www.modelscope.cn/qwen/Qwen-7B-Chat.git

# 创建虚拟环境（可选）
python -m venv qwen_env
source qwen_env/bin/activate

# 安装依赖
pip install -r requirements.txt

姓名：付煜超
课程：人工智能导论
指导教师：沈莹老师

