import matplotlib.pyplot as plt

with plt.xkcd():
    labels = 'Insults', 'Profanity', 'Didn\'t Read\nthe Question', '"Let\'s talk\nabout me!"', 'Actual Insightful\nComments\n(Not to Scale)'
    sizes = [15, 15, 31, 37, 2]
    explode = (0, 0, 0, 0, 0.2)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, colors=('w','w','w','w','w'), wedgeprops={'linewidth':1, 'edgecolor':'black'}, labels=labels, startangle=300)
    ax1.axis('equal')
    fig1.suptitle('Classification of Reddit Responses', fontsize=20)

    plt.show()
