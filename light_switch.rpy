default switch_on = True

screen light_switch():

    modal True
    tag switch

    if switch_on:

        # 🔼 FIRST STATE (ON)
        imagebutton:
            xpos 800
            ypos 300

            idle "on.png"
            hover "on.png"

            action SetVariable("switch_on", False)

    else:

        # 🔽 SECOND STATE (OFF)
        imagebutton:
            xpos 803
            ypos 283

            idle "off.png"
            hover "off.png"

            action Return(True)