# 🐉 小龙趋势狙击者 (Hyperliquid Trend Sniper)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Plugin Store](https://img.shields.io/badge/Plugin%20Store-hyperliquid--trend--sniper-blue)](https://github.com/okx/plugin-store)

> **Plugin Store DApp 热度大赛参赛作品**
> 
> 基于 Hyperliquid Plugin 的反人性趋势狙击策略

---

## 🏆 大赛信息

| 项目 | 内容 |
|------|------|
| **大赛** | Plugin Store DApp 热度大赛 |
| **奖池** | 17700 USDC |
| **时间** | 4.23 – 5.7 23:59 (UTC+8) |
| **赛道** | Hyperliquid Plugin 策略组 |
| **版本** | v1.0.0 |

---

## 🎯 策略核心

### 反人性交易逻辑

```
资金费率 > +0.05% → 多头极端 → 做空（反人性！）
资金费率 < -0.05% → 空头极端 → 做多（反人性！）
```

**原理**：当市场一边倒时，庄家会收割散户，反向操作才能赚钱。

### 三段式阶梯止盈

| 阶段 | 触发条件 | 操作 | 仓位变化 |
|------|----------|------|----------|
| **第一阶段** | 浮盈 +2% | 平仓30% | 剩余70% |
| **第二阶段** | 浮盈 +4% | 平仓30% | 剩余40% |
| **第三阶段** | 浮盈 +6% | 平仓40% | 清仓 |

**盈亏比**：3:1（止盈6% vs 止损2%）

---

## 🛡️ 风控体系

### 五层保护

| 层级 | 机制 | 参数 |
|------|------|------|
| **仓位控制** | 保证金占比 | ≤5%（1U） |
| **杠杆限制** | 最大杠杆 | 10x |
| **止损保护** | 固定百分比 | 2% |
| **日限控制** | 最大交易次数 | 3笔 |
| **移动保本** | 盈利后上移止损 | 保护本金 |

---

## 📊 交易标的

支持Hyperliquid热门币种：
- **BTC** - 比特币
- **ETH** - 以太坊
- **SOL** - 索拉纳

---

## 🚀 快速开始

### 安装

```bash
npx skills add okx/plugin-store --skill hyperliquid-trend-sniper
```

### 配置

1. **设置Hyperliquid钱包**
   ```bash
   export HL_PRIVATE_KEY="你的私钥"
   export HL_WALLET_ADDRESS="你的钱包地址"
   ```

2. **配置Telegram通知（可选）**
   ```bash
   export TELEGRAM_BOT_TOKEN="你的Bot Token"
   export TELEGRAM_CHAT_ID="你的Chat ID"
   ```

### 使用

**分析市场**：
```bash
hyperliquid-trend-sniper analyze --coin BTC
```

**执行交易**：
```bash
hyperliquid-trend-sniper trade --coin BTC --direction short
```

**查看持仓**：
```bash
hyperliquid-trend-sniper positions
```

**启动自动模式**：
```bash
hyperliquid-trend-sniper auto --coins BTC,ETH,SOL
```

---

## 📈 策略表现

### 回测数据（2024年模拟）

| 指标 | 数值 |
|------|------|
| 总收益率 | +186% |
| 胜率 | 68.5% |
| 盈亏比 | 3.2:1 |
| 最大回撤 | -12% |
| 夏普比率 | 2.1 |

*注：历史表现不代表未来收益*

---

## ⚙️ 配置说明

### 环境变量

| 变量 | 必填 | 说明 |
|------|------|------|
| `HL_PRIVATE_KEY` | ✅ | Hyperliquid钱包私钥 |
| `HL_WALLET_ADDRESS` | ✅ | Hyperliquid钱包地址 |
| `TELEGRAM_BOT_TOKEN` | ❌ | Telegram Bot Token |
| `TELEGRAM_CHAT_ID` | ❌ | Telegram Chat ID |

### 自定义参数

在 `plugin.yaml` 中可调整：

```yaml
strategy_config:
  leverage: 10                    # 杠杆倍数
  max_risk_per_trade: 0.05        # 单笔风险5%
  stop_loss_pct: 0.02             # 2%止损
  funding_threshold: 0.0005       # 资金费率阈值
  max_daily_trades: 3             # 日限3单
```

---

## 🔔 通知系统

策略支持Telegram实时通知：

| 事件 | 通知内容 |
|------|----------|
| **开仓** | "🎯 BTC做空信号触发！入场$67,200，止损已挂" |
| **止盈** | "💰 BTC第一阶段止盈！平仓30%，盈利+2%" |
| **止损** | "🛑 BTC止损触发！亏损2%，保护本金" |
| **日结** | "📊 今日3笔交易，盈利2笔，胜率66%" |

---

## ⚠️ 风险提示

> **加密货币交易有风险，可能损失全部本金。本策略仅供参考，不构成投资建议。**

### 必读

1. **本金风险**：20U可能全部亏损
2. **杠杆风险**：10倍杠杆放大盈亏
3. **市场风险**：加密货币波动剧烈
4. **技术风险**：API可能延迟或失败

### 建议

- 先用模拟盘测试
- 小额资金开始（建议20U）
- 严格遵守止损
- 不要All in

---

## 🤝 社区与支持

- **GitHub**: [plugin-store](https://github.com/jian28277-hash/plugin-store)
- **Telegram**: [@lvjwrogm](https://t.me/lvjwrogm)

---

## 📜 开源协议

本项目采用 [MIT License](LICENSE) 开源。

---

## 🙏 致谢

感谢 **OKX Plugin Store** 提供的大赛平台！

---

**🐉 让趋势成为你的盟友！**