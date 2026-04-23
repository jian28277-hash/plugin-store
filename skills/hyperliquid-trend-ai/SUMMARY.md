# hyperliquid-trend-ai

## Overview

Hyperliquid AI Trend Strategy is an automated trend-following trading system for Hyperliquid DEX. It uses multi-timeframe technical analysis to identify high-probability entry points in BTC, ETH, and SOL perpetual markets.

Core operations:

- Multi-timeframe trend analysis (15m signals + 1h trend confirmation)
- Dynamic position sizing based on market volatility
- Automated entry and exit with trailing stops
- Risk management with daily trade limits and position caps

Tags: `hyperliquid` `trading` `strategy` `trend` `perpetual`

## Prerequisites

- Hyperliquid account with USDC deposit
- Supported assets: BTC-PERP, ETH-PERP, SOL-PERP
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
   Ask the agent to "analyze BTC trend" to get current signal

4. **Execute trade**
   When score ≥ 70, tell agent "execute BTC long with 0.05 size"
   The agent will automatically set stop-loss and take-profit

5. **Monitor positions**
   Ask "show my positions" to see P&L and stop/target levels

6. **Close or let it run**
   The strategy auto-manages exits via trailing stops and take-profits
