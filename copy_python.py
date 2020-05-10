import shutil
flowers=["Daffodil","Snowdrop","LilyValley","Bluebell","Crocus","Iris","Tigerlily","Tulip","Fritillary","Sunflower","Daisy","ColtsFoot","Dandelion","Cowslip","Buttercup","Windflower","Pansy"]
prf="/home/hrushikesh/images/17flowers"
list2=[prf]*17
#performs element wise addition of 2 elements
addresses=[a +"/"+ b for a, b in zip(list2, flowers)] 
my_dict={}
for i in range(0,17):
    my_dict[flowers[i]]=addresses[i]
img_prf=prf+"/jpg/"+"image_"
suffix=".jpg"
counter=0
for i in my_dict.values():
    for j in range(1,81):
        k=j+(80*counter)
        src=img_prf+str(k).zfill(4)+suffix
        shutil.copy(src,i+"/"+str(k)+".jpg")
    counter+=1

