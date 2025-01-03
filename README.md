# Introduction

Swarm框架学习记录

## Install

`pip install git+ssh://git@github.com/openai/swarm.git`

`pip install openai`

## Non openai api key usage

### Config api key

新建`.env`文件，设置`DEEPSEEK_API_KEY`变量

### Config Usage

1. 初始化`openai`包中的`OpenAI` `client`对象，设置第三方供应商兼容的参数`api_key`和`base_url`
2. 初始化`Swarm`对象时，将上述`client`对象传入给`Swarm`对象的`client`参数
3. 构造`Agent`对象时传入`model='deepseek-chat'`
