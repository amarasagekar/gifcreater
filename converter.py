import imageio
import os

clip = os.path.abspath('Demo Use.mp4')

def gifmaker(inputpath, targetformat):
    outputpath = os.path.splitext(inputpath)[0] + targetformat

    print(f'converting{targetformat} to \n {outputpath}')
    reader = imageio.get_reader(inputpath)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(outputpath, fps=fps)

    for frame in reader:
        writer.append_data(frame)
        print(f'Frame :{frame}')

    print('DONE')

    writer.close()

gifmaker(clip, '.gif')