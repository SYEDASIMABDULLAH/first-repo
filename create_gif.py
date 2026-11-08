import imageio.v3 as iio
filenames = ['1.png','2.png']
images = []
for current_filename in filenames :
    #Read an image file and get its image data.
    #Add that image data to the images list.
    images_data = iio.imread(current_filename)
    images.append(images_data)
iio.imwrite('final.gif', images,duration = 500, loop=0)#i was thing if need to create a seprate fileto stor the gif so shoul be creating useing terminal or i can do it on explore 
