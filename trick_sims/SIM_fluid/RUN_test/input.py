exec(open("Modified_data/realtime.py").read())

#==================================
# Start the variable server client.
#==================================
var_server_port = trick.var_server_get_port()
fluid_graphics_path = os.environ['HOME'] + "/trick_fork/trick_sims/SIM_fluid/Fluid_VSC.py"
if (os.path.isfile(fluid_graphics_path)) :
	fluid_graphics_cmd = "python3 " + fluid_graphics_path + " " + str(var_server_port) + " &"
	print(fluid_graphics_cmd)
	os.system(fluid_graphics_cmd)
else :
	print('Oops! Can\'t find ' + fluid_graphics_path)