"""
Created by Samantha Harper
Last Modified 5.7.24
This program is for Elli-May's Smoked BBQ food truck. It will allow customers to view our hours, location,
menu and complete an order prior to visiting the food truck.
"""
# importing tkinter
from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox


class MAINWINDOW:
    """ Main window of application which will display the food truck name and buttons to access the location and hours,
    menu, and order now windows of program. """
    def __init__(self, master):
        self.master = master
        # displaying images on main window
        # pulled chicken photo
        self.chickens_img = PhotoImage(file="EM_Chicken.png")
        # onions rings photo
        self.rings_img = PhotoImage(file="EM_Orings.png")
        # slaw-py sandwich photo
        self.sandwich_img = PhotoImage(file="EM_Sandwich.png")
        # creating title for window
        self.master.title("Elli-May's Smoked BBQ")
        # setting window size
        self.master.geometry('1050x800')
        # setting window to not be resized by user
        self.master.resizable(False, False)
        # setting background color
        self.color_background = "light grey"
        # configuring background
        self.master.config(background=self.color_background)
        # creating label font
        self.label_font = ("Helvetica", 15)
        # creating a smaller font for sub labels throughout the program
        self.sub_label_font = Font(font="Helvetica 10 italic")
        # setting button details
        self.button_background = "grey"
        self.button_font = Font(self.master, "Helvetica", size=18)
        # setting font for titles on window
        self.top_font = Font(family="Helvetica", size=25, weight="bold")
        # setting font color
        self.color_font = "Navy"

        # creating title for main window
        title = Label(self.master, text="%60s" % "Elli-May's Smoked BBQ", fg=self.color_font, bg=self.color_background,
                      font=self.top_font)
        title.grid(row=0, column=0, columnspan=2, pady=20, sticky=W)
        # creating location and hours button
        location_button = Button(self.master, text="LOCATION & HOURS", padx=30, pady=12, command=LOCATIONHOURSWINDOW,
                                 fg=self.color_font, bg=self.button_background, font=self.button_font)
        location_button.grid(row=5, column=1, padx=10, pady=10, sticky=W)
        # creating menu button
        menu_button = Button(self.master, text="MENU", padx=84, pady=10, command=MENUWINDOW, fg=self.color_font,
                             bg=self.button_background, font=self.button_font)
        # placing button
        menu_button.grid(row=6, column=1, padx=10, pady=10, sticky=W)
        # creating order now button
        order_button = Button(self.master, text="ORDER NOW!", padx=55, pady=10, command=ORDERNOWWINDOW,
                              fg=self.color_font,
                              bg=self.button_background, font=self.button_font)
        order_button.grid(row=7, column=1, padx=10, pady=10, sticky=W)
        # creating close application button
        close_button = Button(self.master, text="CLOSE", padx=5, pady=10, command=self.master.destroy,
                              fg=self.color_font, bg=self.button_background, font=self.button_font)
        # placing the button
        close_button.grid(row=0, column=2, pady=10, padx=5, sticky=E)

    def load_images(self):
        """ Load images from images folder. """
        # slaw-py sandwich photo
        self.sandwich_img = PhotoImage(file="EM_Sandwich.png")
        # onion rings photo
        self.rings_img = PhotoImage(file="EM_Orings.png")
        # pulled chicken photo
        self.chickens_img = PhotoImage(file="EM_Chicken.png")

    def display_images(self):
        """ Display images after loading images. """
        # label and placement for slaw-py sandwich photo
        sandwich_label = Label(self.master, image=self.sandwich_img)
        sandwich_label.grid(row=2, column=0, padx=5, sticky=W)
        # text for photo
        sandwich_text = Label(self.master, text="Slaw-py Sliders", font=self.sub_label_font, bg=self.color_background,
                              fg=self.color_font, borderwidth=3)
        sandwich_text.grid(row=3, column=0, padx=5, sticky=S)
        # inserting and placing the onion rings photo
        # label and placement for onion rings photo
        rings_label = Label(self.master, image=self.rings_img)
        rings_label.grid(row=2, column=1, padx=5, sticky=W)
        # text for photo
        rings_text = Label(self.master, text="O-Rings", font=self.sub_label_font, bg=self.color_background,
                           fg=self.color_font, borderwidth=3)
        rings_text.grid(row=3, column=1, sticky=S)
        # label and placement for pulled chicken photo
        chickens_label = Label(self.master, image=self.chickens_img)
        chickens_label.grid(row=2, column=2, padx=5, sticky=W)
        # text for photo
        chickens_text = Label(self.master, text="Pulled Chicken", font=self.sub_label_font, bg=self.color_background,
                              fg=self.color_font, borderwidth=3)
        chickens_text.grid(row=3, column=2, sticky=S)

class LOCATIONHOURSWINDOW:
    """ Location and Hours window will display the location of food truck and hours of operation """
    def __init__(self):
        # creating new window for hours and location
        self.win = Toplevel()
        # creating title for window
        self.win.title("Location & Hours")
        # set window size that is not resizeable.
        self.win.resizable(False, False)
        # size of window
        self.win.geometry("650x500")
        # setting font color
        self.win.color_font = "Navy"
        # boarder color
        self.win.config(bg=self.win.color_font)
        # creating frame for details
        self.frame = ttk.Frame(self.win)
        self.frame.pack(padx=5, pady=5, fill="both", expand=True)
        self.label = ttk.Label(self.frame)
        # setting label font
        self.win.label_font = ("Helvetica", 15)
        # setting button details
        self.win.button_background = "grey"
        # setting button font
        self.win.button_font = Font(self.win, "Helvetica", size=18)
        # setting font for titles on window
        self.win.top_font = Font(family="Helvetica", size=25, weight="bold")

        # setting title for window
        self.win.title("Elli-May's Smoked BBQ")

        # creating top label for menu
        location_label = Label(self.frame, text="Location & Hours", fg=self.win.color_font)
        location_label.config(font=self.win.top_font)
        # placing label
        location_label.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="NSEW")

        # creating label for food truck address
        address_label = Label(self.frame, text="Location: 322 E Kirkwood Bloomington, IN 47408", fg=self.win.color_font,
                              font=self.win.label_font)
        address_label.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        # creating hours chart
        hours_label = Label(self.frame, text="%-10s" % "HOURS", fg=self.win.color_font, font=self.win.label_font)
        hours_label.grid(row=3, column=1, columnspan=3, pady=10, padx=5, sticky="NSEW")
        # creating monday hours
        monday = Label(self.frame, text="%10s" % "Monday:", fg=self.win.color_font, font=self.win.label_font)
        monday.grid(row=4, column=1)
        mon_hours = Label(self.frame, text="%5s" % "CLOSED", fg=self.win.color_font, font=self.win.label_font)
        mon_hours.grid(row=4, column=2)
        # creating tuesday hours
        tuesday = Label(self.frame, text="%11s" % "Tuesday:", fg=self.win.color_font, font=self.win.label_font)
        tuesday.grid(row=5, column=1)
        tue_hours = Label(self.frame, text="%10s" % "4PM - 1AM", fg=self.win.color_font, font=self.win.label_font)
        tue_hours.grid(row=5, column=2)
        # creating wednesday hours
        wednesday = Label(self.frame, text="%18s" % "Wednesday:", fg=self.win.color_font, font=self.win.label_font)
        wednesday.grid(row=6, column=1)
        wed_hours = Label(self.frame, text="%10s" % "4PM - 1AM", fg=self.win.color_font, font=self.win.label_font)
        wed_hours.grid(row=6, column=2)
        # creating thursday hours
        thursday = Label(self.frame, text="%13s" % "Thursday:", fg=self.win.color_font, font=self.win.label_font)
        thursday.grid(row=7, column=1)
        thur_hours = Label(self.frame, text="%10s" % "4PM - 1AM", fg=self.win.color_font, font=self.win.label_font)
        thur_hours.grid(row=7, column=2)
        # creating friday hours
        friday = Label(self.frame, text="%8s" % "Friday:", fg=self.win.color_font, font=self.win.label_font)
        friday.grid(row=8, column=1)
        fri_hours = Label(self.frame, text="%10s" % "4PM - 1AM", fg=self.win.color_font, font=self.win.label_font)
        fri_hours.grid(row=8, column=2)
        # creating saturday hours
        saturday = Label(self.frame, text="%13s" % "Saturday:", fg=self.win.color_font, font=self.win.label_font)
        saturday.grid(row=9, column=1)
        sat_hours = Label(self.frame, text="%10s" % "4PM - 1AM", fg=self.win.color_font, font=self.win.label_font)
        sat_hours.grid(row=9, column=2)
        # creating sunday hours
        sunday = Label(self.frame, text="%9s" % "Sunday:", fg=self.win.color_font, font=self.win.label_font)
        sunday.grid(row=10, column=1)
        sun_hours = Label(self.frame, text="%10s" % "4PM - 1AM", fg=self.win.color_font, font=self.win.label_font)
        sun_hours.grid(row=10, column=2)

        # placing exit button
        exit_button = Button(self.frame, text="CLOSE", padx=35, pady=10, command=self.win.destroy,
                             bg=self.win.button_background, font=self.win.button_font, fg=self.win.color_font)
        exit_button.grid(row=11, column=1, pady=5)
        # placing menu button
        menu = Button(self.frame, text="MENU", padx=35, pady=10, command=MENUWINDOW, fg=self.win.color_font,
                      bg=self.win.button_background, font=self.win.button_font)
        menu.grid(row=11, column=2)
        # placing order now button
        order = Button(self.frame, text="ORDER NOW!", padx=5, pady=10, command=ORDERNOWWINDOW, fg=self.win.color_font,
                       bg=self.win.button_background, font=self.win.button_font)
        order.grid(row=0, column=0)


class MENUWINDOW:
    """Menu window will display the details of all items at Elli-May's Smoked BBQ"""
    def __init__(self):
        # creating new window for menu
        self.win2 = Toplevel()
        # creating title for window
        self.win2.title("Elli-May's Menu")
        # set window size that is not resizeable.
        self.win2.resizable(False, False)
        # size of window
        self.win2.geometry("700x800")
        # setting font color
        self.win2.color_font = "Navy"
        # creating label font
        self.win2.label_font = ("Helvetica", 15)
        # creating a smaller font for sub labels throughout the program
        self.win2.sub_label_font = Font(font="Helvetica 10 italic")
        # setting button details
        self.win2.button_background = "grey"
        self.win2.button_font = Font(self.win2, "Helvetica", size=18)
        # setting font for titles on window
        self.win2.top_font = Font(family="Helvetica", size=25, weight="bold")
        # setting background color
        self.win2.color_background = "light grey"
        # creating menu font specs
        self.win2.menu_font = Font(family='Helvetica', size=12)
        # boarder color
        self.win2.config(bg=self.win2.color_font)
        # creating frame for details of menu to be placed in
        self.menu_frame = ttk.Frame(self.win2, borderwidth=5, relief="sunken")
        self.menu_frame.pack(padx=5, pady=5, fill="both", expand=True)
        self.menu_label = ttk.Label(self.menu_frame)

        # creating menu header
        menu_label = Label(self.menu_frame, text="Elli-May's MENU", font=self.win2.top_font, fg=self.win2.color_font)
        # placing menu header
        menu_label.grid(column=0, row=0, columnspan=4, sticky="NSEW")

        # setting sandwich section of menu
        sandwiches_label = Label(self.menu_frame, text="FAMOUS SANDWICHES", fg=self.win2.color_font,
                                 font=self.win2.label_font)
        sandwiches_label.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky="NSEW")

        # creating sandwiches and placing them on menu window
        # pork sliders
        pulled_pork_label = Label(self.menu_frame, text="BBQ Pulled Pork - 8.00", fg=self.win2.color_font,
                                  font=self.win2.menu_font)
        pulled_pork_label.grid(row=4, column=0, columnspan=2, sticky="NSEW")
        pulled_pork_details = Label(self.menu_frame, text=" Slow-roasted to perfection using\ncheery and apple wood",
                                    fg=self.win2.color_font, font=self.win2.sub_label_font)
        pulled_pork_details.grid(row=5, column=0, columnspan=2, sticky="NSEW")
        # slaw-py sliders
        slawpy_sliders_label = Label(self.menu_frame, text="Slaw-py Sliders - 10.00", fg=self.win2.color_font,
                                     font=self.win2.menu_font)
        slawpy_sliders_label.grid(row=4, column=2, columnspan=2, sticky="NSEW")
        slawpy_sliders_details = Label(self.menu_frame, text="BBQ Pork topped with our\nhomemade coleslaw",
                                       fg=self.win2.color_font, font=self.win2.sub_label_font)
        slawpy_sliders_details.grid(row=5, column=2, columnspan=2, sticky="NSEW")
        # beef brisket
        beef_brisket_sliders_label = Label(self.menu_frame, text="BBQ Beef Brisket Sliders - 11.00",
                                           fg=self.win2.color_font, font=self.win2.menu_font)
        beef_brisket_sliders_label.grid(row=6, column=0, columnspan=2, sticky="NSEW")
        brisket_sliders_details = Label(self.menu_frame, text="Low and slow-smoked BBQ Brisket\nserved slider style  ",
                                        fg=self.win2.color_font, font=self.win2.sub_label_font)
        brisket_sliders_details.grid(row=7, column=0, columnspan=2, sticky="NSEW")
        # wrangler
        wrangler_label = Label(self.menu_frame, text="Pork Wrangler - 9.50", fg=self.win2.color_font,
                               font=self.win2.menu_font)
        wrangler_label.grid(row=6, column=2, columnspan=2, sticky="NSEW")
        wrangler_details = Label(self.menu_frame, text="Throw some O-rings on top of\nour pulled pork",
                                 fg=self.win2.color_font,
                                 font=self.win2.sub_label_font)
        wrangler_details.grid(row=7, column=2, sticky="NSEW", columnspan=2)
        # pork sliders
        pork_sliders_label = Label(self.menu_frame, text="BBQ Pork Sliders - 9.00",  fg=self.win2.color_font,
                                   font=self.win2.menu_font)
        pork_sliders_label.grid(row=8, column=0, columnspan=2, sticky="NSEW")
        pork_sliders_details = Label(self.menu_frame, text="Four of our Famous BBQ Pork Sliders",
                                     fg=self.win2.color_font,
                                     font=self.win2.sub_label_font)
        pork_sliders_details.grid(row=9, column=0, columnspan=2, sticky="NSEW")
        # the ringer
        ringer_label = Label(self.menu_frame, text="The Ringer - 11.50", fg=self.win2.color_font,
                             font=self.win2.menu_font)
        ringer_label.grid(row=8, column=2, sticky="NSEW")
        ringer_details = Label(self.menu_frame, text="Brisket and O-Rings together", fg=self.win2.color_font,
                               font=self.win2.sub_label_font)
        ringer_details.grid(row=9, column=2, columnspan=2, sticky="NSEW")
        # best of both worlds
        best_of_both_label = Label(self.menu_frame, text="Best of Both Worlds - 9.00", fg=self.win2.color_font,
                                   font=self.win2.menu_font)
        best_of_both_label.grid(row=10, column=0, columnspan=2, sticky="NSEW")
        best_of_both_details = Label(self.menu_frame, text="A combination of our pulled pork and\nbeef brisket on "
                                                           "a bun", fg=self.win2.color_font,
                                     font=self.win2.sub_label_font)
        best_of_both_details.grid(row=11, column=0, columnspan=2, sticky="NSEW", padx=5)
        # smoked chicken
        smoked_chicken_label = Label(self.menu_frame, text="Smoked Chicken - 9.00", fg=self.win2.color_font,
                                     font=self.win2.menu_font)
        smoked_chicken_label.grid(row=10, column=2, columnspan=2, sticky="NSEW")
        smoked_chicken_details = Label(self.menu_frame,
                                       text="Chicken smoked and shredded sauced\nwith our famous BBQ sauce on a bun",
                                       fg=self.win2.color_font, font=self.win2.sub_label_font)
        smoked_chicken_details.grid(row=11, column=2, columnspan=2, sticky="NSEW", padx=5)
        # BBQ brisket
        brisket_label = Label(self.menu_frame, text="BBQ Beef Brisket - 10.00", fg=self.win2.color_font,
                              font=self.win2.menu_font)
        brisket_label.grid(row=12, column=0, columnspan=2, sticky="NSEW")
        brisket_details = Label(self.menu_frame, text="Slow-roasted beef brisket using cherry wood\nserved with "
                                                      "homemade BBQ sauce", fg=self.win2.color_font,
                                font=self.win2.sub_label_font)
        brisket_details.grid(row=13, column=0, columnspan=2, sticky="NSEW", padx=5)
        # pulled chicken sliders
        chicken_sliders_label = Label(self.menu_frame, text="Chicken Sliders - 9.00", fg=self.win2.color_font,
                                      font=self.win2.menu_font)
        chicken_sliders_label.grid(row=12, column=2, columnspan=2, sticky="NSEW")
        chicken_sliders_details = Label(self.menu_frame, text="Our famous BBQ pulled chicken\nserved slider style",
                                        fg=self.win2.color_font, font=self.win2.sub_label_font)
        chicken_sliders_details.grid(row=13, column=2, columnspan=2, sticky="NSEW", padx=5)
        # slaw-py pork
        slawpy_pork_label = Label(self.menu_frame, text="Slaw-py Pork - 9.50", fg=self.win2.color_font,
                                  font=self.win2.menu_font)
        slawpy_pork_label.grid(row=14, column=0, columnspan=2, sticky="NSEW")
        slawpy_pork_details = Label(self.menu_frame, text="BBQ pulled pork topped with\nour homemade slaw",
                                    fg=self.win2.color_font, font=self.win2.sub_label_font)
        slawpy_pork_details.grid(row=15, column=0, columnspan=2, sticky="NSEW", padx=5)

        # creating tacos section of menu
        tacos_label = Label(self.menu_frame, text="TACOS", fg=self.win2.color_font, font=self.win2.label_font)
        tacos_label.grid(row=22, column=2, columnspan=3, rowspan=2, sticky="NSEW")
        taco_label_details = Label(self.menu_frame, text="Four tacos with your choice of toppings and salsa!",
                                   fg=self.win2.color_font, font=self.win2.sub_label_font)
        taco_label_details.grid(row=24, column=2, columnspan=2, sticky="NSEW")
        # brisket tacos
        brisket_tacos_label = Label(self.menu_frame, text="Brisket Tacos - 11.00",  fg=self.win2.color_font,
                                    font=self.win2.menu_font)
        brisket_tacos_label.grid(row=25, column=2, sticky="E")

        # Pork Tacos
        pork_tacos_label = Label(self.menu_frame, text="Pork Tacos - 9.00",  fg=self.win2.color_font,
                                 font=self.win2.menu_font)
        pork_tacos_label.grid(row=26, column=2, sticky="E")

        # Chicken Tacos
        chicken_tacos_label = Label(self.menu_frame, text="Chicken Tacos - 9.00",  fg=self.win2.color_font,
                                    font=self.win2.menu_font)
        chicken_tacos_label.grid(row=27, column=2, sticky="E")

        # creating side and drink portion of menu
        sides_and_drinks_label = Label(self.menu_frame, text="SIDES & DRINKS", fg=self.win2.color_font,
                                       font=self.win2.label_font)
        sides_and_drinks_label.grid(row=22, column=0, columnspan=2, rowspan=2, sticky="NSEW")
        # coleslaw
        coleslaw_label = Label(self.menu_frame, text="Coleslaw - 3.00", fg=self.win2.color_font,
                               font=self.win2.menu_font)
        coleslaw_label.grid(row=25, column=0, sticky="W")
        # fries
        fries_label = Label(self.menu_frame, text="Fries - 3.00", fg=self.win2.color_font, font=self.win2.menu_font)
        fries_label.grid(row=24, column=0, sticky="W")
        # tator tots
        tator_label = Label(self.menu_frame, text="Tator Tots - 4.00", fg=self.win2.color_font,
                            font=self.win2.menu_font)
        tator_label.grid(row=26, column=0, sticky="W")
        # potato salad
        pot_salad_label = Label(self.menu_frame, text="Potato Salad - 3.50", fg=self.win2.color_font,
                                font=self.win2.menu_font)
        pot_salad_label.grid(row=28, column=0, sticky="W")
        # Onion Rings
        onion_rings_label = Label(self.menu_frame, text="Onion Rings - 4.00", fg=self.win2.color_font,
                                  font=self.win2.menu_font)
        onion_rings_label.grid(row=27, column=0, sticky="W")
        # bottled water
        water_label = Label(self.menu_frame, text="Bottled Water - 2.00", fg=self.win2.color_font,
                            font=self.win2.menu_font)
        water_label.grid(row=24, column=1, sticky="W")
        # soda
        soda_label = Label(self.menu_frame, text="Bottled Pepsi Products - 2.00", fg=self.win2.color_font,
                           font=self.win2.menu_font)
        soda_label.grid(row=25, column=1, sticky="W")

        # creating combo information
        combo_label = Label(self.menu_frame, text="MAKE ANY SANDWICH OR TACO A COMBO FOR JUST 2.00 MORE!",
                            fg=self.win2.color_font, bg=self.win2.color_background, font=self.win2.label_font)
        combo_label.grid(row=29, column=0, columnspan=3, pady=5, padx=5, sticky="NSEW")
        combo_details = Label(self.menu_frame, text="Your choice of side and a drink!", fg=self.win2.color_font,
                              font=self.win2.sub_label_font, bg=self.win2.color_background)
        combo_details.grid(row=30, column=0, columnspan=3, pady=5, sticky="NSEW")

        # Buttons!
        # button to location and hours page
        location_hours = Button(self.menu_frame, text="LOCATION & HOURS", padx=30, pady=10, command=LOCATIONHOURSWINDOW,
                                fg=self.win2.color_font, font=self.win2.button_font, bg=self.win2.button_background)
        location_hours.grid(row=34, column=1)
        # button to order now page
        order = Button(self.menu_frame, text="ORDER NOW!", padx=5, pady=10, command=ORDERNOWWINDOW,
                       fg=self.win2.color_font, bg=self.win2.button_background, font=self.win2.button_font)
        order.grid(row=0, column=0)
        # button to close window
        exit_button = Button(self.menu_frame, text="CLOSE", padx=35, pady=10, command=self.win2.destroy,
                             bg=self.win2.button_background, font=self.win2.button_font, fg=self.win2.color_font)
        exit_button.grid(row=34, column=2)


class ORDERNOWWINDOW:
    """ The Order Now Window Class will include all input fields, dropdowns, and checkboxes for users to select a
        desired meal and place an order which displays a receipt"""

    def __init__(self):
        # creating new window for ordering
        self.win3 = Toplevel()
        # creating title for window
        self.win3.title("Order Now!")
        # set window size that is not resizeable.
        self.win3.resizable(False, False)
        # size of window
        self.win3.geometry("1000x800")

        # setting font color
        self.win3.color_font = "Navy"
        # creating label font
        self.win3.label_font = ("Helvetica", 15)
        # creating a smaller font for sub labels throughout the program
        self.win3.sub_label_font = Font(font="Helvetica 10 italic")
        # setting button details
        self.win3.button_background = "grey"
        self.win3.button_font = Font(self.win3, "Helvetica", size=18)
        # setting font for titles on window
        self.win3.top_font = Font(family="Helvetica", size=25, weight="bold")
        # setting background color
        self.win3.color_background = "light grey"
        # creating menu font specs
        self.win3.menu_font = Font(family='Helvetica', size=12)
        # boarder color
        self.win3.config(bg=self.win3.color_font)
        # setting input font color
        self.win3.input_color = "Black"

        # creating frame for details
        self.order_frame = ttk.Frame(self.win3, borderwidth=5, relief="sunken")
        self.order_frame.pack(padx=5, pady=5, fill="both", expand=True)
        self.menu_label = ttk.Label(self.order_frame)

        # creating top label for ordering page
        order_label = Label(self.order_frame, text="Order NOW!", font=self.win3.top_font, fg=self.win3.color_font)
        # placing label
        order_label.grid(column=1, row=0, columnspan=2, sticky="NSEW", padx=10, pady=30)

        def receipt():
            """ the receipt function will validate input before displaying the order name, phone number, and
            meal details including price"""
            # calling calculation variables and function
            sub_total, sales_tax, order_total = calculate_total()
            calculate_total()

            # validating entry fields
            # creating first name variable
            first_name = first_name_entry.get()
            # validating entry to be letters and not blank
            if not only_letters(first_name, 0):
                messagebox.showerror("Error", "Your first name can only contain letters and "
                                              "cannot be blank! ")
                return
            # creating last name variable
            last_name = last_name_entry.get()
            # validating entry to be letters and not blank
            if not only_letters(last_name, 0):
                messagebox.showerror("Error", "Your last name can only contain letters and cannot be "
                                              "blank! ")
                return
            # creating phone number variable
            phone_number = phone_number_entry.get()
            # validating entry to be digits and not blank
            if not only_numbers(phone_number, 10):
                messagebox.showerror("Error", "Phone Number must be 10 digits long!")
                return
            # creating cardholder first name variable
            cardholder_first_name = cardholder_f_name_entry.get()
            # validating entry to be letters and not blank
            if not only_letters(cardholder_first_name, 0):
                messagebox.showerror("Error", "The cardholder's first name can only contain "
                                              "letters and cannot be blank! ")
                return
            # creating cardholder last name variable
            cardholder_last_name = cardholder_l_name_entry.get()
            # validating entry to be letters and not blank
            if not only_letters(cardholder_last_name, 0):
                messagebox.showerror("Error", "The card holder's last name can only contain letters and "
                                              "cannot be blank! ")
                return
            # creating an address variable
            c_address = address.get()
            # validating entry to be letters and numbers and not blank
            if c_address == "":
                messagebox.showerror("Error", "Cardholder address must contain a valid street address "
                                              "and cannot be blank!")
                return
            # creating city variable
            city = city_entry.get()
            # validating entry to be letters and not blank
            if not only_letters(city, 0):
                messagebox.showerror("Error", "Your city can only contain letters and cannot be blank! ")
                return
            # creating state variable
            state = state_entry.get()
            # validating entry to be letters and to be at least 2 characters
            if not state_validate(state, 2):
                messagebox.showerror("Error", "Your state must be the two letter abbreviation and it"
                                              " cannot be blank!")
                return
            # creating zip code variable
            zip_code = zip_code_entry.get()
            # validating entry to be digits and to be 5 digits
            if not only_numbers(zip_code, 5):
                messagebox.showerror("Error", "Zip Code must be 5 digits and cannot be blank!")
                return
            # creating card number variable
            card = card_entry.get()
            # validating entry to be digits and to be 16 digits
            if not only_numbers(card, 16):
                messagebox.showerror("Error", "Card Number must be 16 digits and cannot be blank!")
                return
            # creating card expiration date variable
            c_exp = card_exp_entry.get()
            # validating entry to be digits and to be 4 digits
            if not only_numbers(c_exp, 4):
                messagebox.showerror("Error", "Your card expiration date must be 4 digits (MMYY) and "
                                              "cannot be blank!!")
                return
            # creating card cvv variable
            c_cvv = card_cvv_entry.get()
            # validating entry to be digits and to be 3 digits
            if not only_numbers(c_cvv, 3):
                messagebox.showerror("Error", "CVV must be 3 digits and cannot be blank!")
                return
            else:
                # else statement to display a receipt message box if all input is valid
                receipt_message = (f"Thank you for your order! Elli-May will see you soon!\n"
                                   f"\n Name: {first_name_entry.get()} {last_name_entry.get()}"
                                   f"\n Phone Number: {phone_number_entry.get()} "
                                   f"\n Sandwich: {sandwich_selected.get()} "
                                   f"\n Taco: {taco_selected.get()} "
                                   f"\n Taco Toppings: {none_selected.get()} {pico_selected.get()} "
                                   f"{cheddar_cheese.get()} {sour_cream.get()} {pickled_onions.get()} "
                                   f"{jack_cheese.get()}"
                                   f"\n Combo: {combo_selected.get()} "
                                   f"\n Side: {side_selected.get()} "
                                   f"\n Drink: {drink_selected.get()}\n"
                                   f"\n Sub Total: ${sub_total:.2f} "
                                   f"\n Tax: ${sales_tax:.2f} "
                                   f"\n Total: ${order_total:.2f}")
                # show receipt in message box
                messagebox.showinfo("Receipt", receipt_message)

        def calculate_total():
            """ calculate_total function to calculate total price of order """
            # initializations of variables for meal calculations
            sub_total = 0
            sales_tax_rate = 0.07
            # add sandwich price if selected
            if sandwich_selected.get() != sandwich_options[0]:
                sandwich_index = sandwich_options.index(sandwich_selected.get())
                # convert list string to floating point number
                sub_total += float(sandwich_prices[sandwich_index])
            # add taco price if selected
            if taco_selected.get() != taco_options[0]:
                taco_index = taco_options.index(taco_selected.get())
                # covert list string to floating point number
                sub_total += float(taco_prices[taco_index])
            # add combo price if needed
            if combo_selected.get() == "Yes":
                # add additional price for combo meal
                sub_total += add_combo
            # add side price if selected and combo is not selected
            if side_selected.get() != side_options[0] and combo_selected.get() != "Yes":
                side_index = side_options.index(side_selected.get())
                # converting string price to floating point number
                sub_total += float(side_prices[side_index])
            # add drink price if selected and combo is not selected
            if drink_selected.get() != drink_options[0] and combo_selected.get() != "Yes":
                # adding cost to drink if needed
                sub_total += add_drink
            # calculate tax and total
            sales_tax = sub_total * sales_tax_rate
            order_total = sub_total + sales_tax

            return sub_total, sales_tax, order_total

        def state_validate(input_text, length):
            """ state_validate function to validate state input to be a specific length (2). This function was required
            as the only letters function validates letter input fields to be greater than the specific length but not
             equal to a specific length"""
            return input_text.isalpha() and len(input_text) == length

        def only_letters(input_text, length):
            """ only letters function will validate input to ensure each only contains letters and is the
            not blank"""
            # reviewing all letter only input fields to ensure they do not include numbers and are not blank
            return input_text.isalpha() and len(input_text) > length

        # creating label for First Name entry
        order_first_name = Label(self.order_frame, text="First Name: ", font=self.win3.label_font,
                                 fg=self.win3.color_font)
        order_first_name.grid(row=3, column=0, sticky="E")
        # creating entry box for first name with validation for characters only
        first_name_entry = Entry(self.order_frame, width=20, borderwidth=3, font=self.win3.label_font,
                                 fg=self.win3.input_color)
        first_name_entry.grid(row=3, column=1, sticky="W")

        # creating label for Last Name entry
        order_last_name = Label(self.order_frame, text="Last Name: ", font=self.win3.label_font,
                                fg=self.win3.color_font)
        order_last_name.grid(row=3, column=2, sticky="E")
        # creating entry box for last name with validation for characters only
        last_name_entry = Entry(self.order_frame, width=20, borderwidth=3, font=self.win3.label_font,
                                fg=self.win3.input_color)
        last_name_entry.grid(row=3, column=3, sticky="W")

        def only_numbers(input_text, length):
            """only numbers function which will validate entry to only allow numbers and specified length"""
            # reviewing all number input fields to ensure they are the required length and do no include letters
            return input_text.isdigit() and len(input_text) == length

        # creating label for phone number entry
        order_phone_number = Label(self.order_frame, text="Phone Number: ", font=self.win3.label_font,
                                   fg=self.win3.color_font)
        order_phone_number.grid(row=4, column=0, sticky="E")
        # creating entry box for phone number with validation for digits only
        phone_number_entry = Entry(self.order_frame, width=10, borderwidth=3, font=self.win3.label_font,
                                   fg=self.win3.input_color)
        phone_number_entry.grid(row=4, column=1, sticky="W")

        # creating sandwich menu selection drop down
        # creating sandwich selection label
        select_sandwich = Label(self.order_frame, text="Sandwich: ", fg=self.win3.color_font, font=self.win3.label_font)
        select_sandwich.grid(row=6, column=0, sticky="E")
        # creating sandwich selection list
        sandwich_options = [
            "No Sandwich",
            "BBQ Pulled Pork",
            "Slaw-py Sliders",
            "BBQ Beef Brisket Sliders",
            "Pork Wrangler",
            "BBQ Pork Sliders",
            "The Ringer",
            "Best of Both Worlds",
            "Smoked Chicken",
            "BBQ Beef Brisket",
            "Chicken Sliders",
            "Slaw-py Pork"
        ]
        # creating parallel list for sandwich prices
        sandwich_prices = [
            "0.00",
            "8.00",
            "10.00",
            "11.00",
            "9.50",
            "9.00",
            "11.50",
            "9.00",
            "9.00",
            "10.00",
            "9.00",
            "9.50"
        ]

        # declaring variable for sandwich_options list
        sandwich_selected = StringVar()
        # setting default value of list
        sandwich_selected.set(sandwich_options[0])
        # creating drop down menu for sandwiches
        self.drop = OptionMenu(self.order_frame, sandwich_selected, *sandwich_options)
        self.drop.config(fg=self.win3.input_color, font=self.win3.label_font)
        self.drop.grid(row=6, column=1, sticky="W", pady=5)

        # creating Taco selection Drop Down
        # creating taco selection label
        select_taco = Label(self.order_frame, text="Tacos: ", fg=self.win3.color_font, font=self.win3.label_font)
        select_taco.grid(row=7, column=0, sticky="E")
        # creating sandwich selection list
        taco_options = [
            "No Tacos",
            "BBQ Brisket Tacos",
            "Pork Tacos",
            "Chicken Tacos"
        ]

        # creating a parallel list for taco prices
        taco_prices = [
            "0.00",
            "11.00",
            "9.00",
            "9.00"
        ]
        # declaring variable for taco_options list
        taco_selected = StringVar()
        # setting default value of list
        taco_selected.set(taco_options[0])
        # creating drop down menu for tacos
        self.drop = OptionMenu(self.order_frame, taco_selected, *taco_options)
        self.drop.config(fg=self.win3.input_color, font=self.win3.label_font)
        self.drop.grid(row=7, column=1, sticky="W", pady=5)

        def handle_check():
            """handle check function to check button clicks"""
            if none_selected.get() == "No Toppings":
                # if no toppings is selected, deselect all other options
                pico_selected.set("")
                cheddar_cheese.set("")
                sour_cream.set("")
                pickled_onions.set("")
                jack_cheese.set("")

        # creating taco topping selection buttons
        # creating label for taco toppings
        topping_label = Label(self.order_frame, text="Taco Toppings:", font=self.win3.label_font,
                              fg=self.win3.color_font)
        topping_label.grid(row=8, column=0, sticky="E")

        # creating list for topping options
        topping_options = [
            "None",
            "Pico",
            "Cheddar Cheese",
            "Sour Cream",
            "Pickled Red Onions",
            "Jack Cheese"
        ]

        # declaring variable as string for no topping option
        none_selected = StringVar()
        none_selected.set("")
        # declaring variable as string for pico option
        pico_selected = StringVar()
        pico_selected.set("")
        # declaring variable as string for cheddar cheese option
        cheddar_cheese = StringVar()
        cheddar_cheese.set("")
        # declaring variable as string for sour cream option
        sour_cream = StringVar()
        sour_cream.set("")
        # declaring variable as string for pickled onions option
        pickled_onions = StringVar()
        pickled_onions.set("")
        # declaring variable as string for jack cheese option
        jack_cheese = StringVar()
        jack_cheese.set("")

        # creating check buttons for each taco topping
        # check box for no toppings
        self.topping_options = Checkbutton(self.order_frame, text=topping_options[0], variable=none_selected,
                                           onvalue="No Toppings", offvalue="", command=handle_check,
                                           fg=self.win3.input_color, font=self.win3.label_font)
        self.topping_options.select()
        self.topping_options.grid(row=8, column=1, sticky="W")
        # check box for pico topping
        self.topping_options = Checkbutton(self.order_frame, text=topping_options[1], variable=pico_selected,
                                           onvalue="Pico ", offvalue="", command=handle_check, fg=self.win3.input_color,
                                           font=self.win3.label_font)
        self.topping_options.deselect()
        self.topping_options.grid(row=8, column=2, sticky="W")
        # check box for cheddar cheese
        self.topping_options = Checkbutton(self.order_frame, text=topping_options[2], variable=cheddar_cheese,
                                           onvalue="Cheddar Cheese ", offvalue="", command=handle_check,
                                           fg=self.win3.input_color, font=self.win3.label_font)
        self.topping_options.deselect()
        self.topping_options.grid(row=9, column=1, sticky="W")
        # check box for sour cream
        self.topping_options = Checkbutton(self.order_frame, text=topping_options[3], variable=sour_cream,
                                           onvalue="Sour Cream ", offvalue="", command=handle_check,
                                           fg=self.win3.input_color, font=self.win3.label_font)
        self.topping_options.deselect()
        self.topping_options.grid(row=9, column=2, sticky="W")
        # check box for pickled red onions
        self.topping_options = Checkbutton(self.order_frame, text=topping_options[4], variable=pickled_onions,
                                           onvalue="Pickled Red Onions ", offvalue="", command=handle_check,
                                           fg=self.win3.input_color, font=self.win3.label_font)
        self.topping_options.deselect()
        self.topping_options.grid(row=10, column=1, sticky="W")
        # check boc for jack cheese
        self.topping_options = Checkbutton(self.order_frame, text=topping_options[5], variable=jack_cheese,
                                           onvalue="Jack Cheese ", offvalue="", command=handle_check,
                                           fg=self.win3.input_color, font=self.win3.label_font)
        self.topping_options.deselect()
        self.topping_options.grid(row=10, column=2, sticky="W")

        # create check buttons for combo selection
        # creating label for combo option
        combo_label = Label(self.order_frame, text="Make your meal a combo: ", font=self.win3.label_font,
                            fg=self.win3.color_font)
        combo_label.grid(row=11, column=0, sticky="W")

        # setting price for combo selection
        add_combo = 2.00

        # declaring variable for combo options
        combo_selected = StringVar()
        combo_selected.set(combo_selected.get())

        # creating check buttons for combo selection
        self.combo_options = Checkbutton(self.order_frame, text="Yes", variable=combo_selected,
                                         onvalue="Yes", offvalue="No", fg=self.win3.input_color,
                                         font=self.win3.label_font)
        self.combo_options.deselect()
        self.combo_options.grid(row=11, column=1, sticky="W")
        self.combo_options = Checkbutton(self.order_frame, text="No", variable=combo_selected, onvalue="No",
                                         offvalue="Yes", fg=self.win3.input_color, font=self.win3.label_font)
        self.combo_options.deselect()
        self.combo_options.grid(row=11, column=2, sticky="W")

        # create side drop down
        select_side = Label(self.order_frame, text="Side: ", fg=self.win3.color_font, font=self.win3.label_font)
        select_side.grid(row=12, column=0, sticky="E")
        # creating side selection list
        side_options = [
            "No Side",
            "Cole Slaw",
            "Fries",
            "Tator Tots",
            "Potato Salad",
            "Onion Rings"
        ]
        side_prices = [
            "0.00",
            "3.00",
            "3.00",
            "4.00",
            "3.50",
            "4.00"
        ]
        # declaring variable for side_options list
        side_selected = StringVar()
        # setting default value of list
        side_selected.set(side_options[0])
        # creating drop down menu for sides
        self.drop = OptionMenu(self.order_frame, side_selected, *side_options)
        self.drop.config(fg=self.win3.input_color, font=self.win3.label_font)
        self.drop.grid(row=12, column=1, sticky="W", pady=5)

        # create drink drop down
        select_drink = Label(self.order_frame, text="Drink: ", fg=self.win3.color_font, font=self.win3.label_font)
        select_drink.grid(row=13, column=0, sticky="E")
        # creating drink selection list
        drink_options = [
            "No Drink",
            "Water",
            "Pepsi",
            "Diet Pepsi",
            "Sierra Mist",
            "Mountain Dew",
            "Diet Mountain Dew",
            "Root Beer"
        ]
        # declaring variable for drink_options list
        drink_selected = StringVar()
        # setting default value of list
        drink_selected.set(drink_options[0])
        # declaring price of adding a drink:
        add_drink = 2.00
        # creating drop down menu for drinks
        self.drop = OptionMenu(self.order_frame, drink_selected, *drink_options)
        self.drop.config(fg=self.win3.input_color, font=self.win3.label_font)
        self.drop.grid(row=13, column=1, sticky="W", pady=5)

        # create cardholder first name input
        order_cardholder_f_name = Label(self.order_frame, text="Cardholder First Name: ", font=self.win3.label_font,
                                        fg=self.win3.color_font)
        order_cardholder_f_name.grid(row=14, column=0, sticky="E")
        # creating entry box for cardholder first name
        cardholder_f_name_entry = Entry(self.order_frame, width=20, borderwidth=3, font=self.win3.label_font,
                                        fg=self.win3.input_color)
        cardholder_f_name_entry.grid(row=14, column=1, sticky="W")
        # creating cardholders last name input
        order_cardholder_l_name = Label(self.order_frame, text="Cardholder Last Name: ", font=self.win3.label_font,
                                        fg=self.win3.color_font)
        order_cardholder_l_name.grid(row=14, column=2, sticky="E")
        # creating entry box for cardholder last name
        cardholder_l_name_entry = Entry(self.order_frame, width=20, borderwidth=3, font=self.win3.label_font,
                                        fg=self.win3.input_color)
        cardholder_l_name_entry.grid(row=14, column=3, sticky="W")

        # create address entry
        order_cardholder_address = Label(self.order_frame, text="Cardholder Address: ", font=self.win3.label_font,
                                         fg=self.win3.color_font)
        order_cardholder_address.grid(row=15, column=0, sticky="E")
        # creating entry box for address
        address = Entry(self.order_frame, width=20, borderwidth=3, font=self.win3.label_font, fg=self.win3.input_color)
        address.grid(row=15, column=1, sticky="W")
        # create city entry
        order_city = Label(self.order_frame, text="City: ", font=self.win3.label_font, fg=self.win3.color_font)
        order_city.grid(row=16, column=0, sticky="E")
        # creating entry box for city with validation for characters only
        city_entry = Entry(self.order_frame, width=20, borderwidth=3, font=self.win3.label_font,
                           fg=self.win3.input_color)
        city_entry.grid(row=16, column=1, sticky="W")

        # create state entry
        order_state = Label(self.order_frame, text="State: ", font=self.win3.label_font, fg=self.win3.color_font)
        order_state.grid(row=15, column=2, sticky="E")
        # creating entry box for state with validation for characters only
        state_entry = Entry(self.order_frame, width=2, borderwidth=3, font=self.win3.label_font,
                            fg=self.win3.input_color)
        state_entry.grid(row=15, column=3, sticky="W")

        # create zip code entry
        order_zip_code = Label(self.order_frame, text="Zip Code: ", font=self.win3.label_font, fg=self.win3.color_font)
        order_zip_code.grid(row=16, column=2, sticky="E")
        # creating entry box for zipcode with validation for digits only
        zip_code_entry = Entry(self.order_frame, width=5, borderwidth=3, font=self.win3.label_font,
                               fg=self.win3.input_color)
        zip_code_entry.grid(row=16, column=3, sticky="W")

        # create card number entry
        order_card = Label(self.order_frame, text="Card Number: ", font=self.win3.label_font, fg=self.win3.color_font)
        order_card.grid(row=17, column=0, sticky="E")
        # creating entry box for card number with validation for digits only
        card_entry = Entry(self.order_frame, width=16, borderwidth=3, font=self.win3.label_font,
                           fg=self.win3.input_color)
        card_entry.grid(row=17, column=1, sticky="W")

        # create expiration date entry
        order_card_exp = Label(self.order_frame, text="Expiration Date: ", font=self.win3.label_font,
                               fg=self.win3.color_font)
        order_card_exp.grid(row=17, column=2, sticky="E")
        # creating entry box for card expiration date with validation for digits only
        card_exp_entry = Entry(self.order_frame, width=4, borderwidth=3, font=self.win3.label_font,
                               fg=self.win3.input_color)
        card_exp_entry.grid(row=17, column=3, sticky="W")

        # create CVC entry
        order_card_cvv = Label(self.order_frame, text="CVV: ", font=self.win3.label_font, fg=self.win3.color_font)
        order_card_cvv.grid(row=18, column=0, sticky="E")
        # creating entry box for card expiration date with validation for digits only
        card_cvv_entry = Entry(self.order_frame, width=3, borderwidth=3, font=self.win3.label_font,
                               fg=self.win3.input_color)
        card_cvv_entry.grid(row=18, column=1, sticky="W")

        # BUTTONS for order window
        # button to open location and hours page
        location_hours = Button(self.order_frame, text="LOCATION & HOURS", padx=10, pady=10,
                                command=LOCATIONHOURSWINDOW, fg=self.win3.color_font, font=self.win3.button_font,
                                bg=self.win3.button_background)
        location_hours.grid(row=0, column=0)
        # creating button to close the order now window
        close_button = Button(self.order_frame, text="CLOSE", padx=30, pady=10, command=self.win3.destroy,
                              fg=self.win3.color_font, bg=self.win3.button_background, font=self.win3.button_font)
        # placing the button
        close_button.grid(row=0, column=3)
        # creating button to submit order
        submit = Button(self.order_frame, text="SUBMIT ORDER", command=receipt, font=self.win3.button_font,
                        fg=self.win3.color_font, bg=self.win3.button_background, padx=5, pady=10)
        submit.grid(row=30, column=3, sticky="NSEW")


def main():
    """ Main function of the application. """
    # setting TK for tkinter
    root = tk.Tk()
    # setting title for root base
    root.title("HarperSamanthaFinalProject")
    # calling main window class
    window = MAINWINDOW(root)
    # calling functions from main window
    window.load_images()
    window.display_images()
    # calling main loop to run
    root.mainloop()


if __name__ == '__main__':
    # calling main
    main()
