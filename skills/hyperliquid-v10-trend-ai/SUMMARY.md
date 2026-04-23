# hyperliquid-v10-trend-ai

## Overview

Hyperliquid V10.0 Trend AI Strategy is an automated trend-following trading system built on Hyperliquid Plugin. It uses a multi-dimensional scoring system to identify high-probability trading opportunities and execute trades automatically on Hyperliquid DEX.

Core operations:

- Multi-timeframe analysis (15m signals + 1h trend confirmation)
- 4-dimension scoring system (max 100 points, entry threshold 70)
- Automatic position sizing based on volatility
- Smart risk management with trailing stops and breakeven protection
- Maximum 2 concurrent positions, 3 trades per day

Tags: `hyperliquid` `trend-following` `AI-strategy` `automated-trading` `risk-management`

## Prerequisites

- Hyperliquid account with USDC deposit
- Supported assets: BTC-PERP, ETH-PERP, SOL-PERP, XRP-PERP, DOGE-PERP, ADA-PERP, LINK-PERP, LTC-PERP
- Minimum account size: $100 USDC recommended
- Risk tolerance: Medium-High (5x max leverage, 2% stop loss)
- Plugin dependency: hyperliquid-plugin
- Paper trading available via --dry-run flag

## Quick Start

1. **Install dependencies**
   Install hyperliquid-plugin: `npx skills add okx/plugin-store --skill hyperliquid-plugin`

2. **Configure risk parameters**
   Set your max leverage (default 5x) and position size (default 20% of equity)

3. **Run analysis**
   Ask the agent to "分析 BTC 趋势" to get current signal

4. **Execute trade**
   When score ≥ 70, tell agent "执行 BTC 做多，数量 0.05"
   The agent will automatically set stop-loss and take-profit

5. **Monitor positions**
   Ask "显示我的持仓" to see P&L and stop/target levels

6. **Auto-management**
   The strategy auto-manages exits via trailing stops and take-profits
