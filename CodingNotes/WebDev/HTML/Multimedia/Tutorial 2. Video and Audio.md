
# Video and audio on the web

The first influx of online videos and audio were made possible by proprietary plugin-based technologies like [Flash](https://en.wikipedia.org/wiki/Adobe_Flash) and [Silverlight](https://en.wikipedia.org/wiki/Microsoft_Silverlight). Both of these had security and accessibility issues, and are now obsolete, in favor of native HTML solutions [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video) and [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio) elements and the availability of JavaScript [APIs](https://developer.mozilla.org/en-US/docs/Glossary/API) for controlling them. We'll not be looking at JavaScript here — just the basic foundations that can be achieved with HTML.

We won't be teaching you how to produce audio and video files — that requires a completely different skill set. We have provided you with [sample audio and video files and example code](https://github.com/mdn/learning-area/tree/main/html/multimedia-and-embedding/video-and-audio-content) for your own experimentation, in case you are unable to get hold of your own.

> **Note:** Before you begin here, you should also know that there are quite a few OVPs (online video providers) like [YouTube](https://www.youtube.com/), [Dailymotion](https://www.dailymotion.com/), and [Vimeo](https://vimeo.com/), and online audio providers like [Soundcloud](https://soundcloud.com/). Such companies offer a convenient, easy way to host and consume videos, so you don't have to worry about the enormous bandwidth consumption. OVPs even usually offer ready-made code for embedding video/audio in your webpages; if you use that route, you can avoid some of the difficulties we discuss in this article. We'll be discussing this kind of service a bit more in the next article.

## The `<video>` element

The [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video) element allows you to embed a video very easily. A really simple example looks like this:

```html
<video src="rabbit320.webm" controls>
  <p>
    Your browser doesn't support HTML video. Here is a
    <a href="rabbit320.webm">link to the video</a> instead.
  </p>
</video>
```

The features of note are:

- [`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video#src)

In the same way as for the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) element, the `src` (source) attribute contains a path to the video you want to embed. It works in exactly the same way.

- [`controls`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video#controls)

Users must be able to control video and audio playback (it's especially critical for people who have [epilepsy](https://en.wikipedia.org/wiki/Epilepsy#Epidemiology).) You must either use the `controls` attribute to include the browser's own control interface, or build your interface using the appropriate [JavaScript API](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement). At a minimum, the interface must include a way to start and stop the media, and to adjust the volume.

- The paragraph inside the `<video>` tags

This is called **fallback content** — this will be displayed if the browser accessing the page doesn't support the `<video>` element, allowing us to provide a fallback for older browsers. This can be anything you like; in this case, we've provided a direct link to the video file, so the user can at least access it some way regardless of what browser they are using.

## Using multiple source formats to improve compatibility

There's a problem with the above example. It is possible that the video might not play for you, because different browsers support different video (and audio) formats. Fortunately, there are things you can do to help prevent this from being an issue.

### Contents of a media file

First, let's go through the terminology quickly. Formats like MP3, MP4 and WebM are called **[container formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Containers)**. They define a structure in which the audio and/or video tracks that make up the media are stored, along with metadata describing the media, what codecs are used to encode its channels, and so forth.

A WebM file containing a movie which has a main video track and one alternate angle track, plus audio for both English and Spanish, in addition to audio for an English commentary track can be conceptualized as shown in the diagram below. Also included are text tracks containing closed captions for the feature film, Spanish subtitles for the film, and English captions for the commentary.

<img src="https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Video_and_audio_content/containersandtracks.png" alt="Diagram conceptualizing the contents of a media file at the track level.", width=40%>

The audio and video tracks within the container hold data in the appropriate format for the codec used to encode that media. Different formats are used for audio tracks versus video tracks. Each audio track is encoded using an [audio codec](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Audio_codecs), while video tracks are encoded using (as you probably have guessed) [a video codec](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Video_codecs). As we talked about before, different browsers support different video and audio formats, and different container formats (like MP3, MP4, and WebM, which in turn can contain different types of video and audio).
