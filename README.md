# GitHub Actions CI/CD Demo

[![CI/CD](https://github.com/sampleyzs/github-actions-cicd-demo/actions/workflows/cicd.yml/badge.svg)](https://github.com/sampleyzs/github-actions-cicd-demo/actions/workflows/cicd.yml)

一个零第三方运行时依赖的 Python 命令行项目，用完整的 GitHub Actions 流水线演示持续集成（CI）和持续交付/部署（CD）。

## 流水线流程

```text
推送 main / 提交 PR / 推送 v* 标签
              │
              ▼
       检出代码、配置 Python
              │
              ▼
          运行单元测试
              │
              ▼
   构建 .pyz 程序和 SHA-256 校验文件
              │
              ▼
       执行构建产物冒烟测试
              │
              ▼
        上传 Actions 构建产物
              │
              ├─ 普通提交或 PR：结束
              │
              └─ v* 标签：自动创建 GitHub Release 并附加产物
```

## 本地运行

需要 Python 3.10 或更高版本，无需安装依赖。

```bash
# 运行全部测试
python -m unittest discover -s tests -v

# 构建可执行 zipapp 和校验文件
python scripts/build.py

# 运行构建产物
python dist/cicd-demo.pyz --version
python dist/cicd-demo.pyz greet "开发者"
python dist/cicd-demo.pyz add 1 2 3.5
```

预期最后一次命令输出 `6.5`。Windows 上可使用 `python dist/cicd-demo.pyz`；Linux/macOS 上也可执行 `./dist/cicd-demo.pyz`。

## 发布新版本

1. 修改 `app/cicd_demo/__init__.py` 中的 `__version__`。
2. 提交并推送到 `main`，确认 CI 通过。
3. 创建与程序版本一致的标签并推送：

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

标签触发同一条工作流；只有测试、构建和冒烟测试全部成功后，`release` 作业才会创建 Release。构建脚本会阻止标签版本和程序版本不一致的发布。

## 工作流说明

工作流位于 `.github/workflows/cicd.yml`：

| 触发方式 | 单元测试 | 构建与冒烟测试 | 上传 Artifact | 创建 Release |
| --- | --- | --- | --- | --- |
| 推送到 `main` | 是 | 是 | 是 | 否 |
| Pull Request | 是 | 是 | 是 | 否 |
| 推送 `v*` 标签 | 是 | 是 | 是 | 是 |
| 手动运行 | 是 | 是 | 是 | 否 |

发布作业使用 GitHub 自动提供的 `GITHUB_TOKEN`，权限限定为当前仓库的 `contents: write`，不需要配置私人令牌或额外密钥。

## 项目结构

```text
.
├── .github/workflows/cicd.yml  # CI/CD 工作流
├── app/
│   ├── __main__.py             # zipapp 入口
│   └── cicd_demo/              # 应用代码与版本号
├── scripts/build.py            # 构建与版本校验脚本
├── tests/                      # 单元测试和 CLI 测试
└── README.md
```
