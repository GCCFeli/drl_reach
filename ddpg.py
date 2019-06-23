def ddpg(n_episodes=2000, max_t=1000):
    scores_deque = deque(maxlen=100)                          # last 100 scores
    scores = []                                                # list containing scores from each episode
    for i_episode in range(1, n_episodes+1):
        env_info = env.reset(train_mode=True)[brain_name]      # reset the environment
        states = env_info.vector_observations                  # get the current state
        agent.reset()
        score = np.zeros(num_agents)
        for t in range(max_t):
            actions = agent.act(states)                        # select an action (for each agent)
            env_info = env.step(actions)[brain_name]           # send all actions to tne environment
            next_states, rewards, dones = env_info.vector_observations, env_info.rewards, env_info.local_done         # get next state (for each agent)

            agent.step(states, actions, rewards, next_states, dones)
            states = next_states                               # roll over states to next time step
            score += rewards                                   # update the score (for each agent)
            if any(dones):                                     # exit loop if episode finished
                break
        scores_deque.append(np.mean(score))                   # save most recent score
        scores.append(np.mean(score))                          # save most recent score
        print('\rEpisode {}\tScore: {:.2f}'.format(i_episode, np.mean(score)))
        if i_episode % 100 == 0:
            print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)))
        if np.mean(scores_deque)>=30.0:
            print('\nEnvironment solved in {:d} episodes!\tAverage Score: {:.2f}'.format(i_episode-100, np.mean(scores_deque)))
            torch.save(agents[0].actor_local.state_dict(), 'checkpoint_actor.pth')
            torch.save(agents[0].critic_local.state_dict(), 'checkpoint_critic.pth')
            break
    return scores

scores = ddpg()

# plot the scores
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(np.arange(len(scores)), scores)
plt.ylabel('Score')
plt.xlabel('Episode #')
plt.show()

env.close()