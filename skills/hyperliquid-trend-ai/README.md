# Hyperliquid AI Trend Strategy

## 参赛说明

本策略参加 **Plugin Store DApp 热度大赛**，基于 Hyperliquid Plugin 构建。

## 策略特点

- **多时间框架分析**：15分钟信号 + 1小时趋势确认
- **AI评分系统**：4维度评分（趋势40% + 动量25% + 突破30% + 波动率5%）
- **智能风控**：2%止损、6%止盈、3:1盈亏比、移动保本
- **严格限制**：最多2持仓、日限3笔、评分≥70才开仓

## 安装

```bash
npx skills add okx/plugin-store --skill hyperliquid-trend-ai
```

## 使用

1. 分析市场：`hyperliquid-trend-ai analyze --asset BTC`
2. 执行交易：`hyperliquid-trend-ai trade --asset BTC --side long --size 0.05`
3. 监控持仓：`hyperliquid-trend-ai monitor`

## 风险提示

- 默认启用模拟模式（--dry-run），实盘需关闭
- 加密货币交易有风险，可能损失全部本金
- 过去表现不代表未来收益

## 开源地址

GitHub: https://github.com/trader-ai/hyperliquid-trend-ai
