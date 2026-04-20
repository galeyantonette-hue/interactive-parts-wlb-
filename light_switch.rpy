default switch_on = True

screen light_switch():

    modal True
    tag switch

    if switch_on:

        # ON (UNA)
        imagebutton:
            xpos 550
            ypos 300

            idle "on.png"
            hover "on.png"

            action SetVariable("switch_on", False)

    else:

        # OFF
        imagebutton:
            xpos 553
            ypos 300

            idle "off.png"
            hover "off.png"

            action Return(True)
