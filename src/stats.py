import numpy as np

def bootstrap_diff(a, b, n_boot=1000):
    diffs = []
    
    for _ in range(n_boot):
        sa = np.random.choice(a, len(a), replace=True)
        sb = np.random.choice(b, len(b), replace=True)
        diffs.append(np.mean(sa) - np.mean(sb))
        
    return np.array(diffs)