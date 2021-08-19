from urllib.request import urlretrieve
link=input('image download link= ')

filename=input('File Name : ')

urlretrieve(link,'image/'+filename+'.jpg')