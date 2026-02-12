import matplotlib.pyplot as plt 

'''--- Image Manipulation ---'''
'''Save Photo as an array (plt.imread)'''
# Use plt.imread to save a photo as an array of numbers
photo = plt.imread('bwCat.tif') 

'''Display the Array as an Image (plt.imshow)'''
# Define a grayscale for black and white image 
plt.set_cmap('gray')

# Remove axes and tick marks 
plt.axis('off') 
fig = plt.gcf() 

# Set background color to white
fig.set_facecolor('white') 

# Display the array (bwCat.tif) as an image using plt.imshow
image = plt.imshow(photo) 
plt.show() 

'''Manipulate Array'''
# If bigger than the mean, the pixel turns black. If smaller than the mean, it turns white.
new_cat = (photo < photo.mean()) 

# Display the manipulated array as a new image
image = plt.imshow(new_cat)
plt.show()

'''Save Array (plt.imsave)'''
# Use plt.imsave to save the array as a jpg file
plt.imsave('cat.jpg', photo, cmap = 'gray') 