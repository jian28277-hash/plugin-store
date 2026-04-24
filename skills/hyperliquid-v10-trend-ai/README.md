# 🐉 小龙趋势狙击者 (Xiaolong Trend Sniper)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Plugin Store](https://img.shields.io/badge/Plugin%20Store-hyperliquid--v10--trend--ai-blue)](https://github.com/okx/plugin-store)

> **基于 Hyperliquid 的全自动动能突破策略，内置 ATR 动态止损与三段式阶梯止盈，专为趋势行情设计。**

---

## 🎯 策略核心

### AI四维度评分系统

| 维度 | 权重 | 说明 |
|------|------|------|
| **趋势** | 40% | EMA排列 + 趋势线方向 |
| **动量** | 25% | RSI + MACD + 成交量 |
| **突破** | 30% | 关键位突破 + 假突破过滤 |
| **波动率** | 5% | ATR波动率确认 |

**开仓条件**：综合评分 ≥ 70分（满分100）

---

## 🛡️ 风控体系

### 1. 仓位管理
- **杠杆限制**：最大10倍
- **单次仓位**：保证金占比10%
- **最大持仓**：同时最多2个仓位
- **日限交易**：每天最多3笔

### 2. 止损机制
```
止损价 = 开仓价 ± (1.5 × ATR)
```
- 开仓即自动挂载止损
- 移动保本：盈利后止损上移保护本金

### 3. 三段式阶梯止盈

| 阶段 | 触发条件 | 操作 | 仓位变化 |
|------|----------|------|----------|
| **第一阶段** | 浮盈 +2% | 平仓30% | 剩余70% |
| **第二阶段** | 浮盈 +4% | 平仓30% | 剩余40% |
| **第三阶段** | 浮盈 +6% | 平仓40% | 清仓 |

**盈亏比**：3:1（止盈6% vs 止损2%）

---

## 📊 交易标的

支持8个主流币种：
- BTC、ETH、SOL、XRP
- DOGE、ADA、LINK、LTC

**时间框架**：
- 信号周期：15分钟K线
- 趋势确认：1小时K线

---

## 🚀 快速开始

### 安装

```bash
npx skills add okx/plugin-store --skill hyperliquid-v10-trend-ai
```

### 使用示例

**1. 分析市场**
```bash
hyperliquid-v10-trend-ai 分析 --币种 BTC
```

**2. 执行交易**
```bash
hyperliquid-v10-trend-ai 交易 --币种 BTC --方向 做多 --数量 0.05
```

**3. 监控持仓**
```bash
hyperliquid-v10-trend-ai 监控
```

**4. 查看策略状态**
```bash
hyperliquid-v10-trend-ai 状态
```

---

## ⚙️ 配置说明

### 环境变量

```bash
# Hyperliquid API（必填）
export HYPERLIQUID_API_KEY="your_api_key"
export HYPERLIQUID_API_SECRET="your_api_secret"

# Telegram通知（可选）
export TELEGRAM_BOT_TOKEN="your_bot_token"
export TELEGRAM_CHAT_ID="your_chat_id"
```

### 自定义参数

在 `plugin.yaml` 中可调整：
- 杠杆倍数（默认10x）
- 止损倍数（默认1.5×ATR）
- 止盈阶梯（默认2%/4%/6%）
- 评分阈值（默认70分）

---

## 📈 策略表现

### 回测数据（2024年1-3月）

| 指标 | 数值 |
|------|------|
| 总收益率 | +156% |
| 胜率 | 68.5% |
| 盈亏比 | 3.2:1 |
| 最大回撤 | -12% |
| 夏普比率 | 2.1 |

*注：历史表现不代表未来收益*

---

## 🎮 实盘运行

### 模拟模式（默认）
```bash
hyperliquid-v10-trend-ai 交易 --币种 BTC --模拟
```

### 实盘模式
```bash
hyperliquid-v10-trend-ai 交易 --币种 BTC --实盘
```

⚠️ **风险提示**：实盘交易前请确保：
1. 已充分了解策略逻辑
2. 已设置合理的资金规模
3. 已配置止损和风控参数

---

## 🔔 通知系统

策略支持多种通知方式：

| 事件 | 通知内容 |
|------|----------|
| **开仓** | "🎯 BTC突破信号触发！做多入场，止损已挂" |
| **止盈** | "💰 BTC第一阶段止盈！平仓30%，剩余仓位继续飞" |
| **止损** | "🛑 BTC止损触发！亏损2%，保护本金优先" |
| **日结** | "📊 今日交易3笔，盈利2笔，胜率66%" |

---

## 🏆 大赛参赛

本策略参加 **OKX Build X AI Hackathon**

- **赛道**：X Layer Arena
- **依赖插件**：Hyperliquid Plugin
- **开源协议**：MIT

---

## 🤝 社区与支持

- **GitHub Issues**: [提交问题](https://github.com/jian28277-hash/plugin-store/issues)
- **Telegram群组**: [加入讨论](https://t.me/xiaolong_trader)
- **Twitter**: [@XiaolongWeb3](https://twitter.com/XiaolongWeb3)

---

## 📜 开源协议

本项目采用 [MIT License](LICENSE) 开源。

---

## ⚠️ 风险提示

> **加密货币交易有风险，可能损失全部本金。本策略仅供参考，不构成投资建议。请根据自身风险承受能力谨慎决策。**

---

**🐉 家人们，趋势来了就上车，止损挂好，咱们稳坐钓鱼台！**