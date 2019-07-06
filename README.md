[//]: # (Image References)

[image1]: https://s3.cn-north-1.amazonaws.com.cn/u-img/5464e11b-d337-48a3-9e50-a1c4cb4353a0 "Environment Description"
[image2]: Demo.gif "Demo"

# Project: Reacher

### Environment Description

![Environment Description][image1]

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

For this project, two separate versions of the Unity environment are provided:

* The first version contains a single agent.
* The second version contains 20 identical agents, each with its own copy of the environment.

### Solving the Environment

#### Option 1: Solve the First Version
The task is episodic, and in order to solve the environment, the agent must get an average score of +30 over 100 consecutive episodes.

#### Option 2: Solve the Second Version
The barrier for solving the second version of the environment is slightly different, to take into account the presence of many agents. In particular, the agents must get an average score of +30 (over 100 consecutive episodes, and over all agents). Specifically,

After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent. This yields 20 (potentially different) scores. We then take the average of these 20 scores.
This yields an average score for each episode (where the average is over all 20 agents).

### Choice

In this solution, `option 2 (20 agents)` is chosen.

### Getting Started

1. Clone this repositry
2. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux_NoVis.zip) to obtain the environment.

3. Place the file in the DRLND GitHub repository, in the root folder, and unzip (or decompress) the file.
4. Make sure python and PyTorch is available.

### Instructions

1. Follow the step 4 `Train the agent` in `Reacher_Train.ipynb` to train the agent. Training algorithm is DDPG with replay buffer and soft update.
2. Training is expected to be done in 200 episodes.
3. The trained weights will be saved in `checkpoint_actor.pth` and `checkpoint_critic.pth`.
4. Follow the steps in and then run step `5` to watch a trained agent.

### Demo for Trained Agent

![Demo][image2]
