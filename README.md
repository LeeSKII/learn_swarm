# Introduction

Swarm框架学习记录

## Install

`pip install git+https://github.com/openai/swarm.git`

`pip install openai`

## Non openai api key usage

### Config api key

新建`.env`文件，设置`DEEPSEEK_API_KEY`变量

### Config Usage

1. 初始化`openai`包中的`OpenAI` `client`对象，设置第三方供应商兼容的参数`api_key`和`base_url`
2. 初始化`Swarm`对象时，将上述`client`对象传入给`Swarm`对象的`client`参数
3. 构造`Agent`对象时传入`model='deepseek-chat'`

## Usage

### Function calling

实际使用下来`deepseek`的模型会进入到无限循环中，模型无法从`function calling`的结果跳出来，会一直输出需要执行`function`，但是`openai`的模型可以正确执行，另测试`anthropic`的`claude-3-5-sonnet-20241022`，模型并不会进入到工具调用，这里可能是`tool`调用的不兼容问题。
