from vpython import *
#Web VPython 3.2
import random
##not the game
winner = ""
while True:
    winner = game(winner)

##The game
def game(winner):
    #home
    pixelsInX = 1650
    pixelsInY = 875
    
    scene = canvas(width = pixelsInX, height = pixelsInY)
    
    scene.userzoom = False
    scene.userspin = False
    scene.userpan = False
    
    ##All on screen text
    title = label(pixel_pos = True, pos = vec(pixelsInX/2,pixelsInY-100,0), text = "Wars in Stars", box = False, font = "monospace", height=(100))
    victory = label(pixel_pos = True, pos = vec(pixelsInX/2,pixelsInY-180,0), text = winner, box = False, font = "monospace", height=(40))
    play = label(pixel_pos = True, pos = vec(150,pixelsInY-300,0), text = " Play ", box = False, font = "monospace", height=(70), align = "left")
    howToPlay = label(pixel_pos = True, pos = vec(150,pixelsInY-400,0), text = " How To Play ", box = False, font = "monospace", height=(70), align = "left")
    DLC = label(pixel_pos = True, pos = vec(150,pixelsInY-500,0), text = " DLC ", box = False, font = "monospace", height=(70), align = "left")
    selecting = label(pixel_pos = True, pos = vec(200,100,0), text = "Use 'q' and 'e' to choose. Then use 'ENTER' to select", box = False, font = "monospace", height=(20), align = "left")
    
    ##creates background ship
    ##points for the ship outline
    a = vertex(pos=vec(0,20,0))
    b = vertex(pos=vec(0,0,50))
    c = vertex(pos=vec(0,-20,0))
    d = vertex(pos=vec(0,0,-50))
    e = vertex(pos=vec(150,0,0))
    f = vertex(pos=vec(-30,0,0))
    
    pa = (pos=vec(0,20,0))
    pb = (pos=vec(0,0,50))
    pc = (pos=vec(0,-20,0))
    pd = (pos=vec(0,0,-50))
    pe = (pos=vec(150,0,0))
    pf = (pos=vec(-30,0,0))
    
    ##creates part of the ship
    topFront= quad(v0=(a),v1=(b),v2=(e),v3=(d))
    botFront= quad(v0=(c),v1=(b),v2=(e),v3=(d))
    topBack = quad(v0=(a),v1=(b),v2=(f),v3=(d))
    botBack = quad(v0=(c),v1=(b),v2=(f),v3=(d))
    
    rad = 1
    lineA1 = cylinder(pos=pa,axis=(pb-pa), radius=rad)
    lineA2 = cylinder(pos=pa,axis=(pd-pa), radius=rad)
    lineA3 = cylinder(pos=pa,axis=(pe-pa), radius=rad)
    lineA4 = cylinder(pos=pa,axis=(pf-pa), radius=rad)
    
    lineC1 = cylinder(pos=pc,axis=(pb-pc), radius=rad)
    lineC2 = cylinder(pos=pc,axis=(pd-pc), radius=rad)
    lineC3 = cylinder(pos=pc,axis=(pe-pc), radius=rad)
    lineC4 = cylinder(pos=pc,axis=(pf-pc), radius=rad)
    
    frontRightL = cylinder(pos=pe,axis=(pb-pe), radius=rad)
    rightBackL = cylinder(pos=pb,axis=(pf-pb), radius=rad)
    backLeftL = cylinder(pos=pf,axis=(pd-pf), radius=rad)
    leftFrontL = cylinder(pos=pd,axis=(pe-pd), radius=rad)
    
    ##torpedo salvo
    salvo = box(pos=vec(40,10,20), size=vec(25,5,10))
    salvo2 = box(pos=vec(40,10,-20), size=vec(25,5,10))
    
    salvo.rotate(angle=-pi/8, axis=pf-pe)
    salvo.rotate(angle=pi/32, axis=pd-pb)
    salvo2.rotate(angle=pi/8, axis=pf-pe)
    salvo2.rotate(angle=pi/32, axis=pd-pb)
    
    intTor = []
    for i in range(4):
        shaft = ellipsoid(length=20, width=2.5, height=2.5, color=vec(0.7,0.7,0.7))
        flair = pyramid(pos=vec(-10,0,0), size=vector(5, 2.5, 2.5), color=vec(0.7,0.7,0.7))
        fire1 = sphere(pos = vec(-10,0,0), radius=(0.5), color = color.red)
        fire2 = sphere(pos = vec(-10,0.5,0.5), radius=(0.5), color = color.red)
        fire3 = sphere(pos = vec(-10,-0.5,0.5), radius=(0.5), color = color.red)
        fire4 = sphere(pos = vec(-10,0.5,-0.5), radius=(0.5), color = color.red)
        fire5 = sphere(pos = vec(-10,-0.5,-0.5), radius=(0.5), color = color.red)
        intTor[i] = compound([shaft, flair, fire1, fire2, fire3, fire4, fire5])
    
    intTor[0].rotate(angle=-pi/8, axis=pf-pe)
    intTor[0].rotate(angle=pi/32, axis=pd-pb)
    intTor[0].pos=vec(45,8.5,22)
    
    intTor[1].rotate(angle=-pi/8, axis=pf-pe)
    intTor[1].rotate(angle=pi/32, axis=pd-pb)
    intTor[1].pos=vec(45,10,18)
    
    ##salvo2
    intTor[2].rotate(angle=pi/8, axis=pf-pe)
    intTor[2].rotate(angle=pi/32, axis=pd-pb)
    intTor[2].pos=vec(45,8.5,-22)
    
    intTor[3].rotate(angle=pi/8, axis=pf-pe)
    intTor[3].rotate(angle=pi/32, axis=pd-pb)
    intTor[3].pos=vec(45,10,-18)
    
    bridge1 = box(pos=vec(0,22.5,0), size=vector(7,15,10))
    bridge2 = box(pos=vec(0,35,0), size=vector(10,10,30))
    
    ##hitbox = box(pos=vec((e.pos.x+f.pos.x)/2, (a.pos.y+c.pos.y)/2, (b.pos.z+d.pos.z)/2), size=vec((e.pos.x - f.pos.x), a.pos.y*2, b.pos.z*2), opacity = 0.3)
    
    ##connect ship and shadow parts and add axis'
    edges = compound([lineA1, lineA2, lineA3, lineA4, lineC1, lineC2, lineC3, lineC4, frontRightL, leftFrontL, rightBackL, backLeftL])
    edges.color = color.green
    ship = compound([topFront, botFront, topBack, botBack, bridge1, bridge2, edges, salvo, salvo2])
    ship.pos += vec(50,0,200)
    ship.rotate(angle=pi*0.8, axis=vec(0,-1,0))
    for i in range(4):
        intTor[i].pos += vec(50,0,200)
        intTor[i].rotate(angle=pi*0.8, axis=vec(0,-1,0), origin=ship.pos)
    
    ##lets user choose in main menu
    menuSelect = 1
    while True:
        rate(100)
        title.visible = True
        play.visible = True
        howToPlay.visible = True
        DLC.visible = True
        selecting.visible = True
        ship.visible = True
        victory.visible = True
        for i in range(4):
            intTor[i].visible = True
        k = keysdown()
        if 'q' in k:
            scene.waitfor("keyup")
            if menuSelect > 1:
                menuSelect -= 1
        if 'e' in k:
            scene.waitfor("keyup")
            if menuSelect < 3:
                menuSelect += 1
        if menuSelect == 1:
            play.text = "[Play]"
        else:
            play.text = " Play "
        if menuSelect == 2:
            howToPlay.text = "[How To Play]"
        else:
            howToPlay.text = " How To Play "
        if menuSelect == 3:
            DLC.text = "[DLC]"
        else:
            DLC.text = " DLC "
        if '\n' in k:
            scene.waitfor("keyup")
            title.visible = False
            play.visible = False
            howToPlay.visible = False
            DLC.visible = False
            selecting.visible = False
            ship.visible = False
            victory.visible = False
            for i in range(4):
                intTor[i].visible = False
            if menuSelect == 1:
                break
            if menuSelect == 2:
                rules()
            if menuSelect == 3:
                content()
    
    ##screen for How to Play
    def rules():
        controlles = label(pixel_pos = True, pos = vec(50,pixelsInY-50,0), box = False, font = "monospace", height=(30), align = "left", text = "")
        scrollText(controlles, "Controlles:\n'wasd' to rotate your ship.\nNumbers 1-9 to show where your ship will move, use 0 to stop your ship.\nUse 'q' and 'e' to select 'Attack' or 'Reload'.\nOnce all options have been selected, use 'ENTER' to confirm and watch the explosions happen.\n\nActions:\n'Attack' will launch a homing torpedo that will zero in on the opponent.\nYou will run out of torpedoes and will have to use 'reload' to get up to 5 again.\n\nThis is a turn based game so take your time.\nLook around with right click and drag with your mouse.\n\n\nPress 'b' to go back to main menu.")
        while True:
            rate(100)
            k = keysdown()
            if 'b' in k:
                scene.waitfor("keyup")
                controlles.visible = False
                del controlles
                break
    
    ##screen for DLC
    def content():
        comingSoon = label(pixel_pos = True, pos = vec(50,pixelsInY-50,0), box = False, font = "monospace", height=(30), align = "left", text = "")
        scrollText(comingSoon, "Coming Soon...\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress 'b' to go back to main menu.")
        while True:
            rate(100)
            k = keysdown()
            if 'b' in k:
                scene.waitfor("keyup")
                comingSoon.visible = False
                del comingSoon
                break
    
    ##clear screen
    title.visible = False
    play.visible = False
    howToPlay.visible = False
    DLC.visible = False
    selecting.visible = False
    ship.visible = False
    victory.visible = False
    for i in range(4):
        intTor[i].visible = False
    del title
    del play
    del howToPlay
    del DLC
    del selecting
    del a
    del b
    del c
    del d
    del e
    del f
    del pa
    del pb
    del pc
    del pd
    del pe
    del pf
    del topFront
    del botFront
    del topBack
    del botBack
    del lineA1
    del lineA2
    del lineA3
    del lineA4
    del lineC1
    del lineC2
    del lineC3
    del lineC4
    del frontRightL
    del rightBackL
    del backLeftL
    del leftFrontL
    del salvo
    del salvo2
    del intTor
    del shaft
    del flair
    del fire1
    del fire2
    del fire3
    del fire4
    del fire5
    del bridge1
    del bridge2
    del edges
    del ship
    del victory
    
    pixelsInX = scene.width
    pixelsInY = scene.height
    
    scene.width = pixelsInX
    scene.height = pixelsInY
    ##sets camera to be centered
    scene.autoscale = False
    scene.userzoom = True
    scene.userspin = True
    scene.userpan = True
    
    ##variable declaration / HUD creation
    ##used to show health
    health = ["||||||||||", "||||||||", "||||||", "||||", "||", ""]
    hit = 0
    hitOP = 0
    
    ##shows torpedo count
    torDisplay = ["", "|\n^", "| |\n^ ^", "| | |\n^ ^ ^", "| | | |\n^ ^ ^ ^", "| | | | |\n^ ^ ^ ^ ^"]
    torTracker = 5
    torTrackerOP = 5
    
    heightFromTop = 15
    
    turn = 0
    turningMax = 50
    
    turnOrder = label(pixel_pos = True, pos = vec(pixelsInX/2,pixelsInY-heightFromTop,0), text = "", font = "monospace", box = False)
    
    ##P1 text stat trackers
    y=0
    hitPointsTitle = label(pixel_pos = True, pos = vec(60,pixelsInY-heightFromTop-(25*y),0), text = "HP", box = False, font = "monospace")
    y+=1
    hitPoints = label(pixel_pos = True, pos = vec(20,pixelsInY-heightFromTop-(25*y),0), text = health[hit], font = "monospace", box = False, align = "left")
    y+=1
    torCountTitle = label(pixel_pos = True, pos = vec(60,pixelsInY-heightFromTop-(25*y),0), text = "Torpedoes", box = False, font = "monospace")
    y+=1
    torCount = label(pixel_pos = True, pos = vec(23,pixelsInY-heightFromTop-(25*y),0), text = torDisplay[torTracker], font = "monospace", box = False, align = "left")
    y+=2
    attack = label(pixel_pos = True, pos = vec(60,pixelsInY-heightFromTop-(25*y),0), text = "Attack", font = "monospace", box = False)
    y+=1
    reload = label(pixel_pos = True, pos = vec(60,pixelsInY-heightFromTop-(25*y),0), text = "Reload", font = "monospace", box = False)
    y+=1
    """
    sheild = label(pixel_pos = True, pos = vec(60,pixelsInY-heightFromTop-(25*y),0), text = "Sheild", font = "monospace", box = False)
    y+=1
    fullSpeed = label(pixel_pos = True, pos = vec(60,pixelsInY-heightFromTop-(25*y),0), text = "Full Speed", font = "monospace", box = False)
    y+=1"""
    
    
    ##P2 text stat trackers
    y=0
    hitPointsTitleOP = label(pixel_pos = True, pos = vec(pixelsInX - 60,pixelsInY-heightFromTop-(25*y),0), text = "HP", box = False, font = "monospace")
    y+=1
    hitPointsOP = label(pixel_pos = True, pos = vec(pixelsInX - 20,pixelsInY-heightFromTop-(25*y),0), text = health[hitOP], font = "monospace", box = False, align = "right")
    y+=1
    torCountTitleOP = label(pixel_pos = True, pos = vec(pixelsInX - 60,pixelsInY-heightFromTop-(25*y),0), text = "Torpedoes", box = False, font = "monospace")
    y+=1
    torCountOP = label(pixel_pos = True, pos = vec(pixelsInX - 23,pixelsInY-heightFromTop-(25*y),0), text = torDisplay[torTrackerOP], font = "monospace", box = False, align = "right")
    y+=2
    attackOP = label(pixel_pos = True, pos = vec(pixelsInX - 60,pixelsInY-heightFromTop-(25*y),0), text = "Attack", font = "monospace", box = False)
    y+=1
    reloadOP = label(pixel_pos = True, pos = vec(pixelsInX - 60,pixelsInY-heightFromTop-(25*y),0), text = "Reload", font = "monospace", box = False)
    y+=1
    """
    sheildOP = label(pixel_pos = True, pos = vec(pixelsInX - 60,pixelsInY-heightFromTop-(25*y),0), text = "Sheild", font = "monospace", box = False)
    y+=1
    fullSpeedOP = label(pixel_pos = True, pos = vec(pixelsInX - 60,pixelsInY-heightFromTop-(25*y),0), text = "Full Speed", font = "monospace", box = False)
    y+=1"""
    
    #################################################### FUNCTIONS STARTS #####################################################################
    
    def select(choice, attack, reload):
        if choice == 1:
            attack.text = "[Attack]"
            reload.text = "Reload"
        elif choice == 2:
            attack.text = "Attack"
            reload.text = "[Reload]"
    
    ##text for displaying health
    def HP(hit, hitPointsTitle, hitPoints):
        subHit = hit-1
        if subHit == -1:
            subHit = 5
        
        hitPoints.text = health[hit]
        for i in range(2):
            hitPoints.text = health[subHit]
            sleep(0.15)
            hitPoints.text = health[hit]
            sleep(0.15)
        if hit == 5:
            ##hitPointsTitle.text = "TOTAL HULL FAILURE EVACUATE IMMEDIATELY"
            hitPointsTitle.align = hitPoints.align
            hitPointsTitle.pos = hitPoints.pos + vec(0,20,0)
            hitPointsTitle.font = "monospace"
            scrollText(hitPointsTitle, "TOTAL HULL FAILURE EVACUATE IMMEDIATELY")
            scrollText(hitPoints, "ALL HANDS ABANDON SHIP. REPET ABANDON SHIP")
        return hit
    
    def scrollText(writeTo, phrase):
        for i in range(len(phrase)+1):
            rate(40)
            ##spaces = " "*(len(phrase)+2 - i)
            writeTo.text = phrase[:i] + " "*(len(phrase)+1 - i)
    
    ####################################################### MOVE/ATT FUNCTIONS ##################################################################
    
    def turning(invert, ship, shipX, shipZ, shadow, shipAxis, intTor, hitbox, collisionPoint):
        ##rotates ship and other parts
        turnAngle=pi/200
        ship.rotate(angle=turnAngle*invert, axis=vector(shipAxis.axis))
        shipX.rotate(angle=turnAngle*invert, axis=vector(shipAxis.axis), origin=(ship.pos))
        shipZ.rotate(angle=turnAngle*invert, axis=vector(shipAxis.axis), origin=(ship.pos))
        
        shadow.rotate(angle=turnAngle*invert, axis=vector(shipAxis.axis), origin=(ship.pos))
        collisionPoint.rotate(angle=turnAngle*invert, axis=vector(shipAxis.axis), origin=(ship.pos))
        
        for i in range(4):
            intTor[i].rotate(angle=turnAngle*invert, axis=vector(shipAxis.axis), origin=(ship.pos))
        for i in range(8):
            hitbox[i].rotate(angle=turnAngle*invert, axis=vector(shipAxis.axis), origin=(ship.pos))
    
    def distance(k, shadow, ship, shipZ, invert):
        ##num keys set distance
        ##delta distance
        if '1' in k:
            dd = 1/4
            shadow.pos = ship.pos + shipZ.axis*dd*invert
        if '2' in k:
            dd = 1/2
            shadow.pos = ship.pos + shipZ.axis*dd*invert
        if '3' in k:
            dd = 3/4
            shadow.pos = ship.pos + shipZ.axis*dd*invert
        if '4' in k:
            dd = 1
            shadow.pos = ship.pos + shipZ.axis*dd*invert
        if '5' in k:
            dd = 5/4
            shadow.pos = ship.pos + shipZ.axis*dd*invert
        if '6' in k:
            dd = 1.5
            shadow.pos = ship.pos + shipZ.axis*dd*invert
        if '7' in k:
            dd = 2
            shadow.pos = ship.pos + shipZ.axis*dd*invert
        if '8' in k:
            dd = 2.5
            shadow.pos = ship.pos + shipZ.axis*dd*invert
        if '9' in k:
            dd = floor(pi)
            shadow.pos = ship.pos + shipZ.axis*dd*invert
        if '0' in k:
            dd = 0
            shadow.pos = ship.pos
    
    def traverse(ship, shipOP, shadow, intTor, hitbox, hitboxOP, turn, hit, hitPointsTitle, hitPoints, collisionPoint):
        ##move ship on enter key and make it opponent turn
        x = 0
        movement = (shadow.pos - ship.pos)/100
        while True:
            rate(100)
            if ceil(ship.pos.x) == ceil(shadow.pos.x) & ceil(ship.pos.y) == ceil(shadow.pos.y) & ceil(ship.pos.z) == ceil(shadow.pos.z):
                shadow.pos = ship.pos
                break
            else if x == 165:
                shadow.pos = ship.pos
                break
            x += 1
            if x <= 100:
                ship.pos += movement*x/100
                for i in range(4):
                    intTor[i].pos += movement*x/100
                for i in range(8):
                    hitbox[i].pos += movement*x/100
                collisionPoint.pos += movement*x/100
            elif x >= 110:
                ship.pos += movement*(210-x)/100
                for i in range(4):
                    intTor[i].pos += movement*(210-x)/100
                for i in range(8):
                    hitbox[i].pos += movement*(210-x)/100
                collisionPoint.pos += movement*(210-x)/100
            else:
                ship.pos += movement
                for i in range(4):
                    intTor[i].pos += movement
                for i in range(8):
                    hitbox[i].pos += movement
                collisionPoint.pos += movement
            
            for i in range(turn):
                ##stop hitting yourself
                if x/10 == floor(x/10) and mag(tor[i].pos-ship.pos) <= 90:
                    if hitReg(tor[i].pos, hitbox) == True:
                        hit += 1
                        HP(hit, hitPointsTitle, hitPoints)
                        empty = i+2
                        while True:
                            if tor[empty].pos.x > 4900:
                                break
                            empty+=2
                        tor[i].pos = tor[empty-2].pos
                        tor[i].axis = tor[empty-2].axis
                        tor[empty-2].pos = vec(5000, 0, 0)
            ##opponent collision
            if mag(shipOP.pos-ship.pos) <= 180:
                if hitReg(collisionPoint.pos, hitboxOP) == True:
                    ship.pos -= movement
                    for i in range(4):
                        intTor[i].pos -= movement
                    for i in range(8):
                        hitbox[i].pos -= movement
                    collisionPoint.pos -= movement
            ##stops ship from going out of bounds
            if mag(ship.pos) >= 4000:
                ship.pos -= movement
                for i in range(4):
                    intTor[i].pos -= movement
                for i in range(8):
                    hitbox[i].pos -= movement
                collisionPoint.pos -= movement
        return(hit)
    
    """
    def lasers():
        laser = []
        for i in range(3):
            laser[i] = ellipsoid(pos=vector(i*40,0,0), length=20, width=2.5, height=2.5, color=color.red)
    
    def lanceAtt():
        lance = ellipsoid(pos=vector(ship), length=2, width=0.25, height=0.25, color=color.red)"""
        
    def torpedo(tor, intTor, OP, torCount):
        randy = random.randint(0,3)
        ##finds next open spot in the array and makes torpedoX
        i=0 + OP
        while True:
            rate(1)
            if tor[i].pos.x > 4900:
                break
            else:
                ##every other array slot. Even(0) for player one. Odd(1) for player two.
                i += 2
        tor[i].pos = intTor[randy].pos
        if OP == 0:
            tor[i].axis = intTor[0].axis
        else:
            tor[i].axis = intTorOP[0].axis
        
        ##torDisplay = 
    
    def torMovement(i, hitbox, hitboxOP, ship, shipOP, hit):
        ##move all p1 tor
        hitTic = 3
        if i == 0:
            while True:
                quickbreak = False
                if tor[i].pos.x > 4900:
                    break
                x = 0
                movement = (tor[i].axis)/5
                while True:
                    rate(300)
                    if x >= 100:
                        break
                    if x <= 30:
                        tor[i].pos += movement*x/30
                    elif x >= 70:
                        tor[i].pos += movement*(100-x)/30
                    else:
                        tor[i].pos += movement
                    ##hit torpedos
                    if x/hitTic == floor(x/hitTic) and mag(tor[i].pos-shipOP.pos) <= 90:
                        if hitReg(tor[i].pos, hitboxOP) == True:
                            boomBoom(tor[i].pos)
                            hit += 1
                            hit = HP(hit, hitPointsTitleOP, hitPointsOP)
                            empty = 0
                            while True:
                                if tor[empty].pos.x > 4900:
                                    break
                                empty+=2
                            tor[i].pos = tor[empty-2].pos
                            tor[i].axis = tor[empty-2].axis
                            tor[empty-2].pos = vec(5000, 0, 0)
                            quickbreak = True
                            break
                    ##stop hitting yourself
                    if x/hitTic == floor(x/hitTic) and mag(tor[i].pos-ship.pos) <= 90:
                        if hitReg(tor[i].pos, hitbox) == True:
                            boomBoom(tor[i].pos)
                            hit += 1
                            hit *= -1
                            empty = 0
                            while True:
                                if tor[empty].pos.x > 4900:
                                    break
                                empty+=2
                            tor[i].pos = tor[empty-2].pos
                            tor[i].axis = tor[empty-2].axis
                            tor[empty-2].pos = vec(5000, 0, 0)
                            quickbreak = True
                            break
                    x += 1
                if quickbreak == False:
                    ##cross product of tor and target
                    CrossPro = cross((shipOP.pos - tor[i].pos), tor[i].axis)
                    
                    ##angle to target 
                    angleToTarget = diff_angle((shipOP.pos - tor[i].pos), tor[i].axis)
                    
                    if angleToTarget >= pi/3:
                        turnRate = pi/3
                        ##print("P1 set")
                    else:
                        ##print("P1 "+angleToTarget)
                        turnRate = angleToTarget
                    tor[i].rotate(angle=(-turnRate), axis=(CrossPro))
                    i += 2
        ##move all p2 tor
        if i == 1:
            while True:
                quickbreak = False
                if tor[i].pos.x > 4000:
                    break
                x = 0
                movement = (tor[i].axis)/5
                while True:
                    rate(300)
                    if x >= 100:
                        break
                    if x <= 30:
                        tor[i].pos += movement*x/30
                    elif x >= 70:
                        tor[i].pos += movement*(100-x)/30
                    else:
                        tor[i].pos += movement
                    ##hit torpedosOP
                    if x/hitTic == floor(x/hitTic) and mag(tor[i].pos-ship.pos) <= 90:
                        if hitReg(tor[i].pos, hitbox) == True:
                            boomBoom(tor[i].pos)
                            hit += 1
                            hit = HP(hit, hitPointsTitle, hitPoints)
                            empty = 1
                            while True:
                                if tor[empty].pos.x > 4900:
                                    break
                                empty+=2
                            tor[i].pos = tor[empty-2].pos
                            tor[i].axis = tor[empty-2].axis
                            tor[empty-2].pos = vec(5000, 0, 0)
                            quickbreak = True
                            break
                    ##stop hitting yourself
                    if x/hitTic == floor(x/hitTic) and mag(tor[i].pos-shipOP.pos) <= 90:
                        if hitReg(tor[i].pos, hitboxOP) == True:
                            boomBoom(tor[i].pos)
                            hit += 1
                            hit *= -1
                            empty = 0
                            while True:
                                if tor[empty].pos.x > 4900:
                                    break
                                empty+=2
                            tor[i].pos = tor[empty-2].pos
                            tor[i].axis = tor[empty-2].axis
                            tor[empty-2].pos = vec(5000, 0, 0)
                            quickbreak = True
                            break
                    x += 1
                if quickbreak == False:
                    ##cross product of tor and target
                    CrossPro = cross((ship.pos - tor[i].pos), tor[i].axis)
                    
                    ##angle to target 
                    angleToTarget = diff_angle((ship.pos - tor[i].pos), tor[i].axis)
                    
                    if angleToTarget >= pi/3:
                        turnRate = pi/3
                        ##print("P1 set")
                    else:
                        ##print("P1 "+angleToTarget)
                        turnRate = angleToTarget
                    tor[i].rotate(angle=(-turnRate), axis=(CrossPro))
                    i += 2
        return(hit)
    
    ##hit registration
    def hitReg(point, hitbox):
        hit = True
        pointAxis = ellipsoid(opacity=0)
        for i in range(8):
            pointAxis.axis = point - hitbox[i].pos
            angleToHit = diff_angle(hitbox[i].axis, pointAxis.axis)
            
            if abs(angleToHit) < pi/2:
                hit = False
                break
        del pointAxis
        return hit
        
    def boomBoom(point):
        andre = sphere(pos=point, radius=(0), texture=("https://t3.ftcdn.net/jpg/03/04/54/36/360_F_304543628_5nns3tVTWRqogZJij4ad4YhquGRI06Pw.jpg"), opacity=0.8)
        for i in range(6):
            rate(100)
            andre.radius += 6-i
        for i in range(6):
            rate(100)
            andre.radius -= i+1
        del andre
    
    ################################################## LEVEL CREATION #######################################################################
    
    ##points for the ship outline
    a = vertex(pos=vec(0,20,0))
    b = vertex(pos=vec(0,0,50))
    c = vertex(pos=vec(0,-20,0))
    d = vertex(pos=vec(0,0,-50))
    e = vertex(pos=vec(150,0,0))
    f = vertex(pos=vec(-30,0,0))
    
    pa = (pos=vec(0,20,0))
    pb = (pos=vec(0,0,50))
    pc = (pos=vec(0,-20,0))
    pd = (pos=vec(0,0,-50))
    pe = (pos=vec(150,0,0))
    pf = (pos=vec(-30,0,0))
    
    ##creates part of the ship
    topFront= quad(v0=(a),v1=(b),v2=(e),v3=(d))
    botFront= quad(v0=(c),v1=(b),v2=(e),v3=(d))
    topBack = quad(v0=(a),v1=(b),v2=(f),v3=(d))
    botBack = quad(v0=(c),v1=(b),v2=(f),v3=(d))
    
    rad = 1
    lineA1 = cylinder(pos=pa,axis=(pb-pa), radius=rad)
    lineA2 = cylinder(pos=pa,axis=(pd-pa), radius=rad)
    lineA3 = cylinder(pos=pa,axis=(pe-pa), radius=rad)
    lineA4 = cylinder(pos=pa,axis=(pf-pa), radius=rad)
    
    lineC1 = cylinder(pos=pc,axis=(pb-pc), radius=rad)
    lineC2 = cylinder(pos=pc,axis=(pd-pc), radius=rad)
    lineC3 = cylinder(pos=pc,axis=(pe-pc), radius=rad)
    lineC4 = cylinder(pos=pc,axis=(pf-pc), radius=rad)
    
    frontRightL = cylinder(pos=pe,axis=(pb-pe), radius=rad)
    rightBackL = cylinder(pos=pb,axis=(pf-pb), radius=rad)
    backLeftL = cylinder(pos=pf,axis=(pd-pf), radius=rad)
    leftFrontL = cylinder(pos=pd,axis=(pe-pd), radius=rad)
    
    ##torpedo salvo
    salvo = box(pos=vec(40,10,20), size=vec(25,5,10))
    salvo2 = box(pos=vec(40,10,-20), size=vec(25,5,10))
    
    salvo.rotate(angle=-pi/8, axis=pf-pe)
    salvo.rotate(angle=pi/32, axis=pd-pb)
    salvo2.rotate(angle=pi/8, axis=pf-pe)
    salvo2.rotate(angle=pi/32, axis=pd-pb)
    
    ##sets points for tor to launch from
    intTor = []
    for i in range(4):
        shaft = ellipsoid(length=20, width=2.5, height=2.5, color=vec(0.7,0.7,0.7))
        flair = pyramid(pos=vec(-10,0,0), size=vector(5, 2.5, 2.5), color=vec(0.7,0.7,0.7))
        fire1 = sphere(pos = vec(-10,0,0), radius=(0.5), color = color.red)
        fire2 = sphere(pos = vec(-10,0.5,0.5), radius=(0.5), color = color.red)
        fire3 = sphere(pos = vec(-10,-0.5,0.5), radius=(0.5), color = color.red)
        fire4 = sphere(pos = vec(-10,0.5,-0.5), radius=(0.5), color = color.red)
        fire5 = sphere(pos = vec(-10,-0.5,-0.5), radius=(0.5), color = color.red)
        intTor[i] = compound([shaft, flair, fire1, fire2, fire3, fire4, fire5])
    
    intTor[0].rotate(angle=-pi/8, axis=pf-pe)
    intTor[0].rotate(angle=pi/32, axis=pd-pb)
    intTor[0].pos=vec(45,8.5,22)
    
    intTor[1].rotate(angle=-pi/8, axis=pf-pe)
    intTor[1].rotate(angle=pi/32, axis=pd-pb)
    intTor[1].pos=vec(45,10,18)
    
    ##salvo2
    intTor[2].rotate(angle=pi/8, axis=pf-pe)
    intTor[2].rotate(angle=pi/32, axis=pd-pb)
    intTor[2].pos=vec(45,8.5,-22)
    
    intTor[3].rotate(angle=pi/8, axis=pf-pe)
    intTor[3].rotate(angle=pi/32, axis=pd-pb)
    intTor[3].pos=vec(45,10,-18)
    
    ##shipOP
    ##sets points for tor to launch from
    intTorOP = []
    for i in range(4):
        shaft = ellipsoid(length=20, width=2.5, height=2.5, color=vec(0.7,0.7,0.7))
        flair = pyramid(pos=vec(-10,0,0), size=vector(5, 2.5, 2.5), color=vec(0.7,0.7,0.7))
        fire1 = sphere(pos = vec(-10,0,0), radius=(0.5), color = color.red)
        fire2 = sphere(pos = vec(-10,0.5,0.5), radius=(0.5), color = color.red)
        fire3 = sphere(pos = vec(-10,-0.5,0.5), radius=(0.5), color = color.red)
        fire4 = sphere(pos = vec(-10,0.5,-0.5), radius=(0.5), color = color.red)
        fire5 = sphere(pos = vec(-10,-0.5,-0.5), radius=(0.5), color = color.red)
        intTorOP[i] = compound([shaft, flair, fire1, fire2, fire3, fire4, fire5])
    
    intTorOP[0].rotate(angle=-pi/8, axis=pf-pe)
    intTorOP[0].rotate(angle=pi/32, axis=pd-pb)
    intTorOP[0].pos=vec(45,8.5,22)
    
    intTorOP[1].rotate(angle=-pi/8, axis=pf-pe)
    intTorOP[1].rotate(angle=pi/32, axis=pd-pb)
    intTorOP[1].pos=vec(45,10,18)
    
    ##salvo2
    intTorOP[2].rotate(angle=pi/8, axis=pf-pe)
    intTorOP[2].rotate(angle=pi/32, axis=pd-pb)
    intTorOP[2].pos=vec(45,8.5,-22)
    
    intTorOP[3].rotate(angle=pi/8, axis=pf-pe)
    intTorOP[3].rotate(angle=pi/32, axis=pd-pb)
    intTorOP[3].pos=vec(45,10,-18)
    
    visable = 0
    hitPoint = []
    hitPoint[0] = cylinder(pos=pa,axis=(pb-pa), radius=rad, opacity = (visable))
    hitPoint[1] = cylinder(pos=pa,axis=(pe-pa), radius=rad, opacity = (visable))
    hitPoint[2] = cylinder(pos=pa,axis=(pd-pa), radius=rad, opacity = (visable))
    hitPoint[3] = cylinder(pos=pa,axis=(pf-pa), radius=rad, opacity = (visable))
    
    hitPoint[4] = cylinder(pos=pc,axis=(pe-pc), radius=rad, opacity = (visable))
    hitPoint[5] = cylinder(pos=pc,axis=(pd-pc), radius=rad, opacity = (visable))
    hitPoint[6] = cylinder(pos=pc,axis=(pf-pc), radius=rad, opacity = (visable))
    hitPoint[7] = cylinder(pos=pc,axis=(pb-pc), radius=rad, opacity = (visable))
    
    hitbox = []
    hitbox[0] = pyramid(axis = cross(hitPoint[3].axis, hitPoint[0].axis), pos = hitPoint[0].pos, opacity = (visable))
    hitbox[1] = pyramid(axis = cross(hitPoint[0].axis, hitPoint[1].axis), pos = hitPoint[1].pos, opacity = (visable))
    hitbox[2] = pyramid(axis = cross(hitPoint[1].axis, hitPoint[2].axis), pos = hitPoint[2].pos, opacity = (visable))
    hitbox[3] = pyramid(axis = cross(hitPoint[2].axis, hitPoint[3].axis), pos = hitPoint[3].pos, opacity = (visable))
    
    hitbox[4] = pyramid(axis = cross(hitPoint[4].axis, hitPoint[7].axis), pos = hitPoint[4].pos, opacity = (visable))
    hitbox[5] = pyramid(axis = cross(hitPoint[5].axis, hitPoint[4].axis), pos = hitPoint[5].pos, opacity = (visable))
    hitbox[6] = pyramid(axis = cross(hitPoint[6].axis, hitPoint[5].axis), pos = hitPoint[6].pos, opacity = (visable))
    hitbox[7] = pyramid(axis = cross(hitPoint[7].axis, hitPoint[6].axis), pos = hitPoint[7].pos, opacity = (visable))
    
    hitboxOP = []
    hitboxOP[0] = pyramid(axis = cross(hitPoint[3].axis, hitPoint[0].axis), pos = hitPoint[0].pos, opacity = (visable))
    hitboxOP[1] = pyramid(axis = cross(hitPoint[0].axis, hitPoint[1].axis), pos = hitPoint[1].pos, opacity = (visable))
    hitboxOP[2] = pyramid(axis = cross(hitPoint[1].axis, hitPoint[2].axis), pos = hitPoint[2].pos, opacity = (visable))
    hitboxOP[3] = pyramid(axis = cross(hitPoint[2].axis, hitPoint[3].axis), pos = hitPoint[3].pos, opacity = (visable))
    
    hitboxOP[4] = pyramid(axis = cross(hitPoint[4].axis, hitPoint[7].axis), pos = hitPoint[4].pos, opacity = (visable))
    hitboxOP[5] = pyramid(axis = cross(hitPoint[5].axis, hitPoint[4].axis), pos = hitPoint[5].pos, opacity = (visable))
    hitboxOP[6] = pyramid(axis = cross(hitPoint[6].axis, hitPoint[5].axis), pos = hitPoint[6].pos, opacity = (visable))
    hitboxOP[7] = pyramid(axis = cross(hitPoint[7].axis, hitPoint[6].axis), pos = hitPoint[7].pos, opacity = (visable))
    
    bridge1 = box(pos=vec(0,22.5,0), size=vector(7,15,10))
    bridge2 = box(pos=vec(0,35,0), size=vector(10,10,30))
    
    ##hitbox = box(pos=vec((e.pos.x+f.pos.x)/2, (a.pos.y+c.pos.y)/2, (b.pos.z+d.pos.z)/2), size=vec((e.pos.x - f.pos.x), a.pos.y*2, b.pos.z*2), opacity = 0.3)
    
    ##connect ship and shadow parts and add axis'
    edges = compound([lineA1, lineA2, lineA3, lineA4, lineC1, lineC2, lineC3, lineC4, frontRightL, leftFrontL, rightBackL, backLeftL])
    edges.color = color.green
    ship = compound([topFront, botFront, topBack, botBack, bridge1, bridge2, edges, salvo, salvo2])
    shadow = compound([topFront, botFront, topBack, botBack, bridge1, bridge2, salvo, salvo2])
    shadow.opacity = 0.3
    visableAxis = 0
    shipX = cylinder(pos=pa,axis=(pd-pb), radius=visableAxis)
    shipY = cylinder(pos=pb,axis=(pc-pa), radius=visableAxis)
    shipZ = cylinder(pos=pe,axis=(pf-pe), radius=visableAxis)
    collisionPoint = sphere(pos=pe, radius=visableAxis)
    
    ship.pos += vector(-500,0,0)
    shadow.pos = ship.pos
    for i in range(4):
        intTor[i].pos += vec(-500,0,0)
    for i in range(8):
        hitbox[i].pos += vec(-500,0,0)
    collisionPoint.pos += vec(-500,0,0)
    ship.texture=textures.metal
    shadow.texture=textures.metal
    
    ##OP = opponent
    ##connect ship and shadow parts and add axis'
    edges.color = color.red
    shipOP = compound([topFront, botFront, topBack, botBack, bridge1, bridge2, edges, salvo, salvo2])
    shadowOP = compound([topFront, botFront, topBack, botBack, bridge1, bridge2, salvo, salvo2])
    shadowOP.opacity = 0.3
    visableAxisOP = 0
    shipXOP = cylinder(pos=pa,axis=(pd-pb), radius=visableAxisOP)
    shipYOP = cylinder(pos=pb,axis=(pc-pa), radius=visableAxisOP)
    shipZOP = cylinder(pos=pe,axis=(pf-pe), radius=visableAxisOP)
    collisionPointOP = sphere(pos=pe, radius=visableAxisOP)
    
    shipOP.texture=textures.metal
    shadowOP.texture=textures.metal
    
    ##ship to new position
    shipOP.pos += vector(500,0,0)
    shipOP.rotate(angle=pi, axis=vector(shipYOP.axis), origin=(shipOP.pos))
    shadowOP.pos = shipOP.pos
    shadowOP.rotate(angle=pi, axis=vector(shipYOP.axis), origin=(shipOP.pos))
    for i in range(4):
        ##530
        intTorOP[i].pos += vec(500,0,0)
        intTorOP[i].rotate(angle=pi, axis=vector(shipYOP.axis), origin=(shipOP.pos))
    for i in range(8):
        ##620
        hitboxOP[i].pos += vec(500,0,0)
        hitboxOP[i].rotate(angle=pi, axis=vector(shipYOP.axis), origin=(shipOP.pos))
    collisionPointOP.pos += vec(500,0,0)
    collisionPointOP.rotate(angle=pi, axis=vector(shipYOP.axis), origin=(shipOP.pos))
    
    for i in range(8):
        hitbox[i].axis.x = round(hitbox[i].axis.x)
        hitbox[i].axis.y = round(hitbox[i].axis.y)
        hitbox[i].axis.z = round(hitbox[i].axis.z)
    for i in range(8):
        hitboxOP[i].axis.x = round(hitboxOP[i].axis.x)
        hitboxOP[i].axis.y = round(hitboxOP[i].axis.y)
        hitboxOP[i].axis.z = round(hitboxOP[i].axis.z)
    
    ##ship creation finished
    
    ##backround
    space = "https://images.pexels.com/photos/998641/pexels-photo-998641.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
    ##background = sphere(radius=4900, texture=(space))
    ##background.rotate(angle = pi/2, axis = vec(0,1,0))
    space1 = box(size=vec(10000,10000,1), pos=vec(0,0,-5000), texture=(space))
    space2 = box(size=vec(10000,1,10000), pos=vec(0,-5000,0), texture=(space))
    space3 = box(size=vec(1,10000,10000), pos=vec(-5000,0,0), texture=(space))
    space4 = box(size=vec(10000,10000,1), pos=vec(0,0,5000), texture=(space))
    space5 = box(size=vec(10000,1,10000), pos=vec(0,5000,0), texture=(space))
    space6 = box(size=vec(1,10000,10000), pos=vec(5000,0,0), texture=(space))
    
    ##preload torpedos
    tor = []
    for i in range(100):
        shaft = ellipsoid(length=20, width=2.5, height=2.5, color=vec(0.7,0.7,0.7))
        flair = pyramid(pos=vec(-10,0,0), size=vector(5, 2.5, 2.5), color=vec(0.7,0.7,0.7))
        fire1 = sphere(pos = vec(-10,0,0), radius=(0.5), color = color.red)
        fire2 = sphere(pos = vec(-10,0.5,0.5), radius=(0.5), color = color.red)
        fire3 = sphere(pos = vec(-10,-0.5,0.5), radius=(0.5), color = color.red)
        fire4 = sphere(pos = vec(-10,0.5,-0.5), radius=(0.5), color = color.red)
        fire5 = sphere(pos = vec(-10,-0.5,-0.5), radius=(0.5), color = color.red)
        tor[i] = compound([shaft, flair, fire1, fire2, fire3, fire4, fire5])
        tor[i].pos = vec(5000,0,0)
    
    ####################################################### RUNNING CODE ##################################################################
    scene.camera.axis = vec(0,0, -1000)
    scene.center = (shipOP.pos + ship.pos)/2
    
    while True:
        ##reset turning
        turn += 1
        turnMaxX = 0
        turnMaxY = 0
        turnOrder.text = "Round "+turn+": Player 1"
        ##scene.camera.axis = -(ship.pos - shipOP.pos - ship.axis + vec(0,300,0))
        ##scene.center = (ship.pos + shipOP.pos)/2
        scene.camera.axis = vec(0,0, -1000)
        scene.center = (shipOP.pos + ship.pos)/2
        choice = 1
        while True:
            rate(100)
            k = keysdown()
            ##turns ship, axis' and shadow based on ship
            if 'w' in k:
                if turnMaxX < turningMax:
                    turning(1, ship, shipX, shipZ, shadow, shipX, intTor, hitbox, collisionPoint)
                    turnMaxX += 1
            if 's' in k:
                if turnMaxX > -turningMax:
                    turning(-1, ship, shipX, shipZ, shadow, shipX, intTor, hitbox, collisionPoint)
                    turnMaxX -= 1
            if 'a' in k:
                if turnMaxY < turningMax:
                    turning(-1, ship, shipX, shipZ, shadow, shipY, intTor, hitbox, collisionPoint)
                    turnMaxY += 1
            if 'd' in k:
                if turnMaxY > -turningMax:
                    turning(1, ship, shipX, shipZ, shadow, shipY, intTor, hitbox, collisionPoint)
                    turnMaxY -= 1
            if 'q' in k:
                scene.waitfor('keyup')
                if choice > 1:
                    choice -= 1
            if 'e' in k:
                scene.waitfor('keyup')
                if choice < 2:
                    choice += 1
            select(choice, attack, reload)
            distance(k, shadow, ship, shipZ, -1)
            if torTracker == 0 and choice == 1:
                scrollText(torCount, "Out Of Ammo")
                choice = 2
            elif '\n' in k:
                scene.waitfor('keyup')
                turnOrder.text = "loading..."
                hit = traverse(ship, shipOP, shadow, intTor, hitbox, hitboxOP, turn, hit, hitPointsTitle, hitPoints, collisionPoint)
                if choice == 1:
                    torpedo(tor, intTor, 0, torCount)
                    torTracker -= 1
                    torCount.text = torDisplay[torTracker]
                elif choice == 2:
                    torTracker = 5
                    torCount.text = torDisplay[torTracker]
                hitOP = torMovement(0, hitbox, hitboxOP, ship, shipOP, hitOP)
                if hitOP < 0:
                    hitOP *= -1
                    hitOP -= 1
                    hit +=1
                    hit = HP(hit, hitPointsTitle, hitPoints)
                break
        if hitOP == 5:
            scrollText(turnOrder, "Game Over: Player 1 wins")
            winner = "Winner: Player 1/Green"
            break
        
        turnOrder.text = "Round "+turn+": Player 2"
        ##scene.camera.axis = -(shipOP.pos - ship.pos - shipOP.axis + vec(0,300,0))
        ##scene.center = (shipOP.pos + ship.pos)/2
        scene.camera.axis = vec(0,0, -1000)
        scene.center = (shipOP.pos + ship.pos)/2
        choice = 1
        
        ##OP = opponent
        turnMaxXOP = 0
        turnMaxYOP = 0
        while True:
            rate(100)
            k = keysdown()
            ##turns ship, axis' and shadow based on ship
            if 'w' in k:
                if turnMaxXOP < turningMax:
                    turning(-1, shipOP, shipXOP, shipZOP, shadowOP, shipXOP, intTorOP, hitboxOP, collisionPointOP)
                    turnMaxXOP += 1
            if 's' in k:
                if turnMaxXOP > -turningMax:
                    turning(1, shipOP, shipXOP, shipZOP, shadowOP, shipXOP, intTorOP, hitboxOP, collisionPointOP)
                    turnMaxXOP -= 1
            if 'a' in k:
                if turnMaxYOP < turningMax:
                    turning(-1, shipOP, shipXOP, shipZOP, shadowOP, shipYOP, intTorOP, hitboxOP, collisionPointOP)
                    turnMaxYOP += 1
            if 'd' in k:
                if turnMaxYOP > -turningMax:
                    turning(1, shipOP, shipXOP, shipZOP, shadowOP, shipYOP, intTorOP, hitboxOP, collisionPointOP)
                    turnMaxYOP -= 1
            if 'q' in k:
                scene.waitfor('keyup')
                if choice > 1:
                    choice -= 1
            if 'e' in k:
                scene.waitfor('keyup')
                if choice < 2:
                    choice += 1
            select(choice, attackOP, reloadOP)
            distance(k, shadowOP, shipOP, shipZOP, 1)
            if torTrackerOP == 0 and choice == 1:
                scrollText(torCountOP, "Out Of Ammo")
                choice = 2
            elif '\n' in k:
                scene.waitfor('keyup')
                turnOrder.text = "loading..."
                hitOP = traverse(shipOP, ship, shadowOP, intTorOP, hitboxOP, hitbox, turn, hitOP, hitPointsTitleOP, hitPointsOP, collisionPointOP)
                if choice == 1:
                    torpedo(tor, intTorOP, 1, torCountOP)
                    torTrackerOP -= 1
                    torCountOP.text = torDisplay[torTrackerOP]
                elif choice == 2:
                    torTrackerOP = 5
                    torCountOP.text = torDisplay[torTrackerOP]
                hit = torMovement(1, hitbox, hitboxOP, ship, shipOP, hit)
                if hit < 0:
                    hit *= -1
                    hit -= 1
                    hitOP += 1
                    hitOP = HP(hitOP, hitPointsTitleOP, hitPointsOP)
                break
        if hit == 5:
            scrollText(turnOrder, "Game Over: Player 2 wins")
            winner = "Winner: Player 2/Red"
            break
    scene.visible = False
    scene.delete()
    return(winner)