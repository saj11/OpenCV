# From: “Learning OpenCV3 Computer Vision with Python Second Edition.”
import cv2
from managers import WindowManager, CaptureManager


class Cameo(object):

    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.on_keypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        """Run the main loop."""
        self._windowManager.create_window()
        while self._windowManager.is_window_created:
            self._captureManager.enter_frame()
            frame = self._captureManager.frame
            if frame is not None:
                # TODO: Filter the frame (Chapter 3).
                pass
            self._captureManager.exit_frame()
            self._windowManager.process_events()

    def on_keypress(self, keycode):
        """Handle a keypress.

        space  -> Take a screenshot.
        tab    -> Start/stop recording a screencast.
        escape -> Quit.

        """
        if keycode == 32:  # space
            self._captureManager.write_image('out.png')
        elif keycode == 9:  # tab
            if not self._captureManager.is_writing_video:
                self._captureManager.start_writing_video('out.avi')
            else:
                self._captureManager.stop_writing_video()
        elif keycode == 27:  # escape
            self._windowManager.destroy_window()


if __name__ == "__main__":
            Cameo().run()
