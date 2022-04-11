import os
import sox
import uuid


def adjust_speed(input_path, output_path, tempo):
    same_destination = False
    if input_path == output_path:
        same_destination = True
        path_, ext = os.path.splitext(input_path)
        output_path = path_ + str(uuid.uuid1()) + ext

    tfm = sox.Transformer()
    tfm.tempo(tempo)
    tfm.build(
        input_filepath=input_path,
        output_filepath=output_path
    )
    if same_destination:
        os.rename(output_path, input_path)

def get_duration(path):
    return sox.file_info.duration(path)
