transform zoom_in:
    zoom 1
    linear 0.5 zoom 2

screen investigation_board():

    modal True
    tag board2

    key "dismiss" action Return()

    add Transform(
        "investigationboard.png",
        xalign=0.5,
        yalign=0.5,
        xsize=config.screen_width,
        ysize=config.screen_height
    )
    
    # HAMMER
    imagebutton:
        idle Transform("hammer.png", zoom=0.12, rotate=-4)
        hover Transform("hammer.png", zoom=0.17, rotate=-4)
        xpos 460 # left - decrease; right - increase
        ypos 370 # taas - decrease; baba - increase
        action NullAction()
    
    # SHOVEL
    imagebutton:
        idle Transform("shovel.png", zoom=0.12, rotate=6)
        hover Transform("shovel.png", zoom=0.17, rotate=6)
        xpos 600 # left - decrease; right - increase
        ypos 365 # taas - decrease; baba - increase
        action NullAction()

    # CROWBAR
    imagebutton:
        idle Transform("crowbar.png", zoom=0.10, rotate=4)
        hover Transform("crowbar.png", zoom=0.15, rotate=4)
        xpos 570 # left - decrease; right - increase
        ypos 300 # taas - decrease; baba - increase
        action NullAction()
    
    # HAND
    imagebutton:
        idle Transform("hand.png", zoom=0.14, rotate=-4)
        hover Transform("hand.png", zoom=0.19, rotate=-4)
        xpos 583 # left - decrease; right - increase
        ypos 190 # taas - decrease; baba - increase
        action NullAction()
    
    # SKULL
    imagebutton:
        idle Transform("skull.png", zoom=0.13, rotate=10)
        hover Transform("skull.png", zoom=0.18, rotate=10)
        xpos 550 # left - decrease; right - increase
        ypos 130 # taas - decrease; baba - increase
        action NullAction()
    
    # SPLATTER (BLOOD DIN, IBA LANG NAME)
    imagebutton:
        idle Transform("splatter.png", zoom=0.13, rotate=-1)
        hover Transform("splatter.png", zoom=0.18, rotate=-1)
        xpos 460 # left - decrease; right - increase
        ypos 250 # taas - decrease; baba - increase
        action NullAction()
    
    # BONES
    imagebutton:
        idle Transform("bones.png", zoom=0.12, rotate=-3)
        hover Transform("bones.png", zoom=0.17, rotate=-3)
        xpos 445 # left - decrease; right - increase
        ypos 150 # taas - decrease; baba - increase
        action NullAction()
    
    # BLOOD
    imagebutton:
        idle Transform("blood.png", zoom=0.13, rotate=5)
        hover Transform("blood.png", zoom=0.18, rotate=5)
        xpos 355 # left - decrease; right - increase
        ypos 230 # taas - decrease; baba - increase
        action NullAction()
    
    # BOY1
    imagebutton:
        idle Transform("boy1.png", zoom=0.19, rotate=1)
        hover Transform("boy1.png", zoom=0.24, rotate=1)
        xpos 765 # left - decrease; right - increase
        ypos 170 # taas - decrease; baba - increase
        action NullAction()
    
    # QUESTION
    imagebutton:
        idle Transform("question.png", zoom=0.23, rotate=2)
        hover Transform("question.png", zoom=0.28, rotate=2)
        xpos 735 # left - decrease; right - increase
        ypos 300 # taas - decrease; baba - increase
        action NullAction()
    
    # GIRL
    imagebutton:
        idle Transform("girl.png", zoom=0.19, rotate=1)
        hover Transform("girl.png", zoom=0.24, rotate=1)
        xpos 960 # left - decrease; right - increase
        ypos 305 # taas - decrease; baba - increase
        action NullAction()

    # BOY2
    imagebutton:
        idle Transform("boy2.png", zoom=0.19, rotate=1)
        hover Transform("boy2.png", zoom=0.24, rotate=1)
        xpos 920 # left - decrease; right - increase
        ypos 180 # taas - decrease; baba - increase
        action NullAction()
