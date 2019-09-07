import re
from cProfile import Profile

def analyze_profiler(profiler: Profile):
    methods = [
        '__add__',
        '__sub__',
        '__mul__',
        '__div__',
        '__pow__',
        'invert',
        '_convert'
    ]
    stats = profiler.getstats()
    stats = filter(lambda row: re.match('.*modularinteger', row.code.co_filename) is not None, stats)
    stats = filter(lambda row: row.code.co_name in methods, stats)
    stats = map(lambda row: (row.code.co_name, row.callcount), stats)
    stats = map(lambda entry: (entry[0].strip('_'), entry[1]), stats)
    total_count = sum((entry[1] for entry in stats), 0)
    return {'total_count': total_count, 'detailed_usage': stats}
