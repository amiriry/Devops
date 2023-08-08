def call(some) {
	echo "Getting into exeme"
	config=readYaml file:'/var/configfiles/myfile.yaml'
	echo "trying to execute the command:"
	commands=config.command
	echo "COMMANDS FIELD:${commands}"
	println "place 1: ${commands}[0]"
	config.command.each { entry ->
		println "aaaaaaaa: $entry"
	}

	for (en in commands) {
		en.each { itr ->
			sh "$itr.value"
		}
	}
}
