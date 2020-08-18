# Main script to run the bot from
import random
import math
import numpy as np
import keyboard
# import platform
from PIL import Image
from collections import namedtuple
import torch
import time
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T
from main.Helpers import get_screen, isalive

# Set restart and bounce according to OS
from main.DirectInputWindows import bounce, restart

# Check if GPU is supported
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 2 possible actions (bounce, not bounce)
n_actions = 2

# Hyperparameters for model training
BATCH_SIZE = 28
GAMMA = 0.999
EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 300
# 10 改为了 2
TARGET_UPDATE = 2
num_episodes = 1500

# Transition dtype that conists of a state (two frames), the action the model took,
# and the resulting state and reward
Transition = namedtuple('Transition',
                        ('state', 'action', 'next_state', 'reward'))
# 不知道变大了管不管用
RESIZE_SIZE = (45, 40)
resize = T.Compose([T.ToPILImage(),
                    T.Resize(RESIZE_SIZE, interpolation=Image.CUBIC),
                    T.ToTensor()])


# Helper class to feed data into network
# (based on https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html)
class ReplayMemory(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
        self.position = 0

    def push(self, *args):
        # Saves a transition
        if len(self.memory) < self.capacity:
            self.memory.append(None)

        # 需要清零吗？？？
        if len(self.memory) >= self.capacity:
            self.memory = [None]
            self.position = 0

        self.memory[self.position] = Transition(*args)
        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size):
        """

        :param batch_size:
        :return: 从 memory列表中随机抽取 batch_size 个为一个子列表（不一定连续抽取）
        """
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)


# Deep Q Network
# (based on https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html)
class DQN(nn.Module):

    def __init__(self, h, w, outputs):
        super(DQN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=5, stride=2)
        self.bn1 = nn.BatchNorm2d(16)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=5, stride=2)
        self.bn2 = nn.BatchNorm2d(32)
        self.conv3 = nn.Conv2d(32, 32, kernel_size=5, stride=2)
        self.bn3 = nn.BatchNorm2d(32)

        # Number of Linear input connections depends on output of conv2d layers
        # and therefore the input image size, so compute it.
        def conv2d_size_out(size, kernel_size=5, stride=2):
            return (size - (kernel_size - 1) - 1) // stride + 1

        convw = conv2d_size_out(conv2d_size_out(conv2d_size_out(w)))
        convh = conv2d_size_out(conv2d_size_out(conv2d_size_out(h)))
        linear_input_size = convw * convh * 32
        self.head = nn.Linear(linear_input_size, outputs)

    # Called with either one element to determine next action, or a batch
    # during optimization. Returns tensor([[left0exp,right0exp]...]).
    def forward(self, x):
        x = F.relu(self.bn1(self.conv1(x)))
        x = F.relu(self.bn2(self.conv2(x)))
        x = F.relu(self.bn3(self.conv3(x)))
        return self.head(x.view(x.size(0), -1))


# Initialize policy and target network
# DQN : def __init__(self, h, w, outputs):
policy_net = DQN(*RESIZE_SIZE, 2).to(device)
target_net = DQN(*RESIZE_SIZE, 2).to(device)
target_net.load_state_dict(policy_net.state_dict())
target_net.eval()

# Initialize optimizer, memory (so planned training set size),
# and set steps done to 0
optimizer = optim.RMSprop(policy_net.parameters())
memory = ReplayMemory(100)
steps_done = 0


# Select an action either according to the network or random selection, where
# the likeliness of a random choice decreases toward 0 with steps_done getting bigger.
# This is to allow for more exploration when the model is still learning and more exploitation
# when the model has improved.
def select_action(state):
    global steps_done
    sample = random.random()
    # EPS_END = 0.05
    # EPS_START = 0.9
    eps_threshold = EPS_END + (EPS_START - EPS_END) * \
                    math.exp(-1. * steps_done / EPS_DECAY)
    steps_done += 1
    # Pick an action according to network
    # print(f'select-action : sample : {sample } ; eps_threshold : {eps_threshold}')
    if sample > eps_threshold:
        with torch.no_grad():
            # policy_net(state).max(1) returns the largest column of
            # each row. The second column is the largest expected reward.
            # print(f'select_action : {state.shape}')
            return policy_net(state).max(1)[1].view(1, 1)

    else:
        # Randomly pick an action
        # return random.randrange(n_actions)
        # 这里要转为 tensor，模仿上面的return即可，否则后来的 state 会报错！！！
        # n_actions = 2
        # return random.randrange(n_actions)
        return torch.tensor(random.randrange(n_actions), device='cuda').view(1, 1)

        # TM 直接跳起来
        # return torch.tensor(1, device='cuda').view(1, 1)


# Function for model optimization
# (based on https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html)
def optimize_model():
    # print(memory.memory)
    if len(memory) < BATCH_SIZE:
        # print('return')
        return

    # BATCH_SIZE = 28
    # transitions 是 一个 列表
    transitions = memory.sample(BATCH_SIZE)
    # print(transitions)
    # Transpose the batch (see https://stackoverflow.com/a/19343/3343043 for
    # detailed explanation). This converts batch-array of Transitions
    # to Transition of batch-arrays.
    batch = Transition(*zip(*transitions))

    # Compute a mask of non-final states and concatenate the batch elements
    # (a final state would've been the one after which simulation ended)
    non_final_mask = torch.tensor(tuple(map(lambda s: s is not None,
                                            batch.next_state)), device=device, dtype=torch.uint8)
    # print(f'optimize_model: non_final_mask: {non_final_mask}')
    non_final_next_states = torch.cat([s for s in batch.next_state
                                       if s is not None])
    # torch.cat(tensors, dim=0, out=None)
    # print(f'batch.state : {batch.state}')
    # print(f'batch.state TYPE : {type(batch.state)}')
    state_batch = torch.cat(batch.state)

    # print(f'batch.action : {batch.action}')
    # print(f'batch.action TYPE : {type(batch.action)}')
    action_batch = torch.cat(batch.action)

    # print(f'batch.reward : {batch.reward}')
    # print(f'batch.reward TYPE : {type(batch.reward)}')
    reward_batch = torch.cat(batch.reward)

    # Compute Q(s_t, a) - the model computes Q(s_t), then we select the
    # columns of actions taken. These are the actions which would've been taken
    # for each batch state according to policy_net
    state_action_values = policy_net(state_batch).gather(1, action_batch)

    # Compute V(s_{t+1}) for all next states.
    # Expected values of actions for non_final_next_states are computed based
    # on the "older" target_net; selecting their best reward with max(1)[0].
    # This is merged based on the mask, such that we'll have either the expected
    # state value or 0 in case the state was final.
    next_state_values = torch.zeros(BATCH_SIZE, device=device)
    next_state_values[non_final_mask.type(torch.bool)] = target_net(non_final_next_states).max(1)[0].detach()
    # Compute the expected Q values
    expected_state_action_values = (next_state_values * GAMMA) + reward_batch
    # Compute Huber loss
    loss = F.smooth_l1_loss(state_action_values, expected_state_action_values.unsqueeze(1))
    # Optimize the model
    optimizer.zero_grad()
    loss.backward()
    for param in policy_net.parameters():
        param.grad.data.clamp_(-1, 1)
    optimizer.step()


# Convert image to tensor to feed into model
def convert_to_n(screen):
    # 变为行连续的，读取速度更快
    screen = np.ascontiguousarray(screen, dtype=np.float32)
    # 变为 0 - 1.0 的小数
    screen = screen / 255  # torch.Size([410, 470])
    screen = torch.from_numpy(screen)
    # Resize, and add a batch dimension (BCHW)
    # torch.Size([1, 1, 40, 45])  RESIZE_SIZE
    return resize(screen).unsqueeze(0).to(device)


def main_train():
    # Main training loop
    for i_episode in range(num_episodes):
        # 从暂停界面开始
        restart()

        # Initialize the training variables
        alive = True
        reward = None
        i = 1

        # torch.Size([1, 1, 40, 45])  RESIZE_SIZE
        last_screen = convert_to_n(get_screen())
        current_screen = convert_to_n(get_screen())
        state = current_screen - last_screen

        # 是否还存活
        while alive:
            # print('ok')
            # Exit condition for windows
            if keyboard.is_pressed('q'):
                exit()

            # Get two consecutive frames
            last_screen = get_screen()
            current_screen = get_screen()

            # 把判断alive放后面
            # 在游戏中还是在暂停界面
            alive = isalive(last_screen, current_screen)

            # Define next state (as we can't assign reward straight away
            if alive:
                next_state = convert_to_n(current_screen) - convert_to_n(last_screen)
            else:
                # End episode if 你的方块 are dead
                next_state = None
                break  # 推出 while 循环


            # 奖励根据 i 来的 ，while 循环一次，i 就加上 1
            # action 是 0 或 1， 0不跳， 1 跳
            # Select and perform an action and
            # give reward no matter the action
            # as the length of survival is important
            action = select_action(state)
            if action:
                bounce()
            reward = i * 0.01

            reward = torch.tensor([reward], device=device)

            # Increase reward multiplier each frame to reward network
            # for surviving longer
            i = i + 1

            # Add the state and result to memory
            memory.push(state, action, next_state, reward)

            state = next_state

            # Perform one step of the optimization (on the target network)
            optimize_model()

            # print(f'while : {i}')

        time.sleep(0.5)

        # Update the target network every 10 episodes
        if i_episode % TARGET_UPDATE == 0:
            target_net.load_state_dict(policy_net.state_dict())
        print("Episode " + str(i_episode) + "done")
        # Reset the reward multiplier each episode as the cube only gets
        # rewarded if it survives long on the same run
        i = 1


main_train()
