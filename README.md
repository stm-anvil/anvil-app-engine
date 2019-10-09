# anvil-app-engine

GCP App Engine project that communicates with an Anvil app.

The Anvil app makes an HTTP request to fire the script (that's how
App Engine works!)

The script communicates back to Anvil using
the Uplink, both by adding rows to Data Tables and by calling a
Server Module function.
