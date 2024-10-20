import PySimpleGUI as sg
sg.theme("DrakGreen4") #penentuan tema
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("TEKNOLOGI INFORMATIKA", size=(25,1),justification="center")],
                           [sg.Text("TEKNOLOGI INFORMATIKA", size=(25,1),justification="left")],
                           [sg.Text("TEKNOLOGI INFORMATIKA", size=(25,1),justification="right")],
                           [sg.Text(("TEKNOLOGI INFORMATIKA"+" ")* 2,size=(25,2),justification="center")],
                           [sg.Text("UNIKSA MAB BANJARMASIN",text_color="#FFCC00")]],
                           size=(400,250),
                           font=("Times", 18))
window()
window.close()