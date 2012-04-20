#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import pango

class Checkers:
	def delete_event(self, widget, event, data=None):
		print "delete event occurred"
		return False

	def destroy(self, widget, data=None):
		print "destroy signal occurred"
		gtk.main_quit()

	def draw_pixbuf(self, widget, event, path):
		pixbuf = gtk.gdk.pixbuf_new_from_file(path)
		widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0,0)

	def clicked_building_callback(self, widget, event):
		if (event.type == gtk.gdk.BUTTON_PRESS and event.button == 1):
			print widget.kind


	def show_city(self, kind):
		# set fixed
		fixed = gtk.Fixed()
		self.window.add(fixed)
		# set hint label
		hint = gtk.Label()
		hint.modify_font(pango.FontDescription('FreeSans 32'))
		hint.set_markup('<b>Choose the building you\'d like to explore</b>')
		hint.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#555555"))
		width_position = hint.get_layout().get_pixel_size()[0]/2
		fixed.put(hint, width_position, 50)
		if (kind == 'big'):
			fixed.connect('expose_event', self.draw_pixbuf, '../images/big city.png')
			buildings = [['../images/townhall.png', 150, 590, 'townhall'],['../images/school.png', 410, 590, 'school'],['../images/church.png', 760, 540, 'church']]
		else:
			fixed.connect('expose_event', self.draw_pixbuf, '../images/small city.png')
			buildings = [['../images/townhall.png', 150, 590, 'townhall'],['../images/school.png', 410, 590, 'school'],['../images/church.png', 760, 540, 'church']]
		for row in buildings:
			building_image = gtk.Image()
			building_image.set_from_file(row[0])
			building_eventbox = gtk.EventBox()
			building_eventbox.set_visible_window(False)
			building_eventbox.connect('button-press-event', self.clicked_building_callback)
			building_eventbox.set_events(gtk.gdk.EXPOSURE_MASK
								| gtk.gdk.BUTTON_PRESS_MASK)
			building_eventbox.add(building_image)
			building_eventbox.kind = row[3]
			building_image.show()
			building_eventbox.show()
			fixed.put(building_eventbox, row[1], row[2])
		self.window.show_all()
		self.window.resize(1200, 800)

	def show_world_map(self):
		# set fixed
		fixed = gtk.Fixed()
		fixed.connect('expose_event', self.draw_pixbuf, '../images/world map.png')
		# set label
		hint = gtk.Label()
		hint.modify_font(pango.FontDescription('FreeSans 32'))
		hint.set_markup('<b>Choose your next destination</b>')
		hint.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#555555"))
		# set countries list
		countries_combobox = gtk.combo_box_new_text()
		countries_combobox.set_wrap_width(4)
		countries_combobox.append_text('China')
		countries_combobox.append_text('France')
		countries_combobox.append_text('Spain')
		countries_combobox.append_text('US')
		fixed.put(hint, (hint.get_layout().get_pixel_size()[0])+75, 25)
		fixed.put(countries_combobox, 550, 100)
		self.window.add(fixed)
		color = gtk.gdk.color_parse('#ffffff')
		self.window.modify_bg(gtk.STATE_NORMAL, color)
		self.window.show_all()
		self.window.resize(1200, 800)

	def show_load_new_game(self):
		# set box
		main_box = gtk.VBox()

	def show_new_game_menu(self):
		# set fixed
		fixed = gtk.Fixed()

	def show_location(self):
		# set box
		main_box = gtk.VBox()

	def __init__(self):
		# set window
		self.window = gtk.Window()
		self.window.set_title('GeoAdventures')
		self.window.set_decorated(False)
		self.window.connect("delete_event", self.delete_event)
		self.window.connect("destroy", self.destroy)
		#self.show_world_map()
		#self.show_city('big')
		self.show_city('small')
		self.window.show_all()

	def main(self):
		gtk.main()

if __name__ == "__main__":
	checkers = Checkers()
	checkers.main()
