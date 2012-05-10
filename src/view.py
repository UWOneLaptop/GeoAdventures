#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import pango
from model import *

class View:
	def delete_event(self, widget, event, data=None):
		print 'delete event occurred'
		return False

	def destroy(self, widget, data=None):
		print 'destroy signal occurred'
		gtk.main_quit()


	# for show_city
	def draw_pixbuf(self, widget, event, path):
		pixbuf = gtk.gdk.pixbuf_new_from_file(path)
		widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0,0)

	def clicked_building_callback(self, widget, event):
		if (event.type == gtk.gdk.BUTTON_PRESS and event.button == 1):
			print widget.kind
			# TODO: query the controller for posible answers and right answer
			answers = ['USA', 'France', 'Spain', 'China', 'Hongkong']
			self.show_location(widget.kind, self.child, 'What\'s the biggest country?', answers, 'China')

	def show_city(self, kind):
		self.window.remove(self.fixed)
		self.window.remove(self.main_box)
		# set fixed
		self.fixed = gtk.Fixed()
		self.window.add(self.fixed)
		# set hint label
		hint = gtk.Label()
		hint.modify_font(pango.FontDescription('FreeSans 32'))
		hint.set_markup('<b>Choose the building you\'d like to explore</b>')
		hint.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#555555'))
		width_position = hint.get_layout().get_pixel_size()[0]/2
		self.fixed.put(hint, width_position, 50)
		if (kind == 'big'):
			self.fixed.connect('expose_event', self.draw_pixbuf, '../images/big city.png')
			buildings = [['../images/townhall.png', 150, 590, 'townhall'],['../images/school.png', 410, 590, 'school'],['../images/church.png', 760, 540, 'church']]
		else:
			self.fixed.connect('expose_event', self.draw_pixbuf, '../images/small city.png')
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
			self.fixed.put(building_eventbox, row[1], row[2])
		self.window.show_all()


	# for show_choose_next_country
	def changed_cb(self, combobox):
		model = combobox.get_model()
		index = combobox.get_active()
		if index and index!='--':
			print 'I chose', model[index][0]
			#TODO: pass it to the controller
			#TODO: get city size (big/small)
			self.show_city('big')

	def show_choose_next_country(self):
		self.window.remove(self.main_box)
		# set fixed
		self.fixed = gtk.Fixed()
		self.fixed.connect('expose_event', self.draw_pixbuf, '../images/world map.png')
		# set label
		hint = gtk.Label()
		hint.modify_font(pango.FontDescription('FreeSans 32'))
		hint.set_markup('<b>Choose the next country</b>')
		hint.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#555555'))
		# set countries list
		countries_combobox = gtk.combo_box_new_text()
		countries_combobox.set_wrap_width(4)
		# TODO: show list of next countries (for the continent)
		countries_combobox.append_text('--')
		countries_combobox.append_text('China')
		countries_combobox.append_text('France')
		countries_combobox.append_text('Spain')
		countries_combobox.append_text('US')
		countries_combobox.set_active(0)
		countries_combobox.connect('changed', self.changed_cb)
		self.fixed.put(hint, (hint.get_layout().get_pixel_size()[0])+150, 25)
		self.fixed.put(countries_combobox, 550, 100)
		self.window.add(self.fixed)
		color = gtk.gdk.color_parse('#ffffff')
		self.window.modify_bg(gtk.STATE_NORMAL, color)
		self.window.show_all()


	# for show_location
	def destroy_callback(self, widget, aux, dialog_text=None):
		if self.run_dialog:
			self.run_dialog = False
			widget.destroy()
			if dialog_text == 'Right! Here is your spacial piece :-)':
				# next country
				self.show_choose_next_country()
				print 'you win!'
			else:
				# next building
				self.show_city('big')
				print 'you loose!'
	
	def check_answer_callback(self, widget, answer, right_answer, player):
		if player == 'carmen':
			if answer == right_answer:
				self.carmos_image.set_from_file('../images/carmen_smiling.png')
				dialog_text = 'Right! Here is your spacial piece :-)'
				dialog_icon = gtk.MESSAGE_INFO
			else :
				self.carmos_image.set_from_file('../images/carmen_sad.png')
				dialog_text = 'Not really, but you can try at another building'
				dialog_icon = gtk.MESSAGE_ERROR
		else:
			if answer == right_answer:
				self.carmos_image.set_from_file('../images/carlos_smiling.png')
				dialog_text = 'Right! Here is your spacial piece :-)'
				dialog_icon = gtk.MESSAGE_INFO
			else :
				self.carmos_image.set_from_file('../images/carlos_sad.png')
				dialog_text = 'Not really, but you can try at another building'
				dialog_icon = gtk.MESSAGE_ERROR
		result_dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, dialog_icon, gtk.BUTTONS_OK, dialog_text)
		self.run_dialog = True
		result_dialog.connect('destroy', self.destroy_callback, dialog_text)
		result_dialog.connect('response', self.destroy_callback, dialog_text)
		result_dialog.run()
	
	def show_location(self, building, player, question, answers, right_answer):
		self.window.remove(self.fixed)
		john_doe_image = gtk.Image()
		if building == 'townhall':
			john_doe_image.set_from_file('../images/politician.png')
		elif building == 'school':
			john_doe_image.set_from_file('../images/scientist.png')
		elif building == 'church':
			john_doe_image.set_from_file('../images/priest.png')
		# carmen + carlos = carmos
		self.carmos_image = gtk.Image()
		if player == 'carmen':
			self.carmos_image.set_from_file('../images/carmen_smiling.png')
		else:
			self.carmos_image.set_from_file('../images/carlos_smiling.png')
		# set question and answers box
		qa_box = gtk.VBox()
		self.question_label = gtk.Label()
		self.question_label.modify_font(pango.FontDescription('FreeSans 32'))
		self.question_label.set_markup('<b>'+question+'</b>')
		self.question_label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#555555'))
		qa_box.add(self.question_label)
		for answer in answers:
			answer_button = gtk.CheckButton(answer)
			answer_button.connect('toggled', self.check_answer_callback, answer, right_answer, player)
			qa_box.add(answer_button)
		# set main box
		self.main_box = gtk.HBox()
		self.main_box.add(self.carmos_image)
		self.main_box.add(qa_box)
		self.main_box.add(john_doe_image)
		self.window.add(self.main_box)
		color = gtk.gdk.color_parse('#ffffff')
		self.window.modify_bg(gtk.STATE_NORMAL, color)
		self.window.show_all()


	# for new game
	def clicked_child_callback(self, widget, event):
		if (event.type == gtk.gdk.BUTTON_PRESS and event.button == 1):
			if self.child == '':
				self.child = widget.kind
				if widget.kind == 'carmen':
					self.carmen_image.set_from_file('../images/carmen_smiling_selected.png')
				else:
					self.carlos_image.set_from_file('../images/carlos_smiling_selected.png')
			else :
				if self.child == 'carmen' and widget.kind == 'carmen':
					self.child = ''
					self.carmen_image.set_from_file('../images/carmen_smiling.png')
				elif self.child == 'carmen' and widget.kind == 'carlos':
					self.child = widget.kind
					self.carlos_image.set_from_file('../images/carlos_smiling_selected.png')
					self.carmen_image.set_from_file('../images/carmen_smiling.png')
				elif self.child == 'carlos' and widget.kind == 'carlos':
					self.child = ''
					self.carlos_image.set_from_file('../images/carlos_smiling.png')
				else:
					
					self.child = widget.kind
					self.carlos_image.set_from_file('../images/carlos_smiling.png')
					self.carmen_image.set_from_file('../images/carmen_smiling_selected.png')
	
	def ok_callback(self, widget):
		self.name = self.name_entry.get_text()
		if self.name != '' and self.child !='' and self.country !='--':
			model = Model({'name': self.name, 'gender': self.child, 'country': self.country})
			self.game_state = model.new_game()
			# TODO: play intro
			self.show_choose_next_country()
	
	def changed_country_callback(self, combobox):
		model = combobox.get_model()
		index = combobox.get_active()
		if index and index!='--':
			self.country = model[index][0]
	
	def show_new_game_menu(self):
		# set main box
		self.name = ''
		self.child = ''
		self.country = '--'
		self.main_box = gtk.VBox()
		name_label = gtk.Label()
		name_label.modify_font(pango.FontDescription('FreeSans 32'))
		name_label.set_markup('<b>Please, enter your name</b>')
		name_label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#555555'))
		self.main_box.add(name_label)
		self.name_entry = gtk.Entry(255)
		self.main_box.add(self.name_entry)
		child_label = gtk.Label()
		child_label.modify_font(pango.FontDescription('FreeSans 32'))
		child_label.set_markup('<b>Choose wether you are a girl or a boy</b>')
		child_label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#555555'))
		self.main_box.add(child_label)
		child_box = gtk.HBox()
		self.carmen_image = gtk.Image()
		self.carmen_image.set_from_file('../images/carmen_smiling.png')
		carmen_eventbox = gtk.EventBox()
		carmen_eventbox.set_visible_window(False)
		carmen_eventbox.connect('button-press-event', self.clicked_child_callback)
		carmen_eventbox.set_events(gtk.gdk.EXPOSURE_MASK
										| gtk.gdk.BUTTON_PRESS_MASK)
		carmen_eventbox.add(self.carmen_image)
		carmen_eventbox.kind = 'carmen'
		child_box.add(carmen_eventbox)
		carmen_eventbox.show()
		self.carlos_image = gtk.Image()
		self.carlos_image.set_from_file('../images/carlos_smiling.png')
		carlos_eventbox = gtk.EventBox()
		carlos_eventbox.set_visible_window(False)
		carlos_eventbox.connect('button-press-event', self.clicked_child_callback)
		carlos_eventbox.set_events(gtk.gdk.EXPOSURE_MASK
										| gtk.gdk.BUTTON_PRESS_MASK)
		carlos_eventbox.add(self.carlos_image)
		carlos_eventbox.kind = 'carlos'
		child_box.add(carlos_eventbox)
		carlos_eventbox.show()
		self.main_box.add(child_box)
		country_label = gtk.Label()
		country_label.modify_font(pango.FontDescription('FreeSans 32'))
		country_label.set_markup('<b>Please, choose your country</b>')
		country_label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#555555'))
		self.main_box.add(country_label)
		countries_combobox = gtk.combo_box_new_text()
		countries_combobox.set_wrap_width(4)
		# TODO: fill with list of countries from the model
		countries_combobox.append_text('--')
		countries_combobox.append_text('China')
		countries_combobox.append_text('France')
		countries_combobox.append_text('Spain')
		countries_combobox.append_text('US')
		countries_combobox.set_active(0)
		countries_combobox.connect('changed', self.changed_country_callback)
		continue_button = gtk.Button('Continue', 'gtk-ok')
		continue_button.connect("clicked", self.ok_callback)
		self.main_box.pack_end(continue_button, True, False)
		self.main_box.pack_end(countries_combobox, True, False)
		self.window.add(self.main_box)
		color = gtk.gdk.color_parse('#ffffff')
		self.window.modify_bg(gtk.STATE_NORMAL, color)

	def __init__(self):
		# set window
		self.window = gtk.Window()
		self.window.set_title('GeoAdventures')
		self.window.set_decorated(False)
		self.window.connect('delete_event', self.delete_event)
		self.window.connect('destroy', self.destroy)
		self.show_new_game_menu()
		self.window.show_all()
		self.window.resize(1200, 800)

	def main(self):
		gtk.main()

if __name__ == '__main__':
	view = View()
	view.main()
