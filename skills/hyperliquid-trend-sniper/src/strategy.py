#!/usr/bin/env python3
"""
小龙趋势狙击者 - Hyperliquid Plugin策略
Plugin Store DApp 热度大赛参赛作品

核心逻辑：
1. 监控Hyperliquid资金费率
2. 极端情绪时反向交易（反人性）
3. 三段式阶梯止盈
4. 严格风控保护本金
"""

import os
import time
import json
import requests
from datetime import datetime
from typing import Dict, Optional, List

# Hyperliquid API配置
HL_API_URL = "https://api.hyperliquid.xyz/info"

class HyperliquidAPI:
    """Hyperliquid API封装"""
    
    def __init__(self):
        self.session = requests.Session()
    
    def _post(self, payload: dict) -> Optional[dict]:
        """发送POST请求"""
        try:
            response = self.session.post(HL_API_URL, json=payload, timeout=30)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"API请求失败: {e}")
            return None
    
    def get_all_mids(self) -> Dict[str, float]:
        """获取所有币种当前价格"""
        result = self._post({"type": "allMids"})
        if result:
            return {k: float(v) for k, v in result.items()}
        return {}
    
    def get_funding_history(self, coin: str, limit: int = 3) -> List[dict]:
        """获取资金费率历史"""
        now = int(time.time() * 1000)
        result = self._post({
            "type": "fundingHistory",
            "coin": coin,
            "startTime": now - 86400000 * 7,  # 7天
            "endTime": now
        })
        if result and isinstance(result, list):
            return result[-limit:]
        return []
    
    def get_candle_snapshot(self, coin: str, interval: str = "15m", limit: int = 20) -> List[dict]:
        """获取K线数据"""
        now = int(time.time() * 1000)
        result = self._post({
            "type": "candleSnapshot",
            "req": {
                "coin": coin,
                "interval": interval,
                "startTime": now - limit * 15 * 60 * 1000,
                "endTime": now
            }
        })
        if result and isinstance(result, list):
            return result
        return []

class TrendSniperStrategy:
    """
    小龙趋势狙击者策略
    
    核心逻辑：
    1. 反人性判断：资金费率极端时反向交易
    2. 三段式止盈：2%/4%/6%分阶段平仓
    3. 严格风控：2%止损 + 10倍杠杆 + 5%风险
    """
    
    def __init__(self, config: dict = None):
        self.api = HyperliquidAPI()
        self.config = config or {}
        
        # 默认配置
        self.leverage = self.config.get("leverage", 10)
        self.max_risk = self.config.get("max_risk_per_trade", 0.05)
        self.stop_loss_pct = self.config.get("stop_loss_pct", 0.02)
        self.funding_threshold = self.config.get("funding_threshold", 0.0005)
        self.max_daily_trades = self.config.get("max_daily_trades", 3)
        self.max_positions = self.config.get("max_positions", 2)
        
        # 交易对
        self.coins = self.config.get("trading_pairs", ["BTC", "ETH", "SOL"])
        
        # 状态
        self.daily_trades = 0
        self.positions = {}
        self.balance = 20  # 默认20U
    
    def analyze_funding_rate(self, coin: str) -> dict:
        """
        分析资金费率（反人性核心）
        
        Returns:
            {
                "funding": float,      # 当前资金费率
                "sentiment": str,      # extreme_long / extreme_short / neutral
                "score": int,          # 0-100评分
                "signal": str,         # long / short / none
                "reason": str          # 原因说明
            }
        """
        # 获取资金费率历史
        funding_history = self.api.get_funding_history(coin, limit=3)
        
        if not funding_history:
            return {
                "funding": 0,
                "sentiment": "neutral",
                "score": 50,
                "signal": "none",
                "reason": "无法获取资金费率"
            }
        
        # 最新资金费率
        latest = funding_history[-1]
        funding_rate = float(latest.get("fundingRate", 0))
        
        # 判断极端情绪
        if funding_rate > self.funding_threshold:
            # 多头付空头，说明多头多 → 做空（反人性）
            return {
                "funding": funding_rate,
                "sentiment": "extreme_long",
                "score": 20,  # 低分 = 做空信号
                "signal": "short",
                "reason": f"多头极端(资金费率+{funding_rate*100:.4f}%)，反向做空"
            }
        elif funding_rate < -self.funding_threshold:
            # 空头付多头，说明空头多 → 做多（反人性）
            return {
                "funding": funding_rate,
                "sentiment": "extreme_short",
                "score": 80,  # 高分 = 做多信号
                "signal": "long",
                "reason": f"空头极端(资金费率{funding_rate*100:.4f}%)，反向做多"
            }
        else:
            return {
                "funding": funding_rate,
                "sentiment": "neutral",
                "score": 50,
                "signal": "none",
                "reason": f"情绪正常(资金费率{funding_rate*100:.4f}%)"
            }
    
    def analyze_technical(self, coin: str) -> dict:
        """
        技术分析确认
        
        Returns:
            {
                "trend": str,      # up / down / neutral
                "score": int,      # 0-100
                "price": float,    # 当前价格
                "sma5": float,     # 5周期均线
                "sma10": float     # 10周期均线
            }
        """
        # 获取K线数据
        candles = self.api.get_candle_snapshot(coin, "15m", 20)
        
        if not candles or len(candles) < 10:
            return {
                "trend": "neutral",
                "score": 50,
                "price": 0,
                "sma5": 0,
                "sma10": 0
            }
        
        # 提取收盘价
        closes = [float(c["c"]) for c in candles]
        current_price = closes[-1]
        
        # 计算均线
        sma5 = sum(closes[-5:]) / 5
        sma10 = sum(closes[-10:]) / 10
        
        # 判断趋势
        if current_price > sma5 > sma10:
            trend = "up"
            score = 60
        elif current_price < sma5 < sma10:
            trend = "down"
            score = 40
        else:
            trend = "neutral"
            score = 50
        
        return {
            "trend": trend,
            "score": score,
            "price": current_price,
            "sma5": sma5,
            "sma10": sma10
        }
    
    def generate_signal(self, coin: str) -> dict:
        """
        生成交易信号
        
        综合资金费率（反人性）+ 技术分析
        """
        print(f"\n📊 分析 {coin}...")
        
        # 1. 资金费率分析（权重60%）
        funding = self.analyze_funding_rate(coin)
        print(f"   资金费率: {funding['funding']*100:.4f}%")
        print(f"   情绪: {funding['sentiment']}")
        print(f"   信号: {funding['signal']}")
        
        # 2. 技术分析（权重40%）
        technical = self.analyze_technical(coin)
        print(f"   价格: {technical['price']:.2f}")
        print(f"   趋势: {technical['trend']}")
        
        # 3. 综合评分
        # 反人性为主，技术确认
        if funding["signal"] == "long" and technical["trend"] == "up":
            # 多头信号 + 上涨趋势 = 强做多信号
            final_signal = "long"
            final_score = 90
        elif funding["signal"] == "short" and technical["trend"] == "down":
            # 空头信号 + 下跌趋势 = 强做空信号
            final_signal = "short"
            final_score = 10  # 低分表示做空
        elif funding["signal"] != "none":
            # 有信号但技术不匹配，降低置信度
            final_signal = funding["signal"]
            final_score = 70 if funding["signal"] == "long" else 30
        else:
            final_signal = "none"
            final_score = 50
        
        return {
            "coin": coin,
            "signal": final_signal,
            "score": final_score,
            "price": technical["price"],
            "funding": funding,
            "technical": technical,
            "timestamp": datetime.now().isoformat()
        }
    
    def calculate_position(self, signal: dict) -> dict:
        """
        计算仓位
        
        严格风控：
        - 保证金 = 本金 × 5%
        - 名义仓位 = 保证金 × 10倍杠杆
        """
        price = signal["price"]
        if not price:
            return None
        
        # 计算保证金（5%风险）
        margin = self.balance * self.max_risk
        
        # 名义仓位（10倍杠杆）
        notional = margin * self.leverage
        
        # 数量
        qty = notional / price
        
        # 止损价
        if signal["signal"] == "long":
            stop_loss = price * (1 - self.stop_loss_pct)
            take_profit_1 = price * 1.02
            take_profit_2 = price * 1.04
            take_profit_3 = price * 1.06
        else:
            stop_loss = price * (1 + self.stop_loss_pct)
            take_profit_1 = price * 0.98
            take_profit_2 = price * 0.96
            take_profit_3 = price * 0.94
        
        return {
            "margin": margin,
            "notional": notional,
            "qty": qty,
            "price": price,
            "leverage": self.leverage,
            "stop_loss": stop_loss,
            "take_profit_1": take_profit_1,
            "take_profit_2": take_profit_2,
            "take_profit_3": take_profit_3
        }
    
    def execute_trade(self, signal: dict, position: dict) -> bool:
        """
        执行交易
        
        实际使用时通过Hyperliquid Plugin下单
        """
        print(f"\n{'='*60}")
        print(f"🎯 交易信号确认")
        print(f"{'='*60}")
        print(f"币种: {signal['coin']}")
        print(f"方向: {signal['signal'].upper()}")
        print(f"评分: {signal['score']}/100")
        print(f"-")
        print(f"当前价格: {position['price']:.2f}")
        print(f"保证金: {position['margin']:.2f} USDC")
        print(f"杠杆: {position['leverage']}x")
        print(f"名义仓位: {position['notional']:.2f} USDC")
        print(f"数量: {position['qty']:.6f}")
        print(f"-")
        print(f"止损价: {position['stop_loss']:.2f}")
        print(f"止盈1: {position['take_profit_1']:.2f} (+2%)")
        print(f"止盈2: {position['take_profit_2']:.2f} (+4%)")
        print(f"止盈3: {position['take_profit_3']:.2f} (+6%)")
        print(f"{'='*60}")
        
        # 确认交易（实际使用时自动执行）
        print("\n📤 正在通过Hyperliquid Plugin下单...")
        print("✅ 订单已提交（模拟）")
        
        self.daily_trades += 1
        return True
    
    def run_scan(self):
        """扫描市场"""
        print(f"\n{'='*60}")
        print(f"🔍 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 扫描市场")
        print(f"💰 本金: {self.balance}U | 今日: {self.daily_trades}/{self.max_daily_trades}单")
        print(f"{'='*60}")
        
        # 检查日限
        if self.daily_trades >= self.max_daily_trades:
            print("\n🚫 今日交易已满，停止扫描")
            return False
        
        signals = []
        
        for coin in self.coins:
            # 生成信号
            signal = self.generate_signal(coin)
            
            if signal["signal"] != "none":
                # 计算仓位
                position = self.calculate_position(signal)
                
                if position:
                    signals.append({
                        "signal": signal,
                        "position": position
                    })
            else:
                print(f"   💤 无交易信号\n")
        
        return signals
    
    def run(self):
        """主循环"""
        print("\n" + "="*60)
        print("🐉 小龙趋势狙击者 - Hyperliquid Plugin策略")
        print("="*60)
        print("Plugin Store DApp 热度大赛参赛作品")
        print("="*60)
        print(f"\n📊 配置参数:")
        print(f"   杠杆: {self.leverage}x")
        print(f"   单笔风险: {self.max_risk*100}%")
        print(f"   止损: {self.stop_loss_pct*100}%")
        print(f"   资金费率阈值: {self.funding_threshold*100}%")
        print(f"   日限: {self.max_daily_trades}单")
        print(f"   交易对: {', '.join(self.coins)}")
        print("="*60 + "\n")
        
        while True:
            try:
                # 扫描市场
                signals = self.run_scan()
                
                if signals:
                    print(f"\n🎯 发现 {len(signals)} 个交易信号！")
                    
                    for item in signals:
                        self.execute_trade(item["signal"], item["position"])
                
                # 等待
                print(f"\n⏳ 等待5分钟...")
                time.sleep(300)
                
            except KeyboardInterrupt:
                print("\n\n🛑 策略停止")
                break
            except Exception as e:
                print(f"\n⚠️ 错误: {e}")
                time.sleep(60)

# CLI接口
def main():
    """命令行入口"""
    import argparse
    
    parser = argparse.ArgumentParser(description="小龙趋势狙击者")
    parser.add_argument("--coins", default="BTC,ETH,SOL", help="交易对，逗号分隔")
    parser.add_argument("--balance", type=float, default=20, help="本金（U）")
    parser.add_argument("--leverage", type=int, default=10, help="杠杆")
    parser.add_argument("--risk", type=float, default=0.05, help="单笔风险")
    
    args = parser.parse_args()
    
    # 配置
    config = {
        "trading_pairs": args.coins.split(","),
        "leverage": args.leverage,
        "max_risk_per_trade": args.risk
    }
    
    # 创建策略
    strategy = TrendSniperStrategy(config)
    strategy.balance = args.balance
    
    # 运行
    strategy.run()

if __name__ == "__main__":
    main()
