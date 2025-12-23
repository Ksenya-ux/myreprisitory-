import sys
import struct

def read_wav_header():

    header = sys.stdin.buffer.read(44)
    

    if len(header) < 44:
        print("NO")
        return
    

    if header[0:4] != b'RIFF' or header[8:12] != b'WAVE':
        print("NO")
        return
    
    file_size = struct.unpack('<I', header[4:8])[0]
    audio_format = struct.unpack('<H', header[20:22])[0]
    num_channels = struct.unpack('<H', header[22:24])[0]
    sample_rate = struct.unpack('<I', header[24:28])[0]
    bits_per_sample = struct.unpack('<H', header[34:36])[0]
    data_size = struct.unpack('<I', header[40:44])[0]
    

    print(f"Size={file_size}, Type={audio_format}, Channels={num_channels}, Rate={sample_rate}, Bits={bits_per_sample}, Data size={data_size}")

if __name__ == '__main__':
    read_wav_header()
