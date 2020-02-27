# anvil-app-engine

GCP App Engine project that communicates with an [Anvil app](https://anvil.works).

The Anvil app makes an HTTP request to fire the script (that's how
App Engine works!)

The script communicates back to Anvil using
the Uplink, both by adding rows to Data Tables and by calling a
Server Module function.

See [this Forum post](https://anvil.works/forum/t/connecting-via-uplink-to-google-app-engine-initially-for-data-loading-using-singer-io/3423) for motivation.
