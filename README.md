# hoghacks-2024
Hackathon Spring 2024

## API
GET /api/v1/formations

GET /api/v1/predictions

GET /api/v1/situation

```json
{
    "away_score": 0,
    "home_score": 0,
    "position": {
        "distance": 10,
        "down": 1,
        "is_possessing_team": false,
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
