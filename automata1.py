from automata import *
import sys

def main(inp):
    print("Regular Expression: ", inp)
    nfaObj = NFAfromRegex(inp)
    nfa = nfaObj.getNFA()
    dfaObj = DFAfromNFA(nfa)
    dfa = dfaObj.getDFA()
    print("\nDFA: ")
    dfaObj.displayDFA()
    if isInstalled("dot"):        
        drawGraph(dfa, "dfa")
        
        

if __name__  ==  '__main__':
    t = time.time()
    inp = " b*ab*(ab*ab*)*"
    try:
        main(inp)
    except BaseException as e:
        print("\nFailure:", e)
    print("\nExecution time: ", time.time() - t, "seconds")
