import soundfile as sf
import os
#import numpy as np
#import wave
#import ffmpeg
#from pydub import AudioSegment as am
import resampy
import audioop
import asyncio

inputPath = "input/"

async def asynch_convert():
    
    multTask_Limit = 100
    converterTasks = []
    convertQueue = os.listdir(inputPath)

    for limit in  range (0,multTask_Limit):
      print("Converter ",limit," started my liege !")
      converterTasks.append(asyncio.ensure_future(converter(convertQueue)))
      
    print("I will notify you on completion of each 100 files. ")
    try:
      while converterTasks:
          done, pending = await asyncio.wait(converterTasks)
          converterTasks[:] = pending
      return 0
    except Exception as e:
        print("ERROR IN converterTasks QUEUE TASK MESSAGE : "+ str(e))  


async def converter(convertQueue):

    try:
        while(convertQueue):
            fileName = str(convertQueue.pop(0))
            if (len(convertQueue) % 100 == 0):
                print(str(len(convertQueue))+" files left")
            #print(fileName)
            output = "convert_output/"+fileName.split(".")[0]+".wav"
            #print(output)
            data, samplerate = sf.read(inputPath+fileName)
            #downSample = audioop.ratecv(data, 2, 1, 32000, 32000,None)
            if (samplerate != 16000): 
                downSample = resampy.resample(data, samplerate, 16000)
            
                sf.write(output, downSample,16000,'PCM_16',format="wav")
            else:
                sf.write(output, data,samplerate,'PCM_16',format="wav")
    except Exception as e:
        print("ERROR IN converter, TASK MESSAGE : "+ str(e))  
    
    #samplingArray, srOrig = librosa.load('test.ogg', sr=None)

   

 





def downsampleWav(src, dst, inrate, outrate, inchannels, outchannels):
    """
    if not os.path.exists(src):
        print ('Source not found!')
        return False

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))
    """
    try:
        s_read = wave.open("test.ogg", 'rb')
        s_write = wave.open("new_file.ogg", 'wb')
    except:
        print ('Failed to open files!')
        return False

    n_frames = s_read.getnframes()
    data = s_read.readframes(n_frames)

    try:
        converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
        if outchannels == 1:
            converted = audioop.tomono(converted[0], 2, 1, 0)
    except:
        print ('Failed to downsample wav')
        return False

    try:
        s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
        s_write.writeframes(converted)
    except:
        print ('Failed to write wav')
        return False

    try:
        s_read.close()
        s_write.close()
    except:
        print ('Failed to close wav files')
        return False

    return True