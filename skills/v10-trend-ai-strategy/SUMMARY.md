# v10-trend-ai-strategy

## Overview

V10.0 is an AI-powered trend-following trading strategy for OKX exchange. It uses a multi-dimensional scoring system (trend + momentum + breakout + volatility) to identify high-probability trading opportunities across 8 major cryptocurrencies.

Core operations:

- Multi-timeframe analysis (15m signals + 1h trend confirmation)
- 4-dimension scoring system (max 100 points, entry threshold 70)
- Automatic position sizing based on volatility
- Smart risk management with trailing stops and breakeven protection
- Maximum 2 concurrent positions, 3 trades per day

Tags: `trend-following` `AI-strategy` `automated-trading` `risk-management` `okx`

## Prerequisites

- OKX account with USDT deposit
- Supported assets: BTC-USDT-SWAP, ETH-USDT-SWAP, SOL-USDT-SWAP, XRP-USDT-SWAP, DOGE-USDT-SWAP, ADA-USDT-SWAP, LINK-USDT-SWAP, LTC-USDT-SWAP
- Minimum account size: $100 USDT recommended
- Risk tolerance: Medium-High (5x max leverage, 2% stop loss)
- Plugin dependencies: okx-cex-trade, okx-cex-market, okx-cex-portfolio
- Paper trading available via --dry-run flag

## Quick Start

1. **Install dependencies**
   Install required plugins:
   ```
   npx skills add okx/plugin-store --skill okx-cex-trade
   npx skills add okx/plugin-store --skill okx-cex-market
   npx skills add okx/plugin-store --skill okx-cex-portfolio
   ```

2. **Configure risk parameters**
   Set your max leverage (default 5x) and position size (default 20% of equity)

3. **Run analysis**
   Ask the agent to "分析 BTC 趋势" to get current signal

4. **Execute trade**
   When score ≥ 70, tell agent "执行 BTC 做多，数量 0.01"
   The agent will automatically set stop-loss and take-profit

5. **Monitor positions**
   Ask "显示我的持仓" to see P&L and stop/target levels

6. **Auto-management**
   The strategy auto-manages exits via trailing stops and take-profits
