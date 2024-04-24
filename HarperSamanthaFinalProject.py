"""
Created by Samantha Harper
Last Modified 4.26.24
This program is for Elli-May's Smoked BBQ. It will allow users to view the hours, location, menu and complete an
order prior to visiting the food truck
"""
# importing tkinter
import tkinter
from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox


class MenuWindow:
    # The menu for Elli-May's Smoked BBQ will display all available products with pricing information.
    def __init__(self):
        # creating new window for menu
        self.win2 = Toplevel()
        # creating title for window
        self.win2.title("Elli-May's Menu")
        # set window size that is not resizeable.
        self.win2.resizable(False, False)
        # size of window
        self.win2.geometry("700x800")
        # boarder color
        self.win2.config(bg=color_font)
        # creating frame for details of menu to be placed in
        self.menu_frame = ttk.Frame(self.win2, borderwidth=5, relief="sunken")
        self.menu_frame.pack(padx=5, pady=5, fill="both", expand=True)
        self.menu_label = ttk.Label(self.menu_frame)

        # creating menu header
        menu_label = Label(self.menu_frame, text="Elli-May's MENU", font=top_font, fg=color_font)
        # placing menu header
        menu_label.grid(column=0, row=0, columnspan=4, sticky="NSEW")
        # creating menu font specs
        menu_font = Font(family='Helvetica', size=12)

        # setting sandwich section of menu
        sandwiches_label = Label(self.menu_frame, text="FAMOUS SANDWICHES", fg=color_font, font=label_font)
        sandwiches_label.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky="NSEW")

        # creating sandwiches and placing them on menu window
        # pork sliders
        pulled_pork_label = Label(self.menu_frame, text="BBQ Pulled Pork - 8.00", fg=color_font, font=menu_font)
        pulled_pork_label.grid(row=4, column=0, columnspan=2, sticky="NSEW")
        pulled_pork_details = Label(self.menu_frame, text=" Slow-roasted to perfection using\ncheery and apple wood",
                                    fg=color_font, font=sub_label_font)
        pulled_pork_details.grid(row=5, column=0, columnspan=2, sticky="NSEW")
        # slaw-py sliders
        slawpy_sliders_label = Label(self.menu_frame, text="Slaw-py Sliders - 10.00", fg=color_font, font=menu_font)
        slawpy_sliders_label.grid(row=4, column=2, columnspan=2, sticky="NSEW")
        slawpy_sliders_details = Label(self.menu_frame, text="BBQ Pork topped with our\nhomemade coleslaw",
                                       fg=color_font, font=sub_label_font)
        slawpy_sliders_details.grid(row=5, column=2, columnspan=2, sticky="NSEW")
        # beef brisket
        beef_brisket_sliders_label = Label(self.menu_frame, text="BBQ Beef Brisket - 11.00", fg=color_font,
                                           font=menu_font)
        beef_brisket_sliders_label.grid(row=6, column=0, columnspan=2, sticky="NSEW")
        brisket_sliders_details = Label(self.menu_frame, text="Low and slow-smoked BBQ Brisket\nserved slider style  ",
                                        fg=color_font, font=sub_label_font)
        brisket_sliders_details.grid(row=7, column=0, columnspan=2, sticky="NSEW")
        # wrangler
        wrangler_label = Label(self.menu_frame, text="Pork Wrangler - 9.50", fg=color_font, font=menu_font)
        wrangler_label.grid(row=6, column=2, columnspan=2, sticky="NSEW")
        wrangler_details = Label(self.menu_frame, text="Throw some O-rings on top of\nour pulled pork", fg=color_font,
                                 font=sub_label_font)
        wrangler_details.grid(row=7, column=2, sticky="NSEW", columnspan=2)
        # pork sliders
        pork_sliders_label = Label(self.menu_frame, text="BBQ Pork Sliders - 9.00",  fg=color_font, font=menu_font)
        pork_sliders_label.grid(row=8, column=0, columnspan=2, sticky="NSEW")
        pork_sliders_details = Label(self.menu_frame, text="Four of our Famous BBQ Pork Sliders", fg=color_font,
                                     font=sub_label_font)
        pork_sliders_details.grid(row=9, column=0, columnspan=2, sticky="NSEW")
        # the ringer
        ringer_label = Label(self.menu_frame, text="The Ringer - 11.50", fg=color_font, font=menu_font)
        ringer_label.grid(row=8, column=2, sticky="NSEW")
        ringer_details = Label(self.menu_frame, text="Brisket and O-Rings together", fg=color_font, font=sub_label_font)
        ringer_details.grid(row=9, column=2, columnspan=2, sticky="NSEW")
        # best of both worlds
        best_of_both_label = Label(self.menu_frame, text="Best of Both Worlds - 9.00", fg=color_font, font=menu_font)
        best_of_both_label.grid(row=10, column=0, columnspan=2, sticky="NSEW")
        best_of_both_details = Label(self.menu_frame, text="A combination of our pulled pork and\nbeef brisket on "
                                                           "a bun", fg=color_font, font=sub_label_font)
        best_of_both_details.grid(row=11, column=0, columnspan=2, sticky="NSEW", padx=5)
        # smoked chicken
        smoked_chicken_label = Label(self.menu_frame, text="Smoked Chicken - 9.00", fg=color_font, font=menu_font)
        smoked_chicken_label.grid(row=10, column=2, columnspan=2, sticky="NSEW")
        smoked_chicken_details = Label(self.menu_frame,
                                       text="Chicken smoked and shredded sauced\nwith our famous BBQ sauce on a bun",
                                       fg=color_font, font=sub_label_font)
        smoked_chicken_details.grid(row=11, column=2, columnspan=2, sticky="NSEW", padx=5)
        # BBQ brisket
        brisket_label = Label(self.menu_frame, text="BBQ Beef Brisket - 10.00", fg=color_font, font=menu_font)
        brisket_label.grid(row=12, column=0, columnspan=2, sticky="NSEW")
        brisket_details = Label(self.menu_frame, text="Slow-roasted beef brisket using cherry wood\nserved with "
                                                      "homemade BBQ sauce", fg=color_font, font=sub_label_font)
        brisket_details.grid(row=13, column=0, columnspan=2, sticky="NSEW", padx=5)
        # pulled chicken sliders
        chicken_sliders_label = Label(self.menu_frame, text="Chicken Sliders - 9.00", fg=color_font, font=menu_font)
        chicken_sliders_label.grid(row=12, column=2, columnspan=2, sticky="NSEW")
        chicken_sliders_details = Label(self.menu_frame, text="Our famous BBQ pulled chicken\nserved slider style",
                                        fg=color_font, font=sub_label_font)
        chicken_sliders_details.grid(row=13, column=2, columnspan=2, sticky="NSEW", padx=5)
        # slaw-py pork
        slawpy_pork_label = Label(self.menu_frame, text="Slaw-py Pork - 9.50", fg=color_font, font=menu_font)
        slawpy_pork_label.grid(row=14, column=0, columnspan=2, sticky="NSEW")
        slawpy_pork_details = Label(self.menu_frame, text="BBQ pulled pork topped with\nour homemade slaw",
                                    fg=color_font, font=sub_label_font)
        slawpy_pork_details.grid(row=15, column=0, columnspan=2, sticky="NSEW", padx=5)

        # creating tacos section of menu
        tacos_label = Label(self.menu_frame, text="TACOS", fg=color_font, font=label_font)
        tacos_label.grid(row=22, column=2, columnspan=3, rowspan=2, sticky="NSEW")
        taco_label_details = Label(self.menu_frame, text="Four tacos with your choice of toppings and salsa!",
                                   fg=color_font, font=sub_label_font)
        taco_label_details.grid(row=24, column=2, columnspan=2, sticky="NSEW")
        # brisket tacos
        brisket_tacos_label = Label(self.menu_frame, text="Brisket Tacos - 11.00",  fg=color_font, font=menu_font)
        brisket_tacos_label.grid(row=25, column=2, sticky="E")

        # Pork Tacos
        pork_tacos_label = Label(self.menu_frame, text="Pork Tacos - 9.00",  fg=color_font, font=menu_font)
        pork_tacos_label.grid(row=26, column=2, sticky="E")

        # Chicken Tacos
        chicken_tacos_label = Label(self.menu_frame, text="Chicken Tacos - 9.00",  fg=color_font, font=menu_font)
        chicken_tacos_label.grid(row=27, column=2, sticky="E")

        # creating side and drink portion of menu
        sides_and_drinks_label = Label(self.menu_frame, text="SIDES & DRINKS", fg=color_font, font=label_font)
        sides_and_drinks_label.grid(row=22, column=0, columnspan=2, rowspan=2, sticky="NSEW")
        # coleslaw
        coleslaw_label = Label(self.menu_frame, text="Coleslaw - 3.00", fg=color_font, font=menu_font)
        coleslaw_label.grid(row=25, column=0, sticky="W")
        # fries
        fries_label = Label(self.menu_frame, text="Fries - 3.00", fg=color_font, font=menu_font)
        fries_label.grid(row=24, column=0, sticky="W")
        # tator tots
        tator_label = Label(self.menu_frame, text="Tator Tots - 4.00", fg=color_font, font=menu_font)
        tator_label.grid(row=26, column=0, sticky="W")
        # potato salad
        pot_salad_label = Label(self.menu_frame, text="Potato Salad - 3.50", fg=color_font, font=menu_font)
        pot_salad_label.grid(row=28, column=0, sticky="W")
        # Onion Rings
        onion_rings_label = Label(self.menu_frame, text="Onion Rings - 4.00", fg=color_font, font=menu_font)
        onion_rings_label.grid(row=27, column=0, sticky="W")
        # bottled water
        water_label = Label(self.menu_frame, text="Bottled Water - 2.00", fg=color_font, font=menu_font)
        water_label.grid(row=24, column=1, sticky="W")
        # soda
        soda_label = Label(self.menu_frame, text="Bottled Pepsi Products - 2.00", fg=color_font, font=menu_font)
        soda_label.grid(row=25, column=1, sticky="W")

        # creating combo information
        combo_label = Label(self.menu_frame, text="MAKE ANY SANDWICH OR TACO A COMBO FOR JUST 2.00 MORE!",
                            fg=color_font, bg=color_background, font=label_font)
        combo_label.grid(row=29, column=0, columnspan=3, pady=5, padx=5, sticky="NSEW")
        combo_details = Label(self.menu_frame, text="Your choice of side and a drink!", fg=color_font,
                              font=sub_label_font, bg=color_background)
        combo_details.grid(row=30, column=0, columnspan=3, pady=5, sticky="NSEW")

        # Buttons!
        # button to location and hours page
        location_hours = Button(self.menu_frame, text="LOCATION & HOURS", padx=30, pady=10, command=LocationHoursWindow,
                                fg=color_font, font=button_font, bg=button_background)
        location_hours.grid(row=34, column=1)
        # button to order now page
        order = Button(self.menu_frame, text="ORDER NOW!", padx=5, pady=10, command=OrderNowWindow, fg=color_font,
                       bg=button_background, font=button_font)
        order.grid(row=0, column=0)
        # button to close window
        exit_button = Button(self.menu_frame, text="CLOSE", padx=35, pady=10, command=self.win2.destroy,
                             bg=button_background, font=button_font, fg=color_font)
        exit_button.grid(row=34, column=2)


class OrderNowWindow:
    def __init__(self):
        # creating new window for ordering
        self.win3 = Toplevel()
        # creating title for window
        self.win3.title("Order Now!")
        # set window size that is not resizeable.
        self.win3.resizable(False, False)
        # size of window
        self.win3.geometry("1000x800")
        # boarder color
        self.win3.config(bg=color_font)
        # setting input font color
        input_color = "Black"
        # creating frame for details
        self.order_frame = ttk.Frame(self.win3, borderwidth=5, relief="sunken")
        self.order_frame.pack(padx=5, pady=5, fill="both", expand=True)
        self.menu_label = ttk.Label(self.order_frame)

        # creating top label for ordering page
        order_label = Label(self.order_frame, text="Order NOW!", font=top_font, fg=color_font)
        # placing label
        order_label.grid(column=1, row=0, columnspan=2, sticky="NSEW", padx=10, pady=30)

        def receipt():
            """ the receipt function will validate input before displaying the order name, phone number, and
            meal details including price"""
            # creating variables for all entry fields for input to be validated before receipt is printed
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            phone_number = phone_number_entry.get()
            cardholder_first_name = cardholder_f_name_entry.get()
            cardholder_last_name = cardholder_l_name_entry.get()
            city = city_entry.get()
            state = state_entry.get()
            zip_code = zip_code_entry.get()
            card = card_entry.get()
            c_exp = card_exp_entry.get()
            c_cvv = card_cvv_entry.get()

            # creating if statements to display a specific error message if input is missing or invalid.
            if not only_letters(first_name):
                messagebox.showerror("Error", "First Name must be only letters")
            elif not only_letters(last_name):
                messagebox.showerror("Error", "Last Name must be only letters")
            elif not only_letters(cardholder_first_name):
                messagebox.showerror("Error", "Cardholder First Name must be only letters")
            elif not only_letters(cardholder_last_name):
                messagebox.showerror("Error", "Cardholder Last Name must be only letters")
            elif not only_letters(city):
                messagebox.showerror("Error", "City must be only letters")
            elif not only_letters(state):
                messagebox.showerror("Error", "State must be only letters")
            elif not only_numbers(phone_number):
                messagebox.showerror("Error", "Phone Number must be 10 numbers!")
            elif not only_numbers(card):
                messagebox.showerror("Error", "Card must be 16 numbers!")
            elif not only_numbers(zip_code):
                messagebox.showerror("Error", "Zip Code must be 5 numbers!")
            elif not only_numbers(c_exp):
                messagebox.showerror("Error", "Card Exp must be 4 numbers!")
            elif not only_numbers(c_cvv):
                messagebox.showerror("Error", "Card CVV must be 3 numbers!")
            else:
                # else statement to display a receipt message box if all input is valid
                receipt_message = (f"Thank you for your order! Elli-May will see you soon!\n"
                                   f"\n Name: {first_name_entry.get()} {first_name_entry.get()}"
                                   f"\n Phone Number: {phone_number_entry.get()} "
                                   f"\n Sandwich: {sandwich_selected.get()} "
                                   f"\n Taco: {taco_selected.get()} "
                                   f"\n Taco Toppings: {none_selected.get()} {pico_selected.get()} {cheddar_cheese.get()} "
                                   f"{sour_cream.get()} {pickled_onions.get()} {jack_cheese.get()}"
                                   f"\n Combo: {combo_selected.get()} "
                                   f"\n Side: {side_selected.get()} "
                                   f"\n Drink: {drink_selected.get()}\n"
                                   f"\n Sub Total: {sub_total} "
                                   f"\n Tax: {sales_tax} "
                                   f"\n Total: {meal_total}")
                messagebox.showinfo("Receipt", receipt_message)

        def only_letters(input_text):
            """ only letters function will validate input to ensure each only contains letters and is not left blank"""
            if input_text.isalpha() and len(first_name_entry.get()) > 0:
                return True
            elif input_text.isalpha() and len(last_name_entry.get()) > 0:
                return True
            elif input_text.isalpha() and len(cardholder_f_name_entry.get()) > 0:
                return True
            elif input_text.isalpha() and len(cardholder_l_name_entry.get()) > 0:
                return True
            elif input_text.isalpha() and len(city_entry.get()) > 0:
                return True
            elif input_text.isalpha() and len(state_entry.get()) > 0:
                return True
            else:
                return False

        # creating label for First Name entry
        order_first_name = Label(self.order_frame, text="First Name: ", font=label_font, fg=color_font)
        order_first_name.grid(row=3, column=0, sticky="E")
        # creating entry box for first name with validation for characters only
        first_name_entry = Entry(self.order_frame, width=20, borderwidth=3, font=label_font, fg=input_color)
        first_name_entry.grid(row=3, column=1, sticky="W")

        # creating label for Last Name entry
        order_last_name = Label(self.order_frame, text="Last Name: ", font=label_font, fg=color_font)
        order_last_name.grid(row=3, column=2, sticky="E")
        # creating entry box for last name with validation for characters only
        last_name_entry = Entry(self.order_frame, width=20, borderwidth=3, font=label_font, fg=input_color)
        last_name_entry.grid(row=3, column=3, sticky="W")

        def only_numbers(input_text):
            """only numbers function which will validate entry to only allow numbers and specified length"""
            if input_text.isdigit() and len(phone_number_entry.get()) == 10:
                return True
            elif input_text.isdigit() and len(card_entry.get()) == 16:
                return True
            elif input_text.isdigit() and len(zip_code_entry.get()) == 5:
                return True
            elif input_text.isdigit() and len(card_exp_entry.get()) == 4:
                return True
            elif input_text.isdigit() and len(card_cvv_entry.get()) == 2:
                return True
            else:
                return False

        # creating label for phone number entry
        order_phone_number = Label(self.order_frame, text="Phone Number: ", font=label_font, fg=color_font)
        order_phone_number.grid(row=4, column=0, sticky="E")
        # creating entry box for phone number with validation for digits only
        phone_number_entry = Entry(self.order_frame, width=10, borderwidth=3, font=label_font, fg=input_color)
        phone_number_entry.grid(row=4, column=1, sticky="W")

        # creating sandwich menu selection drop down
        # creating sandwich selection label
        select_sandwich = Label(self.order_frame, text="Sandwich: ", fg=color_font, font=label_font)
        select_sandwich.grid(row=6, column=0, sticky="E")
        # creating sandwich selection list
        sandwich_options = [
                            "No Sandwich",
                            "BBQ Pulled Pork",
                            "Slaw-py Sliders",
                            "BBQ Beef Brisket",
                            "Pork Wrangler",
                            "BBQ Pork Sliders",
                            "The Ringer",
                            "Best of Both Worlds",
                            "Smoked Chicken",
                            "BBQ Beef Brisket Sliders",
                            "Chicken Sliders",
                            "Slaw=py Pork"
                            ]
        # creating parallel list for sandwich prices
        sandwich_prices = [
            "0.00"
            "8.00",
            "10.00",
            "10.00",
            "9.50",
            "9.00",
            "11.50",
            "9.00",
            "9.00",
            "11.00",
            "9.00",
            "9.50"
        ]

        # declaring variable for sandwich_options list
        sandwich_selected = StringVar()
        # setting default value of list
        sandwich_selected.set(sandwich_options[0])
        # creating drop down menu for sandwiches
        self.drop = OptionMenu(self.order_frame, sandwich_selected, *sandwich_options)
        self.drop.config(fg=input_color, font=label_font)
        self.drop.grid(row=6, column=1, sticky="W", pady=5)

        # creating Taco selection Drop Down
        # creating taco selection label
        select_taco = Label(self.order_frame, text="Tacos: ", fg=color_font, font=label_font)
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
            "9.00",
        ]
        # declaring variable for taco_options list
        taco_selected = StringVar()
        # setting default value of list
        taco_selected.set(taco_options[0])
        # creating drop down menu for tacos
        self.drop = OptionMenu(self.order_frame, taco_selected, *taco_options)
        self.drop.config(fg=input_color, font=label_font)
        self.drop.grid(row=7, column=1, sticky="W", pady=5)

        # creating taco topping selection buttons

        # creating label for taco toppings
        topping_label = Label(self.order_frame, text="Taco Toppings:", font=label_font, fg=color_font)
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
        none_selected.set(none_selected.get())
        # declaring variable as string for pico option
        pico_selected = StringVar()
        pico_selected.set(pico_selected.get())
        # declaring variable as string for cheddar cheese option
        cheddar_cheese = StringVar()
        cheddar_cheese.set(cheddar_cheese.get())
        # declaring variable as string for sour cream option
        sour_cream = StringVar()
        sour_cream.set(sour_cream.get())
        # declaring variable as string for pickled onions option
        pickled_onions = StringVar()
        pickled_onions.set(pickled_onions.get())
        # declaring variable as string for jack cheese option
        jack_cheese = StringVar()
        jack_cheese.set(jack_cheese.get())

        # creating check buttons for each taco topping
        # check box for no toppings
        self.topping_options = Checkbutton(self.order_frame, text=topping_options[0], variable=none_selected,
                                           onvalue="No Toppings", offvalue="", fg=input_color, font=label_font)
        self.topping_options.deselect()
        self.topping_options.grid(row=8, column=1, sticky="W")
        # check box for pico topping
        self.topping_options = Checkbutton(self.order_frame, text=topping_options[1], variable=pico_selected,
                                           onvalue="Pico ", offvalue="", fg=input_color, font=label_font)
        self.topping_options.deselect()
        self.topping_options.grid(row=8, column=2, sticky="W")
        # check box for cheddar cheese
        self.topping_options = Checkbutton(self.order_frame, text=topping_options[2], variable=cheddar_cheese,
                                           onvalue="Cheddar Cheese ", offvalue="", fg=input_color, font=label_font)
        self.topping_options.deselect()
        self.topping_options.grid(row=9, column=1, sticky="W")
        # check box for sour cream
        self.topping_options = Checkbutton(self.order_frame, text=topping_options[3], variable=sour_cream,
                                           onvalue="Sour Cream ", offvalue="", fg=input_color, font=label_font)
        self.topping_options.deselect()
        self.topping_options.grid(row=9, column=2, sticky="W")
        # check box for pickled red onions
        self.topping_options = Checkbutton(self.order_frame, text=topping_options[4], variable=pickled_onions,
                                           onvalue="Pickled Red Onions ", offvalue="", fg=input_color, font=label_font)
        self.topping_options.deselect()
        self.topping_options.grid(row=10, column=1, sticky="W")
        # check boc for jack cheese
        self.topping_options = Checkbutton(self.order_frame, text=topping_options[5], variable=jack_cheese,
                                           onvalue="Jack Cheese ", offvalue="", fg=input_color, font=label_font)
        self.topping_options.deselect()
        self.topping_options.grid(row=10, column=2, sticky="W")

        # create check buttons for combo selection
        # creating label for combo option
        combo_label = Label(self.order_frame, text="Make your meal a combo: ", font=label_font, fg=color_font)
        combo_label.grid(row=11, column=0, sticky="W")

        # declaring variable for combo options
        combo_selected = StringVar()
        combo_selected.set(combo_selected.get())

        # creating check buttons for combo selection
        self.combo_options = Checkbutton(self.order_frame, text="Yes", variable=combo_selected,
                                         onvalue="Yes", offvalue="No", fg=input_color, font=label_font)
        self.combo_options.deselect()
        self.combo_options.grid(row=11, column=1, sticky="W")
        self.combo_options = Checkbutton(self.order_frame, text="No", fg=input_color, font=label_font)
        self.combo_options.deselect()
        self.combo_options.grid(row=11, column=2, sticky="W")

        # create side drop down
        select_side = Label(self.order_frame, text="Side: ", fg=color_font, font=label_font)
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
            "4.00",
        ]
        # declaring variable for side_options list
        side_selected = StringVar()
        # setting default value of list
        side_selected.set(side_options[0])
        # creating drop down menu for sides
        self.drop = OptionMenu(self.order_frame, side_selected, *side_options)
        self.drop.config(fg=input_color, font=label_font)
        self.drop.grid(row=12, column=1, sticky="W", pady=5)

        # create drink drop down
        select_drink = Label(self.order_frame, text="Drink: ", fg=color_font, font=label_font)
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
        # creating drop down menu for drinks
        self.drop = OptionMenu(self.order_frame, drink_selected, *drink_options)
        self.drop.config(fg=input_color, font=label_font)
        self.drop.grid(row=13, column=1, sticky="W", pady=5)

        # create cardholder first name input
        order_cardholder_f_name = Label(self.order_frame, text="Cardholder First Name: ", font=label_font, fg=color_font)
        order_cardholder_f_name.grid(row=14, column=0, sticky="E")
        # creating entry box for cardholder first name
        cardholder_f_name_entry = Entry(self.order_frame, width=20, borderwidth=3, font=label_font, fg=input_color)
        cardholder_f_name_entry.grid(row=14, column=1, sticky="W")
        # creating cardholders last name input
        order_cardholder_l_name = Label(self.order_frame, text="Cardholder Last Name: ", font=label_font,
                                        fg=color_font)
        order_cardholder_l_name.grid(row=14, column=2, sticky="E")
        # creating entry box for cardholder last name
        cardholder_l_name_entry = Entry(self.order_frame, width=20, borderwidth=3, font=label_font, fg=input_color)
        cardholder_l_name_entry.grid(row=14, column=3, sticky="W")

        # create address entry
        order_cardholder_address = Label(self.order_frame, text="Cardholder Address: ", font=label_font, fg=color_font)
        order_cardholder_address.grid(row=15, column=0, sticky="E")
        # creating entry box for address
        address = Entry(self.order_frame, width=20, borderwidth=3, font=label_font, fg=input_color)
        address.grid(row=15, column=1, sticky="W")
        # create city entry
        order_city = Label(self.order_frame, text="City: ", font=label_font, fg=color_font)
        order_city.grid(row=16, column=0, sticky="E")
        # creating entry box for city with validation for characters only
        city_entry = Entry(self.order_frame, width=20, borderwidth=3, font=label_font, fg=input_color)
        city_entry.grid(row=16, column=1, sticky="W")

        # create state entry
        order_state = Label(self.order_frame, text="State: ", font=label_font, fg=color_font)
        order_state.grid(row=15, column=2, sticky="E")
        # creating entry box for state with validation for characters only
        state_entry = Entry(self.order_frame, width=2, borderwidth=3, font=label_font, fg=input_color)
        state_entry.grid(row=15, column=3, sticky="W")

        # create zip code entry
        order_zip_code = Label(self.order_frame, text="Zip Code: ", font=label_font, fg=color_font)
        order_zip_code.grid(row=16, column=2, sticky="E")
        # creating entry box for zipcode with validation for digits only
        zip_code_entry = Entry(self.order_frame, width=5, borderwidth=3, font=label_font, fg=input_color)
        zip_code_entry.grid(row=16, column=3, sticky="W")

        # create card number entry
        order_card= Label(self.order_frame, text="Card Number: ", font=label_font, fg=color_font)
        order_card.grid(row=17, column=0, sticky="E")
        # creating entry box for card number with validation for digits only
        card_entry = Entry(self.order_frame, width=16, borderwidth=3, font=label_font, fg=input_color)
        card_entry.grid(row=17, column=1, sticky="W")

        # create expiration date entry
        order_card_exp = Label(self.order_frame, text="Expiration Date: ", font=label_font, fg=color_font)
        order_card_exp.grid(row=17, column=2, sticky="E")
        # creating entry box for card expiration date with validation for digits only
        card_exp_entry = Entry(self.order_frame, width=4, borderwidth=3, font=label_font, fg=input_color)
        card_exp_entry.grid(row=17, column=3, sticky="W")

        # create CVC entry
        order_card_cvv= Label(self.order_frame, text="CVV: ", font=label_font, fg=color_font)
        order_card_cvv.grid(row=18, column=0, sticky="E")
        # creating entry box for card expiration date with validation for digits only
        card_cvv_entry = Entry(self.order_frame, width=3, borderwidth=3, font=label_font, fg=input_color)
        card_cvv_entry.grid(row=18, column=1, sticky="W")

        # create subtotal display for receipt
        sub_total = float(0)
        sales_tax = float(.07)
        meal_total = float(0)

        # create tax display
        self.sub_total = sub_total
        self.sales_tax = sales_tax
        self.total = sub_total * sales_tax

        """ creating loop to calculate total price of order """

        # BUTTONS for order window
        # button to open location and hours page
        location_hours = Button(self.order_frame, text="LOCATION & HOURS", padx=10, pady=10,
                                command=LocationHoursWindow, fg=color_font, font=button_font, bg=button_background)
        location_hours.grid(row=0, column=0)
        # creating button to close the order now window
        close_button = Button(self.order_frame, text="CLOSE", padx=30, pady=10, command=self.win3.destroy,
                              fg=color_font, bg=button_background, font=button_font)
        # placing the button
        close_button.grid(row=0, column=3)
        # creating button to submit order
        submit = Button(self.order_frame, text="SUBMIT ORDER", command=receipt, font=button_font, fg=color_font,
                        bg=button_background, padx=5, pady=10)
        submit.grid(row=30, column=3, sticky="NSEW")


class LocationHoursWindow:
    # this window will display the location of food truck and hours of operation
    def __init__(self):
        # creating new window for hours and location
        self.win = Toplevel()
        # creating title for window
        self.win.title("Location & Hours")
        # set window size that is not resizeable.
        self.win.resizable(False, False)
        # size of window
        self.win.geometry("650x400")
        # boarder color
        self.win.config(bg=color_font)
        # creating frame for details
        self.frame = ttk.Frame(self.win)
        self.frame.pack(padx=5, pady=5, fill="both", expand=True)
        self.label = ttk.Label(self.frame)

        # setting title for window
        self.win.title("Elli-May's Smoked BBQ")

        # creating top label for menu
        location_label = Label(self.frame, text="Location & Hours", fg=color_font)
        location_label.config(font=top_font)
        # placing label
        location_label.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="NSEW")

        # creating label for food truck address
        address_label = Label(self.frame, text="Location: 322 E Kirkwood Bloomington, IN 47408", fg=color_font,
                              font=label_font)
        address_label.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        # creating hours chart
        hours_label = Label(self.frame, text="%-10s" % "HOURS", fg=color_font, font=label_font)
        hours_label.grid(row=3, column=1, columnspan=3, pady=10, padx=5, sticky="NSEW")
        # creating monday hours
        monday = Label(self.frame, text="%10s" % "Monday:", fg=color_font, font=label_font)
        monday.grid(row=4, column=1)
        mon_hours = Label(self.frame, text="%5s" % "CLOSED", fg=color_font, font=label_font)
        mon_hours.grid(row=4, column=2)
        # creating tuesday hours
        tuesday = Label(self.frame, text="%11s" % "Tuesday:", fg=color_font, font=label_font)
        tuesday.grid(row=5, column=1)
        tue_hours = Label(self.frame, text="%10s" % "4PM - 1AM", fg=color_font, font=label_font)
        tue_hours.grid(row=5, column=2)
        # creating wednesday hours
        wednesday = Label(self.frame, text="%18s" % "Wednesday:", fg=color_font, font=label_font)
        wednesday.grid(row=6, column=1)
        wed_hours = Label(self.frame, text="%10s" % "4PM - 1AM", fg=color_font, font=label_font)
        wed_hours.grid(row=6, column=2)
        # creating thursday hours
        thursday = Label(self.frame, text="%13s" % "Thursday:", fg=color_font, font=label_font)
        thursday.grid(row=7, column=1)
        thur_hours = Label(self.frame, text="%10s" % "4PM - 1AM", fg=color_font, font=label_font)
        thur_hours.grid(row=7, column=2)
        # creating friday hours
        friday = Label(self.frame, text="%8s" % "Friday:", fg=color_font, font=label_font)
        friday.grid(row=8, column=1)
        fri_hours = Label(self.frame, text="%10s" % "4PM - 1AM", fg=color_font, font=label_font)
        fri_hours.grid(row=8, column=2)
        # creating saturday hours
        saturday = Label(self.frame, text="%13s" % "Saturday:", fg=color_font, font=label_font)
        saturday.grid(row=9, column=1)
        sat_hours = Label(self.frame, text="%10s" % "4PM - 1AM", fg=color_font, font=label_font)
        sat_hours.grid(row=9, column=2)

        # placing exit button
        exit_button = Button(self.frame, text="CLOSE", padx=35, pady=10, command=self.win.destroy,
                             bg=button_background, font=button_font, fg=color_font)
        exit_button.grid(row=11, column=1, pady=5)
        # placing menu button
        menu = Button(self.frame, text="MENU", padx=35, pady=10, command=MenuWindow, fg=color_font,
                      bg=button_background,
                      font=button_font)
        menu.grid(row=11, column=2)
        # placing order now button
        order = Button(self.frame, text="ORDER NOW!", padx=5, pady=10, command=OrderNowWindow, fg=color_font,
                       bg=button_background,
                       font=button_font)
        order.grid(row=0, column=0)


class MainWindow:
    # this is the main window of application
    def __init__(self, master):
        self.master = master
        # creating title for window
        self.master.title("Elli-May's Smoked BBQ")
        # setting window size
        self.master.geometry('1050x500')
        # setting window to not be resized by user
        self.master.resizable(False, False)
        # setting background color
        self.master.configure(background=color_background)
        # setting window font and size
        title_font = Font(family="Helvetica", size=20, weight="bold")

        # creating title for main window
        title = Label(root, text="%70s" % "Elli-May's Smoked BBQ", fg=color_font, bg=color_background, font=title_font)
        title.grid(row=0, column=0, columnspan=2, pady=20, sticky=W)

        # creating location and hours button
        location_button = Button(self.master, text="LOCATION & HOURS", padx=30, pady=12, command=LocationHoursWindow,
                                 fg=color_font, bg=button_background, font=button_font)
        location_button.grid(row=5, column=1, padx=10, pady=10, sticky=W)
        # creating menu button
        menu_button = Button(self.master, text="MENU", padx=84, pady=10, command=MenuWindow, fg=color_font,
                             bg=button_background,
                             font=button_font)
        # placing button
        menu_button.grid(row=6, column=1, padx=10, pady=10, sticky=W)
        # creating order now button
        order_button = Button(self.master, text="ORDER NOW!", padx=55, pady=10, command=OrderNowWindow, fg=color_font,
                              bg=button_background, font=button_font)
        order_button.grid(row=7, column=1, padx=10, pady=10, sticky=W)
        # creating close application button
        close_button = Button(self.master, text="CLOSE", padx=5, pady=10, command=self.master.destroy, fg=color_font,
                              bg=button_background, font=button_font)
        # placing the button
        close_button.grid(row=0, column=2, pady=10, padx=5, sticky=E)


# creating root as tkinter TK for operation
root = tkinter.Tk()
# setting font color
color_font = "Navy"
# setting background color
color_background = "light grey"
# setting label background color
label_background = "light grey"
# creating label font
label_font = ("Helvetica", 15)
# creating a smaller font for sub labels throughout the program
sub_label_font = Font(font="Helvetica 10 italic")
# setting button details
button_background = "grey"
button_font = Font(root, "Helvetica", size=18)
# setting font for titles on window
top_font = Font(family="Helvetica", size=25, weight="bold")

# inserting and placing the slaw-py sandwich photo
sandwich_img = PhotoImage(file="EM_Sandwich.png")
sandwich_label = Label(root, image=sandwich_img)
sandwich_label.grid(row=2, column=0, padx=5, sticky=W)
# text for photo
sandwich_text = Label(root, text="Slaw-py Sliders", font=sub_label_font, bg=color_background, fg=color_font,
                      borderwidth=3)
sandwich_text.grid(row=3, column=0, padx=5, sticky=S)
# inserting and placing the onion rings photo
rings_img = PhotoImage(file="EM_Orings.png")
rings_label = Label(root, image=rings_img)
rings_label.grid(row=2, column=1, padx=5, sticky=W)
rings_text = Label(root, text="O-Rings", font=sub_label_font, bg=color_background, fg=color_font, borderwidth=3)
rings_text.grid(row=3, column=1, sticky=S)
# inserting and placing the pulled chicken photo
chickens_img = PhotoImage(file="EM_Chicken.png")
chickens_label = Label(root, image=chickens_img)
chickens_label.grid(row=2, column=2, padx=5, sticky=W)
chickens_text = Label(root, text="Pulled Chicken", font=sub_label_font, bg=color_background, fg=color_font,
                      borderwidth=3)
chickens_text.grid(row=3, column=2, sticky=S)
# creating main window
window = MainWindow(root)
# calling program
root.mainloop()
