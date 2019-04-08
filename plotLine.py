'''
Fun: parse the ground truth data
'''

import csv,json
import matplotlib.pyplot as plt


'''
Fun: read the result
'''
def read_result_file(file_name):
	label_lst = []
	y = []
	with open(file_name,"r") as f:
		csvfile = csv.reader(f)
		header = next(csvfile)
		for line in csvfile:
			arr = line[1:]
			accy = [round(float(k), 3) for k in arr]
			y.append(accy)
			label_lst.append(line[0])

	return label_lst, y, header[1:]

'''
Fun: plot figure
'''
def plot_figure(x,y,label_lst,x_title,location):
	fig = plt.figure()
	linewidth = 2 #linewidth
	colors = ['black', 'red','blue','green','orchid','orange','grey','yellow','purple','cyan']
	markers = ['o', '+', '.', 'x', '*', '>', '^','s']
	linestyles = ['-', '--', '-.', ':']
	n = len(y)
	for i in range(n):
		plt.plot(x, y[i], marker = markers[i], color = colors[i], linestyle=linestyles[2],\
			lw = linewidth, markersize=10, label = label_lst[i])
	
	font2 = {'family' : 'Times New Roman','weight': 'normal','size': 15}
	plt.tick_params(labelsize = 15)
	# plt.xlabel(x_title, fontsize = 14)  #we can use font 2
	# plt.ylabel('Number of events/actions', fontsize = 14)
	plt.xticks(x, x)#show the X values
	plt.title('Comparison of different algorithms',fontsize = 14)
	plt.legend(loc = 'best', prop={'size': 9.5})  #loc = "best",'upper left' = 2,'lower left'=3
	# plt.legend(bbox_to_anchor=(0,1.02,1,0),ncol=2,loc=0,mode='expand',borderaxespad=0)
	x_title = x_title.split('@')
	fig.savefig('figs/' + x_title[0] + '-compare.eps',dpi = 600)
	plt.show()


## main function
def main():
	## compare the hit ratio
	x = [5,10,15,20]
	file_name = 'hitRate.csv'
	x_title = 'HR@K'
	label_lst,y,x = read_result_file(file_name)
	print(y)
	print("methods:", label_lst)
	location = 'best'
	# label_lst = ['GCN-weight','GCN-unweighted','NCF', 'MF', 'BPR','LINE','Cosine']
	plot_figure(x,y,label_lst,x_title,location)
	
	## compare the MRR
	file_name = 'MRR.csv'
	x_title = 'MRR@K'
	label_lst,y,x = read_result_file(file_name)
	location = 'best'
	plot_figure(x,y,label_lst,x_title,location)

	## compare the MRR
	file_name = 'MAP.csv'
	x_title = 'MAP@K'
	label_lst,y,x = read_result_file(file_name)
	location = 'best'
	plot_figure(x,y,label_lst,x_title,location)
	


## main function
if __name__ == '__main__':
	main()
	




	



