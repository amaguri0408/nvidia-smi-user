# nvidia-smi-user

This program adds `user` information to the `nvidia-smi` command.

# Environment

Python >= 3.5

# Example

normal `nvidia-smi`
```
...
|   9  NVIDIA GeForce ...  On   | 00000000:0F:00.0 Off |                  N/A |          
| 72%   83C    P2   252W / 250W |   9521MiB / 11264MiB |     82%      Default |          
|                               |                      |                  N/A |          
+-------------------------------+----------------------+----------------------+  

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A     29776      C   python3                         10671MiB |
|    1   N/A  N/A     29776      C   python3                          1379MiB |
|    2   N/A  N/A     29269      C   python3                          3961MiB |
|    3   N/A  N/A     29269      C   python3                          3239MiB |
|    5   N/A  N/A      7184      C   python                           7827MiB |
|    6   N/A  N/A      7184      C   python                           5391MiB |
|    7   N/A  N/A      5120      C   python3                          2113MiB |
|    9   N/A  N/A     21118      C   python                           9517MiB |
+-----------------------------------------------------------------------------+
```

This program
```
...
|   9  NVIDIA GeForce ...  On   | 00000000:0F:00.0 Off |                  N/A |          
| 72%   83C    P2   252W / 250W |   9521MiB / 11264MiB |     82%      Default |          
|                               |                      |                  N/A |          
+-------------------------------+----------------------+----------------------+  

+---------------------------------------------------------------------------------------+          
| Processes:                                                                            |          
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory  USER     |          
|        ID   ID                                                   Usage                |          
|=======================================================================================|          
|    0   N/A  N/A     29776      C   python3                         10671MiB  amaguri  |          
|    1   N/A  N/A     29776      C   python3                          1379MiB  amaguri  |          
|    2   N/A  N/A     29269      C   python3                          3961MiB  amaguri  |          
|    3   N/A  N/A     29269      C   python3                          3239MiB  amaguri  |          
|    5   N/A  N/A      7184      C   python                           7827MiB  amaguri  |          
|    6   N/A  N/A      7184      C   python                           5391MiB  amaguri  |          
|    7   N/A  N/A      5120      C   python3                          2113MiB  amaguri  |
|    9   N/A  N/A     21118      C   python                           9517MiB  amaguri  |          
+---------------------------------------------------------------------------------------+    
```

# Installation

```bash
git clone https://github.com/amaguri0408/nvidia-smi-user.git
```

# Usage

```
python3 main.py
```
option  
`-n`, `--input`: Update interval (default: 0.5)

Type 'Ctrl + c' to exit


# Note

I recommend adding the following to the `.bashrc`.
```bash
alias nvidia-smi='python3 <ABSOLUTE_PATH>'
```
or
```bash
alias n='python3 <ABSOLUTE_PATH>'
```
Restart the shell.

If you have registered `alias nvidia-smi='python3 <ABSOLUTE_PATH>'` but want to use the normal `nvidia-smi` command, just add `\` at the beginning
```
\nvidia-smi
```