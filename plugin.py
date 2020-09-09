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
avg_change = 0

for symbol in symbols:
    data, _ = ts.get_quote_endpoint(symbol)

    change = data['10. change percent']

    results_dict[symbol] = (data['05. price'], change)

    change_substr = change[:-1]
    avg_change = avg_change + float(change_substr)


