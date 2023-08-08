def call(name) {
	echo "This is basic step - called from shared lib - its argument is name: ${name}"
	echo "Doing ls"
	sh("ls -l")
}
