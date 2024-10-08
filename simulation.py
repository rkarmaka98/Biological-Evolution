from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
import numpy as np

def run_simulation():
    session = WolframLanguageSession()
    result = session.evaluate(wlexpr('RandomInteger[{1, 100}, 10]'))
    session.terminate()
    return result

def rule_30(state):
    """Apply Rule 30 to the current state."""
    new_state = np.zeros_like(state)
    for i in range(1, len(state) - 1):
        left = state[i - 1]
        center = state[i]
        right = state[i + 1]
        new_state[i] = left ^ (center | right)
    return new_state

def generate_automaton(initial_state, steps):
    """Generate the cellular automaton for a given number of steps."""
    states = [initial_state]
    current_state = initial_state
    for _ in range(steps):
        current_state = rule_30(current_state)
        states.append(current_state)
    return np.array(states)