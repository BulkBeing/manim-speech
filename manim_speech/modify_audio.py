import os
import sox
import uuid


def adjust_speed(input_path, output_path, tempo):
    # sample_rate = sox.file_info.sample_rate(path)
    # n_samples = sox.file_info.num_samples(path)
    # is_silent = sox.file_info.silent("path/to/file.aiff")

    # tmp_output_path =
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