from window_slider import Slider
import numpy


def slide(y, window_size, noverlap):
    list = numpy.array(y)
    bucket_size = int(window_size)
    overlap_count = int(noverlap)
    slider = Slider(bucket_size, overlap_count)
    slider.fit(list)
    while True:
        window_data = slider.slide()
        if len(window_data) < window_size:
            break
        yield window_data
        if slider.reached_end_of_list():
            break