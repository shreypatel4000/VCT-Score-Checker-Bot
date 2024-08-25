from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from VCTScore2 import mainMssg


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\shrey\Python\VCT Score Checker Bot\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

score = mainMssg('dpdaXOdFTp3Hx0')     # Add the official youtube livestream link here

if score!='No Nightbot reply' and score!="No live chat found for this video.":

    score = score.split('|')[2]
    score = score.split(' ')

    window1 = Tk()

    window1.geometry("691x304")
    window1.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window1,
        bg = "#FFFFFF",
        height = 304,
        width = 691,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        345.0,
        152.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        352.0,
        149.0,
        image=image_image_2
    )

    # Team 1
    canvas.create_text(
        121.0,
        21.0,
        anchor="nw",
        text=score[1],
        fill="#FFFFFF",
        font=("Anton Regular", 36 * -1)
    )

    # T1
    try:
        canvas.create_text(
        31.0,
        169.0,
        anchor="nw",
        text=score[4],
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )
    except IndexError:
        canvas.create_text(
        31.0,
        169.0,
        anchor="nw",
        text="NrN",
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )

    # T2
    try:
        canvas.create_text(
        31.0,
        211.0,
        anchor="nw",
        text=score[7],
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )
    except IndexError:
        canvas.create_text(
        31.0,
        211.0,
        anchor="nw",
        text='NrN',
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )

    # T3
    try:
        canvas.create_text(
        31.0,
        260.0,
        anchor="nw",
        text=score[10],
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )
    except IndexError:
        canvas.create_text(
        31.0,
        260.0,
        anchor="nw",
        text="NrN",
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )

    # S1
    canvas.create_text(
        320.0,
        82.0,
        anchor="nw",
        text=score[2][0]+"\n",
        fill="#FFFFFF",
        font=("Anton Regular", 40 * -1)
    )

    # S2
    try:
        canvas.create_text(
            368.0,
            81.0,
            anchor="nw",
            text=score[2][2],
            fill="#FFFFFF",
            font=("Anton Regular", 40 * -1)
        )
    except:
        canvas.create_text(
            368.0,
            81.0,
            anchor="nw",
            text='NrN',
            fill="#FFFFFF",
            font=("Anton Regular", 40 * -1)
        )

    # ss3
    try:
        canvas.create_text(
        263.0,
        214.0,
        anchor="nw",
        text=score[8].split('-')[0],
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )
    except IndexError:
        canvas.create_text(
        263.0,
        214.0,
        anchor="nw",
        text='NrN',
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )
    
    # ss4
    try:
        canvas.create_text(
        424.0,
        214.0,
        anchor="nw",
        text=score[8].split('-')[1],
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )
    except IndexError:
        canvas.create_text(
        424.0,
        214.0,
        anchor="nw",
        text="NrN",
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )

    # ss5
    try:
        canvas.create_text(
        263.0,
        260.0,
        anchor="nw",
        text=score[11].split('-')[0],
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )
    except IndexError:
        canvas.create_text(
        263.0,
        260.0,
        anchor="nw",
        text="NrN",
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )

    # ss6
    try:
        canvas.create_text(
        424.0,
        260.0,
        anchor="nw",
        text=score[11].split('-')[1],
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )
    except IndexError:
        canvas.create_text(
        424.0,
        260.0,
        anchor="nw",
        text="NrN",
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )

    # ss1
    try:
        canvas.create_text(
        263.0,
        169.0,
        anchor="nw",
        text=score[5].split('-')[0],
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )
    except IndexError:
        canvas.create_text(
        263.0,
        169.0,
        anchor="nw",
        text='NrN',
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )

    # ss2
    try:
        canvas.create_text(
        424.0,
        169.0,
        anchor="nw",
        text=score[5].split('-')[1],
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )
    except IndexError:
        canvas.create_text(
        424.0,
        169.0,
        anchor="nw",
        text="NrN",
        fill="#FFFFFF",
        font=("Anton Regular", 24 * -1)
    )

    # Team2
    try:
        canvas.create_text(
            485.0,
            21.0,
            anchor="nw",
            text=score[3],
            fill="#FFFFFF",
            font=("Anton Regular", 36 * -1)
        )
    except:
        canvas.create_text(
            485.0,
            21.0,
            anchor="nw",
            text='NrN',
            fill="#FFFFFF",
            font=("Anton Regular", 36 * -1)
        )
    
    window1.mainloop()

else:
    print(score)
