# Import everything needed to edit video clips
from moviepy.editor import *
import pygame
   
clip = VideoFileClip("C:/Users/ASUS/Desktop/ELA/data/generated/mygeneratedvideo.avi")
   
# getting only first 5 seconds
clip = clip.subclip(0, 30)
   
# applying speed effect
final = clip.fx( vfx.speedx, 500)
  
# showing final clip
clip.ipython_display()