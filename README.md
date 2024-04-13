# hoghacks-2024
Hackathon Spring 2024

## API
GET /api/v1/formations

GET /api/v1/predictions

GET /api/v1/situation

```json
{
    "away_score": int,
    "home_score": int,
    "position": {
        "distance": int,
        "down": int,
        "is_possessing_team": bool,
        "yard": int
    },
    "quarter": int,
    "time": string
}
```

POST /api/v1/time

```json
{
  "time": string,
  "quarter": int
}
```

POST /api/v1/reset
