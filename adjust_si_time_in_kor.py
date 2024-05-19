"""
This file exposes a function adjust_si_time_in_kor that can be used to adjust
times of SI units in .kor files used bu the program Fjww.

NOTE! Please verify that adjustments made by this program has been made correctly
for all participants with a diff tool such as WinMerge!

This file does not handle the following cases:
 * Sub second time
 * Date (if competition goes over midnight)

2024-05-19 Mattias Eriksson. Initial code to handle time offsets of SI-units for N2 competition
"""
from datetime import timedelta
from datetime import datetime
import re

def adjust_si_time_in_kor(input_kor_path, si_diff_dict):
    output_kor_path = re.sub('.kor$', '_adjusted.kor', input_kor_path)

    def si_time_repl(matchobj):
        time = datetime.strptime(matchobj.group(1), '%H:%M:%S')
        si_unit = matchobj.group(2)
        if si_unit in si_diff_dict:
            time = time + si_diff_dict[si_unit]

        # Replace old time with new adjusted time
        return matchobj.group(0).replace(matchobj.group(1), time.strftime('%H:%M:%S'))


    # Open and read file
    f = open(input_kor_path, "r", encoding="utf-8")
    content = f.read()
    f.close()

    # Typical line in .kor file:
    #    4  6 10:14:02'00 19.5.24 0; @id25812 @si43
    content = re.sub(r"[\n\r]+ *\d+ *\d+ +(\d\d:\d\d:\d\d)'\d\d.+\@(si\d+)", si_time_repl, content)

    # Write new content to file
    f = open(output_kor_path, "w", encoding="utf-8")
    f.write(content)
    f.close()
