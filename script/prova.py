#!/usr/bin/env python3

'''
    Fai sfasare i tuoi amici mentre stanno svolgendo
    un lavoro serio(molto serio) al pc.
    ---------------------------------------
    Per divertiti ti occorre:
        + python 3
        + tkinter
        + sshpass & ssh
        + xmessage
        + chromium
'''

import tkinter
from os import system


class Application(tkinter.Frame):
    def __init__(self, master):
            master.title('Lo Sfasatore')
            tkinter.Frame.__init__(self, master)
            self.pack()
            self.createWidgets()

    def createWidgets(self):
            #Variabili dell'interfaccia
            self.varUser = tkinter.StringVar()
            self.varPwd = tkinter.StringVar()
            self.varIp = tkinter.StringVar()
            self.varMsg = tkinter.StringVar()
            self.varNum = tkinter.StringVar()
            self.varNum.set('1')

            #Sezioni
            self.frameInput = tkinter.LabelFrame(self, text='Host')
            self.frameOther = tkinter.LabelFrame(self, text='Se ti annoi')
            self.frameMsg = tkinter.LabelFrame(self, text='Messaggio')
            self.frameBrowser = tkinter.LabelFrame(self, text='Browser-mania')

            #Widget
            self.USER = tkinter.Entry(self.frameInput, textvariable=self.varUser)
            self.PWD = tkinter.Entry(self.frameInput, show='%', textvariable=self.varPwd)
            self.IP = tkinter.Entry(self.frameInput, textvariable=self.varIp)
            self.MSG = tkinter.Entry(self.frameMsg, textvariable=self.varMsg)
            self.NUM = tkinter.Entry(self.frameMsg, textvariable=self.varNum)
            self.QUIT = tkinter.Button(self.frameOther, text='Mi sono rotto', command=self.quit)
            self.SEND = tkinter.Button(self.frameMsg, text='Spedisci', command=self.sendMessage)
            self.NOTHING = tkinter.Button(self.frameOther, text='Clicca per non fare niente', command=None)
            self.GUY = tkinter.Button(self.frameBrowser, text='Epic Sax Guy', command=lambda: self.browser('guy'))
            self.GANDALF = tkinter.Button(self.frameBrowser, text='Epic Sax Gandalf', command=lambda: self.browser('gandalf'))
            self.PIRATE = tkinter.Button(self.frameBrowser, text='You are a pirate', command=lambda: self.browser('pirate'))
            self.SATTOH = tkinter.Button(self.frameBrowser, text='Sattoh', command=lambda: self.browser('sattoh'))

            #Disposizione dei widget
            tkinter.Label(self.frameInput, text='Utente:').grid(row=0, column=0)
            self.USER.grid(row=0, column=1)
            tkinter.Label(self.frameInput, text='Password:').grid(row=1, column=0)
            self.PWD.grid(row=1, column=1)
            tkinter.Label(self.frameInput, text='Indirizzo:').grid(row=2, column=0)
            self.IP.grid(row=2, column=1)
            self.frameInput.grid(row=0, column=0)

            self.QUIT.grid(row=0, column=0)
            self.NOTHING.grid(row=1, column=0)
            self.frameOther.grid(row=0, column=1)

            tkinter.Label(self.frameMsg, text='Testo:').grid(row=0, column=0)
            self.MSG.grid(row=0, column=1)
            tkinter.Label(self.frameMsg, text='Quanti?').grid(row=1, column=0)
            self.NUM.grid(row=1, column=1)
            self.SEND.grid(row=2, columnspan=2)
            self.frameMsg.grid(row=1, column=0)

            self.GUY.grid(row=0, column=0)
            self.GANDALF.grid(row=1, column=0)
            self.PIRATE.grid(row=2, column=0)
            self.SATTOH.grid(row=3, column=0)
            self.frameBrowser.grid(row=1, column=1)

            tkinter.Label(self, text='Questo programma è una cosa seria, molto seria...').grid(row=2, columnspan=2)

    def sendMessage(self):
        for _ in range(int(self.varNum.get())):
            system('sshpass -p %s ssh %s@%s "xmessage -display :0 %s" &' % (self.varPwd.get(), self.varUser.get(), self.varIp.get(), self.varMsg.get()))

    def browser(self, video):
        if video == 'guy':
            url = 'https://www.youtube.com/watch?v=kxopViU98Xo'
        elif video == 'gandalf':
            url = 'https://www.youtube.com/watch?v=Gy_1_bk2-7w'
        elif video == 'pirate':
            url = 'https://www.youtube.com/watch?v=IBH4g_ua5es'
        elif video == 'sattoh':
            url = 'https://www.youtube.com/watch?v=GLJ3n5uSrs8'

        system('sshpass -p %s ssh %s@%s "chromium --display :0 %s" &' % (self.varPwd.get(), self.varUser.get(), self.varIp.get(), url))

if __name__ == '__main__':
        root = tkinter.Tk()
        app = Application(master=root)
        app.mainloop()
        root.destroy()
