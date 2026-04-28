# HYPE Grid Strategy

## 策略概述

**HYPE 高频网格交易策略** - 基于 Hyperliquid Plugin 的自动化交易机器人，专为 Plugin Store DApp Heat Competition 设计。

- **作者**: 韭菜 (@lvjwrogm)
- **策略ID**: hype-grid-v1
- **钱包地址**: 0x3af180895d91ecd778585dbadf37f196ca89e3c1
- **比赛**: Plugin Store DApp Heat Competition (2026.04.23 - 2026.05.07)

## 策略原理

### 网格交易
- **交易对**: HYPE-USDC
- **网格间距**: 2%
- **价格区间**: $36 - $45
- **订单大小**: 0.25 HYPE
- **杠杆**: 10x 全仓

### 交易逻辑
1. **价格下跌** → 在支撑位买入建仓
2. **价格上涨** → 在阻力位卖出止盈
3. **双向交易** → 同时挂买单和卖单
4. **高频刷量** → 每5分钟执行一次

## 使用方式

### 手动执行
```bash
# 买入
hyperliquid order --coin HYPE --side buy --size 0.25 --price 40.00 --strategy-id hype-grid-v1

# 卖出
hyperliquid order --coin HYPE --side sell --size 0.25 --price 41.00 --strategy-id hype-grid-v1
```

### 批量下单
```bash
hyperliquid order-batch --strategy-id hype-grid-v1 --orders '[
  {"coin":"HYPE","side":"buy","size":"0.25","price":"40.00"},
  {"coin":"HYPE","side":"sell","size":"0.25","price":"41.00"}
]'
```

### 自动运行
```bash
# 使用 cron 定时任务，每5分钟执行
*/5 * * * * /path/to/hype-grid.sh
```

## 技术配置

### 环境要求
- Onchain OS v2.5.0+
- Hyperliquid Plugin v0.3.9+
- Agentic Wallet 已登录

### 合规链路
```
Agentic Wallet → Onchain OS → Skill → Hyperliquid Plugin → 交易
```

每笔交易自动上报到大赛统计系统，确保合规统计。

## 风险控制

### 参数
- **清算价格**: ~$123 (10x杠杆安全距离)
- **保证金使用**: <5%
- **最大持仓**: 0.25 HYPE/单

### 安全措施
- 自动检查账户余额
- 价格异常检测
- 自动止损机制

## 文件结构

```
hype-grid-strategy/
├── plugin.yaml      # 插件配置
├── SKILL.md         # 本文件
├── hype-grid.sh     # 执行脚本
└── README.md        # 说明文档
```

## 作者信息

- **Telegram**: @lvjwrogm
- **邮箱**: jian28277@gmail.com
- **ERC20地址**: 0x3af180895d91ecd778585dbadf37f196ca89e3c1

## 免责声明

⚠️ **高风险策略** - 使用杠杆交易，可能导致资金损失。请谨慎使用，仅用于比赛目的。
