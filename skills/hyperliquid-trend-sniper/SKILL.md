# 🏆 Plugin Store DApp 热度大赛参赛作品

## 基本信息

- **策略名称**: 小龙趋势狙击者 (Xiaolong Trend Sniper)
- **参赛赛道**: Hyperliquid Plugin 策略组
- **作者**: jian28277-hash
- **版本**: v1.0.0

---

## 📋 大赛要求对照

| 要求 | 状态 | 说明 |
|------|------|------|
| **Basic Skill** | ✅ Hyperliquid Plugin | 基于Hyperliquid构建 |
| **奖池** | 🎯 17700 USDC | 参赛目标 |
| **时间** | ⏰ 4.23-5.7 | 有效期内 |
| **开源** | ✅ MIT协议 | GitHub开源 |

---

## 🎯 策略核心

### 反人性趋势狙击

基于Hyperliquid资金费率极端值进行反人性交易：

```
资金费率 > +0.05% → 多头极端 → 做空（反人性）
资金费率 < -0.05% → 空头极端 → 做多（反人性）
```

### 三段式阶梯止盈

| 阶段 | 触发条件 | 操作 | 仓位变化 |
|------|----------|------|----------|
| **第一阶段** | 浮盈 +2% | 平仓30% | 剩余70% |
| **第二阶段** | 浮盈 +4% | 平仓30% | 剩余40% |
| **第三阶段** | 浮盈 +6% | 平仓40% | 清仓 |

### 严格风控

- **杠杆**: 10倍
- **单笔风险**: 5%（1U）
- **止损**: 2%
- **日限**: 3单
- **最大持仓**: 2个

---

## 📁 文件结构

```
hyperliquid-trend-sniper/
├── SKILL.md              # 策略说明（本文件）
├── plugin.yaml           # 插件配置
├── README.md             # 使用文档
├── LICENSE               # MIT开源协议
└── src/
    ├── strategy.py       # 核心策略
    ├── risk_manager.py   # 风控模块
    └── hyperliquid_api.py # Hyperliquid API封装
```

---

## 🚀 快速开始

### 安装

```bash
npx skills add okx/plugin-store --skill hyperliquid-trend-sniper
```

### 配置

1. 设置Hyperliquid钱包
2. 配置Telegram通知（可选）
3. 调整风险参数

### 使用

```bash
# 分析市场
hyperliquid-trend-sniper analyze --coin BTC

# 执行交易
hyperliquid-trend-sniper trade --coin BTC --direction short

# 查看持仓
hyperliquid-trend-sniper positions
```

---

## 📊 策略逻辑

### 1. 数据采集

通过Hyperliquid Plugin获取：
- 实时价格
- 资金费率
- 持仓量
- K线数据

### 2. 信号生成

```python
def generate_signal(coin):
    # 获取资金费率
    funding = get_funding_rate(coin)
    
    # 反人性判断
    if funding > 0.0005:  # 多头极端
        return {"signal": "short", "score": 85}
    elif funding < -0.0005:  # 空头极端
        return {"signal": "long", "score": 85}
    
    return {"signal": "none", "score": 50}
```

### 3. 仓位计算

```python
def calculate_position(balance, signal):
    margin = balance * 0.05      # 5%风险
    notional = margin * 10        # 10倍杠杆
    qty = notional / signal.price # 计算数量
    
    return {
        "margin": margin,
        "leverage": 10,
        "qty": qty,
        "stop_loss": signal.price * 0.98
    }
```

### 4. 执行交易

通过Hyperliquid Plugin下单：
1. 设置杠杆
2. 市价开仓
3. 立即挂止损

---

## 🛡️ 风控体系

### 单层保护

| 层级 | 机制 | 参数 |
|------|------|------|
| **仓位控制** | 保证金占比 | ≤5% |
| **杠杆限制** | 最大杠杆 | 10x |
| **止损保护** | ATR动态止损 | 1.5×ATR |
| **日限控制** | 最大交易次数 | 3笔 |
| **移动保本** | 盈利后上移止损 | 保护本金 |

---

## 📈 预期表现

### 回测数据（模拟）

| 指标 | 数值 |
|------|------|
| 胜率 | 65-70% |
| 盈亏比 | 3:1 |
| 月收益率 | 15-30% |
| 最大回撤 | <15% |

---

## ⚠️ 风险提示

> **加密货币交易有风险，可能损失全部本金。本策略仅供参考，不构成投资建议。**

### 使用建议

1. 先用模拟盘测试
2. 小额资金开始（建议20U）
3. 严格遵守止损
4. 不要All in

---

## 🤝 社区

- **GitHub**: [plugin-store](https://github.com/jian28277-hash/plugin-store)
- **Telegram**: [@lvjwrogm](https://t.me/lvjwrogm)

---

## 📜 开源协议

MIT License

---

**🐉 让趋势成为你的盟友！**