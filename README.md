# Cyberattacks Classification Model

_A project containing a simple neural network for predictive analysis of cyberattack severity (Typical Severity) based on the description (Name)_

## Install All Dependencies
_You can install all required dependencies for the project using this line of code_
```commandline
pip install --no-cache -r requirements.txt
```

## Running App on Docker
```commandline
docker compose up
```

_In subsequent builds you will have to add the 'build' option to add any changes made in the python code_
```commandline
docker compose up --build
```

## Endpoint

The request method is **POST**

The url for the endpoint is 
```code
/get-severity
```

Sample Request Body
```json
{
    "data": [
        "Accessing Functionality Not Properly Constrained by ACLs",
        "Buffer Overflow via Environment Variables"
    ]
}
```

Sample Response
```json
[
    {
        "severity": "High",
        "text": "Accessing Functionality Not Properly Constrained by ACLs"
    },
    {
        "severity": "High",
        "text": "Buffer Overflow via Environment Variables"
    }
]
```