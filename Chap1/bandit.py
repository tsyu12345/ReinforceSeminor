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

class Agent:

    def __init__(self, epsilon: float, action_size: int):
        """
        Args:
            epsilon: float ε-greedy法のε
            action_size: int 行動数
        """
        self.epsilon = epsilon
        self.Qs: ndarray = np.zeros(action_size) #マシンごとの推定価値
        self.play_counts = np.zeros(action_size) #各マシンのプレイ回数

    def update(self, action: int , reward: int):
        """
        推定価値の更新
        Args:
            action: int 選択したスロットマシンの番号
            reward: int 報酬
        """
        self.play_counts[action] += 1
        self.Qs[action] = self.Qs[action] + (reward - self.Qs[action]) / self.play_counts[action]

    def get_action(self):
        """
        ε-greedy法に基づいて行動を選択
        Returns:
            int 選択したスロットマシンの番号
        """
        action: int
        if np.random.rand() < self.epsilon:
            action = np.random.randint(0, len(self.Qs))
        else:
            action = np.argmax(self.Qs)
        return action

if __name__ == '__main__':

    # 1つのスロットマシンを10回回したときの推定価値 Q
    bandit = Bandit(1)
    Q: float = 0.0
    N: const = 10

    for n in range(1, N+1):
        action = 0
        reward = bandit.play(action)

        Q = Q + (reward - Q) / n
        print(f"{n}回目 : {Q}")
    
    # 10台のスロットマシンそれぞれの推定価値をもとめる
    bandits = Bandit(10)
    Qs: ndarray = np.zeros(10) #マシンごとの推定価値
    play_counts = np.zeros(10) #各マシンのプレイ回数
    N: const = 10

    for n in range(1, N+1):
        action: int = np.random.randint(10) #スロットマシンの選択
        reward = bandits.play(action)

        play_counts[action] += 1
        Qs[action] = Qs[action] + (reward - Qs[action]) / play_counts[action]
        print(f"{n}回目 : {Qs}")

    #e-greedy search
    epsilon: const = 0.3
    action: int
    if np.random.rand() < epsilon:
        action = np.random.randint(0, len(Qs)) # マシンをランダムに選択 (探索)
        print(f"ランダムに選択(探索) : {action}")
    else:
        action = np.argmax(Qs) # 推定価値が最大のマシンを選択 (活用)
        print(f"推定価値が最大のマシンを選択(活用) : {action}")

