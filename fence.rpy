default board1_removed = False
default board2_removed = False
default fence_solved = False

# PYTHON LOGIC
init python:

    def check_fence_exit():
        if store.board1_removed and store.board2_removed:
            renpy.restart_interaction()
            store.fence_solved = True


    def board1_dragged(drags, drop):
        store.board1_removed = True
        check_fence_exit()


    def board2_dragged(drags, drop):
        store.board2_removed = True
        check_fence_exit()

# SCREEN
screen fence_minigame():

    tag fencegame
    modal True

    # MAIN BG
    add Transform(
        "main_bg.png",
        xalign=0.5,
        yalign=0.5,
        xsize=config.screen_width,
        ysize=config.screen_height
)

    add Transform(
    "fence.png",
    xalign=0.5,
    yalign=0.5,
    zoom=1,
    yoffset=243,
    xoffset=473
    )

    add Transform(
    "fence_bg.png",
    xalign=0.5,
    yalign=0.5,
    zoom=1,
    yoffset=250
    )

    add Transform(
    "fence.png",
    xalign=0.5,
    yalign=0.5,
    zoom=1,
    yoffset=240,
    xoffset=-470
    )

    # BOARD 1
    if not board1_removed:
        drag:
            drag_name "board1"
            child Transform("board1.png", zoom=1)
            xpos 595
            ypos 515
            draggable True
            droppable False
            dragged board1_dragged

    # BOARD 2
    if not board2_removed:
        drag:
            drag_name "board2"
            child Transform("board2.png", zoom=1)
            xpos 665
            ypos 515
            draggable True
            droppable False
            dragged board2_dragged

    # exit part mag work ka ples
    if fence_solved:
        timer 0.5 action Return(True)
