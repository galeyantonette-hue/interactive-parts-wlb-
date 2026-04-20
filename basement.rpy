default hover_msg = ""

screen item_text():

    if hover_msg is not None:
        frame:
            xalign 0.5
            yalign 0.2
            padding (15, 10)

            text hover_msg size 30

screen basement_puzzle():

    modal True
    tag puzzle

    add "basement_bg.png":
        xpos 0
        ypos 0
        xsize config.screen_width
        ysize config.screen_height

    use item_text

    # SHOVEL
    imagebutton:
        idle Transform("shovel2.png", zoom=0.17, rotate=-2)
        hover Transform("shovel2.png", zoom=0.18, rotate=-2)

        xpos 234 # left - decrease; right - increase
        ypos 378 # taas - decrease; baba - increase

        action NullAction()

        hovered SetVariable("hover_msg", "Too thick to fit the groove.")
        unhovered SetVariable("hover_msg", None)

    # HAMMER
    imagebutton:
        idle Transform("hammer2.png", zoom=0.15, rotate=15)
        hover Transform("hammer2.png", zoom=0.16, rotate=15)

        xpos 900 # left - decrease; right - increase
        ypos 530 # taas - decrease; baba - increase

        action NullAction()

        hovered SetVariable("hover_msg", "Won’t be able to pull it properly.")
        unhovered SetVariable("hover_msg", None)

    # CROWBAR
    imagebutton:
        idle Transform("crowbar2.png", zoom=0.22, rotate=1)
        hover Transform("crowbar2.png", zoom=0.23, rotate=1)

        xpos 388 # left - decrease; right - increase
        ypos 298 # taas - decrease; baba - increase

        action Return("crowbar")

        hovered SetVariable("hover_msg", "Perfect.")
        unhovered SetVariable("hover_msg", None)
