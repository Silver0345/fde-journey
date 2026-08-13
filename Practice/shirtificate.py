'''In a file called shirtificate.py, implement a program that prompts the user
for their name and outputs, using fpdf2, a CS50 shirtificate PDF customized
with that name, per shirtificate.py's specification:
Portrait orientation, A4 format, "CS50 Shirtificate" centered at the top,
shirtificate.png centered horizontally, and the user's name in white text
on top of the shirt.
'''

from fpdf import FPDF


def generate_shirtificate(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("helvetica", style="B", size=24)
    pdf.cell(w=0, h=20, text="CS50 Shirtificate", align="C")

    pdf.image("shirtificate.png", x=20, y=40, w=170)

    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(20, 100)
    pdf.cell(w=170, h=20, text=f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


def main():
    name = input("Name: ")
    generate_shirtificate(name)


if __name__ == "__main__":
    main()
