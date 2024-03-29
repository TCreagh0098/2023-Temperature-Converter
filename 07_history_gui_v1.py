from tkinter import *
from functools import partial  # to prevent unwanted windows


class Converter:

    def __init__(self):
        # common format for all buttons
        # arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # five item list
        # self.all_calculations = ['0 F° is -18 C°', '0 C° is 3 F°',
        #                          '30 F° is -1 C°', '30 C° is 57 F°',
        #                          '40 F° is 4 C°']

        # six item list
        self.all_calculations = ['0 F° is -18 C°', '0 C° is 3 F°',
                                 '30 F° is -1 C°', '30 C° is 57 F°',
                                 '40 F° is 4 C°', '100 C° is 212 F°']

        # set up GUI frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)

        self.to_history_export_button = Button(self.button_frame,
                                               text="History / Export",
                                               bg="#004C99",
                                               fg=button_fg,
                                               font=button_font, width=12,
                                               state=DISABLED,
                                               command=self.to_history)
        self.to_history_export_button.grid(row=1, column=1, padx=5, pady=5)

        # remove when integrating!
        self.to_history_export_button.config(state=NORMAL)

    def to_history(self):
        HistoryExport(self)


class HistoryExport:

    def __init__(self, partner):
        # setup dialogue box and background colour
        background = "#f0f0f0"
        self.history_box = Toplevel()

        # disable help button
        partner.to_history_export_button.config(state=DISABLED)

        # if users press cross at top, closes help and
        # 'releases' help button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, width=300, height=200,
                                   bg=background)

        self.history_frame.grid()

        self.history_heading_label = Label(self.history_frame, bg=background,
                                           text="History / Export",
                                           font=("Arial", "14", "bold"))
        self.history_heading_label.grid(row=0)

        # history text and label
        hist_text = "Below are your recent calculations - " \
                    "showing 3 / 3 calculations. " \
                    "All calculations are shown to the nearest degree"
        self.text_instructions_label = Label(self.history_frame,
                                             text=hist_text,
                                             width=45, justify="left",
                                             wraplength=300,
                                             padx=10, pady=10)
        self.text_instructions_label.grid(row=1)

        self.all_calcs_label = Label(self.history_frame,
                                     text="calculations go here",
                                     padx=10, pady=10, bg="#ffe6cc",
                                     width=40, justify="left")
        self.all_calcs_label.grid(row=2)

        # instructions for saving files
        save_text = "Either choose a custom file name (and push " \
                    "<Export>) or simply push <Export> to save your " \
                    "calculations in a text file. If the " \
                    "filename already exists, it will be overwritten!"
        self.save_instructions_label = Label(self.history_frame,
                                             text=save_text,
                                             wraplength=300,
                                             justify="left", width=40,
                                             padx=10, pady=10)
        self.save_instructions_label.grid(row=3)

        # filename entry widget, white background to start
        self.filename_entry = Entry(self.history_frame,
                                    font=("Arial", "14"),
                                    bg="#ffffff", width=25)
        self.filename_entry.grid(row=4, padx=10, pady=10)

        self.filename_error_label = Label(self.history_frame,
                                          text="Filename error goes here:",
                                          fg="#9C0000",
                                          font=("Arial", "12", "bold"))
        self.filename_error_label.grid(row=5)

        self.button_frame = Frame(self.history_frame)
        self.button_frame.grid(row=6)

        self.export_button = Button(self.button_frame,
                                    font=("Arial", "12", "bold"),
                                    text="Export", bg="#004C99",
                                    fg="#FFFFFF", width=12)
        self.export_button.grid(row=0, column=0, padx=10, pady=10)

        self.dismiss_button = Button(self.button_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#666666",
                                     fg="#FFFFFF", width=12,
                                     command=partial(self.close_history,
                                                     partner))
        self.dismiss_button.grid(row=0, column=1, padx=10, pady=10)

    # closes help dialogue (used by button and x at top of dialogue)
    def close_history(self, partner):
        # put help button back to normal...
        partner.to_history_export_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    Converter()
    root.mainloop()
