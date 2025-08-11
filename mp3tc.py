import sys
import pathlib
from ffmpeg import FFmpeg 


def clean_name(input_name: str) -> str:
    output_name = input_name.split(".")[0]
    output_name += ".mp3"
    return output_name


def transcode(input_name: str, output_name: str):
    try:
        ffmpeg = (
            FFmpeg()
            .input(input_name)
            .output(
                output_name, {"codec:a": "libmp3lame", "q:a": "0"}, preset="veryslow"
            )
        )

        print(f"Converting: {input_name}")
        ffmpeg.execute()
        print("Done")

    except ffmpeg.errors.FFmpegUnsupportedCodec:
        print("Invalid encoder, is lame installed?")
        return
        
    except ffmpeg.Error as ex:
        print(f"FFmpeg error: {ex}")
        return

    except Exception as ex:
        print(f"An error has occurred: {ex}")
        return
    
    return


def get_flac_files() -> list:
    flacs = pathlib.Path(".").glob("*.flac")
    file_names = [file.name for file in flacs]
    return file_names


def main():
    for file_name in get_flac_files():
        output_name = clean_name(file_name)
        transcode(file_name, output_name)


if __name__ == "__main__":
    main()
