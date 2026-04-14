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
        zoom=2,
        yoffset=318,
        xoffset=813
    )

    add Transform(
    "fence_bg.png",
    xalign=0.5,
    yalign=0.5,
    zoom=2,
    yoffset=330
    )

    add Transform(
    "fence.png",
    xalign=0.5,
    yalign=0.5,
    zoom=2,
    yoffset=318,
    xoffset=-820
    )

    # BOARD 1
    if not board1_removed:
        drag:
            drag_name "board1"
            child Transform("board1.png", zoom=2)
            xpos 880
            ypos 680
            draggable True
            droppable False
            dragged board1_dragged

    # BOARD 2
    if not board2_removed:
        drag:
            drag_name "board2"
            child Transform("board2.png", zoom=2)
            xpos 1000
            ypos 680
            draggable True
            droppable False
            dragged board2_dragged

    # ✅ THIS MAKES IT EXIT PROPERLY
    if fence_solved:
        timer 0.5 action Return(True)