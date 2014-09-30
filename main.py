#      _   _        __   __
#     /_\ | |__ _ _ \ \ / /_ _ _ _ __ _ ___
#    / _ \| / _` | ' \ V / _` | '_/ _` / _ \
#   /_/ \_\_\__,_|_||_\_/\__,_|_| \__, \___/
#                                 |___/
# execute programm by subprocess
import subprocess

p = subprocess.Popen(['Python', 'client_multi_xor.py'], shell = True , stdout = subprocess.PIPE)
