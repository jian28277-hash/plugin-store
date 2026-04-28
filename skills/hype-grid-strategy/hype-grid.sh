#!/bin/bash
# HYPE Grid Strategy - 高频网格交易脚本
# 策略ID: hype-grid-v1
# 作者: 韭菜 (@lvjwrogm)

set -e

# 配置
COIN="HYPE"
STRATEGY_ID="hype-grid-v1"
WALLET="0x3af180895d91ecd778585dbadf37f196ca89e3c1"
GRID_SPACING=0.02  # 2%
ORDER_SIZE=0.25
LEVERAGE=10

# 价格区间
PRICE_MIN=36.00
PRICE_MAX=45.00

# 当前价格获取
get_current_price() {
    # 使用 hyperliquid prices 命令获取当前价格
    hyperliquid prices --coin $COIN 2>/dev/null | grep -o '"price":"[0-9.]*"' | head -1 | cut -d'"' -f4
}

# 计算网格档位
calculate_grid_levels() {
    local current_price=$1
    local levels=()
    
    # 计算买入档位（低于当前价）
    for i in 1 2 3 4 5; do
        local buy_price=$(echo "$current_price * (1 - $GRID_SPACING * $i)" | bc -l)
        if (( $(echo "$buy_price >= $PRICE_MIN" | bc -l) )); then
            levels+=("buy:$buy_price")
        fi
    done
    
    # 计算卖出档位（高于当前价）
    for i in 1 2 3 4 5; do
        local sell_price=$(echo "$current_price * (1 + $GRID_SPACING * $i)" | bc -l)
        if (( $(echo "$sell_price <= $PRICE_MAX" | bc -l) )); then
            levels+=("sell:$sell_price")
        fi
    done
    
    echo "${levels[@]}"
}

# 执行网格交易
execute_grid() {
    local current_price=$(get_current_price)
    
    if [ -z "$current_price" ]; then
        echo "错误: 无法获取当前价格"
        exit 1
    fi
    
    echo "当前 HYPE 价格: $current_price"
    echo "策略ID: $STRATEGY_ID"
    echo "---"
    
    # 计算网格档位
    local levels=$(calculate_grid_levels $current_price)
    
    # 执行交易
    for level in $levels; do
        local side=$(echo $level | cut -d':' -f1)
        local price=$(echo $level | cut -d':' -f2)
        
        echo "挂单: $side $ORDER_SIZE HYPE @ $price"
        
        hyperliquid order \
            --coin $COIN \
            --side $side \
            --size $ORDER_SIZE \
            --price $price \
            --strategy-id $STRATEGY_ID \
            --confirm 2>/dev/null || echo "挂单失败: $side @$price"
        
        sleep 1
    done
}

# 主函数
main() {
    echo "=== HYPE Grid Strategy v1 ==="
    echo "时间: $(date)"
    echo "钱包: $WALLET"
    echo "---"
    
    execute_grid
    
    echo "---"
    echo "网格交易执行完成"
}

# 运行
main
