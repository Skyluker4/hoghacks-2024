# hoghacks-2024
Hackathon Spring 2024

## API
GET /api/v1/formations

```json
[
    {
        "image": "/images/placeholder.png",
        "name": "4-3 Formation",
        "weight": 1.0
    },
    {
        "image": "/images/placeholder.png",
        "name": "3-4 Formation",
        "weight": 1.0
    },
    {
        "image": "/images/placeholder.png",
        "name": "Nickel Formation",
        "weight": 1.0
    },
    {
        "image": "/images/placeholder.png",
        "name": "Dime Formation",
        "weight": 1.0
    },
    {
        "image": "/images/placeholder.png",
        "name": "Quarter Formation",
        "weight": 1.0
    },
    {
        "image": "/images/placeholder.png",
        "name": "Goal Line Formation",
        "weight": 1.0
    }
]
```

GET /api/v1/predictions

```json
[
    {
        "formation": "I Formation",
        "image": "/static/images/placeholder.png",
        "name": "Run",
        "weight": 1.0
    },
    {
        "formation": "I Formation",
        "image": "/static/images/placeholder.png",
        "name": "PA Pass",
        "weight": 1.0
    },
    {
        "formation": "I Formation",
        "image": "/static/images/placeholder.png",
        "name": "Screen Pass",
        "weight": 1.0
    },
    {
        "formation": "Singleback Formation",
        "image": "/static/images/placeholder.png",
        "name": "Run",
        "weight": 1.0
    }
]
```

GET /api/v1/situation

```json
{
    "away_score": 0,
    "home_score": 0,
    "is_possessing_team": false,
    "position": {
        "distance": 10,
        "down": 1,
        "yard": 0
    },
    "quarter": 1,
    "time": "15:00"
}
```

POST /api/v1/time

```json
{
  "time": "15:00",
  "quarter": 1
}
```

POST /api/v1/reset

POST /api/v1/score

```json
{
  "away_score": 0,
  "home_score": 0
}
```

POST /api/v1/possession

```json
{
  "is_possessing_team": true
}
```

POST /api/v1/position

```json
{
  "distance": 10,
  "down": 1,
  "yard": 0
}
```
