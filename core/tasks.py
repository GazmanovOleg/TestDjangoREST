from .models import File
import os
from celery import shared_task
import random
import string
from demo.celery import app
from .logs import logger
from . serializers import FileVideoSerializer

def get_random_string(string_len = 6):
    return ''.join(string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase))] for _ in range(string_len))

@app.task(name = "change_video_extension")
def change_video_extension(input_file, width, height):
    output_file = f"{get_random_string()}.mp4"
    os.system(f"ffmpeg -i {input_file} -s {width}x{height} {output_file}")
    #logger.info(f"videfile after file extension {output_file} type is {type(output_file)}")
    return output_file
