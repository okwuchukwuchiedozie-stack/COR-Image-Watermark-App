from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os



def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

    if not file_path:
        return

    try:
        original_image = Image.open(file_path)

    except Exception as e:
        messagebox.showerror("Error", f"Could not open image:\n{e}")
        return

    else:
        watermarked = original_image.copy()
        draw = ImageDraw.Draw(watermarked)

        text = "@COR_CARES"

        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except OSError:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]

        padding = 20
        x = (watermarked.width - text_w) // 2
        y = watermarked.height - text_h - padding

        draw.text((x, y), text, fill=(255, 255, 255, 180), font=font)

        preview = watermarked.copy()
        preview.thumbnail((500, 350))

        photo = ImageTk.PhotoImage(preview)

        canvas.delete("all")
        canvas.create_image(0, 0, image=photo, anchor=NW)
        canvas.image = photo

        base = os.path.basename(file_path)
        name, ext = os.path.splitext(base)

        output_name = f"{name}_watermarked.png"

        os.makedirs("outputs", exist_ok=True)
        output_path = os.path.join("outputs", output_name)

        watermarked.save(output_path)

        messagebox.showinfo(
            "Success",
            f"Watermark added automatically!\nSaved as {output_path}"
        )


window = Tk()
window.title("COR Image Water App")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


canvas = Canvas(bg="white", width=500, height=350)
canvas.grid(column=1, row=0)

upload_button = Button(text="Upload Image", command=upload_image)
upload_button.grid(column=1, row=1)



window.mainloop()