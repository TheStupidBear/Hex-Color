from tkinter import *

red = {
    'IndianRed': '#CD5C5C',
    'LightCoral': '#F08080',
    'Salmon': '#FA8072',
    'DarkSalmon': '#E9967A',
    'LightSalmon': '#FFA07A',
    'Crimson': '#DC143C',
    'Red': '#FF0000',
    'FireBrick': '#B22222',
    'DarkRed': '#8B0000'
}
pink = {
        'Pink': '#FFC0CB',
        'LightPink': '#FFB6C1',
        'HotPink': '#FF69B4',
        'DeepPink': '#FF1493',
        'MediumVioletRed': '#C71585',
        'PaleVioletRed': '#DB7093'
    }
orange = {
        'Coral':'#FF7F50',
        'Tomato':'#FF6347',
        'OrangeRed':'#FF4500',
        'DarkOrange':'#FF8C00',
        'Orange':'#FFA500'
    }
yellow = {
    'Gold': '#FFD700',
    'Yellow': '#FFFF00',
    'LightYellow': '#FFFFE0',
    'LemonChiffon': '#FFFACD',
    'LightGoldenrodYellow': '#FAFAD2',
    'PapayaWhip': '#FFEFD5',
    'Moccasin': '#FFE4B5',
    'PeachPuff': '#FFDAB9',
    'PaleGoldenrod': '#EEE8AA',
    'Khaki': '#F0E68C',
    'DarkKhaki': '#BDB76B'
}
purple = {
    'Lavender': '#E6E6FA',
    'Thistle': '#D8BFD8',
    'Plum': '#DDA0DD',
    'Violet': '#EE82EE',
    'Orchid': '#DA70D6',
    'Magenta': '#FF00FF',
    'MediumOrchid': '#BA55D3',
    'MediumPurple': '#9370DB',
    'BlueViolet': '#8A2BE2',
    'DarkViolet': '#9400D3',
    'DarkOrchid': '#9932CC',
    'DarkMagenta': '#8B008B',
    'Purple': '#800080',
    'Indigo': '#4B0082',
    'SlateBlue': '#6A5ACD',
    'DarkSlateBlue': '#483D8B'
}
brown = {
    'Cornsilk': '#FFF8DC',
    'BlanchedAlmond': '#FFEBCD',
    'Bisque': '#FFE4C4',
    'NavajoWhite': '#FFDEAD',
    'Wheat': '#F5DEB3',
    'BurlyWood': '#DEB887',
    'Tan': '#D2B48C',
    'RosyBrown': '#BC8F8F',
    'SandyBrown': '#F4A460',
    'Goldenrod': '#DAA520',
    'DarkGoldenRod': '#B8860B',
    'Peru': '#CD853F',
    'Chocolate': '#D2691E',
    'SaddleBrown': '#8B4513',
    'Sienna': '#A0522D',
    'Brown': '#A52A2A',
    'Maroon': '#800000'
}
green = {
    'GreenYellow': '#ADFF2F',
    'Chartreuse': '#7FFF00',
    'LawnGreen': '#7CFC00',
    'Lime': '#00FF00',
    'LimeGreen': '#32CD32',
    'PaleGreen': '#98FB98',
    'LightGreen': '#90EE90',
    'MediumSpringGreen': '#00FA9A',
    'SpringGreen': '#00FF7F',
    'MediumSeaGreen': '#3CB371',
    'SeaGreen': '#2E8B57',
    'ForestGreen': '#228B22',
    'Green': '#008000',
    'DarkGreen': '#006400',
    'YellowGreen': '#9ACD32',
    'OliveDrab': '#6B8E23',
    'Olive': '#808000',
    'DarkOliveGreen': '#556B2F',
    'MediumAquamarine': '#66CDAA',
    'DarkSeaGreen': '#8FBC8F',
    'LightSeaGreen': '#20B2AA',
    'DarkCyan': '#008B8B',
    'Teal': '#008080'
}
blue = {
    'Aqua': '#00FFFF',
    'LightCyan': '#E0FFFF',
    'PaleTurquoise': '#AFEEEE',
    'Aquamarine': '#7FFFD4',
    'Turquoise': '#40E0D0',
    'MediumTurquoise': '#48D1CC',
    'DarkTurquoise': '#00CED1',
    'CadetBlue': '#5F9EA0',
    'SteelBlue': '#4682B4',
    'LightSteelBlue': '#B0C4DE',
    'PowderBlue': '#B0E0E6',
    'LightBlue': '#ADD8E6',
    'SkyBlue': '#87CEEB',
    'LightSkyBlue': '#87CEFA',
    'DeepSkyBlue': '#00BFFF',
    'DodgerBlue': '#1E90FF',
    'CornflowerBlue': '#6495ED',
    'MediumSlateBlue': '#7B68EE',
    'RoyalBlue': '#4169E1',
    'Blue': '#0000FF',
    'MediumBlue': '#0000CD',
    'DarkBlue': '#00008B',
    'MidnightBlue': '#191970'
}
white = {
    'White': '#FFFFFF',
    'Snow': '#FFFAFA',
    'Honeydew': '#F0FFF0',
    'MintCream': '#F5FFFA',
    'Azure': '#F0FFFF',
    'AliceBlue': '#F0F8FF',
    'GhostWhite': '#F8F8FF',
    'WhiteSmoke': '#F5F5F5',
    'Seashell': '#FFF5EE',
    'Beige': '#F5F5DC',
    'OldLace': '#FDF5E6',
    'FloralWhite': '#FFFAF0',
    'Ivory': '#FFFFF0',
    'AntiqueWhite': '#FAEBD7',
    'Linen': '#FAF0E6',
    'LavenderBlush': '#FFF0F5',
    'MistyRose': '#FFE4E1'
}
grey = {
    'Gainsboro': '#DCDCDC',
    'LightGrey': '#D3D3D3',
    'Silver': '#C0C0C0',
    'DarkGrey': '#A9A9A9',
    'Grey': '#808080',
    'DimGrey': '#696969',
    'LightSlateGrey': '#778899',
    'SlateGrey': '#708090',
    'DarkSlateGrey': '#2F4F4F',
    'Black': '#000000'
}

# главная функция, принимающая словарь оттенков цвета и
# вызывающая функцию очистки фрэймов и функцию выбора фрэйма
def tone(dictionary):
    k = 0
    # очищаю Frame от виджетов
    clear_frames()
    for key, value in dictionary.items():
        choice_frame(key, value, k)
        k = k + 1

# функция очищает все внутренние фрэймы
def clear_frames():
    for vidgets in first_frame.pack_slaves():
        vidgets.destroy()
    for vidgets in second_frame.pack_slaves():
        vidgets.destroy()
    for vidgets in third_frame.pack_slaves():
        vidgets.destroy()
    for vidgets in fourth_frame.pack_slaves():
        vidgets.destroy()
    for vidgets in fifth_frame.pack_slaves():
        vidgets.destroy()
    for vidgets in sixth_frame.pack_slaves():
        vidgets.destroy()
    for vidgets in seventh_frame.pack_slaves():
        vidgets.destroy()
    for vidgets in eighth_frame.pack_slaves():
        vidgets.destroy()
    for vidgets in ninth_frame.pack_slaves():
        vidgets.destroy()
    for vidgets in tenth_frame.pack_slaves():
        vidgets.destroy()

# функция выбирает внутренний фрэйм и вызывает функцию создания кнопок
def choice_frame(key, value, k):
    if k <= 4:
        create_button(key, value, first_frame)
    elif k <= 9:
        create_button(key, value, second_frame)
    elif k <= 14:
        create_button(key, value, third_frame)
    elif k <= 19:
        create_button(key, value, fourth_frame)
    elif k <= 24:
        create_button(key, value, fifth_frame)
    elif k <= 29:
        create_button(key, value, sixth_frame)
    elif k <= 34:
        create_button(key, value, seventh_frame)
    elif k <= 39:
        create_button(key, value, eighth_frame)
    elif k <= 44:
        create_button(key, value, ninth_frame)
    elif k <= 49:
        create_button(key, value, tenth_frame)

# функция для создания кнопок
def create_button(name, hex, frame):
    Button(frame, bg=hex, width=5, height=2,
               command=lambda name_color=name, hex_color=hex:
               change(name_color, hex_color)).pack(side=LEFT, padx=1, pady=1)

# функция для изменения текста Entry и label
def change(name_color, hex_color):
    l['text'] = name_color
    e.delete(0, END)
    e.insert(0, hex_color)


# Количество фрэймов = 14 (14 Карл)
if __name__ == "__main__":
    root = Tk()
    root.title('Hex Color')
    root.geometry('400x500+200+200')
    # 3 фрэйма для кнопок с текстом
    main_text_frame = Frame(root)
    text_button_frame1 = Frame(main_text_frame)
    text_button_frame2 = Frame(main_text_frame)
    # создаю главный фрэйм для кнопок
    button_frame = Frame(root)

    # создаю 10 дополнительных фрэймов в главном фрэйме
    first_frame = Frame(button_frame)
    second_frame = Frame(button_frame)
    third_frame = Frame(button_frame)
    fourth_frame = Frame(button_frame)
    fifth_frame = Frame(button_frame)
    sixth_frame = Frame(button_frame)
    seventh_frame = Frame(button_frame)
    eighth_frame = Frame(button_frame)
    ninth_frame = Frame(button_frame)
    tenth_frame = Frame(button_frame)

    l = Label(root, bg='#F5F5F5', fg='#000000', width=25)
    e = Entry(root, width=25, justify='center')

    l.pack(padx=4, pady=4)
    e.pack(padx=4, pady=4)
    main_text_frame.pack()
    text_button_frame1.pack(side=LEFT, anchor=N)
    text_button_frame2.pack(side=LEFT, anchor=N)


    Button(text_button_frame1, text="Красные тона", font="Arial 12", bg='#F5FFFA', width=14,
           command=lambda: tone(red)).pack()
    Button(text_button_frame1, text="Розовые тона", font="Arial 12", bg='#F5FFFA', width=14,
           command=lambda: tone(pink)).pack()
    Button(text_button_frame1, text="Оранжевые тона", font="Arial 12", bg='#F5FFFA', width=14,
           command=lambda: tone(orange)).pack()
    Button(text_button_frame1, text="Жёлтые тона", font="Arial 12", bg='#F5FFFA', width=14,
           command=lambda: tone(yellow)).pack()
    Button(text_button_frame1, text="Фиолетовые тона", font="Arial 12", bg='#F5FFFA', width=14,
           command=lambda: tone(purple)).pack()
    Button(text_button_frame2, text="Коричневые тона", font="Arial 12", bg='#F5FFFA', width=14,
           command=lambda: tone(brown)).pack()
    Button(text_button_frame2, text="Зелёные тона", font="Arial 12", bg='#F5FFFA', width=14,
           command=lambda: tone(green)).pack()
    Button(text_button_frame2, text="Синие тона", font="Arial 12", bg='#F5FFFA', width=14,
           command=lambda: tone(blue)).pack()
    Button(text_button_frame2, text="Белые тона", font="Arial 12", bg='#F5FFFA', width=14,
           command=lambda: tone(white)).pack()
    Button(text_button_frame2, text="Серые тона", font="Arial 12", bg='#F5FFFA', width=14,
           command=lambda: tone(grey)).pack()

    # создал пустой label для пробела после кнопок с текстом
    Label(root).pack()
    button_frame.pack()

    first_frame.pack()
    second_frame.pack()
    third_frame.pack()
    fourth_frame.pack()
    fifth_frame.pack()
    sixth_frame.pack()
    seventh_frame.pack()
    eighth_frame.pack()
    ninth_frame.pack()
    tenth_frame.pack()

    root.mainloop()


