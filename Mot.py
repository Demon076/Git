'''hbtbgpylint '''
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("trees.csv")
dff=df.sort_values(by='Girth')
mn=dff[['Girth']].min()[0]
mx=dff[['Girth']].max()[0]
fig, ax = plt.subplots(3, 2)

x=[]
x.append(dff['Girth'])
y=[]
y=x
ax[0,0].set_title('Girth')
ax[0, 0].plot(x,y,'ro')
ax[0,1].set_title('Girth')
ax[0,1].hist(df['Girth'], bins=10)

dff=df.sort_values(by='Height')
mn=dff[['Height']].min()[0]
mx=dff[['Height']].max()[0]
x=[]
x.append(dff['Height'])
y=[]
y=x

ax[1,0].set_title('Height')
ax[1,0].plot(x,y,'ro')

ax[1,1].set_title('Height')
ax[1,1].hist(df['Height'], bins=10)

dff=df.sort_values(by='Volume')
mn=dff[['Volume']].min()[0]
mx=dff[['Volume']].max()[0]


x=[]
x.append(dff['Volume'])
y=[]
y=x

ax[2,0].set_title('Volume')
ax[2,0].plot(x,y,'ro')

ax[2,1].set_title('Volume')
ax[2,1].hist(df['Volume'], bins=10)
plt.show()