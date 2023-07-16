# Pax (Rest Api For Check Anxiety Disorder) 🏥

Hello there 👋, Today I built a rest api that functions to check whether a user has Anxiety disorder or not, I built this using random forest algorithm, dont forget to star this repo ⭐

- [Pax](#Pax)
  - [Tech Stack](#techstack)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Authors](#authors)

## Tech Stack
 - Flask 🌶
 - scikit-learn 💻
 - pandas 🗃

## Installation

Clone this repo

```sh
git clone https://github.com/ariear/pax-api.git
```

Install the requirements
```sh
pip install -r requirements.txt
```

Run server
```sh
python app.py
```

## Usage

[Sympton Here](https://drive.google.com/file/d/1pFRCoyrVkrcTe5gAGc89LYtbKwKNXTf1/view?usp=sharing)

| Endpoint | Method | Usage | Body |
|----------|-------|-------|-------|
| post symptom | POST | `/predict` | { "gejala1": "", "gejala2": "", "gejala3": ""} |
| get symptom | GET | `/symptom` | - |

## Authors
  - ArieAr
  - ChatGPT
