#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys, gi
from time import sleep
from datetime import datetime

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib

fnt = '"Sans 22"'
setmkup1 = "<span font_desc=" + fnt + ">"
setmkup2 = "</span>"
onsymbol = "■" # unicode u25A0
offsymbol = "□" # unicode u25A1
on = setmkup1 + onsymbol + setmkup2
off = setmkup1 + offsymbol + setmkup2
spc = setmkup1 + " " + setmkup2

class GridWindow(Gtk.Window):
	def __init__(self):
		super(GridWindow, self).__init__(title="Binclock-Gtk-Py")
		self.set_default_size(200, 150)
		self.set_decorated(False)
		self.set_icon_from_file("/usr/share/icons/hicolor/32x32/apps/binclock-gtk-py.png")
        
		self.D1 = Gtk.Label()
		self.C1 = Gtk.Label()
		self.B1 = Gtk.Label()
		self.A1 = Gtk.Label()
		self.D2 = Gtk.Label()
		self.C2 = Gtk.Label()
		self.B2 = Gtk.Label()
		self.A2 = Gtk.Label()
		self.D3 = Gtk.Label()
		self.C3 = Gtk.Label()
		self.B3 = Gtk.Label()
		self.A3 = Gtk.Label()
		self.D4 = Gtk.Label()
		self.C4 = Gtk.Label()
		self.B4 = Gtk.Label()
		self.A4 = Gtk.Label()
		self.D5 = Gtk.Label()
		self.C5 = Gtk.Label()
		self.B5 = Gtk.Label()
		self.A5 = Gtk.Label()
		self.D6 = Gtk.Label()
		self.C6 = Gtk.Label()
		self.B6 = Gtk.Label()
		self.A6 = Gtk.Label()
		
		spc1 = Gtk.Label()
		spc2 = Gtk.Label()
		spc3 = Gtk.Label()
		spc4 = Gtk.Label()
		spc5 = Gtk.Label()
		spc6 = Gtk.Label()
		spc7 = Gtk.Label()
		spc8 = Gtk.Label()
		
		spc1.set_markup(spc)
		spc2.set_markup(spc)
		spc3.set_markup(spc)
		spc4.set_markup(spc)
		spc5.set_markup(spc)
		spc6.set_markup(spc)
		spc7.set_markup(spc)
		spc8.set_markup(spc)
		
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		vbox.set_margin_start(4)
		vbox.set_margin_end(4)
		vbox.set_margin_bottom(4)
		self.add(vbox)
		
		hbox = Gtk.Box()
		vbox.set_center_widget(hbox)
		
		grid = Gtk.Grid()
		
		hbox.set_center_widget(grid)
		
		grid.add(self.D1)
		grid.attach(self.D2, 1, 0, 1, 1)
		grid.attach(spc1, 2, 0, 1, 1)
		grid.attach(self.D3, 3, 0, 1, 1)
		grid.attach(self.D4, 4, 0, 1, 1)
		grid.attach(spc2, 5, 0, 1, 1)
		grid.attach(self.D5, 6, 0, 1, 1)
		grid.attach(self.D6, 7, 0, 1, 1)
		
		grid.attach(self.C1, 0, 1, 1, 1)
		grid.attach(self.C2, 1, 1, 1, 1)
		grid.attach(spc3, 2, 1, 1, 1)
		grid.attach(self.C3, 3, 1, 1, 1)
		grid.attach(self.C4, 4, 1, 1, 1)
		grid.attach(spc4, 5, 1, 1, 1)
		grid.attach(self.C5, 6, 1, 1, 1)
		grid.attach(self.C6, 7, 1, 1, 1)

		grid.attach(self.B1, 0, 2, 1, 1)
		grid.attach(self.B2, 1, 2, 1, 1)
		grid.attach(spc5, 2, 2, 1, 1)
		grid.attach(self.B3, 3, 2, 1, 1)
		grid.attach(self.B4, 4, 2, 1, 1)
		grid.attach(spc6, 2, 2, 1, 1)
		grid.attach(self.B5, 6, 2, 1, 1)
		grid.attach(self.B6, 7, 2, 1, 1)
		
		grid.attach(self.A1, 0, 3, 1, 1)
		grid.attach(self.A2, 1, 3, 1, 1)
		grid.attach(spc7, 2, 3, 1, 1)
		grid.attach(self.A3, 3, 3, 1, 1)
		grid.attach(self.A4, 4, 3, 1, 1)
		grid.attach(spc8, 2, 3, 1, 1)
		grid.attach(self.A5, 6, 3, 1, 1)
		grid.attach(self.A6, 7, 3, 1, 1)
		
		self.timeout_id = GLib.timeout_add(1000, self.on_timeout, None)
		self.activity_mode = False
		
	def on_timeout(self, user_data):

		tm = datetime.today().strftime("%H%M%S")
		H1 = tm[0]
		H2 = tm[1]
		M1 = tm[2]
		M2 = tm[3]
		S1 = tm[4]
		S2 = tm[5]
		
		# HOUR 1
		if H1 == "0":
			self.D1.set_markup(off)
			self.C1.set_markup(off)
			self.B1.set_markup(off)
			self.A1.set_markup(off)
		elif H1 == "1":
			self.D1.set_markup(off)
			self.C1.set_markup(off)
			self.B1.set_markup(off)
			self.A1.set_markup(on)
		elif H1 == "2":
			self.D1.set_markup(off)
			self.C1.set_markup(off)
			self.B1.set_markup(on)
			self.A1.set_markup(off)
					
		# HOUR 2
		if H2 == "0":
			self.D2.set_markup(off)
			self.C2.set_markup(off)
			self.B2.set_markup(off)
			self.A2.set_markup(off)
		elif H2 == "1":
			self.D2.set_markup(off)
			self.C2.set_markup(off)
			self.B2.set_markup(off)
			self.A2.set_markup(on)
		elif H2 == "2":
			self.D2.set_markup(off)
			self.C2.set_markup(off)
			self.B2.set_markup(on)
			self.A2.set_markup(off)
		elif H2 == "3":
			self.D2.set_markup(off)
			self.C2.set_markup(off)
			self.B2.set_markup(on)
			self.A2.set_markup(on)
		elif H2 == "4":
			self.D2.set_markup(off)
			self.C2.set_markup(on)
			self.B2.set_markup(off)
			self.A2.set_markup(off)
		elif H2 == "5":
			self.D2.set_markup(off)
			self.C2.set_markup(on)
			self.B2.set_markup(off)
			self.A2.set_markup(on)
		elif H2 == "6":
			self.D2.set_markup(off)
			self.C2.set_markup(on)
			self.B2.set_markup(on)
			self.A2.set_markup(off)
		elif H2 == "7":
			self.D2.set_markup(off)
			self.C2.set_markup(on)
			self.B2.set_markup(on)
			self.A2.set_markup(on)
		elif H2 == "8":
			self.D2.set_markup(on)
			self.C2.set_markup(off)
			self.B2.set_markup(off)
			self.A2.set_markup(off)
		elif H2 == "9":
			self.D2.set_markup(on)
			self.C2.set_markup(off)
			self.B2.set_markup(off)
			self.A2.set_markup(on)
		
		# MINUTE 1
		if M1 == "0":
			self.D3.set_markup(off)
			self.C3.set_markup(off)
			self.B3.set_markup(off)
			self.A3.set_markup(off)
		elif M1 == "1":
			self.D3.set_markup(off)
			self.C3.set_markup(off)
			self.B3.set_markup(off)
			self.A3.set_markup(on)
		elif M1 == "2":
			self.D3.set_markup(off)
			self.C3.set_markup(off)
			self.B3.set_markup(on)
			self.A3.set_markup(off)
		elif M1 == "3":
			self.D3.set_markup(off)
			self.C3.set_markup(off)
			self.B3.set_markup(on)
			self.A3.set_markup(on)
		elif M1 == "4":
			self.D3.set_markup(off)
			self.C3.set_markup(on)
			self.B3.set_markup(off)
			self.A3.set_markup(off)
		elif M1 == "5":
			self.D3.set_markup(off)
			self.C3.set_markup(on)
			self.B3.set_markup(off)
			self.A3.set_markup(on)
		
		# MINUTE 2
		if M2 == "0":
			self.D4.set_markup(off)
			self.C4.set_markup(off)
			self.B4.set_markup(off)
			self.A4.set_markup(off)
		elif M2 == "1":
			self.D4.set_markup(off)
			self.C4.set_markup(off)
			self.B4.set_markup(off)
			self.A4.set_markup(on)
		elif M2 == "2":
			self.D4.set_markup(off)
			self.C4.set_markup(off)
			self.B4.set_markup(on)
			self.A4.set_markup(off)
		elif M2 == "3":
			self.D4.set_markup(off)
			self.C4.set_markup(off)
			self.B4.set_markup(on)
			self.A4.set_markup(on)
		elif M2 == "4":
			self.D4.set_markup(off)
			self.C4.set_markup(on)
			self.B4.set_markup(off)
			self.A4.set_markup(off)
		elif M2 == "5":
			self.D4.set_markup(off)
			self.C4.set_markup(on)
			self.B4.set_markup(off)
			self.A4.set_markup(on)
		elif M2 == "6":
			self.D4.set_markup(off)
			self.C4.set_markup(on)
			self.B4.set_markup(on)
			self.A4.set_markup(off)
		elif M2 == "7":
			self.D4.set_markup(off)
			self.C4.set_markup(on)
			self.B4.set_markup(on)
			self.A4.set_markup(on)
		elif M2 == "8":
			self.D4.set_markup(on)
			self.C4.set_markup(off)
			self.B4.set_markup(off)
			self.A4.set_markup(off)
		elif M2 == "9":
			self.D4.set_markup(on)
			self.C4.set_markup(off)
			self.B4.set_markup(off)
			self.A4.set_markup(on)
		
		# SECOND 1
		if S1 == "0":
			self.D5.set_markup(off)
			self.C5.set_markup(off)
			self.B5.set_markup(off)
			self.A5.set_markup(off)
		elif S1 == "1":
			self.D5.set_markup(off)
			self.C5.set_markup(off)
			self.B5.set_markup(off)
			self.A5.set_markup(on)
		elif S1 == "2":
			self.D5.set_markup(off)
			self.C5.set_markup(off)
			self.B5.set_markup(on)
			self.A5.set_markup(off)
		elif S1 == "3":
			self.D5.set_markup(off)
			self.C5.set_markup(off)
			self.B5.set_markup(on)
			self.A5.set_markup(on)
		elif S1 == "4":
			self.D5.set_markup(off)
			self.C5.set_markup(on)
			self.B5.set_markup(off)
			self.A5.set_markup(off)
		elif S1 == "5":
			self.D5.set_markup(off)
			self.C5.set_markup(on)
			self.B5.set_markup(off)
			self.A5.set_markup(on)
		
		# SECOND 2
		if S2 == "0":
			self.D6.set_markup(off)
			self.C6.set_markup(off)
			self.B6.set_markup(off)
			self.A6.set_markup(off)
		elif S2 == "1":
			self.D6.set_markup(off)
			self.C6.set_markup(off)
			self.B6.set_markup(off)
			self.A6.set_markup(on)
		elif S2 == "2":
			self.D6.set_markup(off)
			self.C6.set_markup(off)
			self.B6.set_markup(on)
			self.A6.set_markup(off)
		elif S2 == "3":
			self.D6.set_markup(off)
			self.C6.set_markup(off)
			self.B6.set_markup(on)
			self.A6.set_markup(on)
		elif S2 == "4":
			self.D6.set_markup(off)
			self.C6.set_markup(on)
			self.B6.set_markup(off)
			self.A6.set_markup(off)
		elif S2 == "5":
			self.D6.set_markup(off)
			self.C6.set_markup(on)
			self.B6.set_markup(off)
			self.A6.set_markup(on)
		elif S2 == "6":
			self.D6.set_markup(off)
			self.C6.set_markup(on)
			self.B6.set_markup(on)
			self.A6.set_markup(off)
		elif S2 == "7":
			self.D6.set_markup(off)
			self.C6.set_markup(on)
			self.B6.set_markup(on)
			self.A6.set_markup(on)
		elif S2 == "8":
			self.D6.set_markup(on)
			self.C6.set_markup(off)
			self.B6.set_markup(off)
			self.A6.set_markup(off)
		elif S2 == "9":
			self.D6.set_markup(on)
			self.C6.set_markup(off)
			self.B6.set_markup(off)
			self.A6.set_markup(on)

		return True

win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
