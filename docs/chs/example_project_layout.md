```
python_tools/
├── 📁 .github/                    # GitHub配置
│   ├── workflows/                # CI/CD流水线
│   └── ISSUE_TEMPLATE/          # Issue模板
│
├── 📁 .vscode/                   # VS Code配置（可选）
│   └── settings.json
│
├── 📁 docs/                      # 文档
│   └── chs/
│       ├── architecture/            # 架构文档（本文档位置）
│       ├── api/                     # API文档
│       └── guides/                  # 使用指南
│
├── 📁 scripts/                   # 工具脚本
│   ├── bootstrap.py            # 项目初始化
│   ├── validate_architecture.py # 架构验证
│   └── generate_scaffold.py    # 代码脚手架生成
│
├── 📁 requirements/              # 分层依赖管理
│   ├── core.txt                # core层依赖（通常为空）
│   ├── framework.txt           # framework层依赖
│   ├── modules.txt             # modules层依赖
│   └── dev.txt                 # 开发依赖
│
├── 📁 tests/                     # 分层测试
│   ├── 📁 core/                 # core层测试
│   │   ├── conftest.py
│   │   └── test_primitives.py
│   │
│   ├── 📁 framework/            # framework层测试
│   │   └── test_services.py
│   │
│   ├── 📁 modules/              # modules层测试
│   │   ├── sqlalchemy/
│   │   └── fastapi/
│   │
│   └── 📁 integration/          # 集成测试
│
├── 📁 src/                       # 源代码（可安装包结构）
│   └── 📁 project_name/         # 主包
│       ├── __init__.py
│       ├── py.typed            # 类型提示标记
│       │
│       ├── 📁 core/            # CORE层
│       │   ├── __init__.py
│       │   │
│       │   ├── 📁 types/       # core/types/
│       │   │   ├── __init__.py
│       │   │   ├── user_id.py  # UserId = NewType('UserId', int)
│       │   │   └── email.py    # Email值对象
│       │   │
│       │   ├── 📁 errors/      # core/errors/
│       │   │   ├── __init__.py
│       │   │   └── domain.py   # DomainError基类
│       │   │
│       │   ├── 📁 primitives/  # core/primitives/
│       │   │   ├── money.py    # Money值对象
│       │   │   └── address.py
│       │   │
│       │   └── 📁 constants/   # core/constants/
│       │       └── settings.py # 核心常量
│       │
│       ├── 📁 framework/       # FRAMEWORK层
│       │   ├── __init__.py
│       │   │
│       │   ├── 📁 services/    # framework/services/
│       │   │   ├── __init__.py
│       │   │   ├── payment.py  # PaymentService(Protocol)
│       │   │   └── user.py     # UserService(Protocol)
│       │   │
│       │   ├── 📁 repositories/ # framework/repositories/
│       │   │   ├── __init__.py
│       │   │   └── user.py     # UserRepository(Protocol)
│       │   │
│       │   ├── 📁 models/      # framework/models/
│       │   │   ├── __init__.py
│       │   │   ├── user.py     # User(pydantic)
│       │   │   └── order.py
│       │   │
│       │   ├── 📁 pipelines/   # framework/pipelines/
│       │   │   └── data_processing.py
│       │   │
│       │   └── 📁 validators/  # framework/validators/
│       │       └── user_validator.py
│       │
│       └── 📁 modules/         # MODULES层
│           ├── __init__.py
│           │
│           ├── 📁 di/          # modules/di/
│           │   ├── __init__.py
│           │   ├── container.py # DI容器配置
│           │   └── providers.py # 提供者定义
│           │
│           ├── 📁 db/          # modules/db/
│           │   ├── sqlalchemy/  # modules/db/sqlalchemy/
│           │   │   ├── __init__.py
│           │   │   │
│           │   │   ├── 📁 repositories_impl/  # 仓储实现
│           │   │   │   ├── user_repository.py
│           │   │   │   └── order_repository.py
│           │   │   │
│           │   │   ├── 📁 models_orm/        # ORM模型
│           │   │   │   └── user_orm.py
│           │   │   │
│           │   │   ├── 📁 migrations/        # 数据库迁移
│           │   │   │   └── alembic.ini
│           │   │   │
│           │   │   └── session.py           # 会话管理
│           │   │
│           │   ├── redis/       # modules/db/redis/
│           │   │   ├── client.py
│           │   │   └── cache.py
│           │   │
│           │   └── mongodb/     # modules/db/mongodb/
│           │
│           ├── 📁 web/         # modules/web/
│           │   ├── fastapi/     # modules/web/fastapi/
│           │   │   ├── __init__.py
│           │   │   │
│           │   │   ├── 📁 routers/          # 路由定义
│           │   │   │   ├── users.py
│           │   │   │   └── orders.py
│           │   │   │
│           │   │   ├── 📁 handlers/         # 请求处理器
│           │   │   │   ├── user_handler.py
│           │   │   │   └── order_handler.py
│           │   │   │
│           │   │   ├── 📁 middleware/       # 中间件
│           │   │   │   └── auth.py
│           │   │   │
│           │   │   ├── 📁 schemas/         # API Schema
│           │   │   │   └── user_schema.py
│           │   │   │
│           │   │   └── app.py              # FastAPI应用实例
│           │   │
│           │   └── flask/       # modules/web/flask/
│           │
│           ├── 📁 payment/     # modules/payment/
│           │   ├── stripe/      # modules/payment/stripe/
│           │   │   ├── client.py
│           │   │   └── webhooks.py
│           │   │
│           │   └── paypal/      # modules/payment/paypal/
│           │
│           ├── 📁 auth/        # modules/auth/
│           │   ├── jwt/         # modules/auth/jwt/
│           │   └── oauth/       # modules/auth/oauth/
│           │
│           ├── 📁 messaging/   # modules/messaging/
│           │   ├── redis/       # modules/messaging/redis/
│           │   └── kafka/       # modules/messaging/kafka/
│           │
│           └── 📁 storage/     # modules/storage/
│               ├── s3/          # modules/storage/s3/
│               └── local/       # modules/storage/local/
│
├── 📁 examples/                 # 使用示例
│   ├── basic_usage.py
│   └── web_example.py
│
├── 📁 config/                   # 配置文件
│   ├── development.yaml
│   ├── production.yaml
│   └── testing.yaml
│
├── 📁 .venv/                    # 虚拟环境（可选）
│
├── .gitignore
├── .python-version             # Python版本
├── pyproject.toml              # 现代Python项目配置
├── README.md
├── LICENSE
└── Makefile                    # 常用命令封装
```