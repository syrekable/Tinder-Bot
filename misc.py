'''
    createFolder(directory):
        creates folders needed for program to run
        directory - string, folder name

    changeCoords(coords):
        saves desired screenshot position to coords.json file
        coords - list

    menu():
        speaks for itself, I guess
'''

import os
import json
from time import sleep

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def setCoordsImg(coords):

    keys, values = ["left_x","top_y","width","height"], coords.split(',')
    values = [int(x) for x in values]

    coordinates = dict(zip(keys,values))
    j = json.dumps(coordinates)

    with open('./res/coords_img.json','w') as f:
        f.write(j)
        f.close()

def setCoordsBtn(btn,coords):
    keys, values = ['x','y'],coords.split(',')
    values = [int(x) for x in values]

    coordinates = dict(zip(keys,values))
    j = json.dumps(coordinates)

    if btn:
        with open('./res/coords_btn_like.json','w') as f:
            f.write(j)
            f.close()
    else:
        with open('./res/coords_btn_dislike.json','w') as f:
            f.write(j)
            f.close()

def setInitCoords():
    #TODO: just ugly spaghetti, improve it
    init_coords_img, init_coords_like_btn, init_coords_dislike_btn = '960,110,480,700', '1280,860', '1100,860'

    setCoordsImg(init_coords_img)

    setCoordsBtn(1,init_coords_like_btn)
    setCoordsBtn(0,init_coords_dislike_btn)

def menu():
    possAns = ['y','Y','yes','YES','t','T','tak','TAK']

    folderNames = {'./screenshots/','./screenshots/alan/','./res/'}

    messages = {
        'greet':'WELCOME TO TINDER BOT v0.1',
        'question':'\nDo you want to change INITIAL photo position?\nType y/n:',
        'info':'\nSwitch Tinder in your browser, program starts in 5 seconds...\nPress ctrl+c to terminate program.',
        'info2':'\nLIKE BUTTON',
        'info3':'\nDISLIKE BUTTON',
        'instruction1':'\nMake a screenshot of your browser with Tinder on, paste it into Paint and:\n1.Draw a rectangle around the photo\n2.Read the x/y of top left corner\n3.Read WIDTH AND HEIGHT of the rect\n4.Type: top left x, top left y, rect width, rect height.',
        'instruction2':'\nType in the rectangle coordinates, each separated with coma (ex. 900,600,100,50): ',
        'instruction3':'\nType in button\'s coordinates, each separated with coma (ex. 200,300)'
    }

    for name in folderNames:
        createFolder(name)

    setInitCoords()
    
    print(messages['greet'])
    choice = input(messages['question'])

    if choice in possAns:
        print(messages['instruction1'])
        coords = input(messages['instruction2'])
        setCoordsImg(coords)

        #setting LIKE
        print(messages['info2'])
        coords = input(message['instruction3'])
        setCoordsBtn(1,coords)

        #setting DISLIKE
        print(messages['info3'])
        coords = input(message['instruction3'])
        setCoordsBtn(0,coords)

    print(messages['info'])
    sleep(5)