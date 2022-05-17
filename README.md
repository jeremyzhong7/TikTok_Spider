# Tiktok-Spider
## 介绍
**目的**：批量`高速`爬取博主无水印视频 解决`GIL`锁!!!
**此开源项目后续暂时不考虑维护（除非**`Star`**比较多hhh）**
> **此版本为 2022.4 编写 后续无法保证一直能正常使用**
> 
> **有任何问题请提`Issues`请务必清晰阐述问题**
> 
> **若需要定制开发 请联系 `jeremyzhong2021@163.com`**

## 运行环境

- [Python3](https://www.python.org/)
- [anaconda3（可选项）](https://www.anaconda.com/)
## 第三方库

- `requests`
## 使用教程
### 1. 请务必谨慎配置`processThreadPool.py`中的`process_cnt`和`thread_cnt`，小白请自行[Google](https://google.com)、[Bing](https://bing.com)
### 2. 运行`processThreadPool.py`
```shell
# 先打开抖音复制博主的主页地址 把地址复制下来作为参数携带
$ python .\processThreadPool.py https://v.douyin.com/xxxxx/
# 运行后会自动将该博主视频的所有信息爬取并保存在json目录内
```
> **Tips**：虽说可以最大性能的爬取，但也受限于`自身带宽`
> **Tips：若视频数量过少< 6，则进程池默认只启动**`一核心`**，减小进程创建销毁开销加快速度**
> **若视频无标题，则会随机生成一个UUID作为文件名.mp4并存储**

### 3. 运行效果
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26683478/1652776220821-cd6422db-c608-420d-b0d3-68c6ce7d8eec.png#clientId=u0970921a-0d1b-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=229&id=uff77ccda&margin=%5Bobject%20Object%5D&name=image.png&originHeight=229&originWidth=942&originalType=binary&ratio=1&rotation=0&showTitle=false&size=55840&status=done&style=none&taskId=u222bf0fe-acf8-4d0f-8dab-fafe2770a08&title=&width=942)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/26683478/1652776290029-f6eac5df-4e01-478a-824c-fd4d39ad0c4d.png#clientId=u0970921a-0d1b-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=649&id=ua0dd7d01&margin=%5Bobject%20Object%5D&name=image.png&originHeight=649&originWidth=1457&originalType=binary&ratio=1&rotation=0&showTitle=false&size=125714&status=done&style=none&taskId=u3e0b97cb-d3de-4d98-88ca-39b3614553c&title=&width=1457)
> **实际速度请自行尝试 可以尝试修改参数**`process_cnt`**和**`thread_cnt`**电脑配置不同 参数不唯一**

## 特别声明
本仓库发布的`Tiktok-Spider`项目中涉及的任何脚本，仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。
本项目内所有资源文件，禁止任何公众号、自媒体进行任何形式的转载、发布。
本人对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害。
间接使用脚本的任何用户，包括但不限于建立VPS或在某些行为违反国家/地区法律或相关法规的情况下进行传播, 本人 对于由此引起的任何隐私泄漏或其他后果概不负责。
请勿将`Tiktok-Spider`项目的任何内容用于商业或非法目的，否则后果自负。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
> **以任何方式查看此项目的人或直接或间接使用 `Tiktok-Spider`项目的任何脚本的使用者都应仔细阅读此声明。本人 保留随时更改或补充此免责声明的权利。 一旦使用并复制了任何相关脚本或 `Tiktok-Spider`项目，则视为您`已接受`此免责声明。**

**您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
本项目遵循 `GPL-3.0 License`协议，如果本特别声明与 `GPL-3.0 License`协议有冲突之处，以本特别声明为准。**