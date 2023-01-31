from pytube import YouTube

# Postar Video
video = YouTube('https://www.youtube.com/watch?v=jRz7U762U4Q')

#Configura Qualidade
stream = video.streams.get_highest_resolution()

#Pasta Salva
stream.download(output_path='./saida')