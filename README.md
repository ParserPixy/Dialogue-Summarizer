# End-to-End Dialogue-Summarizer
This project utilizes the Summarization capabilities of the pretrained [google/pegasus-cnn_dailymail](https://arxiv.org/abs/1912.08777) Transformer model to summarize the conversations on the [Samsum dataset](https://arxiv.org/abs/1911.12237v2)

## Workflows

1. Update config.yaml
2. params.yaml
3. Update entity
4. Update configuration manager in src config.yaml
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py

## How to run?

### STEPS:

Clone the repository to your local machine

```bash
git clone https://github.com/ParserPixy/Text-Summarizer
```
01- Create a conda environment after opening the repository

```bash
conda create -n textS python=3.8 -y
```

```bash
conda activate textS
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python -m streamlit run streamlit_app.py
```

Now,
```bash
open up you local host and port
```

## Streamlit deployment

### STEPS:
1. Create your [streamlit account](https://share.streamlit.io/)
2. Connect your Github account
3. Choose `Create app` button
4. Select your Github repo, branch and set `streamlit_app.py` as your main file path
5. Select your App URL and Deploy!
