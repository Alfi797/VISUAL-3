import PySimpleGUI as sg
susunan= [[sg.VPush(),
           sg.Text("UNIKSA MAAB",font=("helvetica",24)),
           sg.Push()],
           [sg.Push(),
            sg.Text("BANJARMASIN", font=("courier",18)),
            sg.Push()]
            ]
window = sg.Window(title="Elemen Text",
                   layout=susunan,
                   size=(430,200))
window.read()
window.close()