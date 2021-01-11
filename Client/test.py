import sys
import platform

func = platform.system().lower()
info_data = func()
print(info_data)
