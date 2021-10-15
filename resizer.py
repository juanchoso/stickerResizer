from PIL import Image
from io import BytesIO
import os, sys

#region directories
# Creates the directories in case they do not exist
if not (os.path.exists(os.getcwd() + r'\input')):
    os.mkdir(os.getcwd() + r'\input')

if not (os.path.exists(os.getcwd() + r'\output')):
    os.mkdir(os.getcwd() + r'\output')
#endregion

# Loads inputs
path = os.getcwd() + r'\input\\'
dirs = os.listdir(path)

tries = 0
successful = 0
quality_loss_sum = 0

# Processing each image in input folder:
for file in dirs:
    if os.path.isfile(path+file):
        loss = 0 # Unused measurement of quality loss.
        tries += 1
        im = Image.open(path+file)
        f, e = os.path.splitext(file)
        
        #
        width, height = im.size        
        width_lead = (width >= height)
        newSize = (0,0)
        if width_lead:
            factor = 512/width
            newSize = (512,round(height*factor))
        else:
            factor = 512/height
            newSize = (round(width*factor),512)
        
        imResize = im.resize(newSize, Image.ANTIALIAS)
        currentQuality = 100
        success = 0
        # Check if it's too heavy:
        while success == 0 and currentQuality > 0:
            img_file = BytesIO()
            imResize.save(img_file, 'PNG', quality=currentQuality)
            fileSize = img_file.tell()
            
            if fileSize <= 512000: # 512kb
                success = True
            else:
                currentQuality -= 5
                loss += 5
            del img_file
        if success:
            imResize.save(os.getcwd() + "\output\\" + f + ".png", 'PNG', quality=currentQuality)
            print(f"[IMG] {f}.png resized succesfully. {loss}% quality loss due to size restriction.")
            successful += 1
            quality_loss_sum += loss
        else: 
            print("[FAILURE] Couldn't resize {file}, perhaps it's too heavy or detailed, not even lowering the quality could achieve less than 512kb.")

print(f"Finished, resized {successful} images from {tries}.")
print(f"Success ratio: {successful*100/max(1,tries)}%.")
print(f"Average quality loss: {quality_loss_sum/successful}%")
        
        

        

