from ffmpeg import FFmpeg

input_name:str = "208-led_zeppelin-nobodys_fault_but_mine.flac"

def clean_name(input_name: str) -> str:
    output_name = input_name.split(".")[0]
    output_name += ".mp3"
    return output_name

output_name:str = clean_name(input_name)

ffmpeg = (
    FFmpeg()
    .input(input_name)
    .output(output_name, {"codec:a": "libmp3lame", "q:a": "0"}, preset="veryslow")
)

ffmpeg.execute()
