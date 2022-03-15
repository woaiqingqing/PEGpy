import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.tick_params(labelsize=16)

ax = plt.subplot(1,1,1)
colors = ['b', 'r', 'y', 'g', 'm', 'c', 'k', 'violet', 'darkviolet', 'orange', 'lime']  # color list

for cindex, Dg in enumerate(np.arange(0.0, 1.1, 0.1)):
    df = pd.read_csv(f'time_evolution_Dg_{Dg:.1f}_Dr_{Dg:.1f}.csv')
    ax.scatter(df['time'], df['Fc'], s = 15, c = colors[cindex], label = f'Dg={Dg:.1f}, Dr={Dg:.1f}') 
    ax.set_ylim([0, 1.0])
    ax.set_xscale('log')
    ax.set_xticks([1,10,100,1000])
    ax.set_title('Time evolution of Fc', fontsize=16)
    ax.set_xlabel('Time step',fontsize=20)
    ax.set_ylabel('Fraction of cooperation',fontsize=20)
    ax.legend(loc='upper right')                      

plt.tight_layout()
plt.savefig('Dgloop.png')
plt.show()
