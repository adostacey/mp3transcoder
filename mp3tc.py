import sys
from ffmpeg import FFmpeg, errors


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
                output_name, {"codec:a": "libmp3zlame", "q:a": "0"}, preset="veryslow"
            )
        )

        ffmpeg.execute()
    except errors.FFmpegUnsupportedCodec:
        print("Invalid encoder, is lame installed?")
        return
        
    return


def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Please enter a file name.")
        return

    output_name: str = clean_name(file_name)

    transcode(file_name, output_name)


if __name__ == "__main__":
    main()
