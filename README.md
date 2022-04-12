# manim-speech

This is a [Manim](https://manim.community) plugin for generating voiceovers for your Manim animations.

It currently supports [Azure Text to Speech](https://azure.microsoft.com/en-us/services/cognitive-services/text-to-speech/).

## Install

This plugin requires that [SoX](http://sox.sourceforge.net/) version 14.4.2 or higher is installed.

To install SoX on Mac with Homebrew:

```brew install sox```

On Debian based distros:

```sudo apt-get install sox```

or install [from source](https://sourceforge.net/projects/sox/files/sox/).

Once SoX is installed, proceed with installing `manim-speech`:

```sh
python setup.py install
```

## Configure

Create a file called `.env` in the same directory where you call Manim with your authentication information.

For Azure, you need to specify your subscription key and service region. Check out [Azure docs](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/) for more details.

```sh
AZURE_SUBSCRIPTION_KEY="..."
AZURE_SERVICE_REGION="..."
```

## Examples

See the [examples directory](./examples).
