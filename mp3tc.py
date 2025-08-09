from ffmpeg import FFmpeg

ffmpeg = (
    FFmpeg()
    .input("208-led_zeppelin-nobodys_fault_but_mine.flac")
    .output("output.mp3", {"codec:a": "libmp3lame", "q:a": "0"}, preset="veryslow")
)

ffmpeg.execute()
