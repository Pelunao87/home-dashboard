# A basic Home Dashboard

## Local Transport information
Uses Real-Time information provided by the public API at: https://www.trafiklab.se/api/sl-realtidsinformation-3

Requires an API key that can be obtained by creating a free account at Trafiklab website. The app expects the API key
to be saved as an environment variable: SL_API_KEY_REALTIMEDEP

## Garbage collection
Household waste: every Monday
Food waste: every second Thursday, starting at 31th Dec 2015
So the indicator should show corresponding message one day before those days

## Local server
Start a local webserver by running:

```bash
python app.py
```

## License
This code is dedicated to the public domain to the maximum extent permitted by applicable law, pursuant to CC0 (http://creativecommons.org/publicdomain/zero/1.0/)
