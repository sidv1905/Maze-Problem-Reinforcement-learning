import numpy as np
import pandas as pd

class QlearningTable:
    
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9,e_greedy=0.1):
        self.actions=actions
        self.lr=learning_rate
        self.gamma=reward_decay
        self.epsilon=e_greedy
        # now we need q table
        self.q_table=pd.DataFrame(columns=self.actions, dtype=np.float64)

    def add_state(self,state): 
        if state not in self.q_table.index:
            self.q_table= self.q_table.append(
                pd.Series([0]*len(self.actions)
           ,index=self.q_table.columns, name=state))
        # we addd states as we move
    # Now choosing which action to do
    def choose_action(self, observation):
        self.add_state(observation)
        # we use epsilon to decide to explor or exploit , we generate a random number initially to exoplore and then exploit
        if np.random.uniform()<self.epsilon:
            # action is random choice
            action=np.random.choice(self.actions)
        else:
            # we choose the best action for given obs beacuse now we exploit
            state_action=self.q_table.loc[observation, :]
            state_action=state_action.reindex(np.random.permutation(state_action.index))
            action=state_action.idxmax()
        return action
    # now agent ko learn karwanae
    def learn(self, s, a ,r, s_):
        # first add next state to qtable
        self.add_state(s_)
        q_predict= self.q_table.loc[s,a]
        if s_!= 'terminal':
            #now use bellman equation
            q_target=r+self.gamma * self.q_table.loc[s_,:].max()
            # now we update q target yesss
        else:
                # if not in terminal state q target is just the reward
             q_target=r
        self.q_table.loc[s,a] += self.lr * (q_target - q_predict)



