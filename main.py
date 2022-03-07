import subprocess
import re
import time
import os 

PID_COLUMN = 4
W_LEN = 10
TIME_N = 0.5

time1 = 0
flag = False
while True:
    while time.time() < time1 + TIME_N: pass
    # GPU使用状況を取得
    smi = subprocess.run(['nvidia-smi'], encoding='utf-8', stdout=subprocess.PIPE)
    smi_list = smi.stdout.split("\n")

    # プロセスが書かれてる枠
    processes_list = []
    s_idx = 0
    e_idx = 0
    for i, value in enumerate(smi_list):
        if "Processes" in value:
            s_idx = i - 1
        if value[:2] == "+-":
            e_idx = i + 1
    processes_list = smi_list[s_idx: e_idx]

    # PID取得
    pid_list = []
    for value in processes_list[5:-1]:
        if value[:5] == "|  No": 
            for i in smi_list:
                print(i)
            exit()
        pid_list.append(re.split(" +", value)[PID_COLUMN])

    # プロセス一覧取得
    ps = subprocess.run(["ps", "-ef"], encoding='utf-8', stdout=subprocess.PIPE)
    ps_list = ps.stdout.split("\n")

    # PID→USERの辞書を作成
    pid_user_dict = dict()
    for value in ps_list:
        if not value or value[:4] == "UID": continue
        user, pid = re.split(" +", value)[:2]
        pid_user_dict[pid] = user

    # 後ろにくっつける
    processes_list = list(map(lambda x: x[:-1], processes_list))
    processes_list[0] = f"{processes_list[0]}{'-'*W_LEN}+"
    processes_list[1] = f"{processes_list[1]} {' ':8s} |"
    processes_list[2] = f"{processes_list[2]} {'USER':8s} |"
    processes_list[3] = f"{processes_list[3]} {' ':8s} |"
    processes_list[4] = f"{processes_list[4]}{'='*W_LEN}|"
    for i, value in enumerate(processes_list[5:-1]):
        processes_list[i + 5] = f"{value} {pid_user_dict[pid_list[i]]:8s} |"
    processes_list[-1] = f"{processes_list[-1]}{'-'*W_LEN}+"

    # 出力
    print_list = smi_list[:s_idx] + processes_list + smi_list[e_idx:]
    print_list.append(" ")
    print_list = list(map(lambda x: x + " " * 10, print_list))
    if flag:
        print(f"\033[{len(print_list)}A", end="")
    print("\n".join(print_list))
    flag = True