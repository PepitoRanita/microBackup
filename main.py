import functions, cli_gui 
while True:
	cli_gui.printMenu()
	option = cli_gui.prompt()
	cli_gui.selection(option)
	if option == 9:
		break