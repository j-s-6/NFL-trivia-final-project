# NFL-trivia-final-project

This is a command-line NFL trivia game built with Python. It pulls real NFL team data from the Sportradar API and quizzes the user with multiple-choice questions. Have fun!

## Setup

Create and activate a virtual environment:

```sh
conda create -n NFL-trivia-env python=3.11

conda activate NFL-trivia-env
```

Install packages:

```sh
pip install -r requirements.txt
```

Create .env file in root directory and add your secret API key:

```sh
SPORTRADAR_API_KEY=your_api_key_here
```

## Usage

### Command-line app

Play a game of NFL trivia:

```sh
python -m app.main
```

## Tests

Run the tests:

```sh
pytest
```