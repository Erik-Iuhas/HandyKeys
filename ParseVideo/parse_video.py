from math import ceil
import cv2 as cv
import numpy as np
import os
import json


def parse_video(video_path, output_path):
    """Parse a video for every skip frame and save the frames in the output_path.

    Args:
        video_path (Path to the video being parsed): _description_
        output_path (_type_): _description_
        output_size (_type_): _description_

    """
    # parse video every frame_skip frames
    video = cv.VideoCapture(video_path)
    #create folder called bilat if it doesn't exist
    if not os.path.exists(os.path.join(output_path, 'bilat')):
        os.mkdir(os.path.join(output_path, 'bilat'))
    #create a folder containing the un modifide images if it doesn't exist
    if not os.path.exists(os.path.join(output_path, 'unmodified')):
        os.mkdir(os.path.join(output_path, 'unmodified'))

    #make a training and validation set folder for unmodified images
    if not os.path.exists(os.path.join(output_path, 'unmodified', 'training')):
        os.mkdir(os.path.join(output_path, 'unmodified', 'training'))
    if not os.path.exists(os.path.join(output_path, 'unmodified', 'validation')):
        os.mkdir(os.path.join(output_path, 'unmodified', 'validation'))

    #make a training and validation set folder inside of bilat folder
    if not os.path.exists(os.path.join(output_path, 'bilat', 'training')):
        os.mkdir(os.path.join(output_path, 'bilat', 'training'))
    if not os.path.exists(os.path.join(output_path, 'bilat', 'validation')):
        os.mkdir(os.path.join(output_path, 'bilat', 'validation'))

    frame_count = 0
    # get number of frames in video as int
    num_frames = int(video.get(cv.CAP_PROP_FRAME_COUNT))
    # calculate frame skip so that we only 120 frames in the training set
    frame_skip = ceil(num_frames / 120)
    while True:
        ret, frame = video.read()
        # if the video is over, break
        if not ret:
            break
        if frame_count % frame_skip == 0:
            # resize the frame

            # make a training and validation set using random to select if it goes to the training or validation set folder
            # random selection between 0 and 5
            if np.random.randint(0, 5) == 0:
                #add to validation
                cv.imwrite(os.path.join(output_path,'unmodified','validation', 'frame{}.jpg'.format(frame_count)), frame)
                # save to bilat folder while applying a bilateral filter
                cv.imwrite(os.path.join(output_path,'bilat' ,'validation', 'frame{}.jpg'.format(frame_count)), cv.bilateralFilter(frame, 5, 75, 75))
            else:
                #add to training
                cv.imwrite(os.path.join(output_path,'unmodified','training', 'frame{}.jpg'.format(frame_count)), frame)
                # save to bilat folder while applying a bilateral filter
                cv.imwrite(os.path.join(output_path, 'bilat', 'training', 'frame{}.jpg'.format(frame_count)), cv.bilateralFilter(frame, 5, 75, 75))

        frame_count += 1
        #print when finished
        if frame_count % 100 == 0:
            print('{} frames parsed'.format(frame_count))


def main():
    """Main function."""
    #get all videos in the folder
    video_path = '.\\videos'
    output_path = '.\\frames'
    #if the output folder doesn't exist, create it
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    
    frame_skip = 4
    #iterate through all videos in the folder and make a folder based on the file name
    for video in os.listdir(video_path):
        if video.endswith('.mp4'):
            video_name = video.split('.')[0]
            #create a folder for the video if it doesn't exist
            if not os.path.exists(os.path.join(output_path, video_name)):
                os.mkdir(os.path.join(output_path, video_name))
            parse_video(os.path.join(video_path, video), os.path.join(output_path, video_name))
            print('Video {} parsed'.format(video))

if __name__ == '__main__':
    main()