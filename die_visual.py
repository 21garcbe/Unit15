import plotly.express as px

from die import Die

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analyze results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize results 
title = 'Results of rolling two dice (d6 and d10) 50,000 times'
labels={'x':'Result', 'y':'Frequency'}
fig =px.bar(x=poss_results, y=frequencies, labels=labels, title=title)

fig.update_layout(xaxis_dtick=1)
fig.write_html('die_visual_d6_d10.html')
