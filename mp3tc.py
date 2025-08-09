import sys
from ffmpeg import FFmpeg


def clean_name(input_name: str) -> str:
    output_name = input_name.split(".")[0]
    output_name += ".mp3"
    return output_name


def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Please enter a file name.")
        return

    output_name: str = clean_name(file_name)

    ffmpeg = (
        FFmpeg()
        .input(input_name)
        .output(output_name, {"codec:a": "libmp3lame", "q:a": "0"}, preset="veryslow")
    )

    ffmpeg.execute()


if __name__ == "__main__":
    main()
