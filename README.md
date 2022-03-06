# A simple HatNote websocket analysis

---

The task is to analyse the data stream and produce a report.

Before we can start the jupyter script, we need to install the dependencies for this project.

If you have poetry installed, then all you need to do is run:

```sh
poetry install
```

in the root directory of this project.

If you do not have poetry installed, then you can install it with:

```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

For reference, you can find more information [here](https://python-poetry.org/docs/)

Once poetry install has completed, we can run the jupyter script.

Since I wanted to write a report, I decided to use the slides feature of Jupyter notebook to write the report. The slide could be found [here](./hatnote_websocket/Presentation.slides.html).

To run the notebook, use the following command:

```sh
jupyter-notebook hatnote_websocket/Presentation.slides.html
```
