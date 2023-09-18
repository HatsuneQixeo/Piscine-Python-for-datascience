from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

n = range(333)
duration = 0.005

for elem in ft_tqdm(n):
    sleep(duration)
print()

for elem in tqdm(n):
    sleep(duration)
print()
