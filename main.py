import tkinter as tk
# from PIL import Image, ImageTk

from drawing import draw_atom_animation

def ui():
    global window
    window_width = 905
    window_height = 475
    window = tk.Tk()
    window.geometry(f'{window_width}x{window_height}')
    window.title(f'Chemical element viewer')
    window.protocol("WM_DELETE_WINDOW", on_close)
    window.configure(bg='white')
    
    main_label_color = 'white'
    main_label_text_color = 'black'

    label_main_win = tk.Label(
        window,
        bg=main_label_color,
        fg=main_label_text_color
    )
    label_main_win.place(x=105, y=15, width=495, height=120)
    label_top_text = tk.Label(
        label_main_win,
        text='Periodic table of elements',
        justify='center',
        font=('Times', 14),
        anchor='n',
        bg=main_label_color,
        fg=main_label_text_color
    )
    label_top_text.pack()
    label_second_text = tk.Label(
        label_main_win,
        bg=main_label_color,
        fg=main_label_text_color,
        font=('Times', 12),
        justify='center',
        anchor='n',
        text=f'''This table is designed to schematically represent the electron distribution 
        in an atom of a chemical element. The author learned this at school. 
        Author cannot guarantee the full scientific accuracy and do not claim it. 
        Free license, provided the author is mentioned.''',
    )
    label_second_text.pack()

    # image = Image.open('personal_ico.png')
    # image = image.resize((90,90))
    # photo = ImageTk.PhotoImage(image)
    # label_ico = tk.Label(
    #     image=photo,
    #     bg=main_label_color
    # )
    # label_ico.place(x=5, y=365, width=90, height=90)

    button_created_by = tk.Button(
        text='Created by Artem M. (Karlsonte)',
        border=2,
        borderwidth=2,
        bd=2,
        relief='raised',
        font=('Comicsan', 10),
        command=lambda: copy_to_clipboard()
    )
    button_created_by.place(x=605, y=5, width=245, height=45)
    

    #1
    button_Hydrogen = tk.Button(
        window,
        text="1\nH",
        bg="#a0ffa0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Hydrogen')
        )   
    button_Lithium = tk.Button(
        window,
        text="3\nLi",
        bg="#ff6666",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Lithium')
        )      
    button_Sodium = tk.Button(
        window,
        text="11\nNa",
        bg="#ff6666",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Sodium')
        )       
    button_Potassium = tk.Button(
        window,
        text="19\nK",
        bg="#ff6666",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Potassium')
        )   
    button_Rubidium = tk.Button(
        window,
        text="37\nRb",
        bg="#ff6666",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Rubidium')
        )     
    button_Cesium = tk.Button(
        window,
        text="55\nCs",
        bg="#ff6666",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Cesium')
        )  
    button_Francium = tk.Button(
        window,
        text="87\nFr",
        bg="#ff6666",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Francium')
        )

    #2
    button_Beryllium = tk.Button(
        window,
        text="4\nBe",
        bg="#ffdead",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Beryllium')
        )   
    button_Magnesium = tk.Button(
        window,
        text="12\nMg",
        bg="#ffdead",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Magnesium')
        )    
    button_Calcium = tk.Button(
        window,
        text="20\nCa",
        bg="#ffdead",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Calcium')
        )      
    button_Strontium = tk.Button(
        window,
        text="38\nSr",
        bg="#ffdead",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Strontium')
        )     
    button_Barium = tk.Button(
        window,
        text="56\nBa",
        bg="#ffdead",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Barium')
        )     
    button_Radium = tk.Button(
        window,
        text="88\nRa",
        bg="#ffdead",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Radium')
        )

    #3
    button_Scandium = tk.Button(
        window,
        text="21\nSc",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Scandium')
        )   
    button_Yttrium = tk.Button(
        window,
        text="39\nY",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Yttrium')
        )   
    label_Lanthanides = tk.Label(
        window,
        text="La\nYb",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
    )
    label_Actinides = tk.Label(
        window,
        text="Ac\nNo",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
    )

    #4
    button_Titanium = tk.Button(
        window,
        text="22\nTi",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Titanium')
        )
    button_Zirconium = tk.Button(
        window,
        text="40\nZr",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Zirconium')
        )
    button_Hafnium = tk.Button(
        window,
        text="72\nHf",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Hafnium')
        )
    button_Rutherfordium = tk.Button(
        window,
        text="104\nRf",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Rutherfordium')
        )
    
    #5
    button_Vanadium = tk.Button(
        window,
        text="23\nV",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Vanadium')
        )
    button_Niobium = tk.Button(
        window,
        text="41\nNb",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Niobium')
        )
    button_Tantalum = tk.Button(
        window,
        text="73\nTa",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Tantalum')
        )
    button_Dubnium = tk.Button(
        window,
        text="105\nDb",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Dubnium')
        )

    #6
    button_Chromium = tk.Button(
        window,
        text="24\nCr",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Chromium')
        )
    button_Molybdenum = tk.Button(
        window,
        text="42\nMo",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Molybdenum')
        )
    button_Tungsten = tk.Button(
        window,
        text="74\nW",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Tungsten')
        )
    button_Seaborgium = tk.Button(
        window,
        text="106\nSg",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Seaborgium')
        )
    
    #7
    button_Manganese = tk.Button(
        window,
        text="25\nMn",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Manganese')
        )
    button_Technetium = tk.Button(
        window,
        text="43\nTc",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Technetium')
        )
    button_Rhenium = tk.Button(
        window,
        text="75\nRe",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Rhenium')
        )
    button_Bohrium = tk.Button(
        window,
        text="107\nBh",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Bohrium')
        )
    
    #8
    button_Iron = tk.Button(
        window,
        text="26\nFe",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Iron')
        )
    button_Ruthenium = tk.Button(
        window,
        text="44\nRu",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Ruthenium')
        )
    button_Osmium = tk.Button(
        window,
        text="76\nOs",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Osmium')
        )
    button_Hassium = tk.Button(
        window,
        text="108\nHs",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Hassium')
        )
    
    #9
    button_Cobalt = tk.Button(
        window,
        text="27\nCo",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Cobalt')
        )
    button_Rhodium = tk.Button(
        window,
        text="45\nRh",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Rhodium')
        )
    button_Iridium = tk.Button(
        window,
        text="77\nIr",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Iridium')
        )
    button_Meitnerium = tk.Button(
        window,
        text="109\nMt",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Meitnerium')
        )
    
    #10
    button_Nickel = tk.Button(
        window,
        text="28\nNi",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Nickel')
        )
    button_Palladium = tk.Button(
        window,
        text="46\nPd",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Palladium')
        )
    button_Platinum = tk.Button(
        window,
        text="78\nPt",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Platinum')
        )
    button_Darmstadtium = tk.Button(
        window,
        text="110\nDs",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Darmstadtium')
        )
    
    #11
    button_Copper = tk.Button(
        window,
        text="29\nCu",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Copper')
        )
    button_Silver = tk.Button(
        window,
        text="47\nAg",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Silver')
        )
    button_Gold = tk.Button(
        window,
        text="79\nAu",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Gold')
        )
    button_Roentgenium = tk.Button(
        window,
        text="111\nRg",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Roentgenium')
        )
    
    #12
    button_Zinc = tk.Button(
        window,
        text="30\nZn",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Zinc')
        )
    button_Cadmium = tk.Button(
        window,
        text="48\nCd",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Cadmium')
        )
    button_Mercury = tk.Button(
        window,
        text="80\nHg",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Mercury')
        )
    button_Copernicium = tk.Button(
        window,
        text="112\nCn",
        bg="#ffc0c0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Copernicium')
        )
    
    #13
    button_Boron = tk.Button(
        window,
        text="5\nB",
        bg="#cccc99",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Boron')
        )
    button_Aluminum = tk.Button(
        window,
        text="13\nAl",
        bg="#cccccc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Aluminum')
        )
    button_Gallium = tk.Button(
        window,
        text="31\nGa",
        bg="#cccccc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Gallium')
        )
    button_Indium = tk.Button(
        window,
        text="49\nIn",
        bg="#cccccc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Indium')
        )
    button_Thallium = tk.Button(
        window,
        text="81\nTl",
        bg="#cccccc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Thallium')
        )
    button_Nihonium = tk.Button(
        window,
        text="113\nNh",
        bg="#cccccc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Nihonium')
        )
    
    #14
    button_Carbon = tk.Button(
        window,
        text="6\nC",
        bg="#a0ffa0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Carbon')
        )
    button_Silicon = tk.Button(
        window,
        text="14\nSi",
        bg="#cccc99",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Silicon')
        )
    button_Germanium = tk.Button(
        window,
        text="32\nGe",
        bg="#cccc99",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Germanium')
        )
    button_Tin = tk.Button(
        window,
        text="50\nSn",
        bg="#cccccc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Tin')
        )
    button_Lead = tk.Button(
        window,
        text="82\nPb",
        bg="#cccccc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Lead')
        )
    button_Flerovium = tk.Button(
        window,
        text="114\nFl",
        bg="#cccccc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Flerovium')
        )
    
    #15
    button_Nitrogen = tk.Button(
        window,
        text="7\nN",
        bg="#a0ffa0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Nitrogen')
        )
    button_Phosphorus = tk.Button(
        window,
        text="15\nP",
        bg="#a0ffa0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Phosphorus')
        )
    button_Arsenic = tk.Button(
        window,
        text="33\nAs",
        bg="#cccc99",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Arsenic')
        )
    button_Antimony = tk.Button(
        window,
        text="51\nSb",
        bg="#cccc99",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Antimony')
        )
    button_Bismuth = tk.Button(
        window,
        text="83\nBi",
        bg="#cccccc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Bismuth')
        )
    button_Moscovium = tk.Button(
        window,
        text="115\nMc",
        bg="#cccccc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Moscovium')
        )
    
    #16
    button_Oxygen = tk.Button(
        window,
        text="8\nO",
        bg="#a0ffa0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Oxygen')
        )
    button_Sulfur = tk.Button(
        window,
        text="16\nS",
        bg="#a0ffa0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Sulfur')
        )
    button_Selenium = tk.Button(
        window,
        text="34\nSe",
        bg="#a0ffa0",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Selenium')
        )
    button_Tellurium = tk.Button(
        window,
        text="52\nTe",
        bg="#cccc99",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Tellurium')
        )
    button_Polonium = tk.Button(
        window,
        text="84\nPo",
        bg="#cccc99",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Polonium')
        )
    button_Livermorium = tk.Button(
        window,
        text="116\nLv",
        bg="#cccccc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Livermorium')
        )
    
    #17
    button_Fluorine = tk.Button(
        window,
        text="9\nF",
        bg="#ffff99",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Fluorine')
        )
    button_Chlorine = tk.Button(
        window,
        text="17\nCl",
        bg="#ffff99",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Chlorine')
        )
    button_Bromine = tk.Button(
        window,
        text="35\nBr",
        bg="#ffff99",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Bromine')
        )
    button_Iodine = tk.Button(
        window,
        text="53\nI",
        bg="#ffff99",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Iodine')
        )
    button_Astatine = tk.Button(
        window,
        text="85\nAt",
        bg="#ffff99",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Astatine')
        )
    button_Tennessine = tk.Button(
        window,
        text="117\nTs",
        bg="#ffff99",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Tennessine')
        )
    
    #18
    button_Helium = tk.Button(
        window,
        text="2\nHe",
        bg="#c0ffff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Helium')
        )
    button_Neon = tk.Button(
        window,
        text="10\nNe",
        bg="#c0ffff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Neon')
        )
    button_Argon = tk.Button(
        window,
        text="18\nAr",
        bg="#c0ffff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Argon')
        )
    button_Krypton = tk.Button(
        window,
        text="36\nKr",
        bg="#c0ffff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Krypton')
        )
    button_Xenon = tk.Button(
        window,
        text="54\nXe",
        bg="#c0ffff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Xenon')
        )
    button_Radon = tk.Button(
        window,
        text="86\nRn",
        bg="#c0ffff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Radon')
        )
    button_Oganesson = tk.Button(
        window,
        text="118\nOg",
        bg="#c0ffff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Oganesson')
        )
    
    #Lanthanides
    button_Lanthanum = tk.Button(
        window,
        text="57\nLa",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Lanthanum')
        )
    button_Cerium = tk.Button(
        window,
        text="58\nCe",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Cerium')
        )
    button_Praseodymium = tk.Button(
        window,
        text="59\nPr",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Praseodymium')
        )
    button_Neodymium = tk.Button(
        window,
        text="60\nNd",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Neodymium')
        )
    button_Promethium = tk.Button(
        window,
        text="61\nPm",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Promethium')
        )
    button_Samarium = tk.Button(
        window,
        text="62\nSm",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Samarium')
        )
    button_Europium = tk.Button(
        window,
        text="63\nEu",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Europium')
        )
    button_Gadolinium = tk.Button(
        window,
        text="64\nGd",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Gadolinium')
        )
    button_Terbium = tk.Button(
        window,
        text="65\nTb",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Terbium')
        )
    button_Dysprosium = tk.Button(
        window,
        text="66\nDy",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Dysprosium')
        )
    button_Holmium = tk.Button(
        window,
        text="67\nHo",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Holmium')
        )
    button_Erbium = tk.Button(
        window,
        text="68\nEr",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Erbium')
        )
    button_Thulium = tk.Button(
        window,
        text="69\nTm",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Thulium')
        )
    button_Ytterbium = tk.Button(
        window,
        text="70\nYb",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Ytterbium')
        )
    button_Lutetium = tk.Button(
        window,
        text="71\nLu",
        bg="#ffbfff",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Lutetium')
        )
    
    #Actinides
    button_Actinium = tk.Button(
        window,
        text="89\nAc",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Actinium')
        )
    button_Thorium = tk.Button(
        window,
        text="90\nTh",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Thorium')
        )
    button_Protactinium = tk.Button(
        window,
        text="91\nPa",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Protactinium')
        )
    button_Uranium = tk.Button(
        window,
        text="92\nU",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Uranium')
        )
    button_Neptunium = tk.Button(
        window,
        text="93\nNp",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Neptunium')
        )
    button_Plutonium = tk.Button(
        window,
        text="94\nPu",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Plutonium')
        )
    button_Americium = tk.Button(
        window,
        text="95\nAm",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Americium')
        )
    button_Curium = tk.Button(
        window,
        text="96\nCm",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Curium')
        )
    button_Berkelium = tk.Button(
        window,
        text="97\nBk",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Berkelium')
        )
    button_Californium = tk.Button(
        window,
        text="98\nCf",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Californium')
        )
    button_Einsteinium = tk.Button(
        window,
        text="99\nEs",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Einsteinium')
        )
    button_Fermium = tk.Button(
        window,
        text="100\nFm",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Fermium')
        )
    button_Mendelevium = tk.Button(
        window,
        text="101\nMd",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Mendelevium')
        )
    button_Nobelium = tk.Button(
        window,
        text="102\nNo",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Nobelium')
        )
    button_Lawrencium = tk.Button(
        window,
        text="103\nLr",
        bg="#ff99cc",
        activebackground="black",
        bd=2,              
        highlightthickness=2,
        command=lambda: draw_atom_animation('Lawrencium')
        )

    #1
    button_Hydrogen.place(x=5, y=5, width=45, height=45) 
    button_Lithium.place(x=5, y=55, width=45, height=45) 
    button_Sodium.place(x=5, y=105, width=45, height=45)
    button_Potassium.place(x=5, y=155, width=45, height=45)
    button_Rubidium.place(x=5, y=205, width=45, height=45)
    button_Cesium.place(x=5, y=255, width=45, height=45)
    button_Francium.place(x=5, y=305, width=45, height=45)

    #2
    button_Beryllium.place(x=55, y=55, width=45, height=45)
    button_Magnesium.place(x=55, y=105, width=45, height=45)
    button_Calcium.place(x=55, y=155, width=45, height=45)
    button_Strontium.place(x=55, y=205, width=45, height=45)
    button_Barium.place(x=55, y=255, width=45, height=45)
    button_Radium.place(x=55, y=305, width=45, height=45)

    #3
    button_Scandium.place(x=105, y=155, width=45, height=45)
    button_Yttrium.place(x=105, y=205, width=45, height=45)
    label_Lanthanides.place(x=105, y=255, width=45, height=45)
    label_Actinides.place(x=105, y=305, width=45, height=45)

    #4
    button_Titanium.place(x=155, y=155, width=45, height=45)
    button_Zirconium.place(x=155, y=205, width=45, height=45)
    button_Hafnium.place(x=155, y=255, width=45, height=45)
    button_Rutherfordium.place(x=155, y=305, width=45, height=45)

    #5
    button_Vanadium.place(x=205, y=155, width=45, height=45)
    button_Niobium.place(x=205, y=205, width=45, height=45)
    button_Tantalum.place(x=205, y=255, width=45, height=45)
    button_Dubnium.place(x=205, y=305, width=45, height=45)

    #6
    button_Chromium.place(x=255, y=155, width=45, height=45)
    button_Molybdenum.place(x=255, y=205, width=45, height=45)
    button_Tungsten.place(x=255, y=255, width=45, height=45)
    button_Seaborgium.place(x=255, y=305, width=45, height=45)

    #7
    button_Manganese.place(x=305, y=155, width=45, height=45)
    button_Technetium.place(x=305, y=205, width=45, height=45)
    button_Rhenium.place(x=305, y=255, width=45, height=45)
    button_Bohrium.place(x=305, y=305, width=45, height=45)

    #8
    button_Iron.place(x=355, y=155, width=45, height=45)
    button_Ruthenium.place(x=355, y=205, width=45, height=45)
    button_Osmium.place(x=355, y=255, width=45, height=45)
    button_Hassium.place(x=355, y=305, width=45, height=45)

    #9
    button_Cobalt.place(x=405, y=155, width=45, height=45)
    button_Rhodium.place(x=405, y=205, width=45, height=45)
    button_Iridium.place(x=405, y=255, width=45, height=45)
    button_Meitnerium.place(x=405, y=305, width=45, height=45)

    #10
    button_Nickel.place(x=455, y=155, width=45, height=45)
    button_Palladium.place(x=455, y=205, width=45, height=45)
    button_Platinum.place(x=455, y=255, width=45, height=45)
    button_Darmstadtium.place(x=455, y=305, width=45, height=45)

    #11
    button_Copper.place(x=505, y=155, width=45, height=45)
    button_Silver.place(x=505, y=205, width=45, height=45)
    button_Gold.place(x=505, y=255, width=45, height=45)
    button_Roentgenium.place(x=505, y=305, width=45, height=45)

    #12
    button_Zinc.place(x=555, y=155, width=45, height=45)
    button_Cadmium.place(x=555, y=205, width=45, height=45)
    button_Mercury.place(x=555, y=255, width=45, height=45)
    button_Copernicium.place(x=555, y=305, width=45, height=45)

    #13
    button_Boron.place(x=605, y=55, width=45, height=45)
    button_Aluminum.place(x=605, y=105, width=45, height=45)
    button_Gallium.place(x=605, y=155, width=45, height=45)
    button_Indium.place(x=605, y=205, width=45, height=45)
    button_Thallium.place(x=605, y=255, width=45, height=45)
    button_Nihonium.place(x=605, y=305, width=45, height=45)

    #14
    button_Carbon.place(x=655, y=55, width=45, height=45)
    button_Silicon.place(x=655, y=105, width=45, height=45)
    button_Germanium.place(x=655, y=155, width=45, height=45)
    button_Tin.place(x=655, y=205, width=45, height=45)
    button_Lead.place(x=655, y=255, width=45, height=45)
    button_Flerovium.place(x=655, y=305, width=45, height=45)

    #15
    button_Nitrogen.place(x=705, y=55, width=45, height=45)
    button_Phosphorus.place(x=705, y=105, width=45, height=45)
    button_Arsenic.place(x=705, y=155, width=45, height=45)
    button_Antimony.place(x=705, y=205, width=45, height=45)
    button_Bismuth.place(x=705, y=255, width=45, height=45)
    button_Moscovium.place(x=705, y=305, width=45, height=45)

    #16
    button_Oxygen.place(x=755, y=55, width=45, height=45)
    button_Sulfur.place(x=755, y=105, width=45, height=45)
    button_Selenium.place(x=755, y=155, width=45, height=45)
    button_Tellurium.place(x=755, y=205, width=45, height=45)
    button_Polonium.place(x=755, y=255, width=45, height=45)
    button_Livermorium.place(x=755, y=305, width=45, height=45)

    #17
    button_Fluorine.place(x=805, y=55, width=45, height=45)
    button_Chlorine.place(x=805, y=105, width=45, height=45)
    button_Bromine.place(x=805, y=155, width=45, height=45)
    button_Iodine.place(x=805, y=205, width=45, height=45)
    button_Astatine.place(x=805, y=255, width=45, height=45)
    button_Tennessine.place(x=805, y=305, width=45, height=45)

    #18
    button_Helium.place(x=855, y=5, width=45, height=45)
    button_Neon.place(x=855, y=55, width=45, height=45)
    button_Argon.place(x=855, y=105, width=45, height=45)
    button_Krypton.place(x=855, y=155, width=45, height=45)
    button_Xenon.place(x=855, y=205, width=45, height=45)
    button_Radon.place(x=855, y=255, width=45, height=45)
    button_Oganesson.place(x=855, y=305, width=45, height=45)

    #Lanthanides
    button_Lanthanum.place(x=105, y=375, width=45, height=45)
    button_Cerium.place(x=155, y=375, width=45, height=45)
    button_Praseodymium.place(x=205, y=375, width=45, height=45)
    button_Neodymium.place(x=255, y=375, width=45, height=45)
    button_Promethium.place(x=305, y=375, width=45, height=45)
    button_Samarium.place(x=355, y=375, width=45, height=45)
    button_Europium.place(x=405, y=375, width=45, height=45)
    button_Gadolinium.place(x=455, y=375, width=45, height=45)
    button_Terbium.place(x=505, y=375, width=45, height=45)
    button_Dysprosium.place(x=555, y=375, width=45, height=45)
    button_Holmium.place(x=605, y=375, width=45, height=45)
    button_Erbium.place(x=655, y=375, width=45, height=45)
    button_Thulium.place(x=705, y=375, width=45, height=45)
    button_Ytterbium.place(x=755, y=375, width=45, height=45)
    button_Lutetium.place(x=805, y=375, width=45, height=45)

    #Actinides
    button_Actinium.place(x=105, y=425, width=45, height=45)
    button_Thorium.place(x=155, y=425, width=45, height=45)
    button_Protactinium.place(x=205, y=425, width=45, height=45)
    button_Uranium.place(x=255, y=425, width=45, height=45)
    button_Neptunium.place(x=305, y=425, width=45, height=45)
    button_Plutonium.place(x=355, y=425, width=45, height=45)
    button_Americium.place(x=405, y=425, width=45, height=45)
    button_Curium.place(x=455, y=425, width=45, height=45)
    button_Berkelium.place(x=505, y=425, width=45, height=45)
    button_Californium.place(x=555, y=425, width=45, height=45)
    button_Einsteinium.place(x=605, y=425, width=45, height=45)
    button_Fermium.place(x=655, y=425, width=45, height=45)
    button_Mendelevium.place(x=705, y=425, width=45, height=45)
    button_Nobelium.place(x=755, y=425, width=45, height=45)
    button_Lawrencium.place(x=805, y=425, width=45, height=45)

    def copy_to_clipboard():
        text_to_copy = "Created by Artem M. (Karlsonte)"
        window.clipboard_clear()
        window.clipboard_append(text_to_copy)
        button_created_by.config(text=f"Text copied\nThanks for the mention")
        window.after(3000, lambda: button_created_by.config(text=text_to_copy))

    window.mainloop()

def on_close(): 
    window.destroy()


if __name__ == "__main__":
    ui()
