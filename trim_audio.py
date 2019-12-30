import os
from datasets import audio
from hparams import hparams
from pathlib import Path


def main():
	print("trim audio beggin....")
	input = os.path.join("/Users/zhuribing/Documents", "p225_028.wav")
	output = os.path.join("/Users/zhuribing/Documents", "trim_p225_028.wav")
	wav = audio.load_wav(input, sr=16000)
	wav = audio.trim_silence(wav, hparams)
	audio.save_wav(wav,output, 16000)



def vad():
	print("trim audio beggin....")
	dataset_root = Path("/Users/zhuribing/Project/AccelerateServerTest/audio");
	files = list(dataset_root.joinpath("org").glob("*"))

	print(len(files))
	cnt = 0
	for input in files:
		output = str(input).replace("org","trim", 1)
		wav = audio.load_wav(input, sr=16000)
		wav = audio.trim_silence(wav, hparams)
		audio.save_wav(wav,output, 16000)
		cnt = cnt + 1;
		if(cnt %10 == 0):
			print("complete:", cnt);
		# break


if __name__ == '__main__':
	vad()
