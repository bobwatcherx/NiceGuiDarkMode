from nicegui import ui

dark_mode = False
ui.label("Hello Youtube").classes("text-h1")


# I CREATE TOGGLE BUTtON FOR DARK AND LIGHT THEME

# CREATE FUNCTION TOGGLE
async def toggle_mode():
	global dark_mode
	# IF THEME IS DARK MODE 
	if dark_mode:
		await make_light()
		# CHANGE ICON IN BUTTON
		theme.props("icon=lightbulb")
		# CHANGE TEXT IN BUTTON
		theme.text = "dark mode"
		# SET TO False
		dark_mode = False
	# AND IF THEME IF NOT DARK
	else:
		await make_dark()
		# CHANGE ICON IN BUTTON
		theme.props("icon=light_mode")
		# CHANGE TEXT IN BUTTON
		theme.text = "light mode"
		# SET TO False
		dark_mode = True





# FOR LIGHT MODE
async def make_light():
	await ui.run_javascript('''
	Quasar.Dark.set(false);
	tailwind.config.darkMode = "class";
	document.body.classList.add(dark);

		''',respond=False)


# for DARK MODE
async def make_dark():
	await ui.run_javascript('''
	Quasar.Dark.set(true);
	tailwind.config.darkMode = "class";
	document.body.classList.add(dark);

		''',respond=False)


theme = ui.button("dark mode",on_click=toggle_mode).props("icon=lightbulb")




# I RUN IN WEB MODE
ui.run()
