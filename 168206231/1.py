def quicksort(alist):
  	less=[];greater=[]   #less����С�ڵ��ڻ�׼ֵ��Ԫ����ɵ�������
  						#greater���ɴ��ڻ�׼ֵ��Ԫ����ɵ�������
  	if len(alist)<2:
  		return alist          #��������������Ϊ�ջ�ֻ����һ��Ԫ�أ�ԭ����������
  	else:
  		pivot=alist[0]       #������ĵ�һ��Ԫ����Ϊ��׼ֵ
  		for i in alist[1:]:
  			if i<=pivot:
  				less.append(i) #��С�ڵ��ڻ�׼ֵ��Ԫ�ؼ��뵽less����
  			else:
  				greater.append(i) #�����ڻ�׼ֵ��Ԫ�ؼ��뵽greater����
  		return quicksort(less)+[pivot]+quicksort(greater)
  print(quicksort([7,5,36,59,78,12])) 