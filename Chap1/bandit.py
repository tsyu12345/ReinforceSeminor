from __future__ import annotations
from typing import Final as const
import numpy as np
from numpy import ndarray

class Bandit:
    
    def __init__(self, arms: int= 10):
        """
        Args:
            arms: int スロットマシンの数
        """
        self.rates = np.random.rand(arms)

    def play(self, slot_no: int):
        """
        指定したスロットマシンを1回回す
        Args:
            arms: int スロットマシンの番号
        Returns:
            int 報酬
        """
        rate: float = self.rates[slot_no]
        play_result = np.random.rand()
        reward = 1 if rate > play_result else 0
        return reward


if __name__ == '__main__':

    bandits = Bandit(10)
    play_count = 3
    for i in range(play_count):
        print(f"{i}回目 : {bandits.play(0)}")
