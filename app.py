from maze_env import Maze
from RL_agent import QlearningTable

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pylab as plt

episode_count=50
episodes=range(episode_count)

# track no of movements and rewards
rewards=[]
movements=[]

def run_expermient():
    for episode in episodes:
        print("Episodes {0} / {1}".format(episode,episode_count))
        observation= env.reset()
        moves=0

        while True:
            env.render()
            # get action and send action to  env and recience obs , reward and done signal
            # and also learn from this transitioon
            action= q_learning_agent.choose_action(str(observation))
            observation_, reward, done= env.get_state_reward(action)
            moves+=1
            # now learn from thsi transition by action a from s to s_

            q_learning_agent.learn(str(observation),action, reward, str(observation_))
            observation=observation_
            if done:
                movements.append(moves)
                rewards.append(reward)
                print(" REWARDS IS {0} AND MOVES IS {1}".format(reward,moves))
                break
    print("GAME OVER ")
def plot_reward_movements():
    plt.figure()
    plt.subplot(2, 1,1)
    plt.plot(episodes, movements)
    plt.xlabel("EPISODES")
    plt.ylabel("NO OF MOVEMENTS")

    plt.subplot(2,1,2)
    plt.step(episodes, rewards)
    plt.xlabel("EPISODES")
    plt.ylabel("REWARDS")

    plt.savefig("REWARDS _MOVEMENT_QLEARNING.png")
    plt.show()

if __name__=="__main__":
    env = Maze()
    q_learning_agent=QlearningTable(actions=list(range(env.n_actions)))
    env.window.after(10, run_expermient())
    plot_reward_movements()
    env.window.mainloop()

