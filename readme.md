# Speech To Text Transcribe Script for Cloud based Cognitive Services

This is a Speech to Text script for cloud based cognitive services.

To use it, first you need to get a subscribed account at a cloud provider like azure, google, amazon,  etc.

Then you need to create an endpoint in cloud to be able to work via this script.

----

Put your audio files with .ogg extension to \"input\" folder. Ogg files will be converted to wav file with built in resampling configurations.

Your converted files will be in convert_output. Dont mess with this folder if you dont know what you do !!!

Results of the Speech To Text process will be saved in "csv_output" folder.

usage: .\main.py ServiceProvider Subscription Region Endpoint_id


## NOT COMPLETE YET !!!
