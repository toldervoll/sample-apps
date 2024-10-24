---
title: ColPali 🤝 Vespa - Visual Retrieval
short_description: Visual Retrieval with ColPali and Vespa
emoji: 👀
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: 4.44.0
app_file: main.py
pinned: false
license: apache-2.0
models:
  - vidore/colpaligemma-3b-pt-448-base
  - vidore/colpali-v1.2
preload_from_hub:
  - vidore/colpaligemma-3b-pt-448-base config.json,model-00001-of-00002.safetensors,model-00002-of-00002.safetensors,model.safetensors.index.json,preprocessor_config.json,special_tokens_map.json,tokenizer.json,tokenizer_config.json 12c59eb7e23bc4c26876f7be7c17760d5d3a1ffa
  - vidore/colpali-v1.2 adapter_config.json,adapter_model.safetensors,preprocessor_config.json,special_tokens_map.json,tokenizer.json,tokenizer_config.json 9912ce6f8a462d8cf2269f5606eabbd2784e764f
---

<!-- Copyright Vespa.ai. Licensed under the terms of the Apache 2.0 license. See LICENSE in the project root. -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://assets.vespa.ai/logos/Vespa-logo-green-RGB.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://assets.vespa.ai/logos/Vespa-logo-dark-RGB.svg">
  <img alt="#Vespa" width="200" src="https://assets.vespa.ai/logos/Vespa-logo-dark-RGB.svg" style="margin-bottom: 25px;">
</picture>

# Visual Retrieval ColPali

# Prepare data and Vespa application

First, install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then, run:

```bash
uv sync --extra dev --extra feed
```

Convert the `prepare_feed_deploy.py` to notebook to:

```bash
jupytext --to notebook prepare_feed_deploy.py
```

And launch a Jupyter instance, see https://docs.astral.sh/uv/guides/integration/jupyter/ for recommended approach.

Open and follow the `prepare_feed_deploy.ipynb` notebook to prepare the data and deploy the Vespa application.

# Developing on the web app


Then, in this directory, run:

```bash
uv sync --extra dev
```

This will generate a virtual environment with the required dependencies at `.venv`.

To activate the virtual environment, run:

```bash
source .venv/bin/activate
```

And run development server:

```bash
python hello.py
```

## Preparation

First, set up your `.env` file by renaming `.env.example` to `.env` and filling in the required values.
(Token can be shared with 1password, `HF_TOKEN` is personal and must be created at huggingface)

### Deploying the Vespa app

To deploy the Vespa app, run:

```bash
python deploy_vespa_app.py --tenant_name mytenant --vespa_application_name myapp --token_id_write mytokenid_write --token_id_read mytokenid_read
```

You should get an output like:

```bash
Found token endpoint: https://abcde.z.vespa-app.cloud
````

### Feeding the data

#### Dependencies

In addition to the python dependencies, you also need `poppler`
On Mac:

```bash
brew install poppler
```

First, you need to create a huggingface token, after you have accepted the term to use the model
at https://huggingface.co/google/paligemma-3b-mix-448.
Add the token to your environment variables as `HF_TOKEN`:

```bash
export HF_TOKEN=yourtoken
```

To feed the data, run:

```bash
python feed_vespa.py --vespa_app_url https://myapp.z.vespa-app.cloud --vespa_cloud_secret_token mysecrettoken
```

### Starting the front-end

```bash
python main.py
```

## Deploy to huggingface 🤗

To deploy, run

```bash
huggingface-cli upload vespa-engine/colpali-vespa-visual-retrieval . . --repo-type=space
```

Note that you need to set `HF_TOKEN` environment variable first.
This is personal, and must be created at [huggingface](https://huggingface.co/settings/tokens).
Make sure the token has `write` access.
Be aware that this will not delete existing files, only modify or add,
see [huggingface-cli](https://huggingface.co/docs/huggingface_hub/en/guides/upload#upload-from-the-cli) for more
information.

### Making changes to CSS

To make changes to output.css apply, run

```bash
shad4fast watch # watches all files passed through the tailwind.config.js content section

shad4fast build # minifies the current output.css file to reduce bundle size in production.
```
