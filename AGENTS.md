# AGENTS.md

## 项目概览

- 这是一个无框架的静态网页加法器，使用原生 JavaScript ES Modules。
- 入口页面是 `index.html`；浏览器逻辑位于 `src/app.js`，纯计算逻辑位于 `src/math.js`。
- 测试使用 Node.js 内置 `node:test`，文件位于 `test/`。
- 构建脚本会清理并重新生成 `dist/`，并复制网页与 `src/`。

## 常用命令

- 安装依赖：无需依赖包；当前项目不需要 `npm install`。
- 测试：`npm test`
- 构建：`npm run build`
- 环境要求：`package.json` 指定 Node.js `>=24`。

每次修改代码或测试后运行 `npm test`；涉及发布产物或构建脚本时额外运行 `npm run build`。

## 修改约定

- 保持项目为 ESM：使用 `import`/`export`，不要引入 CommonJS 或包管理依赖，除非需求明确要求。
- 优先将可复用、可单测的计算逻辑放在 `src/math.js`；DOM 事件与页面查询保留在 `src/app.js`。
- 计算函数应继续校验参数，并使用 `TypeError` 表达无效数字输入。
- 修改构建行为时只调整 `scripts/build.js`，避免把构建逻辑分散到多个入口。
- 保持 `dist/` 和 `node_modules/` 只作为生成或依赖目录，不提交到版本控制。

## 验证要求

- 为 `src/math.js` 的行为变化补充或更新 `test/math.test.js`。
- 使用断言验证正常值、边界值和异常输入。
- 提交前确认测试通过且构建产物可以在 `dist/` 生成。
- 不要手动编辑 `dist/`；构建脚本是其唯一生成入口。

## 项目文档

- 本地测试、构建和自动部署说明见 [README.md](README.md)。
