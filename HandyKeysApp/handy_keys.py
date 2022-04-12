import kivy
import cv2 as cv
import TinyHand
import os
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.clock import Clock


class handy_keys(App):
    """ This app is responsible for utlizing a tensorflow model to decide if a key is pressed or not. 
    The model is trained on a dataset of hands the model is then used to predict if a key is pressed or not.
    Kivy displays the model's prediction and the actual key pressed."""
    def build(self):
        """Build the app."""
        #create a box layout
        layout = BoxLayout(orientation='vertical')
        self.image_count =500
        #create tiny hand
        self.tiny_hand = TinyHand.TinyHand('tiny_hand_final.h5')

        # add blank image
        self.webcam = Image(source='', allow_stretch=True)
        # connect to webcam
        self.cap = cv.VideoCapture(0)
        # update webcam with clock 4 times per second
        Clock.schedule_interval(self.update_webcam, 1.0 / 4.0)

        # add image to layout
        layout.add_widget(self.webcam)
        
        # add label to layout
        self.label = Label(text='', font_size=50)
        layout.add_widget(self.label)

        #return the layout
        return layout
    

    # update webcam
    def update_webcam(self, *args):
        """Update webcam."""
        # get the webcam feed
        ret, frame = self.cap.read()
        # get dimensions of webcam feed
        h, w, _ = frame.shape
        # cut a 256 by 256 pixel section from the right of the webcam feed
        frame = frame[0:256, w - 256:w]
        
        
        '''
        #Used for generating more of a dataset.
        #create folder to store images
        if not os.path.exists('images'):
            os.makedirs('images')
        #save image
        cv.imwrite('images/' + str(self.image_count) + '.jpg', frame)
        #increment image count
        self.image_count += 1
        '''
        
        # use frame to predict the key
        prediction = self.tiny_hand.predict(frame)
        print(prediction)
        # update label
        self.label.text = "Current Key" + prediction

        # convert to texture without flipping
        buf1 = cv.flip(frame, -1)
        buf = buf1.tostring()
        image_texture = Texture.create(
            size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')

        # display webcam feed
        self.webcam.texture = image_texture


if __name__ == '__main__':
    handy_keys().run()