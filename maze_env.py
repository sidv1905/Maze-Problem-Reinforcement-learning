import numpy as np
import time
import sys

if sys.version_info==2:
    import Tkinter as tk
else:
    import tkinter as tk

Unit=40
Maze_h=6
Maze_w=6

class Maze:
    def __init__(self):
        '''We create our maze window here'''
        self.window=tk.Tk() #window bnta isse
        self.window.title("Maze With Q-learning")
        self.window.geometry('{0}x{1}'.format(Maze_w*Unit,Maze_h*Unit))
        self.action_space=['u','d','l','r']
        self.n_actions=len(self.action_space)
        self.build_maze()
    def build_maze(self):
        self.canvas=tk.Canvas(self.window,bg='white',width=Maze_w*Unit,height=Maze_h*Unit)
        for c in range(0,Maze_w*Unit,Unit ):
            # to create lines in the maze
            x0, y0, x1, y1=c, 0, c, Maze_w*Unit
            self.canvas.create_line(x0,y0,x1,y1)
        for r in range(0,Maze_h*Unit,Unit ):
            # to create lines in the maze
            x0, y0, x1, y1=0, r,  Maze_h*Unit,r
            self.canvas.create_line(x0,y0,x1,y1)
        # ab start point decide hoga let it be the middle point of the maze

        origin= np.array([20,20])
        hell1_center= origin + np.array([Unit*2,Unit])
        self.hell1=self.canvas.create_rectangle(hell1_center[0]-15, hell1_center[1]-15,
        hell1_center[0]+15, hell1_center[1]+15,fill='black'
        )

        hell2_center= origin + np.array([Unit,Unit*2])
        self.hell2=self.canvas.create_rectangle(hell2_center[0]-15, hell2_center[1]-15,
        hell2_center[0]+15, hell2_center[1]+15,fill='black'
        )
        oval_center= origin + Unit*2
        self.oval=self.canvas.create_oval(oval_center[0]-15, oval_center[1]-15,
        oval_center[0]+15, oval_center[1]+15,fill='yellow'
        )

        
        self.rect=self.canvas.create_rectangle(origin[0]-15, origin[1]-15,
        origin[0]+15, origin[1]+15,fill='red'
        )
        self.canvas.pack()
    def render(self):
        time.sleep(0.1)
        self.window.update()

    def reset(self):
        self.window.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect)
        origin=np.array([20,20])
        self.rect=self.canvas.create_rectangle(
            origin[0]-15, origin[1]-15,
        origin[0]+15, origin[1]+15,fill='red'
        )
        return self.canvas.coords(self.rect)
    
    def get_state_reward(self, action):
        s = self.canvas.coords(self.rect)
        base_action= np.array([0,0])
        if action==0: #going up
            if s[1]> Unit:
                base_action[1]-=Unit
        elif action==1:
            if s[1] < (Maze_h-1)*Unit:
                base_action[1]+=Unit
        elif action==2: # going right
            if s[0]< (Maze_w-1)*Unit:
                base_action[0]+=Unit
        elif action==3: # going left
            if s[0]>Unit:
                base_action[0]-=Unit
        self.canvas.move(self.rect, base_action[0],base_action[1]) # ye hilaega red dabbe ko
        # ab nexxt state milega
        s_=self.canvas.coords(self.rect)

        # now we have new state now we compute the reward
        # reward for hell is -1 and if to goal its +1, else 0
        if s_==self.canvas.coords(self.oval):
            reward =1   
            done=True
            s_="terminal"
        elif s_ in [self.canvas.coords(self.hell1),self.canvas.coords(self.hell2)]:
            reward=-1
            done=True
            s_="terminal"
        else:
            reward=0
            done=False
        return s_,reward,done
if __name__=='__main__':
    maze=Maze()
    maze.build_maze()
    maze.window.mainloop() #Runnning window app





