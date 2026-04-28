# HYPE Grid Strategy

## 概述

**HYPE 高频网格交易策略** - 专为 Plugin Store DApp Heat Competition 设计的自动化交易机器人。

## 策略特点

- ✅ **高频交易** - 每5分钟执行一次
- ✅ **双向网格** - 同时挂买单和卖单
- ✅ **自动上报** - 每笔交易自动上报大赛统计
- ✅ **合规链路** - Agentic Wallet → Onchain OS → Skill → Hyperliquid Plugin

## 技术栈

- **平台**: Hyperliquid
- **交易对**: HYPE-USDC
- **杠杆**: 10x 全仓
- **网格间距**: 2%

## 安装使用

### 1. 安装依赖
```bash
npx skills add okx/onchainos-skills
npx skills add okx/hyperliquid-plugin
```

### 2. 配置钱包
```bash
onchainos wallet login
```

### 3. 运行策略
```bash
./hype-grid.sh
```

## 作者

- **Name**: 韭菜
- **Telegram**: @lvjwrogm
- **Email**: jian28277@gmail.com
- **Wallet**: 0x3af180895d91ecd778585dbadf37f196ca89e3c1

## 比赛信息

- **比赛**: Plugin Store DApp Heat Competition
- **奖池**: 17700 USDC
- **时间**: 2026.04.23 - 2026.05.07
- **策略ID**: hype-grid-v1

## 免责声明

⚠️ 高风险策略，使用杠杆交易可能导致资金损失。请谨慎使用。
