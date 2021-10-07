import quandl
import pandas as pd

feedy_states = pd.read_html('http://simple.wikipedia.org/wiki/List_of_U.S._states')

#print(feedy_states)

print(feedy_states[0][0])

for abbv in feedy_states[0] [0][1:]:
    print('FMAC/HPI_' + str(abbv))
