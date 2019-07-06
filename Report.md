[//]: # (Image References)

[image1]: Rewards.png "Rewards" 
[image2]: Demo.gif "Result"  

# Report

## 1. Getting started

Please follow the instructions in README.md to setup the environment.

## 2. Learning Algorithm

### 2.1 DDPG

This RL problem's state space is continuous, and action space is also continuous. So we choose the well known DDPG([Deep Deterministic Policy Gradient](https://arxiv.org/abs/1509.02971 "Deep Deterministic Policy Gradient")) which perfectly matches the problem.

DDPG is a kind of off-policy Actor-Critic method. The Actor uses DNN to directly map the continuous state space to action space. The Critic estimates the Q value of state-action pair, sharing the same DNN body with the Actor. DDPG uses the ε-greedy method to do exploration, in practics, OU Noise is added to action output. Replay buffer and soft-update which are successful in DQN, are also used in DDPG.

In this problem, we choose a simple 2-layer neural network. Layer sizes are 400, 300. Activation function is ReLU. Loss function is MSE. Optimizer is Adam. Replay buffer and soft update are used to make learning stable. Alghough there are 20 agents in the environment, just one learner is used. Experiences of 20 agents are stored in a shared replay buffer.

### 2.2 Hyperparameters

| Hyperparameter | Value | Desctiption |
| -------------- | ----- | ----------- |
| minibatch size | 128 | Number of training cases over each stochastic gradient descent (SGD) update is computed. |
| replay buffer size | 100000 | SGD updates are sampled from this number of most recent frames. |
| soft update target paramater | 0.001 | Soft update target parameter  τ used to lerp between local network and target network. |
| discount factor | 0.99 | Discount factor gamma used in the Q-learning update. |
| learning rate - Actor | 0.0005 | The init learning rate of Actor used by Adam. |
| learning rate - Critic | 0.001 | The init learning rate of Critic used by Adam. |
| weight decay | 0 | The weight decay parameter of Critic used by Adam. |
| sigma init | 0.2 | The initial sigma of OU Noise. |
| sigma decay | 0.95 | The sigma decay of OU Noise. |
| sigma min | 0.005 | The minimal sigma of OU Noise. |
| mu | 0 | Mu in OU Noise. |
| theta | 0.15 | Theta in OU Noise. |

## 3. Plot of Rewards

Training can be done within 200 episodes.

![Rewards][image1]

## 4. Result

Watch the video below to see the performance of a trained agent.

![Result][image2]

## 5. Ideas for Future Work

The original DDPG algorithm is enough to solve this problem. However, some methods may achieve better performance:
* [Trust Region Policy Optimization (TRPO)](https://arxiv.org/abs/1502.05477 "Trust Region Policy Optimization (TRPO)")
* [Truncated Natural Policy Gradient (TNPG)](http://papers.nips.cc/paper/2073-a-natural-policy-gradient.pdf "Truncated Natural Policy Gradient (TNPG)")
* [Proximal Policy Optimization (PPO)](https://arxiv.org/abs/1707.06347 "Proximal Policy Optimization (PPO)")
* [Distributed Distributional Deterministic Policy Gradients (D4PG)](https://arxiv.org/abs/1804.08617 "Distributed Distributional Deterministic Policy Gradients (D4PG)")

Hyperparameters are manually chosen for this problem. Grid search will be helpful to choose a better hyperparameter set.
