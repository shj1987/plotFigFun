'''
fun: plot the histogram of each actions
'''
import numpy as np
import matplotlib.pyplot as plt
import csv


def read_exp_file(fileName):
	'''read the exp results to csv file'''
	legendNames = []
	y2metrics = dict()
	with open(fileName,"r") as f:
		csvfile = csv.reader(f, delimiter =',')
		for line in csvfile:
			legendNames.append(line[0])
			y2metrics[line[0]] = [float(i) for i in line[1:]]

	return y2metrics,legendNames

def plotHistogram(y2metrics,legendNames,metricList,figName,yLabel):
	'''plot the histogram of each proxy'''
	y = []
	for proxy in y2metrics:
		results = y2metrics[proxy]
		y.append(results)
	print(y)
	## number of metrics
	yRes = np.array(y)
	print(yRes.shape)

	N = len(metricList) # axis = N
	width = 0.8
	labels = legendNames
	colors = ['blue','red','black','magenta','hotpink','orange','green','tan','grey']
	colors = ['lightgreen','lightblue','tan','grey']
	patterns = ["/",'\\',False,'x',"+","/",'.','\\','x']
	y_n = len(yRes)
	_X = np.arange(N)
	for i in range(y_n):
		plt.bar(_X - width/2. + i/float(y_n)*width, yRes[i], width=width/float(y_n),\
			color=colors[i], edgecolor='black', label=labels[i], hatch=patterns[i], align="edge")   
	plt.xticks(_X, metricList)
	# plt.ylabel(yLabel)
	plt.ylim(0, 0.25)
	plt.tick_params(labelsize = 15)
	plt.legend()
	plt.tight_layout()
	plt.savefig(figName, dpi=600)
	plt.show()


## main function
def main():
	fileName = './MAP.csv'
	figName = './figs/MAP.eps'
	yLabel = 'no'
	metricList = ['5','10','15','20']
	y2metrics,legendNames = read_exp_file(fileName)
	plotHistogram(y2metrics,legendNames,metricList,figName,yLabel)
	


if __name__ == '__main__':
	main()
	




