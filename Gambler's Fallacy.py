import random as ra
from tkinter import Frame, Text, Button, Tk, END, Label
from collections import deque


class Application(Frame):
  def __init__(self, master):
    """This initializes the frame"""
    super().__init__(master)
    self.bank = 300
    self.total_bet = ''
    self.runs = 20
    self.choice = 13
    self.result_list = deque(maxlen=20)
    self.grid()
    self.create_features()
    self.money_box.insert(0.0, self.bank)
    self.bet_box.insert(0.0, self.total_bet)
    self.setup()
    

  def create_features(self):
    '''Method that creates and places all the features'''
    content = ['Reset', 'C', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in range(7, 11):
      for col in range(3):
        b = content.pop()
        lbl = Button(self, text=b, command = lambda inp=b : self.input_feed(inp))
        lbl.grid(row=row, column=col, sticky='nsew')


    self.money_lbl = Label(self, text = 'Your money')
    self.money_lbl.grid(row = 3, column = 0, columnspan = 3)
    
    self.textentry = Text(self, width = 26, height=4)
    self.textentry.grid(row = 1, column = 0, columnspan=4, sticky = 'w', padx=5, pady=5)

    self.money_box = Text(self, width = 26, height=1)
    self.money_box.grid(row = 4, column = 0, columnspan=3, sticky = 'w', padx=5, pady=5)

    self.bet_lbl = Label(self, text = "Your bet")
    self.bet_lbl.grid(row = 5, column = 0, columnspan = 3)

    self.bet_box = Text(self, width = 26, height=1)
    self.bet_box.grid(row = 6, column = 0, columnspan=4, sticky = 'w', padx=5, pady=5)

    self.spin_lbl = Label(self, text = 'Spin the wheel!')
    self.spin_lbl.grid(row = 12, column = 0, columnspan = 3)

    self.start_button1 = Button(self, text = '1x', command = lambda imp = 1: self.spin_wheel(imp))
    self.start_button1.grid(row = 13, column = 0)

    self.start_button5 = Button(self, text = '5x', command = lambda imp = 5: self.spin_wheel(imp))
    self.start_button5.grid(row = 13, column = 1)

    self.start_button35 = Button(self, text = '35x', command = lambda imp = 35: self.spin_wheel(imp))
    self.start_button35.grid(row = 13, column = 2)


  def setup(self):
    '''Sets up the first 20 numbers'''
    x = [ra.randint(1,38) for _ in range(20)]
    self.textentry.delete(0.0, END)
    for i in range(20):
      spun = ra.choice(range(1,38))
      self.textentry.insert(END, ' ' +  str(spun))


  def clear(self):
    '''Removes the last entered number'''
    self.total_bet = ''
  

  def spin_wheel(self, arg):
    '''Spins the roulette wheel and saves result in textbox'''
    def spinnit():
      for i in range(self.runs):
        self.bank -= int(self.total_bet)
        self.money_box.delete(0.0, END)
        self.money_box.insert(0.0, self.bank)
        if int(self.bank) <= 0:
          self.bet_box.delete(0.0, END)
          self.bet_box.insert(0.0, "No more money! Hit reset")
          break
        else:
          spin = ra.choice(range(1,38))
          if spin == 13:
            self.bank += (35*int(self.total_bet))
        self.result_list.append(spin)
    if self.total_bet == "":
      self.bet_box.delete(0.0, END)
      self.bet_box.insert(0.0, "Please enter a bet")
    elif self.bank <= 0:
      self.bet_box.delete(0.0, END)
      self.bet_box.insert(0.0, "Stop gambling!")
    else:
      spinnit()

    self.textentry.delete(0.0, END)
    self.textentry.insert(0.0, list(self.result_list))


  def reset(self):
    '''Resets game to original settings'''
    self.total_bet = ''
    self.bank = 300

    self.bet_box.delete(0.0, END)
    self.money_box.delete(0.0, END)
    
    self.bet_box.insert(0.0, self.total_bet)
    self.money_box.insert(0.0, self.bank)

    self.setup()


  def bet_entry(self, arg):
    '''Used for entering the bet size'''
    self.total_bet = str(self.total_bet) + str(arg)
    
    if int(self.total_bet) > self.bank:
      self.reset()


  def input_feed(self, arg):
    '''Receives all inputs from buttons and delegates'''
    if arg in list(range(10)):
      self.bet_entry(str(arg))
    elif arg == 'Reset':
      self.reset()
    elif arg == 'C':
      self.clear()
      
    self.bet_box.delete(0.0, END)
    self.bet_box.insert(0.0, self.total_bet)


root = Tk()
root.title("Gambler's Fallacy")
root.geometry("300x400")
root = Application(root)
root.mainloop()