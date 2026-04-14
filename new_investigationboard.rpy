transform zoom_in:
    zoom 1
    linear 0.5 zoom 2

screen new_investigationboard():

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

    # WATCH
    imagebutton:
        idle Transform("watch.png", zoom=0.20, rotate=7)
        hover Transform("watch.png", zoom=0.30, rotate=7)
        xpos 497
        ypos 516
        action NullAction()
    
    # EARRING
    imagebutton:
        idle Transform("earring.png", zoom=0.20, rotate=-4)
        hover Transform("earring.png", zoom=0.30, rotate=-4)
        xpos 420
        ypos 440
        action NullAction()
    
    # BLOOD
    imagebutton:
        idle Transform("blood.png", zoom=0.19, rotate=5)
        hover Transform("blood.png", zoom=0.29, rotate=5)
        xpos 540
        ypos 350
        action NullAction()

    # GLASS SHARDS
    imagebutton:
        idle Transform("glass_shards.png", zoom=0.25, rotate=5)
        hover Transform("glass_shards.png", zoom=0.35, rotate=5)
        xpos 440
        ypos 200
        action NullAction()

    # BONES
    imagebutton:
        idle Transform("bones.png", zoom=0.19, rotate=-3)
        hover Transform("bones.png", zoom=0.29, rotate=-3)
        xpos 680
        ypos 220
        action NullAction()
    
    # SPLATTER (BLOOD DIN, IBA LANG NAME)
    imagebutton:
        idle Transform("splatter.png", zoom=0.20, rotate=-2)
        hover Transform("splatter.png", zoom=0.30, rotate=-2)
        xpos 690
        ypos 360
        action NullAction()
    
    # HAND
    imagebutton:
        idle Transform("hand.png", zoom=0.22, rotate=-4)
        hover Transform("hand.png", zoom=0.32, rotate=-4)
        xpos 900
        ypos 280
        action NullAction()
    
    # SKULL
    imagebutton:
        idle Transform("skull.png", zoom=0.19, rotate=10)
        hover Transform("skull.png", zoom=0.29, rotate=10)
        xpos 830
        ypos 200
        action NullAction()
    
    # HAMMER
    imagebutton:
        idle Transform("hammer.png", zoom=0.18, rotate=-4)
        hover Transform("hammer.png", zoom=0.28, rotate=-4)
        xpos 700
        ypos 560
        action NullAction()
    
    # SHOVEL
    imagebutton:
        idle Transform("shovel.png", zoom=0.16, rotate=6)
        hover Transform("shovel.png", zoom=0.26, rotate=6)
        xpos 915
        ypos 545
        action NullAction()

    # CROWBAR
    imagebutton:
        idle Transform("crowbar.png", zoom=0.15, rotate=1)
        hover Transform("crowbar.png", zoom=0.25, rotate=1)
        xpos 850
        ypos 450
        action NullAction()
    
    # BOY1
    imagebutton:
        idle Transform("boy1.png", zoom=0.28, rotate=2)
        hover Transform("boy1.png", zoom=0.38, rotate=2)
        xpos 1160
        ypos 260
        action NullAction()
    
    # QUESTION
    imagebutton:
        idle Transform("question.png", zoom=0.33, rotate=1)
        hover Transform("question.png", zoom=0.43, rotate=1)
        xpos 1110
        ypos 455
        action NullAction()
    
    # BOY2
    imagebutton:
        idle Transform("boy2.png", zoom=0.28, rotate=1)
        hover Transform("boy2.png", zoom=0.38, rotate=1)
        xpos 1375
        ypos 265
        action NullAction()

    # GIRL
    imagebutton:
        idle Transform("girl.png", zoom=0.28, rotate=1)
        hover Transform("girl.png", zoom=0.38, rotate=1)
        xpos 1445
        ypos 450
        action NullAction()