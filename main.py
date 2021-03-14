# Imports the Google Cloud client library
#from google.cloud import speech
#from google.cloud import speech_v1p1beta1 as speech
import azure.cognitiveservices.speech as speechsdk
import os
import io
import threading
import asyncio
import glob
import csv
import json
import operator
import argparse
from src import convert, recognition_config, csv_to_text

genericOBJ = []
ServiceProvider = ""
Subscription    = ""
Region          = ""
Endpoint_id     = ""

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


async def transcribe_file(speechFileFullPath,lang,fileName,writer):
    
    """Transcribe the given audio file."""
    
    result = None
    
    speech_config = speechsdk.SpeechConfig(subscription=Subscription, region=Region)
    speech_config.endpoint_id = Endpoint_id
    speech_config.output_format = speechsdk.OutputFormat.Detailed

    audio_input = speechsdk.AudioConfig(filename=speechFileFullPath)
    speech_config.set_profanity(profanity_option= speechsdk.ProfanityOption.Raw )

    #speech_config.speech_recognition_language=lang
    recognizer = speechsdk.SpeechRecognizer(
                speech_config=speech_config, 
                audio_config=audio_input)
                #auto_detect_source_language_config=auto_detect_source_language_config)
    try:
        result = recognizer.recognize_once_async().get()
        confidence = 0
        #temp = json.load()
        
        for key in result.properties.keys():
                temp = eval(result.properties[key])
                if (type(temp) == dict):
                    confidence = temp["NBest"][0]["Confidence"]
                    #print(temp["NBest"][0]["Confidence"])
        

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:

            #print(fileName)
            temp = {
                "Filename"          : fileName,
                "Culture/Accent"    : lang,
                "Text"              : result.text,
                "Confidence"        : confidence
            }
            recognition_config.recognitionResults.append(temp)
            temp = None
            #print(recognition_config.recognitionResults)

        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(result.no_match_details))
            pass
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
    except Exception as e:
        print("Error in Transcribe Function : "+str(e))
        return None
    """
    recognitionResult = recognition_config.recognitionResults[0]

    if(recognitionResult):
            writer.writerow(recognitionResult)
            recognition_config.recognitionResults.clear()
    """


async def asynch_recognition(fileList,writer):
    accentTasks = []
    
    for fileName in  fileList:
        #print("@@@@ ",fileName, " @@@@\n")
        fullPath = os.path.join("convert_output/", fileName)
        accentTasks.append(asyncio.ensure_future(transcribe_file(fullPath,"en-US",fileName,writer)))
        
    try:
        while accentTasks:
            done, pending = await asyncio.wait(accentTasks)
            accentTasks[:] = pending
        
        #print(recognition_config.recognitionResults)
        for result in recognition_config.recognitionResults:
            #print(result)
            if(result):
                    print("WROTE : "+str(result))
                    writer.writerow(result)
        recognition_config.recognitionResults.clear()
    except Exception as e:
            print("ERROR IN accentTasks QUEUE TASK MESSAGE : "+ str(e))   



def main():

    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="SERVICE_ACCOUNT_KEY2.JSON"
    if not os.path.exists('convert_output'):
        os.makedirs('convert_output')
    
    print(">>> CONVERSION START")
    asyncio.run(convert.asynch_convert())
    print(">>> CONVERSION COMPLETE")

    fileList = os.listdir("convert_output/") 
    





    if not os.path.exists('csv_output'):
        os.makedirs('csv_output')
    if os.path.exists('csv_output/audio_recognition.csv'):
        write_mode = 'a'
    else:
        write_mode = 'w'
    
    with open('csv_output/audio_recognition.csv', write_mode, newline='') as openedFile:
        headers = ['Filename','Culture/Accent','Text','Confidence']
        writer = csv.DictWriter(openedFile, fieldnames=headers) 
        if write_mode == 'w':   
            writer.writeheader()
        
        chunkList = chunks(range(0, len(fileList)),50)
        
        for chunk in chunkList:
            print("Online Speech Recognition Chunk : "+str(chunk))
            filePackage = fileList[chunk.start:chunk.stop]
            asyncio.run(asynch_recognition(filePackage,writer))
            print("Done\n")

        
        

if __name__ == '__main__':
    descriptionText =  'This is a Speech to Text script for cloud based cognitive services.\n \n' \
                       'Put your audio files with .ogg extension to \"input\" folder. Ogg files will be conveted to wav file with built in resampling configurations\n' \
                       'Your converted files will be in convert_output. Dont mess with this folder if you dont know what you do !!! \n' \
                       'Results of the Speech To Text process will be saved in "csv_output" folder'

    parser=argparse.ArgumentParser(description=descriptionText)
    parser.add_argument('ServiceProvider',help="Azure, Google, IBM, Wit")
    parser.add_argument('Subscription', help="example : 6fdfbefdcb604baebaf116b3d2d39ca3")
    parser.add_argument('Region',help="switzerlandnorth, germanyeast, etc") 
    parser.add_argument('Endpoint_id',help="example : dddfbefd-cb60-4bae-baf1-16b3d2d39ca3")
    args=parser.parse_args()
    print("Your arguments : ")
    print(parser.print_help())

ServiceProvider = args.ServiceProvider
Subscription    = args.Subscription
Region          = args.Region
Endpoint_id     = args.Endpoint_id


main()
 
#If you want to ready a training set for Azure Cognitive Services, use below function
#Dont forget to add your sheet names to "sheets" array !

#sheets = ["5001 - 10000","10001 - 15000"]
#csv_to_text.create_training_text(sheets)
