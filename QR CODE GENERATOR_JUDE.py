import PySimpleGUI as sg
import qrcode

layout = [
    [sg.Text('Enter a link to generate a QR code:')],
    [sg.Input(key='link')],
    [sg.Text('Choose a color:'), sg.Combo(values=['black', 'red', 'blue'], key='color')],
    [sg.Text('Choose a size:'), sg.Slider(range=(1, 10), default_value=5, orientation='h', key='size')],
    [sg.Button('Generate'), sg.Button('Save As')],
    [sg.Image(key='image')]
]

window = sg.Window('QR Code Generator', layout)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Generate':
        link = values['link']
        color = values['color']
        size = values['size']
        qr = qrcode.QRCode(version=1,box_size=size, border=3, error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color=color, back_color='white')
        img.save('qrcode.png')
        window['image'].update('qrcode.png')
    
    # Saving the Qr code
    if event == 'Save As':
        filename = sg.popup_get_file('Save Qr Code', save_as=True, default_extension='.png')
        if filename:
            img.save(filename)
    
        

window.close()