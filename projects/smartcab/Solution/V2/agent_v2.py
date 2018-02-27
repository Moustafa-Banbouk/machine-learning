import random
import math
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator

class LearningAgent(Agent):
    """ An agent that learns to drive in the Smartcab world.
        This is the object you will be modifying. """ 

    def __init__(self, env, learning=False, epsilon=1.0, alpha=0.5):
        super(LearningAgent, self).__init__(env)     # Set the agent in the evironment 
        self.planner = RoutePlanner(self.env, self)  # Create a route planner
        self.valid_actions = self.env.valid_actions  # The set of valid actions

        # Set parameters of the learning agent
        self.learning = learning # Whether the agent is expected to learn
        self.Q = dict()          # Create a Q-table which will be a dictionary of tuples
        self.epsilon = epsilon   # Random exploration factor
        self.alpha = alpha       # Learning factor

        ###########
        ## TO DO ##
        ###########
        # Set any additional class parameters as needed
        self.count = 0

    def reset(self, destination=None, testing=False):
        """ The reset function is called at the beginning of each trial.
            'testing' is set to True if testing trials are being used
            once training trials have completed. """

        # Select the destination as the new location to route to
        self.planner.route_to(destination)
        
        ########### 
        ## TO DO ##
        ###########
        # Update epsilon using a decay function of your choice
        # Update additional class parameters as needed
        # If 'testing' is True, set epsilon and alpha to 0
        
        self.count = self.count + 1
        
        # Trial 1: Linear Decrease of Epsilon
        # self.epsilon = self.epsilon - 0.05
        # Reliability = F / Safety = F
        
        # Trial 2: Epsilon = 1/x
#         self.epsilon = 1.0/self.count
        # Reliability = F / Safety = F
        
        #Trial 3: Epsilon = 1 / (1 + math.exp(-x))
#         self.epsilon = 1.0-1.0 / (1.0 + math.exp(-self.count))
        # Reliability = F / Safety = F
        
        # Trial #4
        #0.1 => 1/2
        #1 => 20   
#         self.epsilon = math.cos(self.count/40.0)
        # Reliability = C / Safety = F
        
        # Trial #5
#         self.epsilon = 1.0/math.pow(self.count,2)
        # Reliability = F / Safety = F
        
        # Trial #6: Alpha = 0.8
#         self.epsilon = math.cos(self.count/40.0)
        # Reliability = D / Safety = F
        
        # Trial #7: Alpha = 0.7
#         self.epsilon = math.cos(self.count/40.0)
        # Reliability =  A+ / Safety = F
        
        # Trial #8: Alpha = 0.7 / Tolerance = 0.004
#         self.epsilon = math.cos(self.count/40.0)
        # Reliability =  / Safety = F
        
        # Trial #9: Alpha = 0.8
#         self.epsilon = math.cos(self.count/80.0)
        # Reliability =  B / Safety = F
        
        # Trial #10: Alpha = 0.7
#         self.epsilon = math.cos(self.count/40.0)
        # Reliability =  B / Safety = F
        
         # Trial #11: Alpha = 0.7
#         self.epsilon = math.cos(self.count/100.0)
        # Reliability =  A / Safety = C
        
        # Trial #12: Alpha = 0.7
        self.epsilon = math.cos(self.count/1000.0)
        # Reliability =  ? / Safety = ?
        
        if (testing == True): 
            self.epsilon = 0
            self.alpha = 0
            
        # TODO: Check additional class parameters
        
        return None

    def build_state(self):
        """ The build_state function is called when the agent requests data from the 
            environment. The next waypoint, the intersection inputs, and the deadline 
            are all features available to the agent. """

        # Collect data about the environment
        waypoint = self.planner.next_waypoint() # The next waypoint 
        inputs = self.env.sense(self)           # Visual input - intersection light and traffic
        deadline = self.env.get_deadline(self)  # Remaining deadline

        ########### 
        ## TO DO ##
        ###########
        
        # NOTE : you are not allowed to engineer eatures outside of the inputs available.
        # Because the aim of this project is to teach Reinforcement Learning, we have placed 
        # constraints in order for you to learn how to adjust epsilon and alpha, and thus learn about the balance between exploration and exploitation.
        # With the hand-engineered features, this learning process gets entirely negated.
        
        # Set 'state' as a tuple of relevant data for the agent        
        state = None
        
        print "____Inputs: ", inputs
        strInputs = ""
        for k,v in inputs.iteritems():
            print "K: ",k
            print "V: ",v
            strInputs = strInputs + k + ":" + str(v) + ","
         
        state = waypoint + ',' + strInputs
         
        return state


    def get_maxQ(self, state):
        """ The get_max_Q function is called when the agent is asked to find the
            maximum Q-value of all actions based on the 'state' the smartcab is in. """

        ########### 
        ## TO DO ##
        ###########
        # Calculate the maximum Q-value of all actions for a given state

        maxQ = None
        
        print "===> Inside get_maxQ()"
        dicAction = dict()
        dicAction = self.Q[state]
        maxQ = 0
        
        for k,v in self.Q[state].iteritems():
            print "K: ",k
            print "V: ",v
            if (v > maxQ):
                maxQ = v
        
        print "===> Leaving get_maxQ()"
        return maxQ 
      

    def createQ(self, state):
        """ The createQ function is called when a state is generated by the agent. """

        ########### 
        ## TO DO ##
        ###########
        # When learning, check if the 'state' is not in the Q-table
        # If it is not, create a new dictionary for that state
        #   Then, for each action available, set the initial Q-value to 0.0
        print "===> Inside CreateQ()"
        found = False
        print "state: ",state
        dicAction = dict()
        
        for k,v in self.Q.iteritems():
            if (k == state):
                found = True
        
        if (found == False):
            print "state is not found"
            for action in Environment.valid_actions:
                print "Action:",action
                dicAction[action] = 0
            print "dicAction:", dicAction
            
            self.Q[state] = dicAction
        
        print "===> Leaving CreateQ()"

        return


    def choose_action(self, state):
        """ The choose_action function is called when the agent is asked to choose
            which action to take, based on the 'state' the smartcab is in. """

        # Set the agent state and default action
        self.state = state
        self.next_waypoint = self.planner.next_waypoint()
        action = None

        ########### 
        ## TO DO ##
        ###########
        # When not learning, choose a random action
        # When learning, choose a random action with 'epsilon' probability
        # Otherwise, choose an action with the highest Q-value for the current state
        # Be sure that when choosing an action with highest Q-value that you randomly select between actions that "tie".
        
        # Trial 1: No learning is involved
#         action = random.choice(Environment.valid_actions[1:])
        
        # Trial 2: Learning is involved
        if not self.learning:
            # TODO: Randomize based on epsilon probability
            action = random.choice(Environment.valid_actions[1:])
            print "=> Random Action: ", action
        else:
            maxQ = self.get_maxQ(state)
            dicAction = self.Q[state]
            
            ActionMaxLength = 0            
            dicActionMax = dict()
            QActionMax = -999999 
            
            
            print "maxQ: ", maxQ
            print "dicAction: ", dicAction
            
            
            for k,v in dicAction.iteritems():
                print "===>k: ", k
                print "===>v: ", v
                if (v > QActionMax):                   
                    dicActionMax = dict()
                    ActionMaxLength = 0
                    dicActionMax[ActionMaxLength] = k
                    action = k
                    QActionMax = v
                    print "=> Candidate Actions: ", dicActionMax
                elif (v == QActionMax):
                    ActionMaxLength = ActionMaxLength + 1
                    dicActionMax[ActionMaxLength] = k
                    print "=> Equivalent Candidate Actions: ", dicActionMax
            mainAction = random.choice(dicActionMax)
            randomAction = random.choice(Environment.valid_actions[1:])
            
            rnd = random.random()
            print "::=> rnd: ", rnd
            print "::=> epsilon: ", self.epsilon
            
            if (rnd<self.epsilon):
                action = randomAction
                print "==> random Action:", action
            else:
                action = mainAction
                print "==> main Action:", action
            
        return action


    def learn(self, state, action, reward):
        """ The learn function is called after the agent completes an action and
            receives a reward. This function does not consider future rewards 
            when conducting learning. """

        ########### 
        ## TO DO ##
        ###########
        # When learning, implement the value iteration update rule
        #   Use only the learning rate 'alpha' (do not use the discount factor 'gamma')
        
        gamma = 0
        dicAction = self.Q[state]
        Qsa_old = dicAction[action]
        
        # next_state = ???
        #maxQsa = self.get_maxQ(self, next_state)
        
        #In this example gamma = 0 and therefore, whatever maxQsa is, it will not have an influence
        maxQsa = 0
        
        print "Qsa_old: ", Qsa_old          
        Qsa_new = (1-self.alpha)*Qsa_old + self.alpha*(reward + gamma*maxQsa)
        self.Q[state][action] = Qsa_new
        
        return


    def update(self):
        """ The update function is called when a time step is completed in the 
            environment for a given trial. This function will build the agent
            state, choose an action, receive a reward, and learn if enabled. """

        state = self.build_state()          # Get current state
        self.createQ(state)                 # Create 'state' in Q-table
        action = self.choose_action(state)  # Choose an action
        reward = self.env.act(self, action) # Receive a reward
        self.learn(state, action, reward)   # Q-learn

        return
        

def run():
    """ Driving function for running the simulation. 
        Press ESC to close the simulation, or [SPACE] to pause the simulation. """

    ##############
    # Create the environment
    # Flags:
    #   verbose     - set to True to display additional output from the simulation
    #   num_dummies - discrete number of dummy agents in the environment, default is 100
    #   grid_size   - discrete number of intersections (columns, rows), default is (8, 6)
    env = Environment()
    
    ##############
    # Create the driving agent
    # Flags:
    #   learning   - set to True to force the driving agent to use Q-learning
    #    * epsilon - continuous value for the exploration factor, default is 1
    #    * alpha   - continuous value for the learning rate, default is 0.5
    agent = env.create_agent(LearningAgent, learning=True, alpha=0.7)
    
    ##############
    # Follow the driving agent
    # Flags:
    #   enforce_deadline - set to True to enforce a deadline metric
    env.set_primary_agent(agent, enforce_deadline=True)

    ##############
    # Create the simulation
    # Flags:
    #   update_delay - continuous time (in seconds) between actions, default is 2.0 seconds
    #   display      - set to False to disable the GUI if PyGame is enabled
    #   log_metrics  - set to True to log trial and simulation results to /logs
    #   optimized    - set to True to change the default log file name
    sim = Simulator(env, update_delay=0, log_metrics=True, optimized=True)
    
    ##############
    # Run the simulator
    # Flags:
    #   tolerance  - epsilon tolerance before beginning testing, default is 0.05 
    #   n_test     - discrete number of testing trials to perform, default is 0
    sim.run(n_test=10, tolerance=0.005)


if __name__ == '__main__':
    run()