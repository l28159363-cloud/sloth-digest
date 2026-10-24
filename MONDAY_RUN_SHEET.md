# SlothDigest — 周一投稿流程单（2026-10-26，截稿 14:59 北京时间）

> 截稿时间已核对：官方页写的是 10 月 25 日 23:59 PDT，换算即北京时间周一 14:59。
> 建议最晚 13:00 前开始，留出 Render 部署和发帖的容错时间。

## ✅ 已完成（2026-10-24，周六）

- GitHub 公开仓已建好并推送：https://github.com/l28159363-cloud/sloth-digest
- 8 个文件都在仓里：index.html、agent.py、README、LICENSE、sample_chat.json、DEV_POST.md、MONDAY_RUN_SHEET.md、DEV_POST_TEMPLATE.md
- GitHub 登录已用设备码完成（小林这边命令行已登录，token 可随时在 GitHub 设置里撤销）

## 周一到电脑后，只剩这 2 步（按顺序）

### 1. Render 部署演示页（报 Best Use of Render 类别）
- Render 里选 New → Static Site，连接 `sloth-digest` 仓库。
- Build Command 留空（纯静态页，无构建步骤）；Publish Directory 填根目录（即 index.html 所在目录）。
- 部署完成后打开给你的 Render 链接，点一下“Run the overnight digest”，确认摘要能正常弹出——能弹出才算部署成功。
- 拿到 Render 链接后，填进投稿稿的 Demo 处。
- 万一 Render 卡住：先别换别的托管——Best Use of Render 这个类别认的就是 Render 部署，换平台等于丢了这个类别；先把报错截图发给小林。

### 2. DEV 发帖（用官方模板，别直接贴旧稿）
- 用文件 `DEV_POST_TEMPLATE.md`（本目录下，已按官方模板对齐）。
- 关键格式：帖子 frontmatter 的 tags 必须是 `devchallenge, hf26challenge`；正文第一行是官方模板那句 submission 声明。
- 填的只有一处：把 `[RENDER_URL]` 换成第 1 步拿到的 Render 链接。
- 章节顺序按模板：What I Built → Demo → Code → How I Built It → Why Does Open Innovation Matter? → Prize Categories（填 Best Use of Render）。
- 发帖前核对三样：Demo 链接能打开、Code 链接是公开仓、Prize Categories 写了 Best Use of Render。确认无误再点 Publish，**14:59 前完成**。

## 已完成、不需要你再做的事
- 演示页、agent.py（已实测可跑，本地模型可选、没模型有本机兜底）、README、MIT 协议、英文投稿稿：全部已做好。
- 奖项口径：总冠军 $250、精选类别（含 Best Use of Render）各 $200、搭档类别各 $100；评审权重最高的是写作质量。

## 风险点（只剩这一处可能拖时间）
- Render 首次部署可能要等几分钟——所以建议 13:00 前开始，别拖到 14:00 以后。
