import pandas as pd
import matplotlib.pyplot as plt
  
plt.tick_params(labelsize = 16)

ax = plt.subplot(1,1,1)

for episode in range(1, 101):
    df = pd.read_csv(f'time_evolution_episode{episode}.csv')
    ax.scatter(df['time'], df['Fc'], s = 15, label = f'episode{episode}')    
    ax.set_ylim([0, 1.0])
    ax.set_xscale("log")
    ax.set_xticks([1,10,100,1000])
    ax.set_title('Time evolution of Fc', fontsize = 20)
    ax.set_xlabel('Time step', fontsize = 20)
    ax.set_ylabel('Fraction of cooperation', fontsize=20)                      

plt.tight_layout()
plt.savefig('100episodes.png')
plt.show()