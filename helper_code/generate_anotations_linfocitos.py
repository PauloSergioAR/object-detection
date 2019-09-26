import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from generate_xml import write_xml

img = None
tl_list = []
br_list = []
object_list = []

image_folder = 'C:/Users/Paulo/Documents/blood-cells/dataset2-master/dataset2-master/images/TRAIN/LYMPHOCYTE'
save_dir = 'C:/Users/Paulo/Documents/blood-cells/dataset2-master/dataset2-master/images/TRAIN/LYMPHOCYTE_ANOTATIONS'
obj = 'LYMPHOCYTE'

def line_select_callback(clk, rls):
    global tl_list
    global br_list
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(obj)

def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == 'q':
        print(object_list)
        write_xml(image_folder, img, object_list, tl_list, br_list, save_dir)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        plt.close()

def toggle_selector(event):
    toggle_selector.RS.set_active(True)


if __name__ == '__main__':
    lis = os.listdir(save_dir)
    read = len(lis)
    print(read)
    count = 0
    progress = read
    for n, image_file in enumerate(os.scandir(image_folder)):
        count = count + 1        
        if count <= read:            
            continue
        print("progress: " + str(progress))
        progress = progress + 1
        print("continuing from " + str(read))
        img = image_file
        fig, ax = plt.subplots(1)
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(1500, 80, 960, 720)
        image = cv2.imread(image_file.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        fig.canvas.set_window_title(image_file.name)
        ax.imshow(image)

        toggle_selector.RS = RectangleSelector(
            ax, line_select_callback, drawtype='box', useblit=True,
            button=[1], minspanx=5, minspany=5, spancoords='pixels',
            interactive=True
        )
        bbox = plt.connect('key_press_event', toggle_selector)
        key = plt.connect('key_press_event', onkeypress)
        plt.show()

