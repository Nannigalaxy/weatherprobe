INTRO = "\nWelcome to WeatherProbe CLI Application. Type 'commands' to list commands.\n"

PROMPT_MSG = "\n{}@airprobe$ "

HELP_STR = {
	"create":["create",
			 "Create new user for login in database.", [],
			 ["First Name", "Last Name", "Username", "Password", "(All Mandatory)"]],

	"update":["update",
			 "Update user details in database.\n\t\tOnly fill in the fields to be updated.\n\t\tLEAVE BLANK to remain same.", 
			[],
			 ["User ID (Mandatory)", "First Name", "Last Name", "Username", "Password"]],

	"remove":["remove",
			 "Remove user from database.",
			[],
			 ["User ID (Mandatory)"]], 

	"users":["users",
			 "List all users in the database", [],[]],

	"weather":["weather [OPTIONS] ARGS ...",
			 "Get weather forcast info.", 
			 ["--place/-p \t Location name to search. (Default: bengaluru)",
			 "--date/-d \t Date(YYYY-MM-DD). (Default: today's date)",
			 "--time/-t \t Time(HH:MM). (Default: current time)",
			 "--longitude/-lon \t Longitude.",
			 "--latitude/-lat \t Latitide."],
			 []],

	"logout":["logout",
			 "Exist from the application", [], []]
}