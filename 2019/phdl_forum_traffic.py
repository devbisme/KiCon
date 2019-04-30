import matplotlib.pyplot as plt
import datetime

with plt.xkcd():
    year = [datetime.datetime(y,1,1,12,0) for y in range(2011, 2019)]
    num_posts = [20, 108, 22, 23, 11, 2, 2, 18]

    ax = plt.subplot(111)
    ax.bar(year, num_posts, width=300)
    ax.xaxis_date()

    plt.title('PHDL Forum Traffic')
    plt.xlabel('Year')
    plt.ylabel('#Posts')

    plt.show()
