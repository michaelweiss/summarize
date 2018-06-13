Summarize provides a web interface to [TextTeaser](https://github.com/IndigoResearch/textteaser) for summarizing documents.

## Prerequisites

Summarize requires [Flask](http://flask.pocoo.org). You also need to install the libraries required by TextTeaser.

## Use

To start summarize, set it as application to use in the `FLASK_APP` environment variable and start Flask. The command below tells Flask to reload the application whenever you make changes to the code and to accept requests from any hosts. To run this in production you should tweak this.

```sh
> export FLASK_APP=summarize.py
> flask run --reload --host 0.0.0.0
```

## License

This code is released under an MIT License.
