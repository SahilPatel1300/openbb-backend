indicators = [
    {
        'name': 'ad',
        'params': {'offset': 0},
        'value_key': 'AD'
    },
    {
        'name': 'adosc',
        'params': {'fast': 3, 'slow': 10, 'offset': 0},
        'value_key': 'ADOSC_3_10'
    },
    {
        'name': 'adx',
        'params': {'length': 50, 'scalar': 100, 'drift': 1},
        'keys': ['ADX_50', 'DMP_50', 'DMN_50']
    },
    {
        'name': 'aroon',
        'params': {'length': 25, 'scalar': 100},
        'value_key': 'AROONOSC_25'
    },
    {
        'name': 'atr',
        'params': {},
        'value_key': 'ATRr_14'
    },
    {
        'name': 'bbands',
        'params': {'target': 'close', 'length': 50, 'std': 2, 'mamode': 'sma'},
        'keys': ['close_BBL_50_2.0', 'close_BBM_50_2.0', 'close_BBU_50_2.0', 'close_BBB_50_2.0']
    },
    {
        'name': 'cci',
        'params': {'length': 14, 'scalar': 0.015},
        'value_key': 'CCI_14_0.015'
    },
    {
        'name': 'cg',
        'params': {'length': 14},
        'value_key': 'CG_14'
    },
    {
        'name': 'clenow',
        'params': {'period': 90},
        'keys': ['r^2', 'fit_coef', 'factor']
    },
    {
        'name': 'cones',
        'params': {'lower_q': 0.25, 'upper_q': 0.75, 'model': 'std'},
        'keys': ['window', 'realized', 'min', 'lower_25%', 'median', 'upper_75%', 'max']
    },
    {
        'name': 'demark',
        'params': {'offset': 0},
        'keys': ['TD_SEQ_UPa', 'TD_SEQ_DNa']
    },
    {
        'name': 'donchian',
        'params': {'lower_length': 20, 'upper_length': 20, 'offset': 0},
        'keys': ['DCL_20_20', 'DCM_20_20', 'DCU_20_20']
    },
    {
        'name': 'ema',
        'params': {'target': 'close', 'length': 50, 'offset': 0},
        'value_key': 'close_EMA_50'
    },
    {
        'name': 'fib',
        'params': {'period': 120},
        'keys': ['Level', 'Price', 'max_pr']
    },
    {
        'name': 'fisher',
        'params': {'length': 14, 'signal': 1},
        'keys': ['FISHERT_14_1', 'FISHERTs_14_1']
    },
    {
        'name': 'hma',
        'params': {'target': 'close', 'length': 50, 'offset': 0},
        'value_key': 'close_HMA_50'
    },
    {
        'name': 'ichimoku',
        'params': {'conversion': 9, 'base': 26, 'lookahead': False},
        'keys': ['span_ISA_9', 'span_ISB_26', 'ISA_9', 'ISB_26', 'ITS_9', 'IKS_26']
    },
    {
        'name': 'kc',
        'params': {'length': 20, 'scalar': 20, 'mamode': 'ema', 'offset': 0},
        'keys': ['KCLe_20_20.0', 'KCBe_20_20.0', 'KCUe_20_20.0']
    },
    {
        'name': 'macd',
        'params': {'target': 'close', 'fast': 12, 'slow': 26, 'signal': 9},
        'value_key': 'close_MACD_12_26_9'
    },
    {
        'name': 'obv',
        'params': {'offset': 0},
        'value_key': 'OBV'
    },
    {
        'name': 'rsi',
        'params': {'target': 'close', 'length': 14, 'scalar': 100.0, 'drift': 1},
        'value_key': 'close_RSI_14'
    },
    {
        'name': 'sma',
        'params': {'target': 'close', 'length': 50, 'offset': 0},
        'value_key': 'close_SMA_50'
    },
    {
        'name': 'stoch',
        'params': {'fast_k_period': 14, 'slow_d_period': 3, 'slow_k_period': 3},
        'keys': ['STOCHk_14_3_3', 'STOCHd_14_3_3']
    },
    {
        'name': 'vwap',
        'params': {'anchor': 'D', 'offset': 0},
        'value_key': 'VWAP_D'
    },
    {
        'name': 'wma',
        'params': {'target': 'close', 'length': 50, 'offset': 0},
        'value_key': 'close_WMA_50'
    },
    {
        'name': 'zlma',
        'params': {'target': 'close', 'length': 50, 'offset': 0},
        'value_key': 'close_ZL_EMA_50'
    }
]
