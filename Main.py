import tkinter
import customtkinter
import os
from PowerPoint import generate_presentation
from QRcodeGenerate import generate_code_qr
from model import generate_image
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Hackathon2024 - СyberMen")
        self.geometry(f"{400}x{400}")
        self.resizable(False, False)

        # configure grid layout
        self.grid_columnconfigure(1, weight=1)

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Введить запрос для генерации: ")
        self.entry.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(20, 10), sticky="nsew")

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=1, column=1, padx=(20, 20), sticky="w")
        self.radio_var = tkinter.IntVar(value=0)
        self.radio_var.trace_add("write", self.update_entryURL_visibility)  # Add trace to variable
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Доп. функция:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, text="Отсутствует",
                                                           value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, text="С кнопкой",
                                                           value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, text="С QR-кодом",
                                                           value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.combocheckbox_frame = customtkinter.CTkFrame(self)
        self.combocheckbox_frame.grid(row=1, column=2, padx=(20, 20),  sticky="n")

        listStyle = [
            "Arial",
            "Times New Roman",
            "Calibri",
            "Verdana",
            "Segoe UI",
            "Corbel",
            "Palatino",
            "Garamond",
            "Tahoma",
            "Century Gothic"
        ]

        self.label_combocheckbox = customtkinter.CTkLabel(master=self.combocheckbox_frame, text="Настройка генерации:")
        self.label_combocheckbox.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")

        self.combobox_1 = customtkinter.CTkComboBox(master=self.combocheckbox_frame, values=listStyle)
        self.combobox_1.grid(row=1, column=0, pady=(10, 10), padx=20, sticky="n")


        self.switch_1 = customtkinter.CTkSwitch(master=self.combocheckbox_frame, text="Скринсейвер")
        self.switch_1.grid(row=2, column=0, pady=(10, 10), padx=10, sticky="n")
        # self.switch_2 = customtkinter.CTkSwitch(master=self.combocheckbox_frame, text="")
        # self.switch_2.grid(row=3, column=0, pady=(10, 10), padx=10, sticky="n")


        self.entryURL = customtkinter.CTkEntry(self, placeholder_text="Введите URL: ")
        self.entryURL.grid(row=3, column=1, columnspan=2, padx=(20, 20), pady=(10, 0), sticky="nsew")
        self.entryURL.grid_remove()  # Initially hide the URL entry

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2,
                                                     text_color=("gray10", "#DCE4EE"), text = "Генерировать", command=self.on_button_click)
        self.main_button_1.grid(row=4, column=1, columnspan=2, padx=(20, 20), pady=(10, 0), sticky="nsew")

    def update_entryURL_visibility(self, *args):
        if self.radio_var.get() in [1, 2]:  # Show entryURL for "С кнопкой" or "С QR-кодом"
            self.entryURL.grid()
        else:
            self.entryURL.grid_remove()

    def on_button_click(self):
        main_entry_value = self.entry.get()
        prompt = f'Фоновая картинка без текста для баннера на тему "{main_entry_value}"'
        switch_1_value = self.switch_1.get()
        if switch_1_value==1:
            root = Tk()
            root.withdraw()  # Скрываем основное окно
            file_path = asksaveasfilename(defaultextension=".jpg", filetypes=[("Image files", "*.jpg")])
            if file_path:
                image_name = file_path.split('/')[-1]
                dir = "/".join(file_path.split('/')[:-1])
                generate_image(prompt, dirr=dir, name=image_name, width=1920, height=1080)
                print(f"Картинка сохранена по пути: {file_path}")
            else:
                print("Сохранение отменено пользователем")  
            return
        generate_image(prompt, name='1', width=1024, height=1024)
        generate_image(prompt, name='2', width=1024, height=1024)
        generate_image(prompt, name='3', width=1024, height=1024)
        url_value = self.entryURL.get() if self.radio_var.get() in [1, 2] else None
        combobox_value = self.combobox_1.get()
        
        # switch_2_value = self.switch_2.get()
        
        if self.radio_var.get() == 1:
            generate_presentation(main_entry_value, combobox_value, str(switch_1_value), url_value)
        elif self.radio_var.get() == 2:
            generate_code_qr(url_value)
            url_value = "./res/qr-code.png"
            generate_presentation(main_entry_value, combobox_value, str(switch_1_value), url_value)
        else :
            url_value = None
            generate_presentation(main_entry_value, combobox_value, str(switch_1_value), url_value)
        



if __name__ == "__main__":
    app = App()
    app.mainloop()
