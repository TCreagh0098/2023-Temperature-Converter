from tkinter import *


class Converter:

    def __init__(self):

        # initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        # common format for all buttons
        # arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # set up GUI frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Convertor",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and " \
                       "then press one of the buttons to convert " \
                       "it from Centigrade to Fahrenheit."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wrap=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text="",
                                fg="#9C0000")
        self.temp_error.grid(row=3)

        # conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame,
                                        text="To Celsius",
                                        bg="#990099",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        command=self.to_celsius)
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_farenheit_button = Button(self.button_frame,
                                          text="To Farenheit",
                                          bg="#009900",
                                          fg=button_fg,
                                          font=button_font, width=12)
        self.to_farenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_info_button = Button(self.button_frame,
                                          text="Help / Info",
                                          bg="#CC6600",
                                          fg=button_fg,
                                          font=button_font, width=12)
        self.to_help_info_button.grid(row=1, column=0, padx=5, pady=5)

        self.to_history_export_button = Button(self.button_frame,
                                               text="History / Export",
                                               bg="#004C99",
                                               fg=button_fg,
                                               font=button_font, width=12,
                                               state=DISABLED)

        self.to_history_export_button.grid(row=1, column=1, padx=5, pady=5)

# checks user input amd if it's valid, converts temperature
    def check_temp(self, min_value):

        has_error = "no"

        # check that user has entered a valid number...

        response = self.temp_entry.get()

        try:
            response = float(response)

            if response < min_value:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        # sets var_has_error so that entry box and
        # labels can be correctly formatted by formatting function
        if has_error == "yes":
            error = "Please enter a number greater " \
                    "than {}".format(min_value)

            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            return "invalid"

        # if we have no errors...
        else:
            # set to 'no' in case of previous errors
            self.var_has_error.set("no")

            # return number to be converted and
            # enable history button
            self.to_history_export_button.config(state=NORMAL)
            return response

    # check temperature is more than -459 and convert it
    def to_celsius(self):
        to_convert = self.check_temp(-459)

        if to_convert != "invalid":
            # do calculation
            self.var_feedback.set("Converting {} to "
                                  "Celsius: ".format(to_convert))
        self.output_answer()

    # shows user output and clears entry widget
    # ready for next calculation
    def output_answer(self):
        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()

        if has_errors == "yes":
            # red text, pink entry box
            self.temp_error.config(fg="#9C0000")
            self.temp_entry.config(bg="#F8CECC")

        else:
            self.temp_error.config(fg="#004C00")
            self.temp_entry.config(bg="#FFFFFF")

        self.temp_error.config(text=output)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
