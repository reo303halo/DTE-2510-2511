from tkinter import *

class TemperatureConverter:
    def __init__(self):
        window = Tk()
        window.title("Celsius To Fahrenheit")
        window.geometry("400x400")
        window.resizable(0, 0)

        frame = Frame(window).pack() # Setter frame inn i vindu

        self.celcius = StringVar()
        Entry(frame, textvariable = self.celcius).pack() # Alternativ: .grid()

        Button(frame, text = "Convert", command = self.convert).pack()

        self.resultLabel = Label(frame)
        self.resultLabel.pack()
        # .pack() kan gjøres på egen linje slik som dette.
        # Om du gjør du bruker .pack() på egen linje eller ikke vil ikke gjøre noe forskjell,
        # annet enn at koden vil se annerledes ut (noen ganger ønsker man det ene over det andre for ryddighet => Opp til deg).
    

        window.mainloop()

    def convert(self):
        celsius = float(self.celcius.get())
        fahrenheit = (celsius * 9/5) + 32
        self.resultLabel.config(text = f"{fahrenheit} Fahrenheit")


def main():
    TemperatureConverter()

if __name__ == "__main__":
    main()