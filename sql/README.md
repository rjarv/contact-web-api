# Create SQL (postgres)

The scripts in this folder are meant to assist in setting up the DB environment.  The configuration matches the API app.conf in the root. These scripts also assume that the postgres instance has an "admin" role. You may choose to use default postgres DB and simply add a schema to that. If you go that route, simply edit the app.conf file changing the Database entry to the following...

	[Database]
	connection_string: "postgresql://app_user:coding@localhost/postgres"

Likewise with the password. When creating the "app_user" role, the default password is "coding" as seen in the config entry above. That will need to be updated in both the 'createroles.sql' file and in the config entry.

Recommended Execution order:
1. createroles.sql
2. createdb.sql (optional)
3. createschema.sql
4. createzipdomain.sql
5. createaddressbook.sql
6. createfamilykey.sql
7. createspousalkey.sql