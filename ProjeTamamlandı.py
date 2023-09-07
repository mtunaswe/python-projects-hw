from tkinter import *

pencere = Tk()
pencere.title("Giriş")

def telefonrehberi():
    pencere.destroy()
    pencere1 = Tk()
    pencere1.geometry("325x350")
    pencere1.title("Telefon Rehberi")
    çerçeve2 = Frame(pencere1,highlightthickness=1, highlightbackground="black")
    çerçeve2.pack(side = BOTTOM)
    çerçeve3 = Frame(pencere1)
    çerçeve3.pack(side = LEFT)
    çerçeve1 = Frame(pencere1,highlightthickness=1, highlightbackground="black")
    çerçeve1.pack(side = RIGHT)
    telefon_rehberi = open("Telefon Rehberi.txt","a")                             

    def ekle():
        telefon_rehberi = open("Telefon Rehberi.txt.","a")
        isim = isim_entry.get()
        soyad = soyad_entry.get()
        numara = numara_entry.get()
        listbox.insert(END, isim + " " +  soyad + " : " + numara + "\n")
        yaz = open("Telefon Rehberi.txt", "a")
        yaz.write(isim + " " + soyad + " : " + numara + "\n")
       
        isim_entry.delete(0, "end")
        soyad_entry.delete(0, "end")
        numara_entry.delete(0, "end")


    def çıkar():
        seç =listbox.curselection()
        seçilen = seç[0]
        listbox.delete(seçilen)

        liste = list(listbox.get(0,END))
        yaz = open("Telefon Rehberi.txt", "w")
        for kişi in liste:
            yaz.write(kişi)
        yaz.close()

    def düzenle():
        telefon_rehberi = open("Telefon Rehberi.txt","r")
        seç = listbox.curselection()
        seçilen = seç[0]

        pencere2 = Toplevel()
        pencere2.geometry("350x110")
        pencere2.title("Düzenle")

        çerçeve3 = Frame(pencere2)
        çerçeve3.pack(side = LEFT)

        çerçeve4 = Frame(pencere2,highlightthickness=1, highlightbackground="black")
        çerçeve4.pack(side = LEFT)

        isim_etiket = Label(çerçeve4,text = "İsim:", font = ("Courier",9))
        isim_etiket.grid(row = 0,column = 1,sticky = W)

        soyad_etiket = Label(çerçeve4,text = "Soyad:", font = ("Courier",9))
        soyad_etiket.grid(row = 1,column = 1,sticky = W)

        numara_etiket = Label(çerçeve4,text = "Telefon Numarası:", font =("Courier",9))
        numara_etiket.grid(row = 2,column = 1,sticky = W)

        isim_entry = Entry(çerçeve4,relief ="solid", bd = 2,highlightthickness=2, highlightbackground="steelblue")
        isim_entry.grid(row = 0, column = 2)

        soyad_entry = Entry(çerçeve4,relief ="solid", bd = 2,highlightthickness=2, highlightbackground="steelblue")
        soyad_entry.grid(row = 1, column = 2)

        numara_entry = Entry(çerçeve4,relief ="solid", bd = 2,highlightthickness=2, highlightbackground="steelblue")
        numara_entry.grid(row = 2,column = 2)

        etiket4 = Label(çerçeve3,text = "Düzenle",font = ("Courier New",10), image = resim4,compound="top")
        etiket4.grid(row = 0,column = 0)

        def kabul(): 
            isim1 = isim_entry.get()
            soyad1 = soyad_entry.get()
            numara1 = numara_entry.get()

            listbox.delete(seçilen)
            listbox.insert(seçilen,isim1 + " " +  soyad1 + " : " + numara1 + "\n")

            liste = list(listbox.get(0,END))
            yaz = open("Telefon Rehberi.txt", "w")
            for kişi in liste:
                yaz.write(kişi)
            yaz.close()
            pencere2.destroy()

        kabul = Button(çerçeve4, text = "➔",font = ("Courier",10),relief = "groove", overrelief = "solid",command = kabul)
        kabul.grid(row = 3, column = 2)
                

    ara_etiket = Label(çerçeve2,text = "Ara: ", font = ("Courier",9))
    ara_etiket.grid(row = 4,column = 0)

    ara_entry = Entry(çerçeve2,relief ="solid", bd = 2,highlightthickness=2, highlightbackground="steelblue")
    ara_entry.grid(row = 4,column = 1) 


    def ara():
        telefon_rehberi = open("Telefon Rehberi.txt","r")
        isim = ara_entry.get()
        yeni_dosya = open("Ara.txt","a")
        oku = open("Ara.txt","r")
        ara_entry.delete(0, "end")
                  
        for satır in telefon_rehberi:
            if isim in satır:
                yeni_dosya.write(satır)

        def kabul():
            pencere4.destroy()
            pencere3 = Toplevel()
            pencere3.title("Kişiler")
            kişiler = Label(pencere3, text = oku.read(), font = ("Courier",10))
            kişiler.pack()

            etiket5 = Label(pencere3,image = resim3)
            etiket5.pack()
        
            def çıkarkensil():
                pencere3.destroy()
                yeni_dosya = open("Ara.txt","w")

            tamam = Button(pencere3, text = "Tamam", font = ("Courier",10),command = çıkarkensil)
            tamam.pack()

        pencere4 = Tk()
        pencere4.title("Bilgi")
        mesaj = Label(pencere4, text = isim + ",adlı kişiyi arıyorsunuz...", font = ("Courier",10))
        mesaj.grid(row = 0, column = 0)
        kabul_buton = Button(pencere4, text = "➔", font = ("Courier",10),command = kabul)
        kabul_buton.grid(row = 0, column = 1)
      
        
    ara_buton = Button(çerçeve2,text = "➔",font = ("Courier",10),command = ara)
    ara_buton.grid(row = 4,column = 2)

    resim3 = PhotoImage(file ="people.gif")
    resim4 = PhotoImage(file="edit.gif")
    resim = PhotoImage(file="phone-book.gif")

    etiket1 = Label(çerçeve3 ,image = resim)
    etiket1.grid(row = 0, column = 0)

    isim = Label(çerçeve1,text = "İsim:", font = ("Courier",9))
    isim.grid(row = 0,column = 1,sticky = E)

    soyad = Label(çerçeve1,text = "Soyad:", font = ("Courier",9))
    soyad.grid(row = 1,column = 1,sticky = E)

    numara = Label(çerçeve1,text = "Telefon Numarası:", font =("Courier",9))
    numara.grid(row = 2,column = 1,sticky = E)

    isim_entry = Entry(çerçeve1,relief ="solid", bd = 2,highlightthickness=2, highlightbackground="steelblue")
    isim_entry.grid(row = 0, column = 2)

    soyad_entry = Entry(çerçeve1,relief ="solid", bd = 2,highlightthickness=2, highlightbackground="steelblue")
    soyad_entry.grid(row = 1, column = 2)

    numara_entry = Entry(çerçeve1,relief ="solid", bd = 2,highlightthickness=2, highlightbackground="steelblue")
    numara_entry.grid(row = 2,column = 2)

    ekle = Button(çerçeve1,text = "Ekle", font = ("Courier",9,"italic"),relief = "groove", overrelief = "solid",command = ekle)
    ekle.grid(row = 3,column = 2)

    çıkar = Button(çerçeve2,text = "Çıkar", font = ("Courier",9,"italic"),relief = "groove", overrelief = "solid",command = çıkar)
    çıkar.grid(row = 6, column = 0)

    düzenle = Button(çerçeve2,text = "Düzenle", font = ("Courier",9,"italic"),relief = "groove", overrelief = "solid",command = düzenle)
    düzenle.grid(row = 6, column = 1)

    çıkış = Button(çerçeve2,text = "Çıkış", font = ("Courier",9,"italic"),relief = "groove", overrelief = "solid",command = pencere1.destroy)
    çıkış.grid(row = 6, column = 3)

    etiket2 = Label(çerçeve2, text= "Telefon Rehberi",font = ("Courier",9))
    etiket2.grid(row=3, column = 1)

    scrollbar=Scrollbar(çerçeve2)
    listbox= Listbox(çerçeve2,yscrollcommand=scrollbar.set, width=60) 
    listbox.grid(row=5, columnspan=5)
    scrollbar.config(command=listbox.yview)

    oku = open("Telefon Rehberi.txt","r")
    kişiler = oku.readlines()

    for kişi in kişiler:
        listbox.insert(END, kişi)

    pencere1.mainloop()


resim1 = PhotoImage(file="contacts.gif")
resim2 = PhotoImage(file="phone-book-2.gif")

etiket2 = Label(pencere, image = resim1)
etiket2.grid(row = 0, column = 0,rowspan = 3)

yazı = Button(pencere, text = "Telefon Rehberime Gir", command = telefonrehberi, font = ("Courier",10), relief = "groove", overrelief = "solid")
yazı.grid(row = 2, column = 1)

etiket3 = Label(pencere, image = resim2)
etiket3.grid(row = 0, column = 2,rowspan = 3)

pencere.mainloop()








