import PySimpleGUI as sg
sg.theme("Drakgreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profil",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                            font=("Arial",25,"italic","bold","underline"))],
                             [sg.Text("NPM    :2210010078")],
                            [sg.Text("Nama   : Muhammad Alfianur Rahman")],
                            [sg.Text("Kelas     :5B NONREGULER BANJARMASIN")],
                            ],
                            size=(600,500),
                            font=("Times",18))
window()
window.close()
                                           
                                           
                                           
                                           
                                           
                                            
                            