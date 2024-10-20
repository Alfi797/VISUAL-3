import PySimpleGUI as sg
sg.theme("DrakGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profil",
                   layout=[[sg.Text("FTI UNISKA",font=("Helvetica",24))],
                           [sg.Text("FAKULTAS TEKNTIK INFORMATIKA",font=("Courier",18,"italic","bold","underline"))],
                           [sg.Text("UNISKA MABA BANJARMASIN")]],
                           size=(430,200),
                           font=("Times", 18))
window()
window.close()