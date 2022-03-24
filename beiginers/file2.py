import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)
logo = Image.open('')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


def open_file():
    browse_text.set("loading....")
    file = askopenfile(parent=root, mode="rb", title="choose a file ", filetype=[("Pdf  file", "*.pdf")])

    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        print(page_content)

        # text box
        text_box = tk.Text(root, padx=10, pady=10)
        text_box.insert(1.0,page_content)
        text_box.grid(column=1,row=3)


# instruction

instruction = tk.Label(root, text="select a pdf file on the computer to "
                                  "extract its text", font="Raleway")
instruction.grid(columnspan=3, column=0, row=1)

# brows button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), font="Raleway", bg="#20bebe",
                       fg="white", width=20)
browse_text.set("Browse")
browse_btn.grid(row=2, column=1)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()
