# SlothDigest — 周一投稿流程单（2026-10-26，截稿 14:59 北京时间）

> 截稿时间已核对：官方页写的是 10 月 25 日 23:59 PDT，换算即北京时间周一 14:59。
> 建议最晚 13:00 前开始，留出 Render 部署和发帖的容错时间。

## 周一到电脑后，只剩这 4 步（按顺序）

### 1. GitHub 建公开仓（名字已查过：目前不存在）
- 仓库名：`sloth-digest`，公开（Public），**不要勾选自动生成 README**（会和本地文件冲突）。
- 预期地址：`https://github.com/l28159363-cloud/sloth-digest`
- 注意：这一步只能周一做——仓库现在还不存在，上面那个地址打开是 404，属正常。

### 2. 把本地代码推上去（唯一需要你登录的一步）
- 文件都在小林这边：`~/workspace/hackathon/dev-week3-sloth-digest/`，共 8 个文件（index.html、agent.py、README、LICENSE、sample_chat.json、DEV_POST.md，另加新准备的 MONDAY_RUN_SHEET.md 和 DEV_POST_TEMPLATE.md），本地 git 已提交。
- 你上线后告诉小林一声，由小林带你完成推送——这一步需要你本人的 GitHub 登录，别人替不了。
- 推完先打开仓库页确认 8 个文件都在，再往下走。

### 3. Render 部署演示页（报 Best Use of Render 类别）
- Render 里选 New → Static Site，连接上一步的 `sloth-digest` 仓库。
- Build Command 留空（纯静态页，无构建步骤）；Publish Directory 填根目录（即 index.html 所在目录）。
- 部署完成后打开给你的 Render 链接，点一下“Run the overnight digest”，确认摘要能正常弹出——能弹出才算部署成功。
- 拿到 Render 链接后，填进投稿稿的 Demo 处。
- 万一 Render 卡住：先别换别的托管——Best Use of Render 这个类别认的就是 Render 部署，换平台等于丢了这个类别；先把报错截图发给小林。

### 4. DEV 发帖（用官方模板，别直接贴旧稿）
- 用文件 `DEV_POST_TEMPLATE.md`（本目录下新准备的，已按官方模板对齐）。
- 关键格式：帖子 frontmatter 的 tags 必须是 `devchallenge, hf26challenge`；正文第一行是官方模板那句 submission 声明。
- 填的只有一处：把 `[RENDER_URL]` 换成第 3 步拿到的 Render 链接。
- 章节顺序按模板：What I Built → Demo → Code → How I Built It → Why Does Open Innovation Matter? → Prize Categories（填 Best Use of Render）。
- 发帖前核对三样：Demo 链接能打开、Code 链接是新建的公开仓、Prize Categories 写了 Best Use of Render。确认无误再点 Publish，**14:59 前完成**。

## 已完成、不需要你再做的事
- 演示页、agent.py（已实测可跑，本地模型可选、没模型有本机兜底）、README、MIT 协议、英文投稿稿：全部已做好。
- 奖项口径：总冠军 $250、精选类别（含 Best Use of Render）各 $200、搭档类别各 $100；评审权重最高的是写作质量。

## 风险点（只有这两处可能拖时间）
1. GitHub 推送需要你本人登录——这是周一唯一不能提前做的事。
2. Render 首次部署可能要等几分钟——所以建议 13:00 前开始，别拖到 14:00 以后。
