
import pickle
from collections import deque


hq = deque([], 5)

hq.append(22)

with open('hq.pkl', 'wb') as pklf:
    pickle.dump(hq, pklf)
#pickle.dump(hq, open('hq.pkl', 'wb'))

with open('hq.pkl', 'rb') as readpkl:
    hq2 = pickle.load(readpkl)
#readq = pickle.load(open('hq.pkl', 'rb'))




