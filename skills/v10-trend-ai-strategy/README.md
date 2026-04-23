# V10.0 全市场趋势跟踪AI策略

## 参赛说明

本策略参加 **OKX AI Trading大赛**，基于 OKX CEX Trade Kit 构建。

## 策略特点

- **AI四维度评分**：趋势(40%) + 动量(25%) + 突破(30%) + 波动率(5%)
- **高确信信号**：满分100分，70分以上才开仓
- **双时间框架**：15分钟找信号，1小时定方向
- **智能风控**：2%止损 + 6%止盈 + 3:1盈亏比 + 移动保本
- **严格限制**：最多2持仓、日限3笔、余额<50U停止

## 安装

```bash
npx skills add okx/plugin-store --skill v10-trend-ai-strategy
```

## 使用

1. 分析市场：`v10-trend-ai-strategy 分析 --币种 BTC`
2. 执行交易：`v10-trend-ai-strategy 交易 --币种 BTC --方向 做多 --数量 0.01`
3. 监控持仓：`v10-trend-ai-strategy 监控`

## 风险提示

- 默认启用模拟模式（--dry-run），实盘需关闭
- 加密货币交易有风险，可能损失全部本金
- 过去表现不代表未来收益

## 开源地址

GitHub: https://github.com/trader-ai/v10-trend-ai-strategy
