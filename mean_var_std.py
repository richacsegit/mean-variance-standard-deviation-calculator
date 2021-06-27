import numpy as np

def calculate(list):

  calculations= {}

  if len(list)< 9:
    raise ValueError('List must contain nine numbers.')

  arr= np.array(list)
  matrix = np.reshape(arr, (3,3))

  mean_list= [matrix.mean(axis=0).tolist(), matrix.mean(axis= 1).tolist(), matrix.flatten().mean()]

  variance_list= [matrix.var(axis=0).tolist(), matrix.var(axis= 1).tolist(), matrix.flatten().var()]

  sd_list= [matrix.std(axis=0).tolist(), matrix.std(axis= 1).tolist(), matrix.flatten().std()]

  max_list= [matrix.max(axis=0).tolist(), matrix.max(axis= 1).tolist(), matrix.flatten().max()]

  min_list= [matrix.min(axis=0).tolist(), matrix.min(axis= 1).tolist(), matrix.flatten().min()]

  sum_list= [matrix.sum(axis=0).tolist(), matrix.sum(axis= 1).tolist(), matrix.flatten().sum()]

  calculations['mean']= mean_list
  calculations['variance']= variance_list
  calculations['standard deviation']= sd_list
  calculations['max']= max_list
  calculations['min']= min_list
  calculations['sum']= sum_list

  return calculations