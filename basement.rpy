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
        idle Transform("shovel2.png", zoom=0.30, rotate=-6)
        hover Transform("shovel2.png", zoom=0.32, rotate=-6)

        xpos 320
        ypos 520

        action NullAction()

        hovered SetVariable("hover_msg", "Too thick to fit the groove.")
        unhovered SetVariable("hover_msg", None)

    # HAMMER
    imagebutton:
        idle Transform("hammer2.png", zoom=0.20, rotate=2)
        hover Transform("hammer2.png", zoom=0.22, rotate=2)

        xpos 1200
        ypos 730

        action NullAction()

        hovered SetVariable("hover_msg", "Won’t be able to pull it properly.")
        unhovered SetVariable("hover_msg", None)

    # CROWBAR
    imagebutton:
        idle Transform("crowbar2.png", zoom=0.42, rotate=1)
        hover Transform("crowbar2.png", zoom=0.44, rotate=1)

        xpos 500
        ypos 380

        action Return("crowbar")

        hovered SetVariable("hover_msg", "Perfect.")
        unhovered SetVariable("hover_msg", None)