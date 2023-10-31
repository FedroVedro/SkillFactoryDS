{
  "start_date": "2023-10-01",
  "end_date": "2023-10-31",
  "channel_stats": [
    {
      "channel_name": "Канал 1",
      "views": 1000
    },
    {
      "channel_name": "Канал 2",
      "views": 750
    },
    {
      "channel_name": "Канал 3",
      "views": 1200
    }
  ]
}

{
  "type": "object",
  "properties": {
    "start_date": {
      "type": "string",
      "format": "date"
    },
    "end_date": {
      "type": "string",
      "format": "date"
    },
    "channel_stats": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "channel_name": {
            "type": "string"
          },
          "views": {
            "type": "integer"
          }
        },
        "required": ["channel_name", "views"]
      }
    }
  },
  "required": ["start_date", "end_date", "channel_stats"]
}
