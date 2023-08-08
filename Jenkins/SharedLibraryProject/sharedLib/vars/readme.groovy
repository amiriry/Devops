def call(some) {
	echo "getting into readme"
	config=readYaml file:'/var/configfiles/myfile.yaml'
	echo "variable value: ${config.field1.field2.field3}"
}
