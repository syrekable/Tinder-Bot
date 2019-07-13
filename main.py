import misc
misc.menu()

import screenshot
import imageManager
import txtManager
import UIManager
import beeper
from time import sleep

i, a = 0, 0

beeper.c()
while True:
    img = screenshot.takeScreenshot('screenshots/sample_'+str(i)+'.jpg',1)
    thresh = imageManager.threshold(('screenshots/sample_'+str(i)+'.jpg'))
    txt = txtManager.getText(thresh)
    
    sleep(1)

    if 'Alan' in txt:
        beeper.C()
        screenshot.takeScreenshot('screenshots/alan/alan_'+str(a)+'.jpg',0)
        a+=1
        UIManager.like()

    else:
        UIManager.dislike()
    i+=1

beeper.A()