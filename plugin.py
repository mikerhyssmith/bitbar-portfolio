#!/usr/bin/env PYTHONIOENCODING=UTF-8 /home/mike/.pyenv/shims/python

# <bitbar.title>Portfolio</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>mikerhyssmith</bitbar.author>
# <bitbar.author.github>mikerhyssmith</bitbar.author.github>
# <bitbar.desc>Simple portfolio monitor</bitbar.desc>
# <bitbar.image>http://www.hosted-somewhere/pluginimage</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>

import os
from alpha_vantage.timeseries import TimeSeries

symbols = ['lgen.l']
ts = TimeSeries(output_format='json')

results_dict = {}
change = 0

for symbol in symbols:
    data, _ = ts.get_quote_endpoint(symbol)

    symbol_change = data['10. change percent']

    results_dict[symbol] = (data['05. price'], symbol_change)

    change_substr = symbol_change[:-1]
    change = change + float(change_substr)

avg_change = change / len(symbols)
is_positive = avg_change > 0
is_negative = avg_change < 0
is_neutral = avg_change == 0

if is_positive:
    print(f'📈 Portfolio up by {avg_change}% | color=green')
elif is_negative:
    print(f'📉 Portfolio down by {avg_change}% | color=red')
elif is_neutral:
    print('Porfolio changed by 0%')

print('---')

for entry in results_dict.items():
    symbol, values = entry
    print(f'{symbol.upper()}: {values[0]}  {values[1]}')
