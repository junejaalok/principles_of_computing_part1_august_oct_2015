"""
Cookie Clicker Simulator
http://www.codeskulptor.org/#user40_ph56FbBLeL_33.py
not fully implemented Alok (20151005)
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._tot_cook = 0.0
        self._curr_cook = 0.0
        self._curr_time = 0.0
        self._curr_cps = 1.0
        self._history=[(0.0,None,0.0,0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return "\n" + "TotalCookies:" + str(self._tot_cook) + "\n"\
    + "CurrentCookies:" + str(self.get_cookies()) + "\n"\
    + "CurrentTime:" + str(self.get_time()) + "\n"\
    + "CurrentCPS:" + str(self.get_cps()) + "\n"
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._curr_cook
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._curr_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._curr_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self.get_cookies() >= cookies:
            return 0.0
        else:
            return math.ceil((cookies - self.get_cookies())/self.get_cps())
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time <= 0.0:
            pass 
        else:
            self._curr_time += time
            self._tot_cook += self.get_cps() * time
            self._curr_cook += self.get_cps() * time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost > self.get_cookies():
            pass
        else:
            self._curr_cook -= cost 
            self._curr_cps += additional_cps 
            self._history.append((self.get_time(),item_name,cost,self._tot_cook))
    
#def simulate_clicker(build_info, duration, strategy):
#    '''
#    function to run a Cookie Clicker game for the given duration with
#    the given strategy;
#    returns a ClickerState object corresponding to game
#    '''
    # make a clone of the build_info object & create a new ClickerState object
#    cloned_build_info = build_info.clone()
#    new_click = ClickerState()

#    while 0 <= duration:
#        item = strategy(new_click.get_cookies(), new_click.get_cps(), new_click.get_history(),
#                        duration, cloned_build_info)
#        if item is None:
#            # no resources anymore, no more items will be purchased
#            break
#        item_cost = cloned_build_info.get_cost(item)
#        wait_time = new_click.time_until(item_cost)
#        if duration < wait_time:
#            # impossible, would have to wait until after the duration
#            break
#        else:
#            duration -= wait_time
#            new_click.wait(wait_time)
#            new_click.buy_item(item, item_cost, cloned_build_info.get_cps(item))
#            cloned_build_info.update_item(item)
    # if there is still time left, allow cookies to accumulate till the end
#    new_click.wait(duration)
               
#    return new_click

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    source = build_info.clone()
    cstate = ClickerState()

    while 0 <= duration:
        buy_me = strategy(cstate.get_cookies(),cstate.get_cps(),cstate.get_history(),duration,source)

        if buy_me is None:
            break
        wait_time = cstate.time_until(source.get_cost(buy_me))
        item_cost = source.get_cost(buy_me)

        if wait_time > duration:
            break
        else:
            duration -= wait_time
            cstate.wait(wait_time)
            cstate.buy_item(buy_me,item_cost,source.get_cps(buy_me))
            source.update_item(buy_me)
    cstate.wait(duration)
    return cstate


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    return None

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)

run()
    


