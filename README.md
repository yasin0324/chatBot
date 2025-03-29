# WeChat AI Chat Bot

这是一个将 AI 接入微信聊天的自动化回复机器人工具。

## 功能特点

-   自动监听指定微信好友或群组的消息
-   使用 AI 模型自动生成回复
-   可自定义 AI 回复风格和内容

## 安装依赖

```bash
pip install openai wxauto
```

## 配置说明

1. 在`main.py`中设置你的 OpenAI API 密钥和代理地址：

```python
self.client = OpenAI(api_key="your-api-key", base_url="your-proxy-url")
```

2. 在`listen_list`中添加要监听的好友或群组名称

## 运行方法

```bash
python main.py
```

## 自定义回复风格

修改`__ask`方法中的 system prompt 来改变 AI 的回复风格：

```python
{"role": "system", "content": "你的自定义角色描述"}
```

## 注意事项

-   确保微信客户端已登录
-   首次运行时可能需要授权微信自动化权限
