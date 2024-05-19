from datetime import timedelta
from adjust_si_time_in_kor import adjust_si_time_in_kor

################################# README ####################################
# Please verify that adjustments made by this program has been made correctly
# for all participants with a diff tool such as WinMerge!
#
# This file does not handle the following cases:
#  * Sub second time
#  * Date (if competition goes over midnight)
#
# 2024-05-19 Mattias Eriksson. Initial code to handle time offsets of SI-units for N2 competition

# N2 2024 3.5 MHz
si_diff_3_5 = {
    'si37': -timedelta(minutes = 4, seconds = 45), # Fox 3
    'si33': -timedelta(minutes = 5, seconds = 1),  # Fox 2
    'si48': -timedelta(minutes = 3, seconds = 50), # Fox 5
    'si46': -timedelta(minutes = 4, seconds = 28), # Fox 4
    'si32': -timedelta(minutes = 4, seconds = 14), # Fox 1
    'si4': -timedelta(minutes = 0, seconds = 10), # Finish
}

# N2 2024 144 MHz
si_diff_144 = {
    'si41': -timedelta(minutes = 5, seconds = 0),  # Fox 4
    'si42': -timedelta(minutes = 4, seconds = 36), # Fox 5
    'si40': -timedelta(minutes = 4, seconds = 41), # Fox 1
    'si39': -timedelta(minutes = 4, seconds = 12), # Fox 3
    'si43': -timedelta(minutes = 4, seconds = 41), # Fox 2
    'si4': -timedelta(minutes = 0, seconds = 10), # Finish
}

adjust_si_time_in_kor(r"C:\Mattias\Privat\Rävjakt\N2 2024\3.5MHz\N2_2024_3.5MHz.kor", si_diff_3_5)
adjust_si_time_in_kor(r"C:\Mattias\Privat\Rävjakt\N2 2024\144MHz\N2_2024_144MHz.kor", si_diff_144)
