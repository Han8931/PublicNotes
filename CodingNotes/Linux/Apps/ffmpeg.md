# ffmpeg

## Trim Audio
`ffmpeg -ss 00:00:00 -to 00:36:30 -i Recording.m4a Trimmed.m4a`

## Convert Format
`ffmpeg -i LostInTranslation.mkv -codec copy LostInTranslation.mp4`

## Screen Recording
Record my screen: 
- `ffmpeg -f x11grab -i :0.0 out.mkv`
- `ffmpeg -f x11grab -s 1680x1050 -i :0.0 out.mkv`: adjust screen size
	- Note that the screen size has to be placed before `-i`
- To record audio...
	- `ffmpeg -f x11grab -s 1680x1050 -i :0.0 -f alsa -i default out.mkv`: ALSA
	- `ffmpeg -f x11grab -s 1680x1050 -i :0.0 -f pulse -i default out.mkv`: Pulse
